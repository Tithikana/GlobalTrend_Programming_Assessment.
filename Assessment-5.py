def fibonacci(n):
    if n<0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

val=int(input("Enter a number:"))
fib=fibonacci(val)
print("Fibonacci:",fib)
