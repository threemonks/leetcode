"""
1114. Print in Order
Easy

783

139

Add to List

Share
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.



Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""
"""
Lock
"""
from threading import Lock


class Foo0:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock1:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock2:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


"""
Binary Semaphore

Binary Semaphore is just a wrapper on Lock, as semaphore is internally implemented via Lock

Lock vs Semaphore

https://www.developerhelps.com/lock-vs-semaphore/

1. Locks cannot be shared between more than one thread processes but semaphores can have multiple processes of the same thread.
2. Only one thread works with the entire buffer at a given instance of time but semaphores can work on different buffers at a given time.
3. Lock takes care of the locking system however semaphore takes care of the signal system.
4. we consider lock as an object whereas we consider semaphore as an integer with values.
5. The lock has 2 principles that are acquire and release however semaphore has two principles which are wait() and signal().
6. The lock does not have any subtypes of its own however semaphore has 2 subtypes. They are binary semaphores and counting semaphores.
7. Locks can have multiple programs at a time but it cannot perform them all at the same time. Whereas semaphores can have multiple programs and can perform them all at the same time. These are the basic points under lock vs semaphore.

mistakes:
1. Semaphore is implicitly locked at time of creation, while Lock has to be explicitly acquired to lock it.
"""
from threading import Semaphore


class Foo:
    def __init__(self):
        self.semaphore1 = Semaphore(0)
        self.semaphore2 = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.semaphore1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.semaphore1:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.semaphore2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.semaphore2:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
