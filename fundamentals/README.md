# Core Concepts of OOP 

* [Encapsulation](#encapsulation)
* [Abstraction](#abstraction) 
* [Inheritance](#inheritance)
* [Polymorphism](#polymorphism)


<h2 id="encapsulation"> 1. Encapsulation (data hiding) </h2>
The concept of data hiding and restricting access to an object's data to the members of the class. For example, declaring private or protected class variables allows the variables to only be accessible within the scope of the class/subclass. We can then access this private/ protected data from outside the class through getter/setter access methods.

### This allows us to 
* Ensure that not just anyone can directly access and modify class state, for example when it contains sensitive information
* Use the program in an abstract & simpler manner without worrying about the implementation details 
* Make sure no accidental modifications to data occur, since the object's state can only be modified through the object's access methods
* Successfully bundle the data and object as a single entity!

### In Python 
To declare a variable as **protected**, prefix the variable with an underscore. To declare a variable as **private**, prefix the variable with double underscores. 

```
class Example:
    def __init__(self):
        self._protected_data = 'This is protected!'
        self.__private_data = 'This is very private!'

    # Only this method can directly modify private data
    def set_personal_data(self, data):
        self.__private_data = data 
    
    def get_personal_data(self):
        return self.__private_data

example_obj = Example()
example_obj.private_data = 'Not so personal' # Illegal
print(example_obj.private_data) # Raises AttributeError
print(example_obj.get_personal_data()) # Prints 'This is very private!'

```
<h2 id="abstraction"> 2. Abstraction (implementation/detail hiding) </h2>
The goal of abstraction is to simplify user interaction with the program by hiding the complexities of the program. In other words, the user does not need to know all the specifics of how the program works; they just need a high level access to do what they need to do without worrying about the implementation details. 

### This allows us to 
* Provide a simple and intuitive interface to users (given that it's designed well)
* Reduce code duplication and enhance reusability (i.e, when we generalize with an interface that can be inherited by multiple classes)
* Can visualize and break a complicated system down into manageable abstractions 

### In Python 
```
class Computer:

    def turn_on(self):
        self.__start_boot_seq()

    # doesn't need to be known by user
    def __start_boot_seq(self):
        self.__load_os()

    # doesn't need to be known by user
    def __load_os(self):
        ...

computer = Computer()
computer.turn_on() # user only needs to see this method and should not have to worry about implementation details
```
<h2 id="inheritance"> 3. Inheritance (relationship modelling - IS A relationship) </h2>
In the real world, there are many common attributes and functions among objects. For example, although every person has their own distinct traits, there are many commonalities we share with eachother. While we may eat differently and enjoy different types of food, we all need to eat to survive. Inheritance simply refers to this notion of shared commonalities and ways of modelling them in code. With this tool, we can define a child (subclass) that inherits from a parent (super class).

### This allows us to 
* Enhance reusability of code  
* Enhance readability of code since:
    * We repeat less code 
    * We model real life objects and relationships in an intuitive manner 

### In Python 
``` 
class Parent:
    def __init__(self, name):
        ...

class Child(Parent):
    def __init__(self, name):
        Parent.__init__(self, name)
        # OR 
        super().__init__(name)
```
<h2 id="polymorphism"> 4. Polymorphism </h2>
This is formally defined as the ability of an object to take on many forms. In real life, a person may be a mother and at the same time an employee or a student. It's clear that it could quickly get overwhelming to create a different framework for each differing type of object, especially since they may have commonalities. We can tackle this issue through polymorphism. 

### 1. Method Overriding (inheritance required) - methods have the same name and signatures
We can override the behaviour of an existing method in a parent class and define a behaviour specific to our child based on its own characteristics. 

### In Python 
```
class Parent:
    def __init__(self, name):
        ...

    # will be invoked if called from parent class
    def say(self, text):
        print(f"I'm a parent named {self.name} and I'm saying {text}")

class Child(Parent):
    def __init__(self, name):
        ...  

    # will be invoked if called from child class
    def say(self, text):
        print(f"I'm a child named {self.name} and I'm saying {text}")
```

### 2. Method Overloading - methods have the same name but varying signatures
We can extend the behaviour of a method by capturing its variances through method overrloading. Here, we can create multiple methods with the same name but varying signatures, in order to accomodate the different combinations of data types it could accept. 

### In Python 

No such thing as method overloading in Python. We could include two methods with same name and varying signatures in the same class but Python will just use the latest defined method.

```
class Parent:
    def __init__(self, name):
        ...

    # Parent("bob").say("sample text") will raise error
    def say(text):
        print(f"I'm a parent named {self.name} saying {text}")

    # Parent("bob").say("sample text", 3) will work since it's defined as the 'latest'
    def say(text, amount):
        for i in range(amount):
            print(f"I'm a parent named {self.name} saying {text} over and over again!")

```
However, we could still do something like:

``` 
class Parent:
    def __init__(self, name):
        ...
    
    # Parent("bob").say("hi") => "I'm a parent named bob saying hi"
    # Parent("bob").say("hi", 3) => I'm a parent named bob saying hi over and over again!
    #                            => I'm a parent named bob saying hi over and over again!
    #                            => I'm a parent named bob saying hi over and over again!
    def say(text, *args):
        if args:
            for i in range(args[0]):
                print(f"I'm a parent named {self.name} saying {text} over and over again!")
        else:
            print(f"I'm a parent named {self.name} saying {text}")

```
### This allows us to 
* Enhance reusability of code  
* Enhance readability of code since:
    * We repeat less code, since a single variable could represent different object types 
    * Through overriding, child class can write their own implementation without affecting the parent class
* Enhance flexibility of code since: 
    * Through overloading, you could call a method with different data types and get your specific, desired behaviour. 

