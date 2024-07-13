## Author: Francisco Bumanglag
## Project: Monthly Sales Tax
## Assignment: Module 2 Project 6
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 24, 2023


def calculations(sales): 

    #Define constants
    state_sales_tax = 0.05
    county_sales_tax = 0.025
    
    state_sales = sales * state_sales_tax
    county_sales = sales * county_sales_tax
    total_sales = state_sales + county_sales

    return state_sales, county_sales, total_sales

def main():
 
    sales = float(input("Enter the total sales for the month: $"))

    state_sales, county_sales, total_sales = calculations(sales)

    print("The amount of the county sales tax is: $", county_sales)
    print("The amount of the state sales tax is: $", state_sales)
    print("The total sales tax (county plus state) is: $", total_sales)

#Call the main function to start the program
main()


