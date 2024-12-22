# GroceryList_Python-and-MySQL
GroceryList using Python and MySQL database.
# Grocery List Management with MySQL

This project is a Python-based console application that allows users to manage their grocery list interactively. The application integrates with MySQL for persistent data storage and provides functionality to add, remove, view, and manage grocery items effectively.

---

## Features
- **Add an Item**: Insert grocery items into the MySQL database.
- **Remove an Item**: Delete specific items from the database with validation.
- **View the List**: Display all grocery items stored in the database.
- **Exit**: Safely close the application and terminate database connections.

---

## Prerequisites
1. Python 3.x installed on your system.
2. MySQL server installed and running.
3. A database named `grocery_db` with a table `groceries`:
   ```sql
   CREATE DATABASE grocery_db;
   USE grocery_db;
   CREATE TABLE groceries (
       id INT AUTO_INCREMENT PRIMARY KEY,
       item_name VARCHAR(255) NOT NULL
   );
