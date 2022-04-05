
from time import strftime
while True :
    second = strftime("%S") 
    minute = strftime("%M") 
    hour = strftime("%H") 
    print(f"Clock = {hour}:{minute}:{second}\r",end ="")