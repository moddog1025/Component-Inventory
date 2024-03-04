import tkinter as tk
from tkinter import ttk

# Data structure to hold inventory items
inventory = []

# Function to add items to the inventory
def add_to_inventory(component_type, specification, package, amount):
    inventory.append({
        "type": component_type,
        "specification": specification,
        "package": package,
        "amount": amount
    })

# Add Inventory window
def open_add_inventory():
    add_win = tk.Toplevel(root)
    add_win.title("Add Inventory")

    # Component type
    ttk.Label(add_win, text="Component Type:").grid(column=0, row=0)
    component_type_var = tk.StringVar()
    component_type_dd = ttk.Combobox(add_win, textvariable=component_type_var)
    component_type_dd['values'] = ("Resistor", "Capacitor", "Inductor")  # Example component types
    component_type_dd.grid(column=1, row=0)

    # Specification
    ttk.Label(add_win, text="Specification:").grid(column=0, row=1)
    specification_var = tk.StringVar()
    specification_dd = ttk.Combobox(add_win, textvariable=specification_var)
    specification_dd['values'] = ("1k Ohm", "100uF", "10mH")  # Example specifications
    specification_dd.grid(column=1, row=1)

    # Package
    ttk.Label(add_win, text="Package:").grid(column=0, row=2)
    package_var = tk.StringVar()
    package_dd = ttk.Combobox(add_win, textvariable=package_var)
    package_dd['values'] = ("0603", "0805", "1206")  # Example packages
    package_dd.grid(column=1, row=2)

    # Amount
    ttk.Label(add_win, text="Amount:").grid(column=0, row=3)
    amount_entry = ttk.Entry(add_win)
    amount_entry.grid(column=1, row=3)

    # Add Button
    def add_item():
        add_to_inventory(component_type_var.get(), specification_var.get(), package_var.get(), amount_entry.get())
        amount_entry.delete(0, tk.END)  # Clear the amount entry for next input

    ttk.Button(add_win, text="Add Component", command=add_item).grid(column=0, row=4, columnspan=2)

    # Done Button
    ttk.Button(add_win, text="Done", command=lambda: [add_win.destroy(), open_view_inventory()]).grid(column=0, row=5, columnspan=2)

# View Inventory window
def open_view_inventory():
    view_win = tk.Toplevel(root)
    view_win.title("View Inventory")

    tree = ttk.Treeview(view_win, columns=("Type", "Specification", "Package", "Amount"), show="headings")
    tree.heading("Type", text="Component Type")
    tree.heading("Specification", text="Specification")
    tree.heading("Package", text="Package")
    tree.heading("Amount", text="Amount")

    for item in inventory:
        tree.insert("", tk.END, values=(item["type"], item["specification"], item["package"], item["amount"]))
    tree.pack(expand=True, fill='both')

# Main Window
root = tk.Tk()
root.title("Inventory Manager")

ttk.Button(root, text="Add Inventory", command=open_add_inventory).pack(side=tk.LEFT, padx=(20, 10), pady=20)
ttk.Button(root, text="View Inventory", command=open_view_inventory).pack(side=tk.RIGHT, padx=(10, 20), pady=20)

root.mainloop()

