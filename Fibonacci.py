def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input("How many terms?"))

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
        print("The Fibonacci Sequence:")
for i in range(nterms):
    print(fibonacci(i))
