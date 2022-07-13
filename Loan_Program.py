#important to use csv methods
import csv

#method to use file_name
def values():
    global file_name
    user_input4 = str(input("What is the name of the file to write the results to? "))
    file_name = user_input4

#method for writing the csvfile
def testing(csvfile):
    writer = csv.writer(csvfile)

#values used in the program
    loan_amt = 0
    annual_interest_rt = 0
    loan_remaining = 0
    monthly_pay = 0
    month_count = 0
    total_interest = 0
    month_ct = str(month_count)
    loan_num = str(loan_amt)

#user inputs for values
    user_input1 = int(input("How much would you like for a loan? "))
    loan_amt = user_input1

    user_input2 = int(input("How much is the annual interest rate? "))
    annual_interest_rt = user_input2

    user_input3 = int(input("How much are you paid monthly? "))
    monthly_pay = user_input3

#calculates interest and adds to total interest
    interest_eq = (1/ 12) * annual_interest_rt
    total_interest += round(interest_eq, 3)

#writers the header on csvfile: next line writer the month count, loan amount and total interest in respective columns
    writer.writerow(['Month Number', 'Loan Remaining', 'Total Accrued Interest'])
    writer.writerow([month_ct, str(loan_amt), str(total_interest)])

#while loop to determine howeveer many iterations it should run
    while True:
#calculations inside the while loop
        month_count += 1
        loan_amt = round((loan_amt - monthly_pay) + ((1 / 12) * annual_interest_rt), 3)
        total_interest += round(interest_eq, 3)
        month_num = str(month_count)

#if loan amount is less than 0 user paid off loan
        if (loan_amt <= 0):
            writer.writerow([month_num, str(0), str(total_interest)])
            break

#if mont count is 29(month count starts at 0) program should stop since it should iterate 30 times max
        elif (month_count == 30):
            writer.writerow([month_num, str(0), str(total_interest)])
            break

#writers the values on their columns and on a new row
        writer.writerow([month_num, str(loan_amt),str(total_interest)])

#calls back values function: creates csv file according to user specification
values()
with open(file_name + '.csv', 'w') as csvfile:
    testing(csvfile)
