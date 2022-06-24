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
    pets.pop(name)