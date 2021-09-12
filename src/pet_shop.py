# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(name_ot_the_shop):
    return name_ot_the_shop["name"]


def get_total_cash(all_cash):
    return all_cash["admin"]["total_cash"]
    
def add_or_remove_cash(all_cash, amount):
#    prev_amount = all_cash["admin"]["total_cash"]
#    all_cash["admin"]["total_cash"] = prev_amount + amount
    all_cash["admin"]["total_cash"] = get_total_cash(all_cash) + amount

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, number_of_pets):
    pets_sold["admin"]["pets_sold"] = get_pets_sold(pets_sold) + number_of_pets

def get_stock_count(how_many_pets):
    return len(how_many_pets["pets"])


def get_pets_by_breed(list_of_pets, given_breed):
    new_list = []
    for item in list_of_pets['pets']:
        if item["breed"] == given_breed:   
            new_list.append(item)
    return new_list
        
def find_pet_by_name(list_of_pets, pet_name):
    for item in list_of_pets['pets']:
        if item["name"] == pet_name:
            return item

def remove_pet_by_name(list_of_pets, pet_name):
    for item in list_of_pets['pets']:
        if item["name"] == pet_name:
            list_of_pets["pets"].remove(item)

def add_pet_to_stock(list_of_pets, new_pet):
    list_of_pets["pets"].append(new_pet)

def get_customer_cash(list_of_customers):
    return list_of_customers["cash"]

def remove_customer_cash(customer_cash, amount):
    customer_cash["cash"] = get_customer_cash(customer_cash) - amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    
    
