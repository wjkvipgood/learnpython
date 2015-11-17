#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):

    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):
    
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    
    def run(self):
        print('Tortoise is running slowly...')

# Timer is a file-like object
class Timer(object):

    def run(self):
        print('Start...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
