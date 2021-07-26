"""
1115. Print FooBar Alternately
Medium

397

30

Add to List

Share
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will call bar(). Modify the given program to output "foobar" n times.



Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""
"""
Using Lock
"""
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockfoo = Lock()
        self.lockbar = Lock()
        self.lockbar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lockfoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lockbar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lockbar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lockfoo.release()


"""
Using threading.Event

threading.Condition is a combination of a Lock and an Event (simplistically)

An Event manages an internal flag that callers can either set() or clear(). Other threads can wait() for the flag to be set(). Note that the wait() method blocks until the flag is true.

"""
from threading import Event


class FooBar1:
    def __init__(self, n):
        self.n = n
        self.fooprinted = Event()
        self.barprinted = Event()
        self.barprinted.set()  # print foo first

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.barprinted.wait()
            self.barprinted.clear()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.fooprinted.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.fooprinted.wait()
            self.fooprinted.clear()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.barprinted.set()
