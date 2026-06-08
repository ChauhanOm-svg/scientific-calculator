# advance scientific calculator
# start
import math
pi = 3.14159
History=[]

while True:
    txt = "<SCIENTIFIC CALCULATOR>"
    print(txt.center(125))
    try:
     d = int(input("\nEnter domain of operation:\n"
                  "press 1 for arithmetic operation\n"
                  "press 2 for mathematical operation\n"
                  "press 3 for trigonometric operation\n"
                  "press 4 for (GCD||LCM)\n"
                  "press 5 for logical operation\n"
                  "press 6 for bitwise operations\n"
                  "press 7 for mensuration operations\n"
                  "press 8 to watch history\n"
                  "press 9 to clr screen\n"
                  "press 0 to exit the calculator\n"
                   ))
     if d==0:
        print("exit")
        break
     if d == 1:
        print("ARITHMETIC OPERATION")
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        op = int(input("enter operator :\n"
                       "press 1 for addition(+)\n"
                       "press 2 for multiplication(*)\n"
                       "press 3 for division(/)\n"
                       "press 4 for modulo(%)\n"
                       "press 5 for subtraction(-)\n"
                       "press 6 for floor division(//)\n"))

        match op:
          case 1:
            print("Addition:", num1 + num2)
            # place holder
            History.append(f"{num1}+{num2}={num1+num2}")
          case 2:
            print("Multiplication:", num1 * num2)
            History.append(f"{num1}*{num2}={num1 * num2}")
          case 3:
            print("Division:", num1 / num2)
            History.append(f"{num1}/{num2}={num1 / num2}")
          case 4:
            print("Modulo:", num1 % num2)
            History.append(f"{num1}%{num2}={num1 % num2}")
          case 5:
            print("Subtraction:", num1 - num2)
            History.append(f"{num1}-{num2}={num1 - num2}")
          case 6:
            print("Floor Division:", num1 // num2)
            History.append(f"{num1}//{num2}={num1 // num2}")
          case _:
            print("Invalid  arithmetic operator")
            continue
     elif d == 2:
            print("MATHEMATICAL OPERATION")
            value = float(input("enter the value"))
            digit = int(input(
                "press 1 for square root\n"
                "press 2 for absolute value\n"))
            match digit:
                case 1:
                    print("square root:", math.sqrt(value))
                    History.append(f"sqrt{value}={math.sqrt(value)}")
                case 2:
                    print("absolute value:", abs(value))
                    History.append(f"abs{value}={abs(value)}")
                case _:
                    print("Invalid  mathematical operator")
                    continue

     elif d == 3:
                    print("TRIGONOMETRIC OPERATION")
                    option = int(input("press 1 for  value of sin x\n"
                                       "press 2 for  value of cos x\n"
                                       "press 3 for  value of tan x\n"
                                       "press 4 for value of sin inverse x\n"
                                       "press 5 for value of cos inverse x\n"
                                       "press 6 for value of tan inverse x\n"))
                    # python trigonometric functions like sin(),cos() take input in radians
                    angle = int(input("Enter value of angle(degree)"))
                    match option:
                        case 1:
                            print("value of sin x:", math.sin(math.radians(angle)))
                        case 2:
                            print("value of cos x:", math.cos(math.radians(angle)))
                        case 3:
                            print("value of tan x:", math.tan(math.radians(angle)))
                        case 4:
                            print("value of sin inverse x:", math.asin(math.sin(math.radians(angle))))
                        case 5:
                            print("value of cos inverse x:", math.acos(math.cos(math.radians(angle))))
                        case 6:
                            print("value of tan inverse x:", math.atan(math.tan(math.radians(angle))))
                        case _:
                            print("Invalid  trigonometric operator")
                            continue
     elif d == 4:
            print("GCD/LCM OPERATIONS")
            a = int(input("enter the first number:"))
            b = int(input("enter the second number:"))
            choose = int(input("press 1 for gcd(greatest common divisor)\n"
                               "press 2 for lcm(least common multiple)\n"))
            match choose:
                case 1:
                    print("GCD:", math.gcd(a, b))
                    History.append(f"gcd {a} {b} ={ math.gcd(a, b)}")
                case 2:
                    print("LCM:", math.lcm(a, b))
                    History.append(f"lcm {a} {b} ={math.lcm(a, b)}")
                case _:
                    print("Invalid operation")
                    continue
     elif d == 5:
                    print("LOGICAL OPERATIONS")
                    a = int(input("enter the first number:"))
                    b = int(input("enter the second number:"))
                    choose = int(input("press 1 for logical AND\n"
                                       "press 2 for logical OR\n"))
                    match choose:
                        case 1:
                            print("logical AND:", int(bool(a)) and int(bool(b)))
                        case 2:
                            print("logical OR:", int(bool(a)) or int(bool(b)))
                        case _:
                            print("Invalid operation")
                            continue

     elif d == 6:
            print("BITWISE OPERATIONS")
            a = int(input("enter the first number:"))
            b = int(input("enter the second number:"))
            select = int(input("press 1 for bitwise AND\n"
                               "press 2 for bitwise OR\n"
                               "press 3 for bitwise XOR\n"
                               "press 4 for bitwise NOT\n"))
            match select:
                case 1:
                    print("bitwise And:", a & b)
                case 2:
                    print("bitwise Or:", a | b)
                case 3:
                    print("bitwise Xor:", a ^ b)
                case 4:
                    print("bitwise not:", ~a, ~b)
                case _:
                    print("Invalid operation")
                    continue
     elif d == 7:
            print("MENSURATION OPERATIONS")
            selection = int(input("press 1 to calculate the area of square\n"
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
                    History.append(f"Area of square={side * side}")
                case 2:
                    a = float(input("enter side of square"))
                    print("perimeter of square :", a * 4)
                    History.append(f"perimeter of square={a * 4}")
                case 3:
                    l = float(input("enter length of rectangle"))
                    b = float(input("enter breadth of rectangle"))
                    print("area of rectangle =", l * b)
                    History.append(f"Area of rectangle={l * b}")
                case 4:
                    l = float(input("enter length of rectangle"))
                    b = float(input("enter breadth of rectangle"))
                    print("perimeter of rectangle =", 2 * (l + b))
                    History.append(f"perimeter of rectangle={2*(l + b)}")
                case 5:
                    r = float(input("Enter radius of circle"))
                    print("area of circle =", pi * r * r)
                    History.append(f"Area of circle={pi * r * r}")
                case 6:
                    r = float(input("Enter radius of circle"))
                    print("circumference of circle =", pi * r * 2)
                    History.append(f"circumference of circle={pi * r * 2}")
                case 7:
                    h = float(input("enter height of triangle"))
                    b = float(input("enter breadth of triangle"))
                    print("area of triangle =", 0.5 * b * h)
                    History.append(f"area of triangle={0.5 * b * h}")
                case 8:
                    s1 = float(input("enter first side of triangle"))
                    s2 = float(input("enter second side of triangle"))
                    s3 = float(input("enter third side of triangle"))
                    print("perimeter of triangle:", s1 + s2 + s3)
                    History.append(f"perimeter of triangle={s1 + s2 + s3}")
                case _:
                    print("Invalid operation")
                    continue
     elif d==8:
         print(History)
     elif d==9:
         print(" "*50)
         print(" SCREEN CLEARED\n")
     else:
         print("calculator can not perform this operation\n")
    except ValueError:
        print("Invalid input Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Returning to main menu...\n")


















