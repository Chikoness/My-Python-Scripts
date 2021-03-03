# Simple form to make a boba order

from datetime import datetime
import getpass
import os

writeIntoDest = "S:\\Home\\acharlene\\acharlene\\python_scripts\\Boba_Order_Form_Script\\BobaList"
os.chdir(writeIntoDest)

date = datetime.now()
folder = writeIntoDest + "\\" + date.strftime("%d%m%y") + "\\"

def make_file():
    print("==============================================================")
    print("Hello! Thanks for using Charlene's boba call order script!")
    print("No boba call has been initiated yet.")
    shop = raw_input("Where will we be ordering from today? ")

    print("Boba call has been initiated! Waiting for the form to appear.")

    os.makedirs(folder)
    os.chdir(folder)

    fopen = open("_" + shop + ".txt", "a+")
    fopen.writelines("We will be ordering from " + shop + " today! \n")
    fopen.close()
    print("==============================================================\n")

def nicer_username(name):
    if (name == "acharlene"):
        return "Charlene"
    # Other names of my colleagues removed here for privacy
    else:
        return name

def write_into_file(on, sz, tp, sl, il, ex):
    os.chdir(folder)

    username = getpass.getuser()

    fopen = open("boba_list.txt", "a+")
    fopen.writelines("___Boba order from: " + nicer_username(username) + "___\n")
    fopen.writelines(on + "\n")
    fopen.writelines("Size : " + sz + "\n")
    fopen.writelines("Toppings : " + tp + "\n")
    fopen.writelines("Sugar level (%): " + sl + "\n")
    fopen.writelines("Ice level (%): " + il + "\n")
    fopen.writelines("Extra options: \n" + ex + "\n")
    fopen.writelines("\n")

    print("Your order has been taken and listed down. Thank you for ordering!")

    fopen.close()

def run_file():
    if not os.path.exists(folder):
        make_file()

    print("==============================================================")
    print("Hello! Thanks for using Charlene's boba call order script!")
    print("Answer according to the questions, and your order will be taken! <3")
    print("Don't bother trolling, your username is being noted down along with your order. :P")
    print("==============================================================\n")

    orderName = raw_input("Name of drink: ")
    print("\n")
    size = raw_input("Size? (S, M, L or if applicable): ")
    print("\n")
    topping = raw_input("Any toppings? Can list more than one if you're brave: ")
    print("\n")
    sugarLevel = raw_input("What is your preferred sugar level (%)? (If applicable): ")
    print("\n")
    iceLevel = raw_input("What is your ice level (%)? (If applicable): ")
    print("\n")
    extra = raw_input("Anything you want to note down in the Extra column?\n")

    write_into_file(orderName, size, topping, sugarLevel, iceLevel, extra)

# Run the script
run_file()
