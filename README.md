# Y2 2018 Yearlong: Databases

### Before you start: Fork and clone this repository

1. Fork this repository by clicking "Fork" on this page:
![forking](https://image.ibb.co/jHRieT/forking.png)

2. Copy this repository's url by clicking the green clone button:
![copying url](https://image.ibb.co/n2wYeT/copying_clone.png)


## Part 1: Defining The Products Table

1. Open models.py and create the products class (Table). Make sure to include at least 5 attributes of your choice (i.e. price, quantity, description).

2. Open the terminal, navigate to your folder from the terminal (cd y2l...) then start a terminal and import everything from the models.py file (`from models import *`) use that to create Product instance.

3. Show your work to an instructor or a TA.

## Part 2: Database writes
### 2.1 Creating objects

1. Create a function in **databases.py** that adds a product to the database.

2. Call this function to add your first object to the database.

If you open the folder you can notice that there's a new file called **lecture.db** in which all the data is stored (Your database).

3. * Open the python shell (by running `python` in your terminal) 
   * Import the `create_product` function (`from databases import create_product`) 
   * Call the `create_prodduct` function with the inputs you defined in the databases.py file
   * print the database using this command line **python print_database.py lecture.db** to check if you successfully added the object.


### 2.2 Deleting from a database 

1. Create a function in **databases.py** that deletes one product of your choice.

2. Call this function.

3. * Open the python shell (by running `python` in your terminal) 
   * Import the `delete_product` function (`from databases import delete_product`) 
   * Call the `delete_prodduct` function with the inputs you defined in the databases.py file
   * print the database using this command line **python print_database.py lecture.db** to check if you successfully deleted the object.

### 2.3 Updating objects

1. Create a function in **databases.py** that updates 2 attributes of a product from the database.

2. Call this function.

3. * Open the python shell (by running `python` in your terminal) 
   * Import the `update_product` function (`from databases import update_product`) 
   * Call the `update_product` function with the inputs you defined in the databases.py file
   * print the database using this command line **python print_database.py lecture.db** to check if you successfully updated the object.

### Extra: Add a maximium for price
If a user tries to create (or update) a product with a price that's more than "300", throw and error saying that the price is too high

## Part 3: Database Reads

1. Create a function in **databases.py** that gets the first product from the **Prodcuts** table in your database **and returns it**.

2. Call this function and **print** the product.

3. Run **databases.py** and check whether it printed the object or not.

4. Now that you have the basic CRUD (Create/Read/Update/Delete) functions fully working:
* Copy the models.py and database.py files to the folder last week's flask lab. 
* Import functions from the databases.py file
* Change the app.py file to use the import functions and display the details about the **first** product in the database in **"shop.html"** page.
(Guide: in **models.py** file, in the routing function for **"shop.html"** use the retrieve function to get the product, and then pass it to the html page.)

5 Now, instead of displaying only the first product make it display **all** the products. Note that you need to deal with lists this time. Good luck.


### Extra: Displaying Images
Congratulations! If you reached this phase of the lab then you're doing great. Since you are so smart and a database expert now, add an attribute called image to the Product model and have your product details page from last lab display the product's image


### Extra: Displaying The Products
Create a search box in your page that allows you to search a product by it's name.
Extra extra: make your search work if the user provides only the first part of the keyword. (Exampel if user write "key" and there's a product with name "keyboard" a result should be returned)
