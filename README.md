# AirBnB Clone
![N|Solid](https://i.imgur.com/BwWHZVK.png)
# Description of this project
The goal of thi project is to deploy on a server a simple copy of the AirBnB website.

All the features won't be implemented, only some of them to cover all fundamental concepts of the higher level programming track.

The project has 4 steps:

1. A **command interpreter** to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
2. A **website (the front-end)** that shows the final product to everybody: static and dynamic
3. A **database** or files that store data (data = objects)
4. An **API** that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

# 1. The console
This first step consists on program our own Command Line Interpreter in order to manipulate data:
- Create a data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI we will build later, how objects are stored won’t have to be taken on attention or care.

This abstraction will also allow to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

# How to use the console
| Commands | Description |
| ------ | ------ |
| help or ? | Lists the commands of the console | 
| ? *command* / help *command* | Displays a brief description of the *command*
| quit | Exits the program |
| create *class* | Creates a new instance of *class*, returns the id of the newly created instance |
| show *class* id | Prints the string representation of an instance based on the *class* name and id |
| destroy *class* id | Deletes an instance based on the class name and id (save the change into the JSON file) |
| all/ all *class* | Prints all string representation of all instances based or not on the *class* name |
| update *class* id *attribute name* "attribute value" | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
1. To **start** the console, execute the file where the console is located(console.py)

2. 
