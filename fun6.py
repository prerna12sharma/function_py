def sum(n):
    print(n)
    if n==10:
        return 1
    return sum(n+1)
n=int(input("enter number: "))
sum(n)