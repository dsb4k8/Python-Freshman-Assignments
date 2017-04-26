########################################################################
##
## 
## Program #7
## Name  Diego Brown
## Email xxxxxx@xxxx.xxxx.edu
##
## PROBLEM : Provide the user with profitability information given the
##            stock's CSV file information.
##
##            Skills implemented: Functional Decompolition,
##                              String Formatting/ Slicing,
##                              Error Handling: Valid input:
##                                  
## OTHER COMMENTS:
##      Dates are very sensitive. Check csv files to for any discontinueties
##      in date ranges.
########################################################################

import datetime
import csv

DATE_FORMAT = "%m/%d/%Y"

def get_valid_date(prompt):
    #Asks for a valid date and continues asking while invalid entries are given

    while True:
        try:
            user_date = input(prompt)
            return datetime.datetime.strptime(user_date, DATE_FORMAT)
        except ValueError as ec:
            print("You entered an incorrect date, please re-enter in the format MM/DD/YYYY ")
            

def get_to_from_date():
    #Gets a buy and a sell date.  buy date must be prior to sell date.
    while True:
        buy_date = get_valid_date("Enter the stock purchase date ==> ")
        sell_date = get_valid_date("Enter the date you sold the stock ==> ")
        if buy_date < sell_date:
            return buy_date, sell_date
        print("The buy date must be prior to the date you sell\n")


def read_index_file(file_name):
    #Reads in the index file into a list.  ( Dictionary would work better )
    index_file = open(file_name)
    index_file.readline()
    
    index_lst = []

    index_csv = csv.reader(index_file)
    for line in index_csv:
        index_lst.append(line)

    index_file.close()
    return index_lst


def get_valid_stock(prompt, indexes):
    #Returns a valid stock, or None if the user chooses to quit
    while True:
        user_stock = input(prompt).lower()
        if user_stock == "quit":
            return None
        for stock, name in indexes:
            if stock.lower() == user_stock:
                return user_stock, name
        print("Could not find the stock {}.  Please enter another".format(user_stock))


def get_valid_amount(prompt, min_value):
    #Returns a valid amount, if it's not a proper amount or less than the min amount then it will warn user and prompt again
    while True:
        try:
            user_value = int(input(prompt))
            if user_value > min_value:
                return user_value
            print("You must enter a value greater than {}".format(min_value))
        except ValueError:
            print("You must enter a valid integer ")


def read_stock(stock_csv, start_date, end_date, buy_in):
    #reads through th csv and returns the stock_owned, buy_price, owns_stock, found_start
    
    found_start = owns_stock = found_end = False
    stock_owned = buy_price = total_buy_price = 0
    close_price = sold_for = None

    # Loop through the file looking for start_date and end_date and keeping
    # Track of the data in between.
    for line in stock_csv:
        line_date = datetime.datetime.strptime(line[0], DATE_FORMAT)

        #If stock owned, check for a split and update the stock owned
        if owns_stock:
            split = float(line[7])
            if split != 1:
                stock_owned = stock_owned * split

        # If startdate found, buy in our initial amount of stock.
        if line_date == start_date:
            buy_price = float(line[1])
            owns_stock = True
            found_start = True
            stock_owned = buy_in
            total_buy_price = buy_price * buy_in

        # When end date is found, evaluate selling price.
        if line_date == end_date:
            owns_stock = False
            found_end = True
            close_price = float(line[4])
            sold_for = close_price * stock_owned

    return owns_stock, found_start, found_end, buy_price, total_buy_price, stock_owned, close_price, sold_for

#Display Parameters
def display_results(found_start, found_end, stock_name, stock, start_date, end_date, \
                    buy_in, buy_price, total_buy_price, \
                    stock_owned, close_price, sold_for):
    #Output results.
    if not found_start or not found_end:
        if not found_start:
            print("Could not locate the start date of {}".format(start_date))
        if not found_end:
            print("Could not locate the end date of {}".format(end_date))
    else:   # Start and end dates are found. String ormatting to show our prices.
        print("\nOur {} ({}) Portfolio".format(stock_name, stock)) 
        print("{:<10}{:>12}{:>15}{:>15}{:>15}".format("Action", "Date", "Shares", "Price", "Total Price"))
        print("="*70)
        print("{:<10}{:>12}{:>15.1f}{:>15.2f}{:>15.2f}".format("Buy", start_date.strftime(DATE_FORMAT), buy_in, buy_price, total_buy_price))
        print("{:<10}{:>12}{:>15.1f}{:>15.2f}{:>15.2f}".format("Sold", end_date.strftime(DATE_FORMAT), stock_owned, close_price, sold_for))
        print("="*70)
        print(" " * 52 + "{:>15.2f}".format(sold_for - total_buy_price))
    
        
def get_stock_info(stock, stock_name, buy_in, start_date, end_date):
    #Reads in the stock file and finds your profit by buying the buy_in number of stocks

    try:
        stock_file = open(stock.upper() + ".csv")       # Concat .csv for ease of access
        stock_file.readline()                           # Read the header off.  Skip line1
        stock_csv = csv.reader(stock_file)

        # Read the stock file and return the results.
        owns_stock, found_start, found_end, buy_price, total_buy_price, \
                    stock_owned, close_price, sold_for = read_stock(stock_csv, start_date, end_date, buy_in)

        # Display the results
        display_results(found_start, found_end, stock_name, stock, start_date, end_date, \
                        buy_in, buy_price, total_buy_price, \
                        stock_owned, close_price, sold_for)
               
        stock_file.close()
    except FileNotFoundError:
        print("Could not open the file for stock given {}.csv".format(stock))
    except IOError:
        print("Had a general IO Error while opening or reading the file {}.csv".format(stock))


def get_stocks_purchased(prompt):
    """ Asks for the number of stocks purchased.  The value must be greater than 0"""
    while True:
        try:
            stocks = int(input(prompt))
            if stocks > 0:
                return stocks
            print("You must enter a value greater than zero ")
        except ValueError:
            print("Enter an integer only. ")

# Get the stock names and indexes.
indexes = read_index_file("stocklist.csv")

while True:
    result = get_valid_stock("\nEnter the name of the stock purchased.  Enter quit to exit ==> ", indexes)
    if result == None:
        break
    stock, company_name = result    

    # Get stock date.
    buy_date, sell_date = get_to_from_date()

    stocks = get_stocks_purchased("\nHow many stocks were purchased on start date ==> ")

    # Get the results of their choice.    
    get_stock_info(stock, company_name, stocks, buy_date, sell_date)
