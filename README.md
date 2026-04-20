# Mike's Bikes Store Management System

#### Video Demo: <PASTE YOUR VIDEO URL HERE>

#### Description:

Mike’s Bikes Store Management System is a Python-based console application designed to simulate the daily operations of a bicycle retail store. The purpose of this project is to demonstrate practical programming concepts learned throughout the course, including Python syntax, control structures, object-oriented programming (OOP), functions, user input handling, and error management. The system is menu-driven, allowing users to navigate different areas of the program in an organized and user-friendly way.

The program begins with a custom splash screen that displays the Mike’s Bikes company name in ASCII art along with a bicycle graphic. This was intentionally added to make the program feel more polished and professional. After the splash screen, the user presses Enter to continue to the main menu.

The main menu contains four core sections: Customers, Inventory, Orders, and Reports. These sections were chosen because they reflect the most important parts of running a real retail business.

The Customers section allows the user to store and manage customer information. Each customer contains a Customer ID, Name, Phone Number, Email Address, and Membership Status. The membership status options include Normal, Premium, and Elite. This feature demonstrates the use of classes and object attributes, while also showing how businesses organize customer loyalty levels.

The Inventory section manages the products sold by the store. Each product includes a Product ID, Name, Category, Color, Size, Price, and Stock Quantity. This allows the store to track multiple bike models and accessories. I chose to include color and size because these are realistic product details for a bike store and make the project more advanced than a basic inventory list.

The Orders section allows users to create customer purchases. To create an order, the user selects a valid Customer ID, Product ID, and quantity. The system checks for errors such as invalid customer numbers, invalid product numbers, or insufficient stock. If the order is valid, inventory stock is reduced automatically and the total purchase amount is calculated. This demonstrates conditional logic, loops, object interaction, and error handling.

The Reports section summarizes store performance. It currently displays the total number of orders and total sales revenue. This gives the user a management overview of how the business is performing.

The project uses three custom classes: Customer, Product, and Order. I chose classes because the assignment required object-oriented programming principles. Using classes makes the code more organized and easier to expand in the future. Instead of storing unrelated variables, each object keeps related data together.

Several design decisions were made to keep the project beginner-friendly while still professional. I chose a text-based menu system instead of a graphical interface because it focuses on core Python logic rather than UI complexity. I also used clear and specific error messages such as “Invalid Customer ID” and “Item Out of Stock” so the program feels realistic and user-friendly.

Overall, Mike’s Bikes Store Management System demonstrates the ability to apply Python programming skills to a practical business scenario. It combines functionality, organization, and creativity while meeting all project requirements.
