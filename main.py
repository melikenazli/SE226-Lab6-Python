def product_func(n):
    """This function finds the product of the series (n/n+2)-10 replacing n with 1 through n,
    where n is a number specified by the user."""
    global prod
    if n != 1:
        prod = prod * ((n/(n+2))-10)
        product_func(n - 1)
    else:
        prod = prod * ((1/(1+2))-10)


print(product_func.__doc__)
sum = lambda n: (n-3)/(n*n)

number = int(input("Please enter a number:"))
my_list = []
my_list.extend(range(1, number))
my_list.append(number)
print(my_list)
sumOfNumbers = 0
for x in my_list:
    result = sum(x)
    sumOfNumbers = sumOfNumbers + result
print("Sum of numbers is: ", sumOfNumbers)
prod = 1
product_func(number)
print("Result of recursion is: ", prod)