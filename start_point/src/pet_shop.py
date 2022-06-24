# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pets):
    return pets["name"]

def get_total_cash(pets):
    return pets["admin"]["total_cash"]


def add_or_remove_cash(pets,money):
    pets["admin"]["total_cash"] += money
    

def get_pets_sold(pets):
    return pets["admin"]["pets_sold"]

def increase_pets_sold(pets,number):
    pets["admin"]["pets_sold"] += number

def get_stock_count(pets):
    return len(pets["pets"])

def get_pets_by_breed(pets, breed):
    pet_breed = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:
            pet_breed.append(pet)
    return pet_breed

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pets, name):
    for i, pet in enumerate(pets["pets"]):
        if pet["name"] == name:
            del pets["pets"][i]

def add_pet_to_stock(pets,new_pet):
    pets["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]


def remove_customer_cash(customers,cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)


def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(list_of_pets, pet_name, customer):
    





    # for i ,pets in enumerate(list_of_pets["pets"]):
    #     if pets["name"] == pet_name and customer["cash"] >= pets["price"]:
    #         customer["cash"] -= pets["price"]
    #         list_of_pets["admin"]["total_cash"] += pets["price"]
    #         list_of_pets["admin"]["pets_sold"] + 1
    #         customer["pets"].append(list_of_pets)["pets"][i]
    #         del list_of_pets["pets"][i]
