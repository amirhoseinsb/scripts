from cmath import tan
import math


#Calculate Area for Parallelogram
# --------------------------------------------------------
def Parallelogram():  
    print("\nWelcome To The Software\n")
    lob = input("Lentgh Of Base : ")
    mot = input("measurement of height : ")
    area = float(lob) * float(mot)
    print(f"Area Is :{area}")

# ----------------------------------------------------------

#Calculate the volume and total area of ​​the cylinder
# --------------------------------------------------------------
def cylinder():
    print("\nwelcome to the software\n")
    radius = float(input("Please Enter Radius : "))
    height = float(input("Please Enter Height : "))
    volume = (height * radius ** 2 * 3.14)  
    total_area_volume = 2 * 3.14 * radius * height + 2 * (3.14 * (radius ** 2))
    print(f"\nTotal Area Volume Is : {total_area_volume}\n")
    print(f"Volume Cylinder Is : {volume}\n")
# ---------------------------------------------------------------
# Calculate the area and volume of the sphere
def sphere():
    print("\nwelcome to the software\n")
    radius = float(input("Please Enter Radius For Sphere :"))
    print("\n")
    areasphere = 4 * 3.14 * (radius ** 2)
    volumesphere = 4 / 3 * 3.14 * (radius ** 2)
    print(f"Area For Sphere Is : {areasphere}\n")
    print(f"Volume For Sphere Is : {volumesphere}\n")
# ----------------------------------------------------------------------------
# Calculate the area of ​​a polygon

def polygon():
    print("\nwelcome to the software\n")
    sides_length = float(input("Please Enter The sides Length : "))
    print("\n")
    number_sides = int(input("Please Enter The Number Of Sides : "))
    area = (number_sides * (sides_length ** 2)) / (4 * tan(3.14 / number_sides))
    print(f"Area For Polygon Is : {area}")
# ----------------------------------------------------------------------------------
# Repetition String
def repetition():
    print("\nwelcome to the software\n")
    string = str(input("Please Enter The string character : "))
    repetition = int(input("Please Enter The repetition character : "))
    output = repetition * string
    print(output)
# --------------------------------------------------------------------------------------
# Create Complex Number
def __complex():
    print("\nwelcome to the software\n")
    n1 = int(input("Please Enter Number 1 : "))
    print("\n")
    n2 = int(input("Please Enter Number 2 : "))
    print("\n")
    __complex = complex(n1, n2)
    print(f"Your Complex Number Is : {__complex}")
# -------------------------------------------------------------------------------------------
# calculate Number Water molecules
def molecules():
    print("\nwelcome to the software\n")
    w = int(input("Please Enter The weight water in liter : ")) #weight_water
    l = 950
    m = (3.0 * 10 ** -23)
    nwm = ((w * l) / m) #number water molecules
    print(f"Number Water Molecules : {nwm}")
# ----------------------------------------------------------------------------------------------
# Convert Age To Seconds
def convert_age_to_seconds():
    print("\nwelcome to the software\n")
    age = int(input("Please Enter The Age : "))
    year_seconds = (3 / 156 * 10 ** 7)
    seconds_age = age * year_seconds
    print(f"seconds age == {seconds_age}")
# -------------------------------------------------------------------
# Calculate Taxation
def taxation():
    print("\nwelcome to the software\n")
    s = float(input("Please Enter The salary :"))
    print("\n")
    b = s * 0.07 # Insurance
    m = s * 0.1 # Taxation
    p = s - b - m # Received
    print(f"Insurance : {b}\n")
    print(f"Taxation : {m}\n")
    print(f"Received : {p}\n")
# ------------------------------------------------------------------------
# calculate inflation
def inflation():
    print("\nwelcome to the software\n")
    y1 = float(input("Please Enter The Commodity Prices In The previous year : "))  # Commodity prices in the previous year
    y2 = float(input("Please Enter The Commodity prices this year : "))  # Commodity prices this year
    t = (y2-y1) / y1 * 100
    y3 = y2 + y2 * t
    print(f"inflation = %{t} \t price In New Year {y3}")
# ---------------------------------------------------------------------------
def Number_of_weeks_year():
    print("\nwelcome to the software\n")
    year = int(input("please Enter The Year : "))
    week = year * 12 * 4
    print(f"Your Number Of Week Year Is : {week}")
# --------------------------------------------------------------------------------
def minute_for_year():
    print("\nwelcome to the software\n")
    # year = int(input("please Enter The Year : "))
    day = 24 * 60 # 1 hour == 60 minute
    myear = (1 * 365) * day
    print(f"Each year is equal to : {myear} Minute")
# ------------------------------------------------------------------------------------
