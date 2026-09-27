Import tkinter as tk
from tkinter import messagebox
import sqlite3

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

        # Database setup
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # UI
        self.create_widgets()
        self.populate_listbox()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        tk.Label(self.root, text="Item Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Quantity").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Price").grid(row=2, column=0, padx=10, pady=5)

        self.name_var = tk.StringVar()
        self.qty_var = tk.StringVar()
        self.price_var = tk.StringVar()

        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.qty_var).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.price_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Add Item", width=15, command=self.add_item).grid(row=3, column=0, pady=5)
        tk.Button(self.root, text="Update Item", width=15, command=self.update_item).grid(row=3, column=1, pady=5)
        tk.Button(self.root, text="Delete Item", width=15, command=self.delete_item).grid(row=4, column=0, pady=5)
        tk.Button(self.root, text="Clear Fields", width=15, command=self.clear_fields).grid(row=4, column=1, pady=5)
        tk.Button(self.root, text="Search", width=15, command=self.search_item).grid(row=5, column=0, pady=5)
        tk.Button(self.root, text="Exit", width=15, command=self.exit_app).grid(row=5, column=1, pady=5)

        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM inventory")
        for row in self.cursor.fetchall():
            self.listbox.insert(tk.END, f"ID:{row[0]} | Name: {row[1]} | Qty: {row[2]} | Price: ${row[3]:.2f}")

    def add_item(self):
        name = self.name_var.get().strip()
        qty = self.qty_var.get().strip()
        price = self.price_var.get().strip()

        if not name or not qty or not price:
            messagebox.showerror("Error", "Please fill all fields")
            return
        if not qty.isdigit():
            messagebox.showerror("Error", "Quantity must be a number")
            return
        try:
            price_val = float(price)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        self.cursor.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
                            (name, int(qty), price_val))
        self.conn.commit()
        self.populate_listbox()
        self.clear_fields()

    def update_item(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select an item to update")
            return
        item_id = int(self.listbox.get(selected[0]).split('|')[0].split(':')[1])
        name = self.name_var.get().strip()
        qty = self.qty_var.get().strip()
        price = self.price_var.get().strip()

        if not name or not qty or not price:
            messagebox.showerror("Error", "Please fill all fields")
            return

        self.cursor.execute("UPDATE inventory SET name=?, quantity=?, price=? WHERE id=?",
                            (name, int(qty), float(price), item_id))
        self.conn.commit()
        self.populate_listbox()
        self.clear_fields()

    def delete_item(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select an item to delete")
            return
        item_id = int(self.listbox.get(selected[0]).split('|')[0].split(':')[1])
        self.cursor.execute("DELETE FROM inventory WHERE id=?", (item_id,))
        self.conn.commit()
        self.populate_listbox()
        self.clear_fields()

    def clear_fields(self):
        self.name_var.set("")
        self.qty_var.set("")
        self.price_var.set("")

    def on_select(self, event):
        selected = self.listbox.curselection()
        if not selected:
            return
        item = self.listbox.get(selected[0]).split('|')
        self.name_var.set(item[1].split(':')[1].strip())
        self.qty_var.set(item[2].split(':')[1].strip())
        self.price_var.set(item[3].split(':')[1].replace('$', '').strip())

    def search_item(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Error", "Enter item name to search")
            return
        self.listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + name + '%',))
        rows = self.cursor.fetchall()
        if not rows:
            messagebox.showinfo("Search Result", "No items found")
        for row in rows:
            self.listbox.insert(tk.END, f"ID:{row[0]} | Name: {row[1]} | Qty: {row[2]} | Price: ${row[3]:.2f}")

    def exit_app(self):
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
