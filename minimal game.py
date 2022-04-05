

from ast import Break


print("""Hello ,This is a minimal game . 
Each of you can reach 100 as soon as possible.""")

user1 = str(input("Please Enter Your Name : "))
user2 = str(input("Please Enter Your Name : "))



print(f"""
Hello : {user1} ,
hello : {user2}
""")
x = 0


while x != 100 :

    if x < 100 :
        user1_number = int(input(f"{user1} Please Enter Number : "))
        while user1_number > 10 :
            user1_number = int(input(f"{user1} Try Again ! The number entered must be between 1 - 10 : "))

        x+= user1_number 
        print(x)
    else :
        print(f"You Are win :{user1}")
        Break

    if x < 100 :
        user2_number = int(input(f"{user2} Please Enter Number : "))
        while user2_number > 10 :
            user2_number = int(input(f"{user2} Try Again ! The number entered must be between 1 - 10 : "))

        x+= user2_number 
        print(x)
    else :
        print(f"You Are win :{user2}")
        Break
