# Shop_MySQL
Create and manage shop database with MySQL in Python - in progress

<p align="center">
  <img src="https://user-images.githubusercontent.com/99027230/190636802-84c0c89c-db10-4676-8f33-92fefabb0ce2.png" alt="Database"/>
</p>

**database.py** - the file with all necessary functions to create database with tables and to insert records to tables.

**create.py** - this file is for building databases and all necessary tables. In this case there was created Shop database with three tables:
* client - id, name, surname, email, city
* product - id, name, price
* orders - id, clientId, productId, date, status. clientId and productId are foreign keys in orders table.

**manage.py** - this file is for adding records to tables and reading them. Added the ability to group statuses and count them. Displaying the names of customers, the names of products that currently have the status 'Oczekuje'. Determining and displaying the amount, name and surname of the customer with the highest total order value.
