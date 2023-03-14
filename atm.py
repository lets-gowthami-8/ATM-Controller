data={9182991724:"gowthami",9492432425:"mouni",9183999242:"vagdevi",9666430765:"teju"}
data_balance={9182991724:7000,9492432425:69694,9183999242:85674,9666430765:109030}
pin={9182991724:1724,9492432425:6909,9183999242:8574,9666430765:1430}
c_accountnumber=int(input("enter a account number: "))
c_pass=int(input("enter a pin number: "))
print("=====WELCOME======")
if c_accountnumber in data and c_pass == pin[c_accountnumber]:
    print('''  1.deposit
    2.withdraw
    3.ministatement
    4.pin genaration
  5.balance enquary''')
    option=int(input("enter a option: "))
    if(option==1):
        dep=int(input("enter a amount: "))
        data_balance[c_accountnumber] +=dep
        print(data_balance[c_accountnumber])
    elif(option==2):
        withdraw=int(input("enter a amount:"))
        data_balance[c_accountnumber] -=withdraw
        print( data_balance[c_accountnumber] )
    elif(option==3):
        c_name=str(input("enter a name: "))
        print("=====ATM======")
        print("The username----------",c_name)
        print("statement for--------",c_accountnumber)
        print("Total amount=",data_balance[c_accountnumber])
        print("Thank You","\N{grinning face}","\N{grinning face}","\N{grinning face}")
        print("==================")
    elif(option==4):
        print("change pin")
        s=int(input("enter a old pin: "))
        if(s==pin[c_accountnumber]):
            print(int(input("enter a new pin: ")))
            print("pin change successfully")
        else:
            print("pin does not match enter a correct pin")
    elif(option==5):
        print("balance enquiry :\n")
        s=int(input("enter the pin number :"))
        if(s==pin[c_accountnumber]):
            print(data_balance[c_accountnumber])
            print("Thank You","\N{grinning face}","\N{grinning face}","\N{grinning face}")
        else:
            print("enter  wrong pin enter correct pin")
else:
    print("enter a wrong details")
            
        
        