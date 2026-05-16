decimal=int(input("Please give me the value in decimal representation:"))
def converter(decimal):
    intermid=""
    if decimal <= 1:
        return str(decimal)
    elif decimal % 2 != 0:
        intermid="1"
    else:
        intermid="0"
    
    return converter(decimal//2)+intermid
print(converter(decimal))
        
