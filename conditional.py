                                  # condditionals 
# 1. if , if-else
# 2. nested 
# 3. Else if ladder 
# 4. Ternary 
# 5. Switch

#question 
# if cost price and selling price of an item is input through the keyboard , write a program to determine whether the seller has made profit or incurrred loss or no profit no . also dermine how much progit he made or loss he incurred.

# price =  int(input('Buying price '))
# selling = int(input('selling price '))

# if selling>price:
#     print('profit ' , selling-price)
# elif selling == price:
#     print("No Profit")
# else :
#     print('you losses ', price- selling)

#question 2
#Take input percentage of a student and print the grade accoridng to marks:
# a. 81-100 very good
# b. 71-80 good
# c. 61-70 fair
# d. <=40 fail

# number = int (input('how much you got the exam ? '))

# if number>=81:
#     print ('your grade is very good')
# elif number<81 and number>=71:
#     print('your result is good')
# elif number<=70 and number>=61:
#     print('your result is fair ')
# elif number<=61 and number>=40:
#     print('your result is poor')
# elif number<=40:
#     print('your result is fail')
# else:
#     print('invalid mark')




#take a positive interger input and tell if it is a four digit number or not 

a = (input('take a number '))

length = len(a)

if (length == 4):
    print('this is 4 digit number')

else:
    print('input size is ', length)

a = int(input('Give me a number '))
if (a>=1000 and a<=9999):
    print('it is 4 digit number')
else:
    print('it is not 4 digit number')