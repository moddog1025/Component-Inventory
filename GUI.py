import tkinter as tk
from tkinter import ttk

# Initialize inventory list
inventory = []

# Function to add items to the inventory
def add_to_inventory(component_type, specification, package, amount):
    inventory.append({
        "type": component_type,
        "specification": specification,
        "package": package,
        "amount": amount
    })
    update_view_inventory()

# Function to center windows on the screen
def center_window(win, width=400, height=300):
    # Get screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    # Calculate x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    
    win.geometry('%dx%d+%d+%d' % (width, height, x, y))

# Add Inventory window
def open_add_inventory():
    add_win = tk.Toplevel(root)
    add_win.title("Add Inventory")
    center_window(add_win, 300, 200)  # Center the add inventory window

    # Define UI elements for adding inventory
    ttk.Label(add_win, text="Component Type:").grid(column=0, row=0)
    component_type_var = tk.StringVar()
    component_type_dd = ttk.Combobox(add_win, textvariable=component_type_var, width=17)
    component_type_dd['values'] = ("Resistor", "Capacitor", "Inductor")
    component_type_dd.grid(column=1, row=0)

    ttk.Label(add_win, text="Specification:").grid(column=0, row=1)
    specification_var = tk.StringVar()
    specification_dd = ttk.Combobox(add_win, textvariable=specification_var, width=17)
    specification_dd['values'] = ("1k Ohm", "100uF", "10mH")
    specification_dd.grid(column=1, row=1)

    ttk.Label(add_win, text="Package:").grid(column=0, row=2)
    package_var = tk.StringVar()
    package_dd = ttk.Combobox(add_win, textvariable=package_var, width=17)
    package_dd['values'] = ("0603", "0805", "1206")
    package_dd.grid(column=1, row=2)

    ttk.Label(add_win, text="Amount:").grid(column=0, row=3)
    amount_entry = ttk.Entry(add_win, width=20)
    amount_entry.grid(column=1, row=3)

    # Buttons for adding components and closing the window
    ttk.Button(add_win, text="Add Component", command=lambda: [add_to_inventory(component_type_var.get(), specification_var.get(), package_var.get(), amount_entry.get()), amount_entry.delete(0, tk.END)]).grid(column=0, row=4, columnspan=2)
    ttk.Button(add_win, text="Close", command=add_win.destroy).grid(column=0, row=5, columnspan=2)

# Update the inventory view
def update_view_inventory():
    for item in tree.get_children():
        tree.delete(item)
    for item in inventory:
        tree.insert("", tk.END, values=(item["type"], item["specification"], item["package"], item["amount"]))

# View Inventory window setup
root = tk.Tk()
root.title("Inventory Manager")
root.state('zoomed')  # Make the window full-screen

tree = ttk.Treeview(root, columns=("Type", "Specification", "Package", "Amount"), show="headings")
tree.heading("Type", text="Component Type")
tree.heading("Specification", text="Specification")
tree.heading("Package", text="Package")
tree.heading("Amount", text="Amount")
tree.pack(expand=True, fill='both')

ttk.Button(root, text="Add Inventory", command=open_add_inventory).pack(side=tk.TOP, pady=10)
ttk.Button(root, text="Exit", command=root.destroy).pack(side=tk.BOTTOM, pady=10)

root.mainloop()
