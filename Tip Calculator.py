print('Welcome to the tip calculator.')
bill = int(input('Enter the total bill? $'))
tip_percent = int(input('What tip percentage would you like to give? 10, 12, or 15? '))
share = int(input('How many people to split the bill? '))
tip_amount = (tip_percent/bill)*100
tpp = round((tip_amount/share),2)
print('Each person should pay: $',tpp)