"""
Package installer

We are in charge of designing a system to install packages.
We are required to support the installation of a package and
all of its dependent packages.

Here is an example of a package structure that we would need to install:

A depends on B, C
B depends on D, E, F
C depends on F
F depends on G

Define what a package looks like and code a solution to this problem.

Lets assume the installation logic for a singular package will be implemented
by the appropriate platform teams. We just need to agree on an interface.

----

follow up questions:

- if the package installation failed, can we rollback it? - we should rollback
- how to identify circular dependency? - topological sort, if there's circular dependency, then topological sort will fail/detect cycle
- how to deal with different platform variant(os/lang version/etc.)? - add variations (parameters into each package, or with each package class, add attribute variants os/lange/version
- how to deal with version conflict? - introduce dependencies with version included, i.e., A ver 3.0 requires B ver > 2.0


// you don't need to implement this, assume you can get an instance from somewhere
interface PackageInstaller {
  install(pkg);
  uninstall(pkg);
}

a) You have a package repository in which there are dependencies between packages for building like package A has to be built before package B. If you are given dependencies between the packages and package name x, we have find the build order for x.
Ex: A → {B,C}
B → {E}
C → {D,E,F}
D → {}
F → {}
G → {C}

For package A, build order is E B F D C A (may not unique)

Given a function Set getDependencies (Package packageName) which returns a set of dependencies for a given package name, write a method List getBuildOrder(Package packageName) which returns the build order

b) How would you handle cyclic dependencies (Algo only)

One Leetcode User comements:
They weren't looking for something very specific. Instead they were testing to see if you know what a package is, how it operates, with your language of choice, etc.
For instance in python I would have some sort of settings file with things like library location urls, proxy settings, etc. Then I would instantiate a dir within the project and call out to each library location in turn via API to try to populate that directory with contents. This would then map to a location within the current working directory of the project i'm working within so the packages can be imported.

"""
"""
Topological sort
"""

class Package:
    def init(self, id, os, lang, version, url):
        self.id = 0
        self.os = os
        self.lang = lang
        self.version = version
        self.url = url
        self.children = []

from collections import defaultdict, deque

class PackageInstaller:
    def __init__(self, dependencies):
        self.dependencies = dependencies

    def install_package(self, pkg):
        print('installed one package %s' % pkg)

    def uninstall_package(self, pkg):
        print('uninstalled one package %s' % pkg)

    def order_packages(self):
        adj_list = defaultdict(list)

        vertices = set()
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for i, deps in self.dependencies.items():
            vertices.add(i)
            for j in deps:
                vertices.add(j)
                adj_list[j].append(i)
                indegree[i] += 1
                outdegree[j] += 1

        # toplogical sort start with nodes with indegree = 0
        q = deque()
        for v in vertices:
            if indegree[v] == 0:
                q.append(v)

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in adj_list[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(res) == len(vertices):
            return res
        else:
            return -1

    def run(self):
        ordered_packages = self.order_packages()
        for pkg in ordered_packages:
            try:
                self.install_package(pkg)
            except Exception:
                self.uninstall_package(pkg)
                break
def main():
    """
A depends on B, C
B depends on D, E, F
C depends on F
F depends on G
    """
    dependencies = {0: [1, 2], 1: [3,4,5], 2: [5], 5: [6]}
    pi = PackageInstaller(dependencies)
    pi.run()

if __name__ == '__main__':
    main()
