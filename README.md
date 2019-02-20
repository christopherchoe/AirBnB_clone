<h1 align ="center"> AirBnB Clone Project </h1><br>
<p align="center">
Made as a project for Holberton School
</p>

## Authors

* [Alex Yu](https://github.com/alexyu01)
* [Christopher Choe](https://twitter.com/chchchoe)

## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Features](#features)
- [Example](#example)
- [Built With](#built-with)
- [Acknowledgments](#acknowledgments)

## Introduction

The AirBnB Clone Project is an attempt to create a clone of the AirBnB site with some of the features of the real AirBnB website.

The Basic Goals:

* A command interpreter to manipulate data without a visual interface, like in a Shell (for development and debugging)

* A website (front-end) that shows the final product: static and dynamic

* A database of files thats store data i.e. objects

* An API that provides a communication interface between front-end and data (reterive, create, delete, update)

## Description

The Command Interpreter

* The Base Model parent class which will be the base for other classes that store our data e.g. User, State, City, Review, Place, Amenity

* The Base Model class will initialize, serialize, and deserialize future instances

* An instance will be converted to a dictionary, serialized to a JSON string, and then saved to a storage file

* Classes includes are User, State, City, Place, Review, Amenity which inherit from Base Model

* Data storage engine, File Storage class which will store our instances and data

* Unittests for these classes, features, and variables

## Features

* Each class instantiated with a universally unique identifier string, created at datetime, and updated at datetime

* User, State, City, Place, Review, and Amenity class which inherit from Base Model class

* The string representation of a class will have the class name, id, and dictionary of attributes

* Each class will be able to save itself, updating the file storage and update at attribute

* A class can be re created using a dictionary representation as the kwargs

* A representation of all the objects instantiated will be available for the classes to access

* A console/command interpreter which will allow for interactive and non interactive use

* CONSOLE COMMANDS:
	* quit / EOF : can be used to exit the console
	
	* help : will provide documentation and help for using the console
	
	* create : creates a new instance of a specified class
	
	* show : prints the string representation of an instance based on class name and id
	
	* destroy : deletes an instance based on class name and id
	
	* all : prints string representation of all instances of a specified class or all instances if not specified

	* update : updates an instance based on class name, id and by adding/updating an attribute

## Example

QUIT:

```
user@machine: $ ./console.py
(hbnb) quit
user@machine: $
```

HELP:

```
(hbnb) help

Documented commands type help topic:

EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of instances based or not on class
        name:  all BaseModel
	    :  all
```

ALL:

```
(hbnb) all
["[User] (2f0b1cc8-0207-4012-a9de-e784bcc37068) {'updated_at': datetime.datetime(2019, 2, 20, 0, 29, 9, 837924), 'id': '2f0b1cc8-0207-4012-a9de-e784bcc37068', 'created_at': datetime.datetime(2021, 2, 20, 0, 29, 9, 837924)}", "[State] (720dbe47-a8fc-4db1-9206-5ec5f932caab) {'updated_at': datetime.datetime(2019, 2, 20, 0, 29, 9, 810951), 'id': '720dbe47-a8fc-4db1-9206-5ec5f932caab', 'created_at': datetime.datetime(2019, 2, 20, 0, 29, 9, 810951)}"]
```

CREATE:

```
(hbnb) create <class_name>
0b08e2a1-c317-4483-a872-5fd3bb34cb00
```

DESTROY:

```
(hbnb) destroy <class_name> <id>
```

SHOW:

```
(hbnb) show <class_name> <id>
["[<class_name>] (<id>) {'updated_at': datetim    e.datetime(2019, 2, 20, 0, 29, 9, 837924), 'id': '<id>', 'created_at': datetime.datetime(2019, 2, 20, 2, 29,     9, 837924)}"]
```

UPDATE:

```
(hbnb) update <class_name> <id> <attribute> <value>
```

NON INTERACTIVE MODE:

```
user@machine: $ echo "yourcommand and arguments" | ./console.py
(hbnb) yourcommand results
```

### Files

---
File|Description
---|---
console.py | command interpreter for testing and development
models/base_model.py | Base model parent class with id, updated_at, created_at
models/amenity.py | Amenity class inherits from base_model
models/city.py | City class inherits from base_model
models/state.py | State class inherits from base_model
models/review.py | Review class inherits from base_model
models/user.py | User class inherits from base_model
models/engine/file_storage.py | File storage engine which will store all instances for later use.
tests/test_models/test_engine | test heirarchy which will contain corresponding unittest for each of the classes in non tests directory.


## Built With

* [Python 3](https://www.python.org/)
* [Vim](https://www.vim.org/)
* [Vagrant](https://www.vagrantup.com/)
* [Ubuntu](https://www.ubuntu.com/)

## Acknowledgments

* Holberton School
* Chaat Corner
