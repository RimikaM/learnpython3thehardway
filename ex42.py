# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:38:02 2017

@author: rimikamajumdar
"""

# Exercise 42: Is-A, Has-A, Objects, and Classes

## Animal class is-a object
class Animal(object):
    pass

## Dog class is-a Animal
class Dog(Animal):
    
    def __init__(self,name):
        ## Dog has-a name attribute and set it to name
        self.name = name
        
## Cat class is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat has-a name attribute and set it to name
        self.name = name
        
## Person class is-a object
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name attribute and set it to name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None
        
## 
class Employee(Person):
    
    def __init__(self, name, salary):
        ## How you can run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute and set it to salary
        self.salary = salary
        
## Fish class is-a object
class Fish(object):
    pass

## Salmon class is-a fish
class Salmon(Fish):
    pass

## Halibut class is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog with the name "Rover"
## rover is an instance of the class Dog
rover = Dog("Rover")

## satan is-a Cat with the name "Satan"
satan = Cat("Satan")

## mary is-a Person with the name "Mary"
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee with the name "Frank" and salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is an instance of the class Fish
## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()