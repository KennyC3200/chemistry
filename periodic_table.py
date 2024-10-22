import json
import re

with open("periodic_table.json", "r") as file:
    periodic_table = json.load(file)["elements"]

while True:
    user_input = input("Input: ")
    if user_input.lower() == "quit":
        break

    elements = re.findall(r'[A-Z][a-z]*\d*|\(.*?\)\d*', user_input)
    print(elements)
    for element in elements:

        pass
