📄 STATEMENT DOCUMENT –
---------------------- Micro Marketplace (Console Version) -----------------------

1. Problem Statement

Students in colleges often need a simple and convenient way to buy and sell items such as books, accessories, notes, gadgets, and other essentials.
Currently, there is no basic system where users can quickly list items, search for products, or purchase available items without using complex platforms.

The problem is to create a simple, easy-to-use console-based marketplace system that allows users to:

Add items for sale

View available items

Search items

Buy/remove items

Interact through a menu-driven interface


This system should work using only basic Python, without external libraries or web development.


---

2. Scope of the Project

The scope of the project includes:

✔ Functionality

Allow users to add items with name, price, and seller details

Store items temporarily during program execution

Display a list of all available items

Search for items using keywords

Remove an item from the list after purchase

Provide a loop-based menu until the user exits


✔ Technical Scope

Built using Python only (no frameworks, no database)

Console-based interaction

Beginner-friendly menu system

Demonstrates core programming concepts: lists, dictionaries, loops, and functions


✔ Out of Scope

No online database

No user login system

No permanent storage

No GUI or website

No payment processing


The project is intentionally simple to match basic-level Python coursework expectations.


---

3. Target Users

The target users for this project include:

🎓 1. College Students

Students who want to buy or sell second-hand items like:

Books

Bags

Calculators

Accessories

Lab equipment


💻 2. Beginners Learning Python

This project is ideal for students learning:

Python basics

Console applications

Menu-driven programs

Small internal or final projects


🧑‍🏫 3. Teachers / Evaluators

Faculty members can use this as:

A simple project demonstration

A beginner’s assignment

A practical exam question



---

4. High-Level Features

⭐ 1. Add Item

Users can input:

Item name

Price

Seller
The item is stored in an internal Python list.



---

⭐ 2. View Items

Displays all available items with numbering for easy selection.

Example:

1. Shoes - Rs.500 (Seller: Anya)
2. Notes - Rs.150 (Seller: Riya)


---

⭐ 3. Search Item

Allows keyword-based search.
Works even with partial matches.

Example: Searching "shoe" returns "Shoes".


---

⭐ 4. Buy Item

Users can purchase an item by selecting its number.
The item is removed from the list after buying.


---

⭐ 5. Menu-Driven System

The program repeatedly shows a menu:

1. Add Item
2. View Items
3. Search Item
4. Buy Item
5. Exit

This continues until the user chooses Exit.
