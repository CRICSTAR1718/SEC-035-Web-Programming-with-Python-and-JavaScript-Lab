# #WAP TO PRINT AREA OF CIRCLE SQUARE RECTANGLE
def area_circle():
    r=float(input("Enter radius of the circel: "))
    a=3.14*r*r
    print("The area of circle is: ", a)
def area_rectangle():
    l=int(input("Enter length of rectangle: "))
    b=int(input("Enter breadth of rectangle: "))
    a=l*b
    print("The area of rectangle: ", a)
def area_square():
    s= int(input("Enter side of the square: "))
    a=s*s
    print("The area of square is: ", a)

choice =input("Choose calulate area for: circle/rectangle/square:  ").lower()
if choice=="circle":
    area_circle()
elif choice=="rectangle":
     area_rectangle()
elif choice=="square":
    area_square()
else:
    print("Invalid choice")