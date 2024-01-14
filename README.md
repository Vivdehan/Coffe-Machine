# Coffe-Machine
Coffe Machine Program
Coffee Machine Program
Overview
This Python program simulates a simple coffee machine. Users can choose from a menu of drinks (espresso, latte, cappuccino), view the current resources, and insert coins to make a purchase. The program checks for the availability of resources and processes the transaction accordingly.

Features
1. Menu
The coffee machine offers a menu with the following options:

Espresso
Latte
Cappuccino
2. Resource Management
The program maintains a set of resources including water, coffee, and milk. When a user selects a drink, the program checks if there are enough resources to fulfill the order.

3. Coin Insertion
Users can insert coins (quarters, dimes, nickels, and pennies) to pay for their selected drink. The program calculates the total value of the inserted coins.

4. Transaction Processing
If the inserted coins cover the cost of the chosen drink, and there are sufficient resources, the program dispenses the drink and provides change if necessary. If not, it informs the user of insufficient funds or resources.

5. Reporting
Users can request a report that displays the current status of resources, including the amount of water, coffee, and milk available.

How to Use
Run the program.
Enter your drink choice: espresso, latte, cappuccino.
If you choose to check the report, enter "report" when prompted for a drink.
If you choose latte or cappuccino, insert coins when prompted.
Enjoy your drink if the transaction is successful, or receive a refund if not.
Example
python
Copy code
# Run the coffee machine program
python coffee_machine.py
Dependencies
This program does not have any external dependencies. It uses standard Python libraries.
