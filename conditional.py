                                  # condditionals 
# 1. if , if-else
# 2. nested 
# 3. Else if ladder 
# 4. Ternary 
# 5. Switch

#question 
# if cost price and selling price of an item is input through the keyboard , write a program to determine whether the seller has made profit or incurrred loss or no profit no . also dermine how much progit he made or loss he incurred.

price =  int(input('Buying price '))
selling = int(input('selling price '))

if selling>price:
    print('profit ' , selling-price)
elif selling == price:
    print("No Profit")
else :
    print('you losses ', price- selling)
