import tkinter as tk
from tkinter import messagebox, simpledialog

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List App")
        self.shopping_list=[]
        
        self.menu_frame=tk.Frame(self.root)
        self.menu_frame.pack(pady=20)
        
        self.view_button=tk.Button(self.menu_frame, text="View Shopping List", command=self.view_list)
        self.view_button.pack(fill='x')
        
        self.add_button=tk.Button(self.menu_frame, text="Add Item", command=self.add_item)
        self.add_button.pack(fill='x')
        
        self.remove_button=tk.Button(self.menu_frame, text="Remove Item", command=self.remove_item)
        self.remove_button.pack(fill='x')
        
        self.exit_button=tk.Button(self.menu_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(fill='x')
    
    def view_list(self):
        if not self.shopping_list:
            messagebox.showinfo("Shopping List", "Your shopping list is empty.")
        else:
            items="\n".join(f"{index+1}. {item}" for index, item in enumerate(self.shopping_list))
            messagebox.showinfo("Shopping List", items)
            
    def add_item(self):
        item=simpledialog.askstring("Add Item", "Enter the item to add: ")
        if item:
            self.shopping_list.append(item)
            messagebox.showinfo("Shopping List", f"{item} has been added to your shopping list.")
    
    def remove_item(self):
        if not self.shopping_list:
            messagebox.showinfo("Shopping List", "Your shopping list is empty.")
            return
        
        items="\n".join(f"{index+1}. {item}" for index, item in enumerate(self.shopping_list))
        item_index=simpledialog.askinteger("Remove Item", f"Enter the number of the item to remove: \n\n{items}")
        
        if item_index and 1 <= item_index <= len(self.shopping_list):
            removed_item = self.shopping_list.pop(item_index - 1)
            messagebox.showinfo("Shopping List", f"{removed_item} has been removed from your shopping list.")
        else:
            messagebox.showerror("Error", "Invalid item number.")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()