def pattern(n):
    print(n)
    if n==10:
        return 1
    else:
        return pattern(n+3)
n=int(input('enter'))
pattern(n)