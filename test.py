
customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }

cc_pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }




def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet


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
    selling_pet = find_pet_by_name(list_of_pets, pet_name)
    print(selling_pet)
    if customer_can_afford_pet(customer, selling_pet) == True:
        print(True)
        add_or_remove_cash(list_of_pets, selling_pet["price"])
        print("admin cash= ", list_of_pets["admin"]["total_cash"])
        remove_customer_cash(customer, selling_pet["price"])
        print("customers cash= ", customer["cash"])
        add_pet_to_customer(customer, selling_pet)
        print("customer pets= ", customer["pets"])
        remove_pet_by_name(list_of_pets, pet_name)
        # print(list_of_pets["pets"])
        increase_pets_sold(list_of_pets,1)
        print("total sold=", list_of_pets["admin"]["pets_sold"] )


sell_pet_to_customer(cc_pet_shop, "Arthur", customers[0])



