def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("5!:", factorial(5))