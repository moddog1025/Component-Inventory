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

# Add Inventory function (to open from the View Inventory window)
def open_add_inventory():
    add_win = tk.Toplevel(root)
    add_win.title("Add Inventory")
    add_win.attributes('-fullscreen', True)  # Make the Add Inventory window fullscreen

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

    # Done Button to close the Add Inventory window
    ttk.Button(add_win, text="Done", command=add_win.destroy).grid(column=0, row=5, columnspan=2)

# Initialize main application window
root = tk.Tk()
root.title("Inventory Manager")
root.attributes('-fullscreen', True)  # Make the main window fullscreen

# View Inventory setup within the main window
tree = ttk.Treeview(root, columns=("Type", "Specification", "Package", "Amount"), show="headings")
tree.heading("Type", text="Component Type")
tree.heading("Specification", text="Specification")
tree.heading("Package", text="Package")
tree.heading("Amount", text="Amount")

# Function to update the inventory view
def update_view():
    for i in tree.get_children():
        tree.delete(i)
    for item in inventory:
        tree.insert("", tk.END, values=(item["type"], item["specification"], item["package"], item["amount"]))

# Add Inventory button in the main window
ttk.Button(root, text="Add Inventory", command=lambda: [open_add_inventory(), update_view()]).pack(side=tk.TOP, pady=10)

tree.pack(expand=True, fill='both')

root.mainloop()
