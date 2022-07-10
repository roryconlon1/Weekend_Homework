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

def remove_pet_by_name(shop, name):
    no_pet =[]
    for pet in shop["pets"]:
        if pet["name"] == name:
            no_pet.remove(pet)

         
       
            

        