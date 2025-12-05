#🖥️Opearting-System-Project
This repository contains implementations and explanations of various CPU scheduling algorithms, which are essential for operating systems to manage process execution efficiently. The algorithms included cover different strategies to optimize CPU utilization, waiting time, and turnaround time.

##📌Algorithms Included
###🗂️ 1. First Come, First Served (FCFS)
- The simplest scheduling algorithm.  
- Processes are executed in the order they arrive in the ready queue.  
- **Non-preemptive:** once a process starts execution, it cannot be interrupted.  

###🗂️2. Shortest Job First (SJF)
- Selects the process with the shortest burst time to execute next.  
- **Non-Preemptive SJF:** A process runs to completion once selected.  
- **Preemptive SJF (Shortest Remaining Time First):** A running process can be preempted if a new process with a shorter burst time arrives.  

###🗂️3. Priority Scheduling
- Each process is assigned a priority.  
- CPU is allocated to the process with the **highest priority**.  
- Can be **preemptive** or **non-preemptive** depending on implementation.  

###🗂️ 4. Round Robin (RR)
- Each process is assigned a fixed **time slice (quantum)**.  
- Processes are executed in a **cyclic order**, allowing fair CPU sharing.  
- Reduces waiting time for short processes.  

###🗂️ 5. Multilevel Queues
- Processes are grouped into multiple queues based on **priority** or **type**.  
- Each queue can have its own scheduling algorithm.  
- CPU allocation among queues is managed according to a defined policy.  


