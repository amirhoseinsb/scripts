

_month = int(input("""
Please Enter the number for month : 

1 = Farvardin
2 = Ordibehesht
3 = Khordad
4 = Tir
5 = Mordad
6 = Shahrivar
7 = Mehr
8 = Aban
9 = Azar
10 = Dey
11 = Bahman
12 = Esfand

"""))
if _month == 1 : # Farvardin
    day = int(input("What day of the month are you?\t"))
    x = 31 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 2: # Ordibehesht
    day = int(input("What day of the month are you?\t"))
    x = 62 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 3: # Khordad
    day = int(input("What day of the month are you?\t"))
    x = 93 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 4: # Tir
    day = int(input("What day of the month are you?\t"))
    x = 124 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 5: # Mordad
    day = int(input("What day of the month are you?\t"))
    x = 155 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 6: # Shahrivar
    day = int(input("What day of the month are you?\t"))
    x = 186 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 7: # Mehr
    day = int(input("What day of the month are you?\t"))
    x = 216 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")

elif _month == 8: # Aban
    day = int(input("What day of the month are you?\t"))
    x = 246 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")


elif _month == 9: # Azar
    day = int(input("What day of the month are you?\t"))
    x = 276 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")


elif _month == 10: # Dey
    day = int(input("What day of the month are you?\t"))
    x = 306 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")


elif _month == 11: # Bahman
    day = int(input("What day of the month are you?\t"))
    x = 336 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")


elif _month == 12: # Esfand
    day = int(input("What day of the month are you?\t"))
    x = 365 - day
    output = 365 - x
    print(f"\n{output} Remaining until Eid ")