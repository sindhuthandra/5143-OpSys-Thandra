"""
NAME :SAIKIRANREDDY NAGULAPALLY
	  THIRUPATHI REDDY PARSHURAMGARI
	  SINDHU REDDY THANDRA
	  
This is a project that implements job scheduling algorithms.
The program will read input from three input files and process them separately:
  input_data/jobs_in_a.txt
  input_data/jobs_in_b.txt
  input_data/jobs_in_c.txt
Output of each simulation will be written to a separate file. Upon successful completion,
the program will create the following three output files:
  input_data/output_a.txt
  input_data/output_b.txt
  input_data/output_c.txt
"""
#!/usr/bin/python3
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
import random
import time

from sim_components import *




###################################################################################################

# === Class: MLFQ===

class MLFQ(object):
    """Multi-Level Feedback Queue
    - Some general requirements for a MLFQ:
        - Each queue needs its own scheduling algorithm (typically FIF0).
        - The method used to determine when to upgrade a process to a higher-priority queue.
        - The method used to determine when to demote a process to a lower-priority queue.
        - The method used to determine which queue a process will enter when that process needs
        service.
    - Rule 1: If Priority(A) > Priority(B), A runs (B doesn't).
    - Rule 2: If Priority(A) = Priority(B), A & B run in RR.
    - Rule 3: When a job enters the system, it is placed at the highest priority (the topmost
              queue).
    - Rule 4: Once a job uses up its time allotment at a given level (regardless of how many times
              it has given up the CPU), its priority is reduced (i.e., it moves down one queue).
    - Rule 5: After some time period S, move all the jobs in the system to the topmost queue.
    - **Attributes**:
        - self.num_levels
        - self.queues
    """
    def __init__(self, num_levels=2):
        self.num_levels = num_levels
        self.queues = []

        for i in range(self.num_levels):
            self.queues.append(Fifo())

    def firstLevelQueue(self):
        return self.queues[0]

    def secondLevelQueue(self):
        return self.queues[1]

    def getProcess(self, level):
        queue = None
        if level == 1:
            queue = self.firstLevelQueue()
        elif level == 2:
            queue = self.secondLevelQueue()

        if queue is None or queue.empty():
            return None
        else:
            return queue.first()

    def addProcess(self, process, level):
        if level == 1:
            self.firstLevelQueue().add(process)
        elif level == 2:
            self.secondLevelQueue().add(process)
        else:
            raise Exception('Cannot add process to queue #', level)

    def removeProcess(self, level):
        if level == 1:
            self.firstLevelQueue().remove()
        elif level == 2:
            self.secondLevelQueue().remove()
        else:
            raise Exception('Cannot remove process from queue #', level)

    def isEmpty(self):
        return self.getProcess(1) is None and self.getProcess(2) is None

    def new(self, process):
        """This method admits a new process into the system.
        - **Args:**
            - None
        - **Returns:**
            - None
        """
        self.firstLevelQueue().add(process)

    def __str__(self):
        """Visual dump of class state.
        - **Args:**
            - None
        - **Returns:**
            - None
        """
        return my_str(self)

###################################################################################################

# === Class: MySemaphore===

class MySemaphore(object):
    """
    A class that implements a very simple semaphore.
    """
    def __init__(self):
        self.value = 1
        self.waitQueue = Fifo()

    # Acquires the semaphore.
    def acquire(self, process):
        if self.value > 0:
            # self.jobs.add(int(process.process_id))
            self.value -= 1
            return True
        else:
            self.waitQueue.add(process)
            self.value -= 1
            return False

    # Releases the semaphore and returns the next job in the waiting queue (if any).
    def release(self, process):
        self.value += 1

        if not self.waitQueue.empty():
            return self.waitQueue.remove()
        else:
            return None

# === Class: Scheduler===

class Scheduler(object):
    """
    New:        In this status, the Process is just made or created.
    Running:    In the Running status, the Process is being executed.
    Waiting:    The process waits for an event to happen for example an input from the keyboard.
    Ready:      In this status the Process is waiting for execution in the CPU.
    Terminated: In this status the Process has finished its job and is ended.
    """
    def __init__(self, *args, **kwargs):
        self.clock = Clock()
        self.memory = Memory()
        self.cpu = Cpu()
        self.accounting = SystemAccounting()
        # self.semaphore = SemaphorePool(num_sems=5, count=1)
        self.semaphores = [MySemaphore(), MySemaphore(), MySemaphore(), MySemaphore(), MySemaphore()]
        self.job_scheduling_queue = Fifo()
        self.process_scheduling_queue = MLFQ()
        self.ioQueue = []

    def new_process(self,job_info):
        """New process entering system gets placed on the 'job_scheduling_queue'.
        - **Args**:
            - job_info (dict): Contains new job information.
        - **Returns**:
            - None
        """

        # Make sure these two fields are int, not str.
        if 'burst_time' in job_info:
            job_info['burst_time'] = int(job_info['burst_time'])
        if 'ioBurstTime' in job_info:
            job_info['ioBurstTime'] = int(job_info['ioBurstTime'])

        memRequired = job_info.get('mem_required')
        if memRequired is not None and int(memRequired) > 512:
            return

        self.job_scheduling_queue.add(Process(**job_info))

    def perform_io(self,info):
        """Current process on cpu performs io
        """
        pass

    def sem_acquire(self,info):
        """Acquire one of the semaphores
        """
        pass

    def sem_release(self,info):
        """Release one of the semaphores
        """
        pass

# === Class: Simulator===

class Simulator(object):

    """
    Not quite sure yet
    """
    def __init__(self, **kwargs):
        self.outputFile = None

        self.jobArrivalInfo = {}
        self.finishedList = []
        self.jobWaitTimeInfo = {}

        # Must have input file to continue
        if 'input_file' in kwargs:
            self.input_file = kwargs['input_file']
        else:
            raise Exception("Input file needed for simulator")

        if 'output_file' in kwargs:
            self.outputFile = open(kwargs['output_file'], 'w')

        # Can pass a start time in to init the system clock.
        if 'start_clock' in kwargs:
            self.start_clock = kwargs['start_clock']
        else:
            self.start_clock = 0

        # Read jobs in apriori from input file.
        self.jobs_dict = load_process_file(self.input_file,return_type="Dict")

        # create system clock and do a hard reset it to make sure
        # its a fresh instance.
        self.system_clock = Clock()
        self.system_clock.hard_reset(self.start_clock)

        # Initialize all the components of the system.
        self.scheduler = Scheduler()
        self.memory = Memory()
        self.cpu = Cpu()
        self.accounting = SystemAccounting()

        # This dictionary holds key->value pairs where the key is the "event" from the input
        # file, and the value = the "function" to be called.
        # A = new process enters system             -> calls scheduler.new_process
        # D = Display status of simulator           -> calls display_status
        # I = Process currently on cpu performs I/O -> calls scheduler.perform_io
        # S = Semaphore signal (release)            -> calls scheduler.sem_acquire
        # W = Semaphore wait (acquire)              -> calls scheduler.sem_release
        self.event_dispatcher = {
            'A': self.scheduler.new_process,
            'D': self.display_status,
            'I': self.scheduler.perform_io,
            'W': self.scheduler.sem_acquire,
            'S': self.scheduler.sem_release
        }

        # Start processing jobs:

        # While there are still jobs to be processed
        while len(self.jobs_dict) > 0:
            # Events are stored in dictionary with time as the key
            key = str(self.system_clock.current_time())

            # If there are any internal events (I/O completion, quantum expiration, etc), handle them first.
            self.processInternalEventsIfPossible()

            # If current time is a key in dictionary, run that event.
            if key in self.jobs_dict.keys():
                event_data = self.jobs_dict[key]
                event_type = event_data['event']

                # Call appropriate function based on event type
                self.event_dispatcher[event_type](event_data)

                # Print the event to the output.
                self.printEvent(event_type)

                if event_type == 'A':
                    # A new job arrived.
                    memRequired = event_data.get('mem_required')
                    if memRequired is not None and int(memRequired) > 512:
                        self.writeStr("This job exceeds the system's main memory capacity.\n")
                    else:
                        self.jobArrivalInfo[int(event_data['pid'])] = {
                            'arrivalTime' : self.currentTime(),
                            'runTime' : int(event_data['burst_time'])
                        }

                        # New job added, we need to run job scheduling algorithm.
                        self.runJobScheduling()
                elif event_type == 'D':
                    # Display status of the simulator
                    self.printSimulatorStatus()
                elif event_type == 'I':
                    # A job wants to perform I/O.
                    self.moveRunningProcessToIOQueue(event_data['ioBurstTime'])
                elif event_type == 'W':
                    # A job wants to wait on a semaphore.
                    semaphoreNo = int(event_data['semaphore'])
                    self.performWaitOnSemaphore(semaphoreNo)
                elif event_type == 'S':
                    # A job wants to signal a semaphore.
                    semaphoreNo = int(event_data['semaphore'])
                    self.performSignalOnSemaphore(semaphoreNo)

                # Remove job from dictionary
                del self.jobs_dict[key]

            # Make the CPU run for 1 time unit.
            self.executeCPUCycle()

            # Increment the system clock.
            self.system_clock += 1

        # Here, there are no more jobs to process. Finish the outstanding jobs.
        while True:
            isSimulationFinished = True

            if not self.scheduler.job_scheduling_queue.empty():
                # Make sure there are no jobs left in the job scheduling queue.
                isSimulationFinished = False

            if not self.scheduler.process_scheduling_queue.isEmpty():
                # Make sure there are no processes left in the process scheduling queue.
                isSimulationFinished = False

            if self.cpu.running_process is not None:
                # Make sure CPU is not busy.
                isSimulationFinished = False

            if isSimulationFinished:
                break

            self.processInternalEventsIfPossible()
            self.executeCPUCycle()
            self.system_clock += 1

        self.writeStr('\n')
        # Print the final finished list.
        self.printFinishedList(isFinal=True)
        self.writeStr('\n\n')

        # Print the average turnout time.
        averageTurnaroundTime = self.floatWith3Decimals(self.calculateAverageTurnoutTime())
        self.writeStr('The Average Turnaround Time for the simulation was ')
        self.writeStr(str(averageTurnaroundTime))
        self.writeStr(' units.\n')
        self.writeStr('\n')

        # Print the average job scheduling wait time.
        averageJobSchedulingWaitTime = self.floatWith3Decimals(self.calculateAverageJobSchedulingWaitTime())
        self.writeStr('The Average Job Scheduling Wait Time for the simulation was ')
        self.writeStr(str(averageJobSchedulingWaitTime))
        self.writeStr(' units.\n')
        self.writeStr('\n')

        # Print the total memory available in the system.
        self.printMemoryStatus()


    # Runs the job scheduling algorithm.
    def runJobScheduling(self):
        while not self.scheduler.job_scheduling_queue.empty():
            process = self.scheduler.job_scheduling_queue.first()
            if not self.memory.fits(process.mem_required):
                break

            memAllocResult = self.memory.allocate(process)
            if not memAllocResult['success']:
                raise Exception('Could not allocate memory for process')
            process.state = 'Ready'
            process.priority = 1

            # Add this process to the MLFQ and remove it from the job queue.
            self.scheduler.job_scheduling_queue.remove()
            self.scheduler.process_scheduling_queue.new(process)

        # Run the process scheduling algorithm.
        self.runProcessScheduling()

    # Runs the process scheduling algorithm.
    def runProcessScheduling(self):
        # If process scheduling queue is empty, there is nothing to schedule. Return.
        if self.scheduler.process_scheduling_queue.isEmpty():
            return

        process = self.scheduler.process_scheduling_queue.getProcess(1)
        newPriority = 1
        if process is None:
            process = self.scheduler.process_scheduling_queue.getProcess(2)
            newPriority = 2

        running_process = self.cpu.running_process
        if running_process is None:
            # Remove job from the process scheduling queue.
            self.scheduler.process_scheduling_queue.removeProcess(newPriority)
            self.cpu.run_process(process)
            process.state = 'Running'

            jobId = int(process.process_id)
            self.recordStartTimeIfNecessary(jobId, self.currentTime())
        else:
            if running_process.priority > newPriority:
                # We need to preempt the current running process from the CPU.

                running_process.state = 'Ready'
                self.cpu.remove_process()

                # Add preempted job back to the process scheduling queue.
                self.scheduler.process_scheduling_queue.addProcess(running_process, running_process.priority)

                # Remove current job from the process scheduling queue.
                self.scheduler.process_scheduling_queue.removeProcess(newPriority)
                self.cpu.run_process(process)
                process.state = 'Running'

                jobId = int(process.process_id)
                self.recordStartTimeIfNecessary(jobId, self.currentTime())

    # Stores the time at which given job has started.
    def recordStartTimeIfNecessary(self, jobId, startTime):
        info = self.jobArrivalInfo[jobId]
        if 'startTime' not in info:
            info['startTime'] = startTime

    # Prints the current event along with the current time.
    def printEvent(self, event):
        stream = self.outputFile
        if stream is None:
            stream = sys.stdout

        stream.write('Event: ')
        stream.write(event)
        stream.write('   Time: ')
        stream.write(str(self.currentTime()))
        stream.write('\n')

    # If a process is about to be terminated or preempted, this function handles it.
    def processInternalEventsIfPossible(self):
        # Check and handle if an I/O completion is imminent.
        if len(self.scheduler.ioQueue) > 0:
            nextIOEventTuple = self.scheduler.ioQueue[0]
            ioCompTime = nextIOEventTuple[0]
            if self.currentTime() >= ioCompTime:
                # This job's I/O burst has completed. Remove it from the I/O queue and add it to ready queue.
                self.printEvent('C')

                ioEventDict = nextIOEventTuple[1]
                process = ioEventDict['process']
                process.state = 'Ready'
                process.priority = 1
                self.scheduler.process_scheduling_queue.addProcess(process, process.priority)
                self.scheduler.ioQueue.pop(0)
                self.runProcessScheduling()

        runningProcess = self.cpu.running_process
        if runningProcess is None:
            return

        if runningProcess.burst_time <= 0:
            # Job terminated. Remove the process from the CPU.
            self.cpu.remove_process()
            self.memory.deallocate(runningProcess.process_id)

            jobId = int(runningProcess.process_id)
            arrivalTime = self.jobArrivalInfo[jobId]['arrivalTime']
            memReq = int(runningProcess.mem_required)
            runTime = self.jobArrivalInfo[jobId]['runTime']
            startTime = self.jobArrivalInfo[jobId]['startTime']
            finishTime = self.currentTime()

            self.finishedList.append([
                jobId, arrivalTime, memReq, runTime, startTime, finishTime
            ])

            self.printEvent('T')
            self.runJobScheduling()

        timeElapsed = self.system_clock.current_time() - self.cpu.process_start_time
        if runningProcess.priority == 1:
            # Time limit for 1st level jobs.
            maxTime = 100
        elif runningProcess.priority == 2:
            # Time limit for 2nd level jobs.
            maxTime = 300
        else:
            maxTime = 0

        if timeElapsed >= maxTime:
            # Time quantum for this job expired.
            runningProcess.state = 'Ready'
            self.cpu.remove_process()
            runningProcess.priority = 2
            self.scheduler.process_scheduling_queue.addProcess(runningProcess, 2)

            self.printEvent('E')
            self.runProcessScheduling()

    # Runs the CPU for 1 time unit.
    def executeCPUCycle(self):
        runningProcess = self.cpu.running_process
        if runningProcess is not None:
            # CPU is not idle.
            runningProcess.burst_time -= 1

        # Update wait times for jobs waiting in the job scheduling queue.
        for process in self.scheduler.job_scheduling_queue:
            jobId = int(process.process_id)
            if jobId not in self.jobWaitTimeInfo:
                self.jobWaitTimeInfo[jobId] = 1
            else:
                self.jobWaitTimeInfo[jobId] += 1

    # Moves the currently running process to the I/O queue.
    def moveRunningProcessToIOQueue(self, ioBurstTime):
        process = self.cpu.running_process
        if process is None:
            raise Exception('Received I/O event while cpu is idle')

        process.state = 'Waiting'

        jobId = int(process.process_id)
        ioBurst = int(ioBurstTime)
        ioComp = self.currentTime() + ioBurst
        jobIOInfo = {
            'process' : process,
            'ioStart' : self.currentTime(),
            'ioBurst' : ioBurst,
            'ioComp'  : ioComp
        }

        # Preempt the running process from the CPU and put it in the I/O queue.
        # The I/O queue will be sorted based on the job completion time.
        self.scheduler.ioQueue.append((ioComp, jobIOInfo))
        self.scheduler.ioQueue.sort()
        self.cpu.remove_process()
        self.runProcessScheduling()

    # Called when a process wants to wait on a semaphore.
    def performWaitOnSemaphore(self, semaphoreNo):
        if semaphoreNo < 0 or semaphoreNo > 4:
            raise Exception('Invalid semaphore no: ', semaphoreNo)
        process = self.cpu.running_process
        if process is None:
            return

        semaphoreAcquired = self.scheduler.semaphores[semaphoreNo].acquire(process)
        if semaphoreAcquired:
            # Process acquired semaphore, keep running it.
            pass
        else:
            # Process could not acquire semaphore, preempt it.
            self.cpu.remove_process()
            self.runProcessScheduling()

    # Called when a process wants to signal a semaphore.
    def performSignalOnSemaphore(self, semaphoreNo):
        if semaphoreNo < 0 or semaphoreNo > 4:
            raise Exception('Invalid semaphore no: ', semaphoreNo)
        process = self.cpu.running_process

        unstuckProcess = self.scheduler.semaphores[semaphoreNo].release(process)

        if unstuckProcess is not None:
            # If there was a process waiting in the queue, remove it from the semaphore queue and
            # add it to the ready queue.

            unstuckProcess.priority = 1
            self.scheduler.process_scheduling_queue.addProcess(unstuckProcess, unstuckProcess.priority)
            self.runProcessScheduling()

    def display_status(self,info):
        pass
        # print(info)

    # Returns the current simulator time.
    def currentTime(self):
        return self.system_clock.total_ticks

    ###################################################################################################
    # Display-Related Functions
    ###################################################################################################

    # Writes the given string to the standard output without any extra characters (whitespace, newlines, etc).
    def writeStr(self, s):
        if self.outputFile is None:
            sys.stdout.write(s)
        else:
            self.outputFile.write(s)

    # Returns a string in which the given number is right-justified based on the given field width.
    # e.g: justified(123, 5) returns "  123".
    def justified(self, number, width):
        numPadding = int(width) - len(str(number))
        for i in range(numPadding):
            self.writeStr(' ')
        return str(number)

    # Rounds given float value to 3 decimal places.
    # The built-in round() function does not yield the exact results found in the output files. For example,
    # round(7357.236559139785, 3) returns 7357.237. However, the expected result (in the output file provided)
    # is 7357.236. What is deduced from this is that if the 4th digit after the decimal point is less than or
    # equal to 5, we take the first 3 decimal digits. If it is greater than 5, the 3rd digit is rounded up.
    # e.g: 7357.236559139785 -> 7357.236
    #      8551.881720430107 -> 8551.882
    def floatWith3Decimals(self, floatValue):
        intValue = int(floatValue * 1e4)
        roundUp = (intValue % 10 > 5)
        intValue = int(intValue / 10)
        if roundUp:
            intValue += 1
        return float(intValue) / 1e3

    # Prints the current state of the job scheduling queue.
    def printJobSchedulingQueue(self):
        self.writeStr('The contents of the JOB SCHEDULING QUEUE\n')
        self.writeStr('----------------------------------------\n')
        self.writeStr('\n')

        if self.scheduler.job_scheduling_queue.empty():
            self.writeStr('The Job Scheduling Queue is empty.\n')
        else:
            self.writeStr('Job #  Arr. Time  Mem. Req.  Run Time\n')
            self.writeStr('-----  ---------  ---------  --------\n')
            self.writeStr('\n')

            for process in self.scheduler.job_scheduling_queue:
                jobId = int(process.process_id)
                arrivalTime = self.jobArrivalInfo[jobId]['arrivalTime']
                memReq = int(process.mem_required)
                runTime = self.jobArrivalInfo[jobId]['runTime']

                self.writeStr(self.justified(jobId, 5))
                self.writeStr('  ');
                self.writeStr(self.justified(arrivalTime, 9))
                self.writeStr('  ');
                self.writeStr(self.justified(memReq, 9))
                self.writeStr('  ');
                self.writeStr(self.justified(runTime, 8))
                self.writeStr('\n')

    # Prints the current state of the given ready queue.
    def printReadyQueue(self, level):
        if level != 1 and level != 2:
            return

        queue = None
        if level == 1:
            self.writeStr('The contents of the FIRST LEVEL READY QUEUE\n')
            self.writeStr('-------------------------------------------\n')
            queue = self.scheduler.process_scheduling_queue.firstLevelQueue()
        else:
            self.writeStr('The contents of the SECOND LEVEL READY QUEUE\n')
            self.writeStr('--------------------------------------------\n')
            queue = self.scheduler.process_scheduling_queue.secondLevelQueue()
        self.writeStr('\n')

        if queue.empty():
            if level == 1:
                self.writeStr('The First Level Ready Queue is empty.\n')
            else:
                self.writeStr('The Second Level Ready Queue is empty.\n')
        else:
            self.writeStr('Job #  Arr. Time  Mem. Req.  Run Time\n')
            self.writeStr('-----  ---------  ---------  --------\n')
            self.writeStr('\n')

            for process in queue:
                jobId = int(process.process_id)
                arrivalTime = self.jobArrivalInfo[jobId]['arrivalTime']
                memReq = int(process.mem_required)
                runTime = self.jobArrivalInfo[jobId]['runTime']

                self.writeStr(self.justified(jobId, 5))
                self.writeStr('  ')
                self.writeStr(self.justified(arrivalTime, 9))
                self.writeStr('  ')
                self.writeStr(self.justified(memReq, 9))
                self.writeStr('  ')
                self.writeStr(self.justified(runTime, 8))
                self.writeStr('\n')

    # Prints the current states of both ready queues.
    def printReadyQueues(self):
        self.printReadyQueue(1)
        self.writeStr('\n\n')
        self.printReadyQueue(2)

    # Prints the current state of the I/O wait queue.
    def printIOWaitQueue(self):
        self.writeStr('The contents of the I/O WAIT QUEUE\n')
        self.writeStr('----------------------------------\n')
        self.writeStr('\n')

        if len(self.scheduler.ioQueue) == 0:
            self.writeStr('The I/O Wait Queue is empty.\n')
        else:
            self.writeStr('Job #  Arr. Time  Mem. Req.  Run Time  IO Start Time  IO Burst  Comp. Time\n')
            self.writeStr('-----  ---------  ---------  --------  -------------  --------  ----------\n')
            self.writeStr('\n')

            for ioEventTuple in self.scheduler.ioQueue:
                ioComp = ioEventTuple[0]
                infoDict = ioEventTuple[1]
                process = infoDict['process']
                jobId = int(process.process_id)

                arrivalTime = self.jobArrivalInfo[jobId]['arrivalTime']
                memReq = int(process.mem_required)
                runTime = self.jobArrivalInfo[jobId]['runTime']
                ioStartTime = infoDict['ioStart']
                ioBurst = infoDict['ioBurst']
                ioComp = infoDict['ioComp']

                self.writeStr(self.justified(jobId, 5))
                self.writeStr('  ')
                self.writeStr(self.justified(arrivalTime, 9))
                self.writeStr('  ')
                self.writeStr(self.justified(memReq, 9))
                self.writeStr('  ')
                self.writeStr(self.justified(runTime, 8))
                self.writeStr('  ')
                self.writeStr(self.justified(ioStartTime, 13))
                self.writeStr('  ')
                self.writeStr(self.justified(ioBurst, 8))
                self.writeStr('  ')
                self.writeStr(self.justified(ioComp, 10))
                self.writeStr('\n')

        # jobId = int(process.process_id)
        # ioBurst = int(ioBurstTime)
        # ioComp = self.currentTime() + ioBurst
        # jobIOInfo = {
        #     'process' : process,
        #     'ioStart' : self.currentTime(),
        #     'ioBurst' : ioBurst,
        #     'ioComp'  : ioComp
        # }
        # self.scheduler.ioQueue.put((ioComp, jobIOInfo))

    # Prints the current state of the given semaphore.
    def printSemaphore(self, semaphoreNo):
        if semaphoreNo < 0 or semaphoreNo > 4:
            return

        if semaphoreNo == 0:
            self.writeStr('The contents of SEMAPHORE ZERO\n')
            self.writeStr('------------------------------\n')
        elif semaphoreNo == 1:
            self.writeStr('The contents of SEMAPHORE ONE\n')
            self.writeStr('-----------------------------\n')
        elif semaphoreNo == 2:
            self.writeStr('The contents of SEMAPHORE TWO\n')
            self.writeStr('-----------------------------\n')
        elif semaphoreNo == 3:
            self.writeStr('The contents of SEMAPHORE THREE\n')
            self.writeStr('-------------------------------\n')
        else:
            self.writeStr('The contents of SEMAPHORE FOUR\n')
            self.writeStr('------------------------------\n')
        self.writeStr('\n')
        self.writeStr('The value of semaphore ')
        self.writeStr(str(semaphoreNo))
        self.writeStr(' is ')

        semaphoreValue = self.scheduler.semaphores[semaphoreNo].value
        self.writeStr(str(semaphoreValue))
        self.writeStr('.\n')
        self.writeStr('\n')

        semaphoreWaitQueue = self.scheduler.semaphores[semaphoreNo].waitQueue
        if semaphoreWaitQueue.empty():
            self.writeStr('The wait queue for semaphore ')
            self.writeStr(str(semaphoreNo))
            self.writeStr(' is empty.\n')
        else:
            for process in semaphoreWaitQueue:
                self.writeStr(str(process.process_id))
                self.writeStr('\n')

    # Prints the current states of all 5 semaphores.
    def printSemaphores(self):
        numSemaphores = 5
        for i in range(numSemaphores - 1):
            self.printSemaphore(i)
            self.writeStr('\n\n')
        self.printSemaphore(numSemaphores - 1)

    # Prints the current state of the CPU.
    def printCPUStatus(self):
        self.writeStr('The CPU  Start Time  CPU burst time left\n')
        self.writeStr('-------  ----------  -------------------\n')
        self.writeStr('\n')

        runningProcess = self.cpu.running_process
        if runningProcess is not None:
            self.writeStr(self.justified(int(runningProcess.process_id), 7))
            self.writeStr('  ')
            jobId = int(self.cpu.running_process.process_id)
            startTime = self.jobArrivalInfo[jobId]['startTime']
            self.writeStr(self.justified(startTime, 10))
            self.writeStr('  ')
            self.writeStr(self.justified(runningProcess.burst_time, 19))
            self.writeStr('\n')
        else:
            self.writeStr('The CPU is idle.\n')

    # Prints the current state of the finished list.
    def printFinishedList(self, isFinal=False):
        if isFinal:
            self.writeStr('The contents of the FINAL FINISHED LIST\n')
            self.writeStr('---------------------------------------\n')
        else:
            self.writeStr('The contents of the FINISHED LIST\n')
            self.writeStr('---------------------------------\n')
        self.writeStr('\n')

        if len(self.finishedList) == 0:
            self.writeStr('The Finished List is empty.\n')
        else:
            self.writeStr('Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time\n')
            self.writeStr('-----  ---------  ---------  --------  ----------  ---------\n')
            self.writeStr('\n')

            for finishedJob in self.finishedList:
                jobId = finishedJob[0]
                self.writeStr(self.justified(jobId, 5))
                self.writeStr('  ')

                arrivalTime = finishedJob[1]
                self.writeStr(self.justified(arrivalTime, 9))
                self.writeStr('  ')

                memReq = finishedJob[2]
                self.writeStr(self.justified(memReq, 9))
                self.writeStr('  ')

                runTime = finishedJob[3]
                self.writeStr(self.justified(runTime, 8))
                self.writeStr('  ')

                startTime = finishedJob[4]
                self.writeStr(self.justified(startTime, 10))
                self.writeStr('  ')

                finishTime = finishedJob[5]
                self.writeStr(self.justified(finishTime, 9))
                self.writeStr('\n')

    # Prints the current state of the system memory.
    def printMemoryStatus(self):
        self.writeStr('There are ')
        self.writeStr(str(self.memory.available()))
        self.writeStr(' blocks of main memory available in the system.\n')

    # Prints the current state of the entire simulator.
    def printSimulatorStatus(self):
        self.writeStr('\n')
        self.writeStr('************************************************************\n')
        self.writeStr('\n')
        self.writeStr('The status of the simulator at time ')
        self.writeStr(str(self.currentTime()))
        self.writeStr('.\n')
        self.writeStr('\n')

        self.printJobSchedulingQueue()
        self.writeStr('\n\n')
        self.printReadyQueues()
        self.writeStr('\n\n')
        self.printIOWaitQueue()
        self.writeStr('\n\n')
        self.printSemaphores()
        self.writeStr('\n\n')
        self.printCPUStatus()
        self.writeStr('\n\n')
        self.printFinishedList()
        self.writeStr('\n\n')
        self.printMemoryStatus()
        self.writeStr('\n')

    # Calculates and returns the average turnout time.
    def calculateAverageTurnoutTime(self):
        totalTurnaroundTime = float(0)
        for finishedJob in self.finishedList:
            arrivalTime = int(finishedJob[1])
            finishTime = int(finishedJob[5])
            totalTurnaroundTime += (finishTime - arrivalTime)
        return totalTurnaroundTime / len(self.finishedList)

    # Calculates and returns the average job scheduling wait time.
    def calculateAverageJobSchedulingWaitTime(self):
        totalJobSchedulingWaitTime = float(0)
        for finishedJob in self.finishedList:
            jobId = int(finishedJob[0])
            jobSchedulingWaitTime = self.jobWaitTimeInfo.get(jobId)

            if jobSchedulingWaitTime is not None:
                totalJobSchedulingWaitTime += jobSchedulingWaitTime
        return totalJobSchedulingWaitTime / len(self.finishedList)

    def __str__(self):
        """
        Visual dump of class state.
        """
        return my_str(self)

###################################################################################################
# Test Functions
###################################################################################################

def run_tests():
    print("############################################################")
    print("Running ALL tests .....\n")

    test_process_class()
    test_class_clock()
    test_cpu_class()
    test_memory_class()
    test_semaphore_class()

if __name__ == '__main__':

    input_a = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_a.txt'
    input_b = os.path.dirname(os.path.realpath(__file__)) + '/input_data/jobs_in_b.txt'
    input_c = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_c.txt'

    inputs = [input_a, input_b, input_c]
    outputs = ['output_a.txt', 'output_b.txt', 'output_c.txt']

    for i in range(len(inputs)):
        input = inputs[i]
        output = outputs[i]
        S = Simulator(input_file=input, output_file=output)

        print("Written to output file: '" + output + "'");
        S.outputFile.close()
