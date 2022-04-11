def upperlow(): 
    str=input("enter")   
    upper=0
    low=0
    i=0
    while i<len(str):
        if str[i]>='a' and str[i]<='z':
            low=low+1
        elif str[i]>='A'and str[i]<='Z':
            upper=upper+1
        i=i+1
    print('lower',low)
    print('upper',upper)
upperlow()
        