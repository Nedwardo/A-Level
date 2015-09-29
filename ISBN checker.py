while True:
    try:
        ISBN = int(input("what is the barcode? "))
        break
    except:
            print("please input an interger")
while True:
    try:
        format_ = str(input("what is the standard used? "))
        if format_ == "IBSN10":
            result = IBSN10_Check(ISBN)
        elif format_ == "IBSN13":
            result = IBSN13_Check(ISBN)
        elif format_ == "UPC":
            result = UPC_Check(ISBN)
        
        break
    except:
            print("please input an string")

print (" The ", format_" is", result)
            
def IBSN10_Check (ISBN):
    valid = "Valid"
    n = 0
        if len(str(ISBN)) != 10:
            valid = "Invalid"
        else:
            for value in str(ISBN):
                n += 1 
                total += value*(10-n)
            if total%11 != 0:
                valid = "Invalid"
        return valid
    
def IBSN13_Check (ISBN):        
    valid = "Valid"
    n = 0
    if len(str(ISBN)) != 14:
        valid = "Invalid"
    else:
        for value in str(ISBN):
            n+=1
            if n%2 == 0:
                total += value*3
            else:
                total += value
        if total%10 != 0
            valid = "Invalid"
    return valid

def UPC_Check (ISBN):        
    valid = "Valid"
    n = 0
    if len(str(ISBN)) != 14:
        valid = "Invalid"
    else:
        for value in str(ISBN):
            n+=1
            if n%2 != 0:
                total += value*3
            else:
                total += value
        if total%10 != 0
            valid = "Invalid"
    return valid 
