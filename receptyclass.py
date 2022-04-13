###Create recipe class Done
###Create ingrediens class Done
###Create function to create recipe done
###Store ingrediens done 
###Create calls for recipes done
###create fuction that updates database row done
###create function that returns only ingrediens as a list done
###create function that returns possible recipes from ingrediens done
###
###
###
###Create GUI 
###Move recipes and ingrediens online
import mysql.connector
from mysql.connector import Error
import pandas as pd
import itertools


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost", "root", "root")

def database_call():
    cnx = mysql.connector.connect(user="root", password ="root", database = "recepty")
    cursor = cnx.cursor()

    query = ("SELECT Recept_name FROM recepty.recepty_table WHERE Recept_Id = 1;")
    cursor.execute(query)

    for Recept_name in cursor:
        print(Recept_name)
    print(type(cursor))



class Recipe():
    def __init__(self,idn, ing, steps, name, category = "food"):

        self.idn = idn
        self.ing = ing
        self.steps = steps
        self.category = category
        self.name = name 

    def __str__(self):
        return self.name

class Ingre():
    def __init__(self, name, protein=False, secondary=False, side=False):
        self.protein = protein
        self.secondary = secondary
        self.side = side
        self.name = name

    def __str__(self):
        return self.name

###def show_all_category():
    ###for item in all_category:
        ###print(item, end=" ")



def make_recipe():
    rname = input("Name of the recipe: ")
    ringrediens = input("Ingredients separated by comma: ")
    rsteps = input("Steps separated by /")
    rcategory = input(f"Enter category from existing {show_all_category()} \n or enter new one: ")

    def split_ing():
        list_of_ingredients = ringrediens.split(",")
        return list_of_ingredients

    def split_steps():
        list_of_steps = rsteps.split("/")
        return list_of_steps

    def new_ing():
        pass  

def add_recipe(current):
    cnx = mysql.connector.connect(user="root", password ="root", database = "recepty")
    cursor = cnx.cursor()

    add_recipe_str = ("INSERT INTO recepty_table "
               "(recept_id, recept_name, recept_steps, recept_ingre, recept_category) "
               "VALUES (%s, %s, %s, %s, %s)")


    recipe_data = (2, "spagety", "1uvarit2roztocit3nevim", "spagety,maso", "testoviny" )

    
    cursor.execute(add_recipe_str, recipe_data)
    cnx.commit()
    cursor.close()
    cnx.close()


def update_recipe():
    cnx = mysql.connector.connect(user="root", password ="root", database = "recepty")
    cursor = cnx.cursor()
    cursor.execute(f"Update recepty_table set recept_category = 'polevka' where Recept_id = 1;")
    

    cnx.commit()
    cursor.close()
    cnx.close()

def return_ingre():
    cnx = mysql.connector.connect(user="root", password ="root", database = "recepty")
    cursor = cnx.cursor()

    cursor.execute(f"select recept_ingre from recepty_table where Recept_id = 1")

    list_of_ingre = list(itertools.chain.from_iterable(cursor))
    steps = list_of_ingre[0].split("/")
    for step in steps:
        print(step, end="\n")
    

def find_matching_recipe():
    cnx = mysql.connector.connect(user="root", password ="root", database = "recepty")
    cursor = cnx.cursor()

    cursor.execute(f"select Recept_id, recept_ingre from recepty_table")
    re_dict =dict((x, y) for x, y in cursor)
    
    

    owned_ingre = input("What ingrediens do you have:").split(",")

    matched_recipes = set()
    for k,v in re_dict.items():
        for ingre in owned_ingre:
            if ingre in v:
                matched_recipes.add(k)
    print(matched_recipes)

    for i in matched_recipes:
        cursor.execute(f"select Recept_name from recepty_table where Recept_id = {i}")
        print(cursor)
    

   



find_matching_recipe()







