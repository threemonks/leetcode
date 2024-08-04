## Lock vs Mutex vs Semaphore

* Lock - lock allows only one thread to enter the part that's locked and the lock is not shared with any other processes
* Mutex - same as lock but can be system wide (shared by multiple processes)
* Semaphore - same as mutex but allows x number of threads to enter, this can be used for example to limit number of cpu, io, or ram intensive tasks running at the same time.

