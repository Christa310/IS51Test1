


"""
The program is trying to determin with payment option is better (more money).
First option is 100 dollars per day for 10 days. The second option is 1 dollar 
a day with it being doubled each day for 10 days. There should be 2 functions to calculate the pay rate. 
Function 1 will calculate the amount for the first option.
Function 2 will claculate the amount for the 2nd option. 

Function1 will output 100 dollars * 10 days.
Function2 will loop 10 times, with each time doubling the amount and add the amount to the total.

if the amount is equal, we output to the user "Option 1 and Option 2 pays the same"
if option1 is better, we output to the user "Option 1 is better"
if option2 is better, we output to the user "Option2 is better" 
"""

"""
# option1
    return 100 * 10

# option2 
 amount = 1
 list1 = []
 loop 10 times
     add amount to list1
     amount *= 2
 sum = sum of all items in loop
 return sum
# main
    var1 = option1
    var2 = option2

    if var1 = var2 
     "Option 1 and Option 2 pays the same"
    if var1 > var 2 
     "Option 1 is better"
    else
     "Option 2 is better"

main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0,10):
        list1.append(amount)
        amount*=2
    total = sum(list1)
    return total 

def main():
    answer = ""
    var1 = option1() 
    var2 = option2() 
    if var1 == var2:
     answer = "Option 1 and Option 2 pays the same"
    if var1 > var2:
     answer = "Option 1 is better."
    else:
     answer = "Option 2 is better."
     print(answer)


main()