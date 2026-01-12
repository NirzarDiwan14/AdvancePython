# 🐍 Python OOP Learning Journey - Day 01

A comprehensive overview of the Object-Oriented Programming concepts covered today, ranging from basic class structure to advanced management systems.

## 🎓 Topics Covered

### 1. Core Foundations
* **Classes & Objects**: Understanding blueprints vs. instances.
* **The Constructor (__init__)**: Automating object initialization.
* **The self Keyword**: Mastering instance referencing.

### 2. Variable & Method Scoping
* **Instance vs. Class Variables**: Differentiating between object-specific data and shared class-level data.
* **Instance Methods**: Crafting behaviors that interact with object state.
* **String Representation (__str__)**: Customizing how objects are displayed when printed.

### 3. Data Protection & Logic
* **Encapsulation**: Using __private variables and name-mangling to protect sensitive data.
* **Accessors & Mutators**: Implementing Getters and Setters for controlled data access.
* **Decorators**: Using @classmethod for factories and @staticmethod for utility logic.

### 4. Advanced Hierarchy
* **Inheritance**: Building child classes to reuse and extend parent functionality.
* **Method Overriding**: Redefining parent behaviors to fit specific child class needs.

## 🛠 Practical Projects Completed
* **Student Result System**: Managing academic data and calculations.
* **Library Management System**: A complex multi-class interaction involving:
  * **Book Class**: Tracking availability and metadata.
  * **Member Class**: Managing user history and issued items.
  * **Library Class**: Handling the core business logic (Add/Issue/Return).




# 🐍 Python OOP Learning Journey - Day 02

A comprehensive exploration of **Constructors and Methods** designed to make you **company-ready** with industry-standard Python OOP practices.

## 🎓 Topics Covered

### 1. Constructors Deep Dive
* **Basic Constructors (__init__)**: Initializing objects with default behavior.
* **Parameterized Constructors**: Passing data during object creation for dynamic initialization.
* **Constructor Overloading Pattern**: Using default arguments to simulate multiple constructors (Python style).
* **Validation in Constructors**: Ensuring data integrity from object creation.

### 2. Instance Methods
* **Business Logic Implementation**: Writing methods that operate on instance data.
* **State Modification**: Changing object properties through methods.
* **Data Encapsulation**: Protecting internal state while exposing safe interfaces.

### 3. Class Methods (@classmethod)
* **Factory Methods**: Creating alternative constructors for different object types.
* **Shared State Management**: Modifying class-level variables across all instances.
* **Semantic Object Creation**: Building more readable and maintainable code.

### 4. Static Methods (@staticmethod)
* **Utility Functions**: Writing helper methods independent of instance/class state.
* **Validation Logic**: Implementing password, email, and credential validators.
* **Organizational Best Practice**: Grouping related functionality within classes.

### 5. Accessor & Mutator Methods
* **Getter Methods**: Safely reading private data from outside the class.
* **Setter Methods**: Controlled modification of private attributes with validation.
* **Data Protection**: Using private variables (__private) to prevent unauthorized access.

### 6. Real-World Patterns
* **Factory Pattern**: Creating objects using class methods (User.admin(), Connection.local()).
* **Validation Before Assignment**: Rejecting invalid data at setter level.



# 🐍 Python OOP Advanced Concepts - Day 03

A comprehensive deep-dive into **Nested Classes, Inheritance & Method Patterns** designed for **production-ready** Python development.

## 🎓 Topics Covered

### 1. Nested Classes
* **Logical Grouping**: Encapsulating helper classes within parent classes (Address in User, Department in University).
* **Namespace Management**: Cleaner code organization using hierarchical class structures.
* **Real-World Application**: Address inside User, Config inside Service, Response models inside APIs.

### 2. Instance Methods
* **State Management**: Methods that modify object-specific data (add_money, spend_money in Wallet).
* **Business Logic**: Core functionality tied to individual object instances.
* **Encapsulation**: Protecting internal state while exposing controlled interfaces.

### 3. Class Methods (@classmethod)
* **Factory Patterns**: Creating objects and managing class-level configuration (set_environment).
* **Shared State**: Modifying data accessible across all instances (Logger level, User count).
* **Global Configuration**: Setting application-wide parameters without instance creation.

### 4. Static Methods (@staticmethod)
* **Utility Functions**: Validation logic independent of instance/class state (validate_email, length_checker).
* **Helper Operations**: Phone number validation, email verification, and credential checking.
* **Organizational Practice**: Grouping related functionality within domain classes.

### 5. Inheritance & Polymorphism
* **Code Reuse**: Child classes inherit parent behavior (Admin, Customer from User).
* **Method Overriding**: Custom implementations in child classes (send() in EmailNotification).
* **super() Usage**: Proper constructor chaining and parent method access.

### 6. Company-Level Design Patterns
* **User System Architecture**: Base User class with Admin/Customer specialization.
* **Composition Over Inheritance**: Nested Address class for flexible data modeling.
* **Multi-Method Types**: Combining instance, class, and static methods in production systems.



