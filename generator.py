import csv
import random

male_data_set = 'Indian-Names-Dataset/Indian-Male-Names.csv'
Female_data_set = 'Indian-Names-Dataset/Indian-Feale-Names.csv'

def generate(data):
    with open(data, 'r') as f:
        names = csv.reader(f)
        print(random.choice(list(names)))

generate(male_data_set)
