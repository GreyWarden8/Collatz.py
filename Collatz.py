def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number:")
while n != 1:
    n = collatz(int(n))
    
try:
    n = input('Enter number: ') # takes user input
    while n !=1: # performs while loop until 'n' becomes 1
        n = collatz(int(n)) # passes 'n' to collatz() function until it arrives at '1'
except ValueError:
    print('Value Error. Please enter integer.')
