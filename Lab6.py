#1
factorial = lambda n: 1 if n==0 else n*factorial(n-1)

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

term = lambda i: (n**i)/factorial(i)

terms_list = [term(i) for i in range(x+1)]

result = sum(terms_list)

print(f"e^{n} = {result}")


#2
n = int(input("Enter the number: "))
def Sum(n):
    my_sum=0
    for k in range (1,n+1):
        my_sum += (((-1)**(k+1))/k)
        print("The result is: ", my_sum)

Sum(n)
