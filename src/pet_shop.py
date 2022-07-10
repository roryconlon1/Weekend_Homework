# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(money):
    return money["admin"]["total_cash"]

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] = shop["admin"]["total_cash"] + money
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] = shop["admin"]["total_cash"] + money
    return shop["admin"]["total_cash"]


def get_pets_sold(amount_sold):
    return amount_sold["admin"]["pets_sold"]

def increase_pets_sold(amount_sold, number):
    amount_sold["admin"]["pets_sold"] = amount_sold["admin"]["pets_sold"] + number
    return amount_sold     

def get_stock_count(amount):
    return len(amount["pets"])   


def get_pets_by_breed(shop, breed):
    total_pets = []
    for thing in shop["pets"]:
        if thing["breed"] == breed:
            total_pets.append(thing)

    return total_pets


def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

# def remove_pet_by_name(shop, name):
#     for pet in shop["pets"]:
#         if pet["name"] == name:
#             del shop[pet]

def get_customer_cash(cash):
    return cash["cash"]
         
def remove_customer_cash(customer, money):
    customer["cash"] = customer["cash"] - money
    return customer["cash"]      
       
            
def get_customer_pet_count(customer):
    return len(customer["pets"])/4  #not sure if this is right, but divided by 4 for amount of info given per animal in dictionary
 
def add_pet_to_customer(customer, new_pet):
    customer["pets"] = new_pet
    
