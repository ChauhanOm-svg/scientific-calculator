# advance scientific calculator
# start
import math
pi=3.14159

print("welcome to scientific calculator")
d=int(input("Enter domain of operation:\n"
            "press 1 for arithmetic operation\n"
            "press 2 for mathematical operation\n"
            "press 3 for trigonometric operation\n"
            "press 4 to calculate gcd or lcm of two numbers\n"
            "press 5 for bitwise operation\n "
            "press 6 for mensuration operations\n"))
if d==1:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    digit = int(input("enter operation :\n"
                      "press 1 for addition(+)\n"
                      "press 2 for multiplication(*)\n"
                      "press 3 for division(/)\n"
                      "press 4 for modulo(%)\n"
                      "press 5 for subtraction(-)\n"
                      "press 6 for floor division(//)\n"))

    match digit:
        case 1:
            print("Addition:", num1 + num2)
        case 2:
            print("Multiplication:", num1 * num2)
        case 3:
            print("Division:", num1 / num2)
        case 4:
            print("Modulo:", num1 % num2)
        case 5:
            print("Subtraction:", num1 - num2)
        case 6:
           print("Floor Division:", num1 // num2)
        case _:
            print("Invalid  arithmetic operator")
elif d==2:
    value =int(input("enter the value"))
    digit=int(input(
          "press 1 for square root\n"
          "press 2 for absolute value\n"))
    match digit:
        case 1:
            print("square root:",math.sqrt(value))
        case 2:
            print("absolute value:", abs(value))
        case _:
            print("Invalid  mathematical operator")
elif d==3:
    option=int(input("press 1 for  value of sin x\n"
                     "press 2 for  value of cos x\n"
                     "press 3 for  value of tan x\n"
                     "press 4 for value of sin inverse x\n"
                     "press 5 for value of cos inverse x\n"
                     "press 6 for value of tan inverse x\n"))
    x=int(input("Enter value of x"))
    match option:
        case 1:
            print("value of sin x:",math.sin(x))
        case 2:
            print("value of cos x:",math.cos(x))
        case 3:
            print("value of tan x:",math.tan(x))
        case 4:
            print("value of sin inverse x:",math.asin(x))
        case 5:
            print("value of cos inverse x:",math.acos(x))
        case 6:
            print("value of tan inverse x:",math.atan(x))
        case _:
            print("Invalid  trigonometric operator")
elif d==4:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    choose=int(input("press 1 for gcd\n"
                     "press 2 for lcm\n"))
    match choose:
        case 1:
            print("GCD:",math.gcd(a,b))
        case 2:
            print("LCM:",math.lcm(a,b))
        case _:
            print("Invalid operation")
elif d==5:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    select=int(input("press 1 for bitwise AND\n"
                     "press 2 for bitwise OR\n"
                     "press 3 for bitwise XOR\n"))
    match select:
        case 1:
            print("bitwise And:",a & b)
        case 2:
            print("bitwise Or:",a | b)
        case 3:
            print("bitwise Xor:",a ^ b)
        case _:
            print("Invalid operation")
elif d==6:
    selection=int(input("press 1 to calculate the area of square\n"
                        "press 2 to calculate the perimeter of square\n"
                        "press 3 to calculate the area of rectangle\n"
                        "press 4 to calculate the perimeter of rectangle\n"
                        "press 5 to calculate the area of circle\n"
                        "press 6 to calculate the circumference of circle\n"
                        "press 7 to calculate the area of triangle\n"
                        "press 8 to calculate the perimeter of triangle\n"))
    match selection:
      case 1:
          side = float(input("Enter side: "))
          print("Area of square =", side * side)
      case 2:
          a = float(input("enter side of square"))
          print("perimeter of square :", a*4)
      case 3:
          l = float(input("enter length of rectangle"))
          b = float(input("enter breadth of rectangle"))
          print("area of rectangle =", l*b)
      case 4:
          l = float(input("enter length of rectangle"))
          b = float(input("enter breadth of rectangle"))
          print("perimeter of rectangle =",2*(l+b))
      case 5:
          r=float(input("Enter radius of circle"))
          print("area of circle =", pi*r*r)
      case 6:
          r = float(input("Enter radius of circle"))
          print("circumference of circle =", pi * r * 2)
      case 7:
          h= float(input("enter height of triangle"))
          b = float(input("enter breadth of triangle"))
          print("area of triangle =", 0.5*b*h)
      case 8:
          s1= float(input("enter first side of triangle"))
          s2= float(input("enter second side of triangle"))
          s3 = float(input("enter third side of triangle"))
          print("perimeter of triangle:",s1+s2+s3)
      case _:
          print("Invalid operation")
else:
    print("calculator can not perform this operation\n"
          "soryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n")
    print("press 0 to exit")













