import tkinter as tk
from tkinter import ttk

# make a customer balance and a coffee dictionary
customer_balance = 0.00
coffee = {"Latte": 2.50, "Espresso": 1.50, "Cappuccino": 3.00}


def one_dollar():
    """
    .get() wouldn't work used Global to call the balance.
     Add $1 to global balance everytime the $1 function is clicked.
    Set price message to balance.
    """
    global customer_balance
    customer_balance += 1.00
    string_price_message.set(customer_balance)


def two_dollars():
    """
    Add $2 to global balance everytime the $2 function is clicked.
    Set price message to balance.
    """
    global customer_balance
    customer_balance += 2.00
    string_price_message.set(customer_balance)


def twentyfive_cents():
    """
    Add $0.25 to global balance everytime the $0.25 function is clicked.
    Set price message to balance.
    """
    global customer_balance
    customer_balance += 0.25
    string_price_message.set(customer_balance)


def latte_button():
    """
    When Latte button is clicked, set string_coffee message to Latte
    """
    string_coffee.set("Latte($2.50)")


def espresso_button():
    """
    When espresso button is clicked, set string_coffee message to espresso
    """
    string_coffee.set("Espresso($1.50)")


def cappuccino_button():
    """
    When Cappuccino button is clicked, set string_coffee message to Cappuccino
    """
    string_coffee.set("Cappuccino($3.00)")


def make_drink():
    """
    Call the global balance and dict then set drink to whatever coffee was clicked last.
    """
    global customer_balance
    global coffee
    drink = string_coffee.get()
    # if the last drink is equal to the drink have the balance subtract the dictionary to see if you have enough #
    while True:
        if drink == 'Latte($2.50)':
            if customer_balance - coffee["Latte"] < 0:
                string_message.set("You don't have enough funds.")
                break
        # If you have enough subtract from global balance then set the balance to what's left. Set thanks message
            elif customer_balance - coffee["Latte"] >= 0:
                customer_balance -= coffee["Latte"]
                string_price_message.set(customer_balance)
                string_message.set("Latte is great!.")
                break
            break
        # if the last drink is equal to the drink have the balance subtract the dictionary to see if you have enough #
        elif drink == 'Espresso($1.50)':
            if customer_balance - coffee["Espresso"] < 0:
                string_message.set("You don't have enough funds.")
                break
        # If you have enough subtract from global balance then set the balance to what's left. Set thanks message.
            elif customer_balance - coffee["Espresso"] >= 0:
                customer_balance -= coffee["Espresso"]
                string_price_message.set(customer_balance)
                string_message.set("Espresso is great!.")
                break
            break

        # if the last drink is equal to the drink have the balance subtract the dictionary to see if you have enough #
        elif drink == 'Cappuccino($3.00)':
            if customer_balance - coffee["Cappuccino"] < 0:
                string_message.set("You don't have enough funds.")
                break
        # If you have enough subtract from global balance then set the balance to what's left. Set thanks message
            elif customer_balance - coffee["Cappuccino"] >= 0:
                customer_balance -= coffee["Cappuccino"]
                string_price_message.set(customer_balance)
                string_message.set("Cappuccino is great!.")
                break
            break


# Create root window
root = tk.Tk()
root.title("Coffee Machine")
root.geometry("300x200")

# Create main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

# Create label
ttk.Label(frame_home, text="Coffee Maker").grid(column=0, row=0)

# Create entry price box
string_price_message = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_price_message).grid(column=0, row=3, columnspan=3)

string_coffee = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_coffee).grid(column=0, row=4, columnspan=3)

string_message = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_message).grid(column=0, row=6, columnspan=3)

# create all your buttons
ttk.Button(frame_home, text="Latte ($2.50)", command=latte_button).grid(column=0, row=1)
ttk.Button(frame_home, text="Espresso ($1.50)", command=espresso_button).grid(column=1, row=1)
ttk.Button(frame_home, text="Cappuccino ($3.00)", command=cappuccino_button).grid(column=2, row=1)
ttk.Button(frame_home, text="$2.00", command=two_dollars).grid(column=0, row=2)
ttk.Button(frame_home, text="$1.00", command=one_dollar).grid(column=1, row=2)
ttk.Button(frame_home, text="$0.25", command=twentyfive_cents).grid(column=2, row=2)
ttk.Button(frame_home, text="Make Drink", command=make_drink).grid(column=1, row=5)

root.mainloop()
