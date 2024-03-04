import tkinter as tk
from tkinter import ttk
import json

inventory_file = "inventory.json"

def load_inventory():
    try:
        with open(inventory_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory():
    with open(inventory_file, "w") as file:
        json.dump(inventory, file)

def add_to_inventory(component_type, specification, package, amount):
    inventory.append({
        "type": component_type,
        "specification": specification,
        "package": package,
        "amount": amount
    })
    save_inventory()
    update_view_inventory()

# Initialize inventory with loaded data
inventory = load_inventory()

# The rest of your script remains largely unchanged...
