import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, IntVar, StringVar
from PIL import Image, ImageTk

class BulldogExchange:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulldog Exchange")
        self.root.geometry("1000x700")

        self.cart = {}
        self.user_address = ""
        self.used_discount_codes = set()
        self.expired_discount_codes = {"SAVE50"}
        self.valid_discount_codes = {"SAVE10": 0.10, "SAVE20": 0.20}

        self.create_header()
        self.create_footer()
        self.create_home_page()
        self.current_frame = self.home_frame  # Track the current frame

    def create_header(self):
        header = tk.Frame(self.root, bg='#35408e', padx=10, pady=10)
        header.pack(fill=tk.X)

        header_label = tk.Label(header, bg='#35408e', fg='white', 
                                font=("Bahnschrift", 14))
        header_label.pack(side=tk.LEFT)

        nav = tk.Frame(header, bg='#35408e')
        nav.pack(side=tk.RIGHT)

        for item in ["Home", "About Us", "Cart"]:
            btn = tk.Button(nav, text=item, bg='#35408e', fg='white', font=("Helvetica Neue Neue", 12), 
                            command=lambda item=item: self.navigate(item))
            btn.pack(side=tk.LEFT, padx=5)
        
        try:
            bulldog_image = Image.open("bulldog.png")
            bulldog_image = bulldog_image.resize((250, 70))
            bulldog_photo = ImageTk.PhotoImage(bulldog_image)
            bulldog_label = tk.Label(header, image=bulldog_photo, bg='#35408e')
            bulldog_label.image = bulldog_photo
            bulldog_label.pack(side=tk.LEFT, padx=10)
        except Exception as e:
            print(f"Error loading image: {e}")

    def create_footer(self):
        footer = tk.Frame(self.root, bg='#35408e', padx=10, pady=10)
        footer.pack(side=tk.BOTTOM, fill=tk.X)

        footer_label = tk.Label(footer, text="Education that works.", bg='#35408e',font =('times new roman', 25), fg='yellow')
        footer_label.pack(side=tk.LEFT)
    
        bulldog_image = Image.open("aso.png")
        bulldog_image = bulldog_image.resize((250, 70))
        bulldog_photo = ImageTk.PhotoImage(bulldog_image)
        bulldog_label = tk.Label(footer, image=bulldog_photo, bg='#35408e')
        bulldog_label.image = bulldog_photo
        bulldog_label.pack(side=tk.RIGHT, padx=0)
    
    def create_home_page(self):
        self.home_frame = tk.Frame(self.root)
        self.home_frame.pack(fill=tk.BOTH, expand=True)

        # Placeholder for image loading
        

        welcomei = Image.open("discount2.png")
        welcomei = welcomei.resize((500,450))
        welcome_photo = ImageTk.PhotoImage(welcomei)
        welcome2i = tk.Label(self.home_frame, image=welcome_photo)
        welcome2i.image = welcome_photo
        welcome2i.pack(pady = 20)   
        shop_button = tk.Button(self.home_frame, text="SHOP NOW" ,font=('helvetica nueu',15), bg='#35408e', fg='yellow', 
                                borderwidth=0,height = 3, width =30 ,command=self.show_categories)
        
        shop_button.pack(pady=10)

    def show_categories(self):
        self.hide_current_frame()  # Hide the current frame
        self.create_categories_section()
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def hide_current_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

    def create_categories_section(self):
        self.categories_frame = tk.Frame(self.root, padx=10, pady=10)

        category_list = [
            ("Uniform", 20, ["Small", "Medium", "Large"]),
            ("Pants", 25, ["Small", "Medium", "Large"]),
            ("Jackets", 30, ["Small", "Medium", "Large"]),
            ("Tumblers", 15, ["8oz", "16oz", "22oz"]),
            ("Bags", 35, ["Design 1", "Design 2", "Design 3", "Tote Bag"]),
            ("Portable Fans", 20, ["Design 1", "Design 2", "Design 3"]),
            ("Caps", 15, ["Design 1", "Design 2", "Design 3"])
        ]

        for product, base_price, options in category_list:
            category_btn = tk.Button(self.categories_frame, text=product, width=20, font=('helvetica neue',15),
                                      command=lambda p=product, price=base_price, opts=options: self.show_featured_products(p, price, opts))
            
            category_btn.pack(pady=5)

        self.categories_frame.pack(fill=tk.Y, expand=True)  # Pack the categories frame
        self.current_frame = self.categories_frame  # Update current frame

    def show_featured_products(self, product_name, base_price, options):
        self.hide_current_frame()  # Hide the current frame

        self.featured_frame = tk.Frame(self.root, padx=10, pady=10)
        self.featured_frame.pack(fill=tk.X)

        title = tk.Label(self.featured_frame, text=f"{product_name} Options", font=("Helvetica Neue", 18), bg='lightgray')
        title.pack(pady=10)

        product_frame = tk.Frame(self.featured_frame)
        product_frame.pack(pady=5)

        for option in options:
            card_frame = tk.Frame(product_frame, padx=10, pady=10, borderwidth=1, relief="solid")
            card_frame.pack(side=tk.LEFT, padx=10)

            img = tk.Label(card_frame, text=product_name, borderwidth=1, relief="solid", width=15, height=8)
            img.pack(pady=5)

            price_label = tk.Label(card_frame, text=f"Price: ${base_price}", font=("Helvetica Neue", 12))
            price_label.pack(pady=5)

            size_var = StringVar(value=options[0])
            size_dropdown = tk.OptionMenu(card_frame, size_var, *options)
            size_dropdown.pack(pady=5)

            quantity_var = IntVar(value=1)
            quantity_label = tk.Label(card_frame, text="Quantity:")
            quantity_label.pack(pady=5)
            quantity_entry = tk.Entry(card_frame, textvariable=quantity_var, width=5)
            quantity_entry.pack(pady=5)

            add_btn = tk.Button(card_frame, text="Add to Cart",
                                command=lambda p=product_name, price=base_price, q=quantity_var, s=size_var: self.add_to_cart(p, price, q.get(), s.get()))
            add_btn.pack(pady=5)

        back_btn = tk.Button(self.featured_frame, text="Back to Categories", command=self.back_to_categories)
        back_btn.pack(pady=10)

        self.current_frame = self.featured_frame  # Update current frame

    def back_to_categories(self):
        self.featured_frame.pack_forget()  # Hide featured frame
        self.create_categories_section()  # Show categories again

    def add_to_cart(self, product, price, quantity, size):
        quantity = int(quantity)
        item_key = f"{product} ({size})"
        if item_key in self.cart:
            self.cart[item_key]['quantity'] += quantity
        else:
            self.cart[item_key] = {'price': price, 'quantity': quantity}
        messagebox.showinfo("Added to Cart", f"{quantity} x {item_key} has been added to your cart!")

    def view_cart(self):
        cart_window = tk.Toplevel(self.root)
        cart_window.title("Your Cart")
        cart_window.geometry("1000x700")

        total_cost = 0
        cart_frame = tk.Frame(cart_window)
        cart_frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(cart_frame, text="Your Cart", font=("Helvetica Neue", 18))
        title.pack()

        for product, info in self.cart.items():
            item_frame = tk.Frame(cart_frame)
            item_frame.pack(pady=5)

            item_label = tk.Label(item_frame, text=f"{product} - ${info['price']} x {info['quantity']}", font=("Helvetica Neue", 12))
            item_label.pack(side=tk.LEFT)

            remove_one_btn = tk.Button(item_frame, text="Remove 1", command=lambda p=product: self.remove_from_cart(p, 1))
            remove_one_btn.pack(side=tk.LEFT, padx=5)

            remove_all_btn = tk.Button(item_frame, text="Remove All", command=lambda p=product: self.remove_from_cart(p, info['quantity']))
            remove_all_btn.pack(side=tk.LEFT, padx=5)

            total_cost += info['price'] * info['quantity']

        total_label = tk.Label(cart_frame, text=f"Total Cost: ${total_cost}", font=("Helvetica Neue", 14, "bold"))
        total_label.pack(pady=10)

        address_label = tk.Label(cart_frame, text="Enter your delivery address:", font=("Helvetica Neue", 12))
        address_label.pack(pady=5)

        self.address_entry = tk.Entry(cart_frame, width=50)
        self.address_entry.pack(pady=5)

        discount_label = tk.Label(cart_frame, text="Enter Discount Code (if any):", font=("Helvetica Neue", 12))
        discount_label.pack(pady=5)

        self.discount_entry = tk.Entry(cart_frame, width=20)
        self.discount_entry.pack(pady=5)

        checkout_btn = tk.Button(cart_frame, text="Checkout", command=self.checkout)
        checkout_btn.pack(pady=10)

        close_btn = tk.Button(cart_frame, text="Close", command=cart_window.destroy)
        close_btn.pack(pady=5)

    def checkout(self):
        self.user_address = self.address_entry.get()
        discount_code_input = self.discount_entry.get().strip()
        total_cost = sum(info['price'] * info['quantity'] for info in self.cart.values())

        if discount_code_input in self.expired_discount_codes:
            messagebox.showwarning("Expired Code", "This discount code has expired.")
            return

        if discount_code_input in self.valid_discount_codes:
            if discount_code_input in self.used_discount_codes:
                messagebox.showwarning("Already Used Code", "You have already used this discount code.")
                return

            discount_percentage = self.valid_discount_codes[discount_code_input]
            total_cost *= (1 - discount_percentage)
            self.used_discount_codes.add(discount_code_input)

        if not self.user_address:
            messagebox.showwarning("Address Required", "Please enter a delivery address.")
            return

        messagebox.showinfo("Checkout Successful", f"Your order has been placed!\nTotal Cost: ${total_cost:.2f}\nDelivery Address: {self.user_address}")

    def remove_from_cart(self, product, quantity):
        if product in self.cart:
            if self.cart[product]['quantity'] <= quantity:
                del self.cart[product]
            else:
                self.cart[product]['quantity'] -= quantity
            messagebox.showinfo("Removed from Cart", f"{quantity} of {product} has been removed from your cart.")

    def show_about_us(self):
         about_window = tk.Toplevel(self.root)
         about_window.title("About Us")
         about_window.geometry("1000x700")

         about_text = """\
Welcome to the Bulldog Exchange!

Our mission is to provide quality products that celebrate our school spirit.
We have been serving the school community since yesterday, and we are proud to support local initiatives and events.

Our values are centered around quality, affordability, and community engagement.
Thank you for supporting our school!
"""

         about_label = tk.Label(about_window, text=about_text, padx=20, pady=20, 
                            font=("Helvetica Neue", 12), justify="left", wraplength=800)
         about_label.pack(fill=tk.BOTH, expand=True)

    def navigate(self, item):
        if item == "Home":
            self.hide_current_frame()  # Hide the current frame
            self.create_home_page()  # Show the home page
            self.current_frame = self.home_frame  # Update current frame
            self.home_frame.pack(fill=tk.BOTH, expand=True)  # Pack home frame
        elif item == "About Us":
            self.show_about_us()
        elif item == "Cart":
            self.view_cart()

if __name__ == "__main__":
    root = tk.Tk()
    app = BulldogExchange(root)
    root.mainloop()
