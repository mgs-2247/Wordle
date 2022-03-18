def main():
    ans=True
    while ans:
        
        print("MENU")
        print("--------------------------------------")
        print("1.Add")
        print("2.Substract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Even Check")
        print("6.Odd Check")
        print("7.Prime Check")
        print("8.Palindrome Check")
        print("9.Exit")
        print("-------------------------------------")
        ch=int(input("Enter choice(1-9):"))
        print("-------------------------------------")
        if ch==1:
            a = int(input("Enter A: "))
            b = int(input("Enter B: "))
            c = sum(a,b)
            print("Sum    :",c)
        elif ch==2:
            a = int(input("Enter A: "))
            b = int(input("Enter B: "))
            c = sum(a,-b)
            print("difference    :",c)
        elif ch==3:
            a = int(input("Enter A: "))
            b = int(input("Enter B: "))
            c = a*b
            print("Product    :",c)
        elif ch==4:
            a = int(input("Enter A: "))
            b = int(input("Enter B: "))
            c = a/b
            print("Quotient    :",c)
        
        elif ch==9:
            ans=False
        print("-------------------------------------")
        input("Press any key.....")
main()