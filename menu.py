from tkinter import *
import tkinter as tk
import sys
from tkinter import messagebox

# Defining Functions
# Function to credit supermarket and verifying my work  
def credits_message():
    messagebox.showinfo("Price Comparison: Botany Supermarkets", message="This code was developed by Gladwyn Chua ©. " "Thanks to New World, Countdown, and Pak 'n Save for providing me with the prices to compare from. Last Price Updated 13/07/23")

# Function to quit the application
def quit():
    messagebox.showinfo("Price Comparison: Botany Supermarkets", message="Hope to see you again soon!")
    sys.exit()

# Function to create popu menu
def menu_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        #Release the grab
        popup.grab_release()

# Function to create how to use page
def additional_information():
    new_window = Toplevel(win)
    new_window.title("Price Comparison: Botany Supermarkets")
    new_window.attributes("-fullscreen", True)

    # Create a banner for the new window
    banner_frame = tk.Frame(new_window, bg="#00008B")
    banner_frame.pack(fill="x")

    banner_label = tk.Label(banner_frame, text="How To Use", font=("Arial", 25, "bold"), fg="white", bg="#00008B")
    banner_label.pack(pady=10)

    # Create a text widget to display information
    info_text = tk.Text(new_window, font=("Arial", 18), height=22, width=89)
    info_text.insert(tk.END, """
Please read the following details carefully:

1. This program helps you to compare prices of 10 products from different supermarkets in the Botany area.

2. These 10 products consist of: Milk(3L), Eggs (Dozen), Butter Blocks (500g), Bananas, Broccoli, Avocado, Loose Tomatoes, Potatoes, White Sandwich and Ready Salted Chips.
                                           
3. All prices are sourced from New World, Countdown, and Pak 'n Save.

4. The last price update was on 13/07/23.

5. Click on the 'Start' button to begin the price comparison. 
                     
6. Use the dropdown to select the product you want to select (shown on right).

   Select a product:     """)

    # Create a frame to hold the dropdown
    dropdown_frame = tk.Frame(info_text)

    # Create a dropdown to select a product
    product_var = tk.StringVar(new_window)
    product_dropdown = tk.OptionMenu(dropdown_frame, product_var, "Milk (3L)", "Eggs (Dozen)", "Butter Blocks (500g)", "Bananas", "Broccoli", "Avocado", "Loose Tomatoes", "Potatoes", "White Sandwich", "Ready Salted Chips")
    product_dropdown.config(font=("Arial", 12), width=15)
    product_dropdown.pack(side="left")

    # Embed the dropdown frame in the text widget
    info_text.window_create("end", window=dropdown_frame)

    # Add more information 
    info_text.insert(tk.END, """
            
7. Click on the "Compare Price" button.

8. Read the list of different brands of your chosen product and view the cheapest price at the bottom. 
                     
9. Quit the program when you have finished comparing!

10. All data were provided from:
                     1) Countdown - https://www.countdown.co.nz/
                     2) New World - https://www.newworld.co.nz/ 
                     3) Pak 'n Save - https://www.paknsave.co.nz/                   
                     """)

    # Disable text widget editing
    info_text.configure(state="disabled")

    # Pack the text widget
    info_text.pack(pady=10, padx=20)

    # Create a button to go back to the first window
    return_button = Button(new_window, text="Go Back", bg="#00008B", command=new_window.destroy, width=20, fg="white", font=('Arial', 20,'bold'))
    return_button.pack()

# Create an instance of Tkinter frame
win = Tk()
win.attributes("-fullscreen", True)

# Create the banner
banner_frame = tk.Frame(win, bg="#00008B")
banner_frame.pack(fill="x")

banner_label = tk.Label(banner_frame, text="Price Comparison: Botany Supermarkets", font=("Arial", 50, "bold"), fg="white", bg="#00008B")
banner_label.pack(pady=10)

# Add Menu
popup = Menu(win, tearoff=0)

# Start Button
start = tk.Button(win, text="Start", bg="#00008B", command=win.destroy, width=20, fg="white", font=('Arial', 45))
start.place(relx=0.25, rely=0.18)

# How to Use Button
how_to_use = tk.Button(win, text="How To Use", bg="#00008B", command=additional_information, width=20, fg="white", font=('Arial', 45))
how_to_use.place(relx=0.25, rely=0.38)

# Credits Button
recognition = tk.Button(win, text="Credits", bg="#00008B", command=credits_message, width=20, fg="white", font=('Arial', 45))
recognition.place(relx=0.25, rely=0.58)

# Exit Button
exit = tk.Button(win, text="Quit", bg="#00008B", command=quit, width=20, fg="white", font=('Arial', 45))
exit.place(relx=0.25, rely=0.78)

# Execution of python code completed
mainloop()
