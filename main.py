import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import sys
import menu 

# defining Class for the Price Comparison
class PriceComparison:
    # Function using method - manipulate data and perform actions on objects
    def __init__(self, root):
        # Creating main window
        self.root = root
        self.root.title("Price Comparison: Botany Supermarkets")
        self.root.attributes("-fullscreen", True) # Allows programme to be on fullscreen mode
        self.root.configure(bg="#ECECEC") # Set background colour
        
        # Calling function of different aspects and minor components in code
        self.create_banner()
        self.create_product_dropdown()
        self.create_compare_button()
        self.create_results_frame()
        self.create_quit_button()

        # Data structure to store supermarket and details through dictionaries. 
        self.supermarkets = {
            "New World": {
            # Product name, brand and deals
            "Milk (3L)": {
                "Value Standard Milk": (5.69, ""),
                "Value Lite Reduced Fat Milk": (5.69, ""),
                "Anchor Milk Lite Milk": (7.59, ""),
                "Anchor Blue Milk": (7.59, ""),
                "Simply Milk Standard Milk": (6.80, ""),
            },
            "Eggs (Dozen)": {
                "Better Eggs Mixed Free Range Eggs": (12.49, ""),
                "Better Eggs Free Range Size 7 Eggs": (12.99, ""),
            },
            "Butter Blocks (500g)": {
                "Pams Pure Butter": (4.49, ""),
                "Rolling Meadow Butter": (6.49, ""),
                "Anchor Butter": (8.49, ""),
                "Mainland Unsalted Butter": (7.49,""),
            },
            "Bananas": {
                "Bananas": (3.79, "$/kg"),
                "850g Fairtrade Bananas": (3.99, "each"),
                "850g Dole Bobby Bananas": (4.59, "each"),
                "Organic Whole Bananas":(23.90, "$/kg")
            },
            "Broccoli": {
                "Broccoli": (2.49, "each"),
            },
            "Avocado": {
                "1kg Primor Prepacked Avocados": (3.99, "each"),
                "Green Avocado": (0.99, "each"),
            },
            "Loose Tomatoes": {
                "Loose Tomatoes": (10.99, "$/kg"),
            },
            "Potatoes": {
                "White Washed Potatoes": (3.99, "$/kg"),
                "Yellow Agria Potatoes": (4.49,"$/kg"),
                "Brushed Potatoes": (3.99, "$/kg"),
            },
            "White Sandwich": {
                "Tip Top Supersoft White Sandwich Bread": (3.99, "each"),
                "Nature's Fresh White Sandwich Bread": (3.79, "each"),
                "White Wheatmeal Sandwich Bread": (4.29, "each"),
            },
            "Ready Salted Chips": {
                "Bluebird Originals Ready Salted Chips": (2.99, ""),
                "Bluebird Thick Cut Chips Ready Salted Potato Chips": (2.99, ""),
                "Eta Ripple Cut Ready Salted Potato Chips": (2.69, "Deal: Buy 3 for $5.00"),
                "Bluebird Thick Cut Ready Salted Potato Chips": (2.99, ""),
                "Bluebird Original Ready Salted Potato Chips": (3.99, ""),
                "Eta Ridgies Ready Salted Potato Chips": (3.49, ""),
                "Pams Ready Salted Flavour Potato Chips": (1.89, ""),
            },
        },
        "Countdown": {
            # Product name, brand and deals
            "Milk (3L)": {
                "Meadow Fresh Milk Standard Original": (7.26, ""),
                "Anchor Milk Lite 98.5 percent Fat Free": (7.59, ""),
                "Anchor Milk Standard Blue": (7.59, ""),
                "Countdown Milk Trim": (5.57, ""),
                "Countdown Milk Lite": (5.57, ""),
                "Countdwon Milk Standard": (5.57, ""),
            },
            "Eggs (Dozen)": {
                "Macro Eggs Free Range Mixed Grade": (10.90, ""),
                "Macro Eggs Free Range Size 7": (11.50, ""),
                "Countdown Eggs Barn Size 7": (10.30, ""),
                "Countdown Eggs Barn Mixed Grade": (9.80,""),
                "Farmer Brown Eggs Colony Size 6": (8.40,""),
                "Frenz Eggs Free Range Mixed Grade": (12.80,"Out of Stock"),
                "Otaika Valley Eggs Free Range Size 7": (12.80,""),
                "Henergy Eggs Cage Free Size 7": (10.50,"Out of Stock"),
                "Farmer Brown Eggs Colony Size 7": (9.30,""),
                "Traditional Eggs Free Range Size 7": (10.90,""),
                "Animal Welfare Foods Eggs Free Range Mixed Grade": (11.00,""),
                "Farmer Brown Eggs Barn Size 6": (9.70,""),
                "Henergy Eggs Cage Free Size 6": (10.00,"Out of Stock"),
                "Hens Choice Eggs Cage Free Mixed Grade": (9.30,"Out of Stock"),
                "Farmer Brown Eggs Barn Size 7": (10.30,"Out of Stock"),
                "Better Eggs Spca Eggs Free Range Size 7": (12.40,"Out of Stock"),
                "Natural Spca Eggs Free Range": (11.50,"Out of Stock"),
                "Wholesome Barn Eggs Cage Free Size 7": (10.20,"Out of Stock"),
                "Better Eggs Spca Eggs Free Range Mixed Grade": (11.80,"Out of Stock"),
                "Wholesome Barn Eggs Cage Free Size 8": (10.80,"Out of Stock"),
            },
            "Butter Blocks (500g)": {
                "Countdown Butter Salted": (5.30, ""),
                "Tararua Butter ": (8.30, ""),
                "Anchor Butter ": (6.50, "Was $8.50, save $2"),
                "Mainland Butter Unsalted":(7.20,"Was 8.50, save $1.30"),
                "Mainland Butter":(7.20,"Was 8.50, save $1.30"),
            },
            "Bananas": {
                "Fresh Fruit Bananas Yellow": (3.79,""),
                "850g Fresh Fruit Bananas Snack Pack (Pre-packed)": (4.65,""),
                "850g Fresh Fruit Bananas Organic Fair Trade (Pre-packed)": (5.75,"$6.75 per kg"),
                "Fresh Fruit Bananas Green Cooking": (3.75,""),
            },
            "Broccoli": {
                "Fresh Vegetable Broccoli Heads": (2.40, "each"),
            },
            "Avocado": {
                "Fresh Fruit Avocado": (2.30, "each, 2 for $4 special"),
                "The Odd Bunch": (4.00, "Mesh bag 1kg - 4 day sale"),
            },
            "Loose Tomatoes": {
                "Fresh Tomatoes Loose": (11.99, 2.40),
                "Fresh Tomatoes Truss Vine": (11.99, 2.40),
            },
            "Potatoes": {
                "Fresh Vegetable Potatoes White Washed": (3.89,""),
                "Fresh Vegetable Potatoes Agria Brushed": (4.49, ""),
                "Fresh Vegetable Potatoes Red Washed": (4.49,"" ),
                "Fresh Vegetable Potatoes Brushed New Season": (4.99, "Out of Stock"),

            },
            "White Sandwich": {
                "Natures Fresh Sandwich Bread White": (3.80, ""),
                "Tip Top Super Soft Sandwich Bread White": (4.10, ""),

            },
            "Ready Salted Chips": {
                "Bluebird Thin Cut Chips Ready Salted": (3.00, "Deal: Buy 2 for $4.30"),
                "Bluebird Thick Cut Chips Ready Salted": (3.00, "Deal: Buy 2 for $4.30"),
                "Eta Ripples Chips Ready Salted": (2.80, "Deal: Buy 2 for $4.00"),
                "Eta Ridgies Chips Ready Salted": (2.00, "Was $3.50 save $1.50"),
                "Bluebird Originals Chips Ready Salted": (2.00, ""),
                "Bluebird Originals Multipack Chips Ready Salted 108g": (4.00, "6 pack - Deal: Buy 2 for $6.50"),
                "Bluebird Thin Cut Multipack Chips Ready Salted 108g": (4.00, "6 pack - Deal: Buy 2 for $6.50"),
                "Countdown Chips Ready Salted Crinkle Cut": (1.90, ""),
                "Countdown Chips Ready Salted Crinkle Cut 108g": (3.70, "10 pack - $2.06/100g"),
                "Bluebird Originals Potato Chips Ready Salted": (3.00, "Deal: Buy 2 for $4.30"),
                "Bluebird Gluten Free Potato Chips Ready Salted": (3.79, "Deal: Buy 2 for $4.30"),
            },
        },
        "Pak'n Save": {
            # Product name, brand and deals
            "Milk (3L)": {
                "Value Standard Milk": (5.57, ""),
                "Value Lite Reduced Fat Milk": (5.57, ""),
                "Anchor Blue Milk": (7.49, ""),
                "Anchor Lite Milk": (7.49, ""),
            },
            "Eggs (Dozen)": {
                "Rise N Shine 7 12 Pack Colony Eggs": (8.39, ""),
                "Better Eggs Mixed Free Range Eggs": (10.99, ""),
                "Better Eggs Free Rnage Size 7 Eggs": (11.49, ""),
            },  
            "Butter Blocks (500g)": {
                "Pams Pure Butter": (4.89, ""),
                "Tararua Butter": (5.99, ""),
                "Anchor Butter": (7.49, ""),
                "Mainland Unsalted Butter":(7.99, ""),
                "Mainland Salted Butter":(7.99, ""),
            },
            "Bananas": {
                "Bananas": (3.99, "$/kg"),
                "850g Organic Fairtrade Banana Bunch": (4.99, "$/kg"),
            },
            "Broccoli": {
                "Broccoli": (2.99, "$/kg - $2 for $5"),
            },
            "Avocado": {
                "Green Avocado": (0.59, "$/kg - 4 for $2"),
            },
            "Loose Tomatoes": {
                "Loose Red Tomatoes": (7.99, "$/kg"),
            },
            "Potatoes": {
                "White Washed Potatoes": (3.99, "$/kg"),
                "Yellow Agria Potatoes": (3.99, "$/kg"),
            },
            "White Sandwich": {
                "Tip Top Supersoft White Sandwich Bread": (3.29, ""),
            },
            "Ready Salted Chips": {
                "Bluebird Originals Ready Salted Potato Chips": (2.09, ""),
                "Bluebird Thinly Cut Ready Salted Potato Chips": (2.09, ""),
                "Eta Ripple Cut Ready Salted Potato Chips": (1.99, ""),
                "Bluebird Thick Cut Ready Salted Potato Chips": (2.09, ""),
                "Bluebird Original Ready Salted Potato Chips": (3.29, "6 pack 18g chips"),
                "Eta Ridgies Cut Ready Salted Potato Chips": (1.99, ""),
                "Pams Ready Salted Flavour Potato Chips":(1.59, "")
            },
        },
    }

    # Function to create a bannner
    def create_banner(self):
        banner_frame = tk.Frame(self.root, bg="#00008B")
        banner_frame.pack(fill="x")

        banner_label = tk.Label(banner_frame, text="Price Comparison: Botany Supermarkets", font=("Arial", 18, "bold"), fg="white", bg="#00008B")
        banner_label.pack(pady=10)

    # Function to create product dropdown
    def create_product_dropdown(self):# parentheses- argument/parameters which refers to class (object)
        self.product_var = tk.StringVar(self.root)
        self.product_var.set("Milk (3L)")

        product_label = tk.Label(self.root, text="Select Product:", font=("Arial", 14), fg="#00008B", bg="#ECECEC")
        product_label.pack()

        product_dropdown = tk.OptionMenu(self.root, self.product_var, "Milk (3L)", "Eggs (Dozen)", "Butter Blocks (500g)", "Bananas", "Broccoli", "Avocado", "Loose Tomatoes", "Potatoes", "White Sandwich", "Ready Salted Chips")
        product_dropdown.config(font=("Arial", 12), bg="#F5F5F5")
        product_dropdown.pack()

    # Function to create and compare button
    def create_compare_button(self):
        compare_button = tk.Button(self.root, text="Compare Prices", font=("Arial", 12, "bold"), fg="white", bg="#00008B", command=self.compare_prices)
        compare_button.pack(pady=15)

    # Creates frame for results (the price, brand, supermarket)
    def create_results_frame(self):
        result_frame = tk.Frame(self.root, bg="#ECECEC")
        result_frame.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(result_frame)
        scrollbar.pack(side="right", fill="y")

        self.result_label = tk.Text(result_frame, font=("Arial", 12), fg="#00008B", bg="#ECECEC", wrap=tk.WORD)
        self.result_label.pack(fill="both", expand=True)

        self.result_label.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_label.yview)

    # Function to create a quit button
    def create_quit_button(self):
        quit_button = tk.Button(self.root, text="Quit", command=self.quit, width=6, height=2, bg="red", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=1220, y=200)

    # Function for quit messagebox
    def quit(self):
        messagebox.showinfo("Price Comparison: Botany Supermarkets", message="Hope to see you again soon!")
        sys.exit()

    # Function to compare prices
    def compare_prices(self):
        selected_product = self.product_var.get()

        # Variables to track the cheapest price and related details
        cheapest_price = float("inf")
        cheapest_supermarkets = []
        cheapest_brands = []
        cheapest_deals = []

        # Function to fetch product details for each supermarket and find the cheapest option
        def get_product_details(selected_product):
            nonlocal cheapest_price, cheapest_supermarkets, cheapest_brands, cheapest_deals #nonlocal used to work with variables inside nested fucntions - these cases include vairables not belonging in inner functions
            product_details = ""
            # Iterate through each supermarket from data structure
            for supermarket, products in self.supermarkets.items():
                if selected_product in products:
                    selected_items = products[selected_product]
                    product_details += f"--- {supermarket} ---\n"
                    if isinstance(selected_items, dict):
                        for brand, item_info in selected_items.items():
                            if len(item_info) == 2:
                                price = item_info[0]
                                deal = item_info[1]
                            else:
                                price = item_info
                                deal = ""
                            product_details += f"{brand}: ${price:.2f}"
                            if deal:
                                product_details += f" ({deal})"
                            product_details += "\n"

                            # Tracking cheapest price and related details
                            if price < cheapest_price:
                                cheapest_price = price
                                cheapest_supermarkets = [supermarket]
                                cheapest_brands = [brand]
                                cheapest_deals = [deal]
                            elif price == cheapest_price:
                                cheapest_supermarkets.append(supermarket)
                                cheapest_brands.append(brand)
                                cheapest_deals.append(deal)

                    product_details += "\n"

            return product_details

        # Get the product details and find the cheapest option
        product_details = get_product_details(selected_product)

        # Display the product details in the result label
        result_text = f"Product: {selected_product}\n\n{product_details}"
        result_text += f"\nCheapest Price for {selected_product}: ${cheapest_price:.2f}"
        if cheapest_supermarkets:
            result_text += " (from "
            for i in range(len(cheapest_supermarkets)):
                result_text += f"{cheapest_supermarkets[i]} - {cheapest_brands[i]}"
                if cheapest_deals[i]:
                    result_text += f" ({cheapest_deals[i]})"
                if i < len(cheapest_supermarkets) - 1:
                    result_text += ", "
            result_text += ")"

        # Updating result_label widget with the result_text
        self.result_label.config(state="normal")
        self.result_label.delete("1.0", tk.END)
        self.result_label.tag_configure("title", font=("Arial", 16))
        self.result_label.tag_configure("details", font=("Arial", 14))
        self.result_label.insert(tk.END, result_text, "title")
        self.result_label.config(state="disabled")

# Method - main entry point of application
if __name__ == "__main__":
    root = tk.Tk()
    app = PriceComparison(root)
    root.mainloop()


