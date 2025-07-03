import math
num = float(input("Enter a number: "))

if num<0:
    print("SQUARE ROOT OF THE NEGATIVE NUMBER NOT DEFINED(ONLY FOR THE REAL NUMBER)")
else:
    sqrt=math.sqrt(num)
    print(f"SQUARE ROOT OF THE NUMBER OF {num} is {sqrt}")

if num<0:
    print("THE LOG OF THE NUMBER IS NOT DEFINED(ONLY FOR THE REAL NUMBER)")
else:
    log_result =math.log(num)
    print(f"THE LOG OF THE FOLLOWING NUMBER IS {num} is {log_result}")
if num<0:
    print("THE SINE OF THE FOLLOWING NUMBER IS NOT POSSIBLE")
else:
    sin_result = math.sin(num)
    print(f"THE SINE OF THE FOLLOWING IS {num} is {sin_result}")
