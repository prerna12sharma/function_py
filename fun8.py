def fun(n):
    print(n)
    if n==10:
        return 1
    return (fun(n+1)*2)
fun(1)
    
