
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print("1!:", factorial(1))
print("5!:", factorial(5))