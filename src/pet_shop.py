# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(money):
    return money["admin"]["total_cash"]

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] = shop["admin"]["total_cash"] + money
    return shop["admin"]["total_cash"]

#def add_or_remove_cash(pet_shop, amount):
#   pet_shop["admin"]["total_cash"] += amount    

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] = shop["admin"]["total_cash"] + money


def get_pets_sold(amount_sold):
    return amount_sold["admin"]["pets_sold"]

def increase_pets_sold(amount_sold, number):
    amount_sold["admin"]["pets_sold"] = amount_sold["admin"]["pets_sold"] + number
    #return amount_sold    not needed 
    #+= means will work for every time

def get_stock_count(amount):
    return len(amount["pets"])   

# could use for loop make empty list add counter etc, but len easier     


def get_pets_by_breed(shop, breed):
    total_pets = []    #empty list for list of breed
    for thing in shop["pets"]:     #for every pet in list
        if thing["breed"] == breed:    #check if its the breed looking for
            total_pets.append(thing)    # if it is add it to new list

    return total_pets


def find_pet_by_name(shop, name):
    for pet in shop["pets"]:      #for find something, alwaysa loop, will look through untill finds thing looking for and then stop
        if pet["name"] == name:
            return pet

# def remove_pet_by_name(shop, name):
#     for pet in shop["pets"]:
#         if pet["name"] == name:
#             del shop[pet]  should be shop["pets"].remove(pet)  but would delete from original list and mess everything up

# didn't get

#def remove_pet_by_name(pet_shop, name):


def remove_pet_by_name(pet_shop, name):
    pet_to_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_delete)   #got answer in class

#also didnt get this
def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)  #got in class    calling pet_shop which is the shop, accessing pets and appending the pet, which is the dictionary new pet

def get_customer_cash(cash):
    return cash["cash"]
         
def remove_customer_cash(customer, money):
    customer["cash"] -= money
    #return customer["cash"]      #customer["cash"] -= money     dont need return
       
            
def get_customer_pet_count(customer):
    return len(customer["pets"])/4  #not sure if this is right, but divided by 4 for amount of info given per animal in dictionary
                                    # its not right
def add_pet_to_customer(customer, new_pet):
    customer["pets"] = new_pet

#customer["pets"].append(pet)    

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False        

def sell_pet_to_customer(pet_shop, pet, customer):
    if (pet != None and customer_can_afford_pet(customer, pet)):
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(pet_shop, pet["price"])
        remove_customer_cash[customer, pet["price"]]
    
