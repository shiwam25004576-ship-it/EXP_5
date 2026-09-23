

def Empcalc():
    Name=input("ENter NAMe:")
    Age=int(input("Enter Age:"))
    sal=float(input("Enter sal:"))
    HRA=(sal*35)/100
    PF=(sal*25)/100
    NetSal=sal+HRA+PF
    
    if (NetSal >= 30000) and (NetSal <= 100000):
        print("senior manager")
    elif (NetSal >= 20000) and (NetSal <= 29999):
        print("manager")
    else:
        print("front level job")
    return Name,Age,NetSal
    
Name,Age,NetSal=Empcalc()
print("Employee Name:",Name)
print("Employee AGE:",Age)
print("Employee NetSal:",NetSal)
    