"""
abstract classes are classes that cannot be instantiated. This is the case because abstract classes do not specify the implementation of features. Rather, you only specify the method signatures and (sometimes) property types, and every child class must provide its own implementation

"""

from abc import ABC, abstractmethod

class AbstractRenderer(ABC):
    @abstractmethod
    def render(self, data):
        raise NotImplementedError()

class ThreeDRenderer(AbstractRenderer):
    def render(self, data):
        print(data)

renderer = ThreeDRenderer()
renderer.render('some_data')

class AbstractVehicle(ABC):
    @property
    @abstractmethod
    def engine(self):
        raise NotImplementedError()

    @engine.setter
    @abstractmethod
    def engine(self, _engine):
        raise NotImplementedError()


class Car(AbstractVehicle):
    _engine = ''

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, new_engine):
        self._engine = new_engine.upper()


car = Car()
car.engine = 'v8 3.2 liters'
print(car.engine)

"""
Metaclasses are classes for classes. Metaclasses provide blueprints for classes creation. Every class has a metaclass by default (it is called type). To create a custom metaclass, you will have to inherit type:

"""

class CustomMeta(type):
    def __new__(cls, clsname, bases, attrs):
        if 'render' not in attrs.values():
            raise Exception()
        return type(clsname, bases, attrs)

class SomeClass(metaclass=CustomMeta):
    def render(self):
        pass