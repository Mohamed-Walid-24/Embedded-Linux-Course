# datetime
## strftime() 
The `strftime()` method returns a [string](https://www.programiz.com/python-programming/string) representing date and time using [date](https://www.programiz.com/python-programming/datetime#date), time or datetime object.
```python
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	
```
![[Pasted image 20240625155330.png]]
[Cheat Sheet 
](https://strftime.org/)

| Code  | Example                   | Description                                                                                                                                                                              |
| ----- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `%a`  | `Sun`                     | Weekday as locale’s abbreviated name.                                                                                                                                                    |
| `%A`  | `Sunday`                  | Weekday as locale’s full name.                                                                                                                                                           |
| `%w`  | `0`                       | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.                                                                                                                        |
| `%d`  | `08`                      | Day of the month as a zero-padded decimal number.                                                                                                                                        |
| `%-d` | `8`                       | Day of the month as a decimal number. (Platform specific)                                                                                                                                |
| `%b`  | `Sep`                     | Month as locale’s abbreviated name.                                                                                                                                                      |
| `%B`  | `September`               | Month as locale’s full name.                                                                                                                                                             |
| `%m`  | `09`                      | Month as a zero-padded decimal number.                                                                                                                                                   |
| `%-m` | `9`                       | Month as a decimal number. (Platform specific)                                                                                                                                           |
| `%y`  | `13`                      | Year without century as a zero-padded decimal number.                                                                                                                                    |
| `%Y`  | `2013`                    | Year with century as a decimal number.                                                                                                                                                   |
| `%H`  | `07`                      | Hour (24-hour clock) as a zero-padded decimal number.                                                                                                                                    |
| `%-H` | `7`                       | Hour (24-hour clock) as a decimal number. (Platform specific)                                                                                                                            |
| `%I`  | `07`                      | Hour (12-hour clock) as a zero-padded decimal number.                                                                                                                                    |
| `%-I` | `7`                       | Hour (12-hour clock) as a decimal number. (Platform specific)                                                                                                                            |
| `%p`  | `AM`                      | Locale’s equivalent of either AM or PM.                                                                                                                                                  |
| `%M`  | `06`                      | Minute as a zero-padded decimal number.                                                                                                                                                  |
| `%-M` | `6`                       | Minute as a decimal number. (Platform specific)                                                                                                                                          |
| `%S`  | `05`                      | Second as a zero-padded decimal number.                                                                                                                                                  |
| `%-S` | `5`                       | Second as a decimal number. (Platform specific)                                                                                                                                          |
| `%f`  | `000000`                  | Microsecond as a decimal number, zero-padded to 6 digits.                                                                                                                                |
| `%z`  | `+0000`                   | UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).                                                                                                         |
| `%Z`  | `UTC`                     | Time zone name (empty string if the object is naive).                                                                                                                                    |
| `%j`  | `251`                     | Day of the year as a zero-padded decimal number.                                                                                                                                         |
| `%-j` | `251`                     | Day of the year as a decimal number. (Platform specific)                                                                                                                                 |
| `%U`  | `36`                      | Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.         |
| `%-U` | `36`                      | Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific) |
| `%W`  | `35`                      | Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.         |
| `%-W` | `35`                      | Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific) |
| `%c`  | `Sun Sep 8 07:06:05 2013` | Locale’s appropriate date and time representation.                                                                                                                                       |
| `%x`  | `09/08/13`                | Locale’s appropriate date representation.                                                                                                                                                |
| `%X`  | `07:06:05`                | Locale’s appropriate time representation.                                                                                                                                                |
| `%%`  | `%`                       | A literal '%' character.                                                                                                                                                                 |
# Class
## Constructor 
`__init__`
```python
class Person:
    def __init__(self, name):
        self.name = name;
        print(f"{self.name} has been created")

p=Person("mohamed")
```
![[Pasted image 20240625222428.png]]
## Destructor
`__del__`
 - Code_1:
```python
class Person:
    def __init__(self, name):
        self.name = name;
        print(f"{self.name} has been created")
    
    def __del__(self):
        print(f"{self.name} has been deleted")

p=Person("mohamed")
```
![[Pasted image 20240625223855.png]]
The **destructor** is executed automatically because the program ends
- Code_2:
```python
class Person:
    def __init__(self, name):
        self.name = name;
        print(f"{self.name} has been created")
    
    def __del__(self):
        print(f"{self.name} has been deleted")

p=Person("mohamed")
p2=Person("walid")
```
![[Pasted image 20240625224209.png]]
The **destructor** is executed automatically because the program ends
	 - **Mohamed** is deleted first then  **Walid**
- Code_3:
```python
class Person:
    def __init__(self, name):
        self.name = name;
        print(f"{self.name} has been created")
    
    def __del__(self):
        print(f"{self.name} has been deleted")

p=Person("mohamed")
p2=Person("walid")

del p2
print("End of program")
```
![[Pasted image 20240625224720.png]]
	- **Walid** is deleted first because using `del p2` 
## str
When you want to define a string representation of a class object in Python, you can use the `__str__` method. This method should return a string that provides a human-readable representation of the object’s state. The `__str__` method is called automatically when an object is used in a string context, such as when it is printed, or when the built-in `str()` function is called on the object.
```python
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

print(MyClass("Mohamed",20))
```
![[Pasted image 20240625225230.png]]
## doc
- In Python, `__doc__` is a special attribute that is used to store the docstring of a class, function, or module. A docstring is a string literal that occurs as the first statement in a function, class, or module definition. It is used to provide documentation for the code, explaining what the code does, what it returns, and what parameters it takes.
- You can use `help(Vehicles)` to show all the docs of the class and methods together
```python
class Vehicles:
    """
    The Vehicles class represents a collection of vehicles.

    Attributes:
        vehicles (list): A list of vehicle objects.
        num_vehicles (int): The number of vehicles in the collection.

    Methods:
        add_vehicle( vehicle ): Adds a new vehicle to the collection.
        remove_vehicle( vehicle ): Removes a vehicle from the collection.
        get_vehicles(): Returns a list of all vehicles in the collection.
    """

    def __init__(self):
        """
        Initializes the Vehicles class.

        Args:
            None

        Returns:
            None
        """
        self.vehicles = []
        self.num_vehicles = 0

    def add_vehicle(self, vehicle):
        """
        Adds a new vehicle to the collection.

        Args:
            vehicle (Vehicle): The vehicle to add.

        Returns:
            None
        """
        self.vehicles.append(vehicle)
        self.num_vehicles += 1

    def remove_vehicle(self, vehicle):
        """
        Removes a vehicle from the collection.

        Args:
            vehicle (Vehicle): The vehicle to remove.

        Returns:
            None
        """
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            self.num_vehicles -= 1

    def get_vehicles(self):
        """
        Returns a list of all vehicles in the collection.

        Returns:
            list: A list of vehicle objects.
        """
        return self.vehicles

print(Vehicles.__doc__)
print("-"*30)
print(Vehicles.add_vehicle.__doc__)
```
![[Pasted image 20240625230141.png]]
# Tasks
## Task_1
Using **Pyautogui** to open Emails and change Emails from unread to
read
```python
# Using Pyautogui to open Emails and change Emails from unread to read
import pyautogui as pg  
import webbrowser  
import time  
  
gmail = "https://mail.google.com/mail/u/0/#inbox"  
webbrowser.open(gmail)  
  
time.sleep(5)  
c_1 = (474, 256)  
time.sleep(1)  
c_2 = (594, 294)  
  
pg.click(c_1)  
pg.click(c_2)
```
## Task_2
![[Pasted image 20240626001226.png]]
```python
# Write a python program to get the command-line arguments 

import sys

arguments = sys.argv
print("This is the name/path of the script: ",arguments[0])
print(f"('Number of arguments:', {len(arguments)})")
print("('Argument List:',\"", arguments,'")')
```
