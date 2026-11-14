#Grade Identifier
while True:
    try:
        m=int(input("Enter the marks:"))
    except:
        print("Please enter numbers only! Like 80, not eighty")
        continue
    
    if m>100 or m<0:
        print("Invalid marks! Please enter marks between 0 to 100")
    elif m>=80:
        print("A+")
    elif m>=70:
        print("A")
    elif m>=60:
        print("B")
    elif m>=50:
        print("C")
    elif m>=40:
        print("D")
    elif m>=33:
        print("E")
    else:
        print("F")

    again=input("Do you want to check the grades of another student?(Yes/NO):")
    if again!='yes' and again!='Yes':
        print("Program ended")
        break
