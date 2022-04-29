import csv
import random

male_data_set = 'Indian-Names-Dataset/Indian-Male-Names.csv'
female_data_set = 'Indian-Names-Dataset/Indian-Feale-Names.csv'
city_data_set = 'Indian_Cities_Database.csv'

identification_marks = ['mole', 'scratch', 'tattoo']
body_part = ['forehead', 'hand', 'neck']

def generate(data : str) -> str:
    with open(data, 'r') as f:
        names = csv.reader(f)
        print("Name : ",random.choice(list(names))[0])
        addr = gen_address(city_data_set)
        print("Home town : ", addr[0],",", addr[-1],", India")
        print("Longitude, Lattitude : ", addr[1], ",", addr[2],'\n')
        print("Age : ", random.choice(range(18,40)))
        print("Height : ",round(random.uniform(4.50, 7.00), 2),"'")
        print("Weight : ", round(random.choice(range(45, 75))))
        print("Identification mark on body : ", random.choice(identification_marks), " on", random.choice(body_part),'\n')
        print("Mariatal Status : ", random.choice(['married', 'single']))

generate.__doc__ = "This function generates a fake identity based on your parameter (Male or Female). It uses dataset available in the Government website. It provides name, address, age, height, weight, identification mark on body and mariatal status"

def gen_address(data : str) -> str:
    with open(data, 'r') as f:
        address = csv.reader(f)
        addr = random.choice(list(address))
        return addr
    
generate(male_data_set)

