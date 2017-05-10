# Operating Systems CPU Scheduling Simulation Project

## Team Members

| Name     | Email   | Github Username |
|----------|---------|-----------------|
| SAIKIRAN REDDY NAGULAPALLY  | saikiranreddy791@outlook.com| saikiranreddy-nagulapally |
| THIRUPATHI REDDY PARSHURAMGARI  | thirupathi.idks126@gmail.com | thirupathireddy-parshuramgari |
| SINDHU THANDRA|sindhu.thandra94@gmail.com |Sindhuthandra|


## Contributions of each member

#### THIRUPATHI REDDY PARSHURAMGARI 

* Set up the project.

* Fixed minor issues (typos, etc.) to get the project to compile.

* Started working on the job and process scheduling code.

* Started implementing code that prints the current status of the simulation (`writeStatus()` method).

* Implemented code that handles **'A'** (new job), **'D'** (display status), **'E'** (time quantum expiration) and **'T'** (job termination) events.

* ***Time spent working: Approximately   12 days.***
#### SAIKIRAN REDDY NAGULAPALLY 

* Continued working on the implementation of the `writeStatus()` method. Added code that displays the current job scheduling and ready queues.

* Added code that displays the I/O and finished queues, and semaphores.

* Added code that computes and prints average turnout and job scheduling wait times (not considering I/O or semaphores).

* Added code that prints the total memory available in the system.

* Implemented code that handles I/O operations (**'I'** and **'C'** events).

* Modified the writeStatus() method to print the current status of the I/O wait queue.

* Modified time average turnout and job scheduling wait time calculating methods to make sure numbers are formatted properly.

* ***Time spent working: Approximately  15 days.***

#### SINDHU THANDRA

* Implemented semaphore-related code (acquiring, releasing, queueing, signaling, etc).

* Implemented **'W'** (wait on a semaphore) and **'S'** (signal on a semaphore) events.

* Cleaned up the code (refactored/restructured stuff, wrote additional comments, etc).

* Modified the code so that output is printed to files, rather than standard output (stdout).

* Created READEME.MD 

* ***Time spent working: Approximately  10 days.***

## Participation Piechart
![Participation Pie chart](http://i63.tinypic.com/2zfqqyr.png)

## File structure of the project

*Note: Our team modified only the file `assignments/scheduling/simulation.py` in the project. Everything else is part of the starter project provided.*

* assignments
   * cpu_simulation
     * `simulation.py`
     * components
       * \_\_pycache\_\_
         * accounting.cpython-34.pyc
         * accounting.cpython-36.pyc
         * clock.cpython-34.pyc
         * clock.cpython-36.pyc
         * cpu.cpython-34.pyc
         * cpu.cpython-36.pyc
         * fifo.cpython-34.pyc
         * fifo.cpython-36.pyc
         * memory.cpython-34.pyc
         * memory.cpython-36.pyc
         * process.cpython-34.pyc
         * process.cpython-36.pyc
         * semaphore.cpython-34.pyc
         * semaphore.cpython-36.pyc
         * sim_components.cpython-34.pyc
         * sim_components.cpython-36.pyc
       * `accounting.py`
       * accounting.pyc
       * `clock.py`
       * clock.pyc
       * `cpu.py`
       * cpu.pyc
       * docs
         * \_\_init\_\_.html
         * Accounting.html
         * Clock.html
         * Cpu.html
         * Fcfs.html
         * Memory.html
         * MyFuncs.html
         * Process.html
         * pycco.css
         * SimSemaphore.html
       * `fifo.py`
       * fifo.pyc
       * `memory.py`
       * memory.pyc
       * `process.py`
       * process.pyc
       * README.md
       * `run_all.py`
       * `semaphore.py`
       * semaphore.pyc
       * `sim_components.py`
       * sim_components.pyc
       * temp.out
     * csv.m.html
     * docs
       * conf.html
       * cpu_sim.html
       * pycco.css
       * simulation_flow.png
       * source
         * conf.rst
         * cpu_sim.rst
         * modules.rst
       * test_mod.html
     * input_data
       * jobs_c.txt
       * jobs_in_a.txt
       * jobs_in_b.txt
       * jobs_in_c.txt
       * jobs_in_test.txt
       * jobs_out_a.txt
       * jobs_out_b.txt
       * jobs_out_c.txt
       * processes.txt
     * output_a
     * output_b
     * output_c
     * README.md

