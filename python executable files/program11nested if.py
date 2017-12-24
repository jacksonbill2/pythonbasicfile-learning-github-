# nested if else]
email=str(input("enter ur mail" +"  "+"id"))
name=str(input("enter ur name"))
password=str(input("enter ur  password"))  #here string  take the alphanumeric value s which is not possible in int which takes integer value
if email==email:
    if password==password:
        print(  "welcome" + "     "+name+"   "+email)
else:
    print("please check ur password")
    
input()
