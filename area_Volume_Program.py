# Total of Area Functions
def triangle_area(base, height):
    area = (1 / 2) * base * height
    print("Triangle's area: ", area)  # Triangle Area function


def square_area(length, width):
    area = length * width
    print("Square's area: ", area)  # Square's Area function


def circle_area(radius):
    area = (22 / 7) * radius * radius
    print("Circle's area: ", area)  # Circle's Area function


def sector_area(radius, angle):
    area = 2 * (22 / 7) * radius * (angle / 360)
    print("Sector's area: ", area)  # Sector's Area function


def parallelogram_area(base, height):
    area = base * height
    print("Parallelogram's area: ", area)  # Parallelogram's Area function


def trapezoid_area(base, height, top_bar):
    area = ((top_bar + base) / 2) * height
    print("Trapezoid's area: ", area)  # Trapezoid's Area function


# Total of Volume Functions
def cube_vol(length):
    vol = length ** 3
    print("Cube's Volume: ", vol)  # Cube's Volume function


def cuboid_vol(base, height, width):
    vol = base * height * width
    print("Cuboid's Volume: ", vol)  # Cuboid's Volume function


def triangle_prism_vol(base, height, length):
    vol = (base * height * length) / 2
    print("Triangle prism's Volume: ", vol)  # Triangle Prism's Volume function


def cylinder_vol(radius, height):
    vol = (22 / 7) * (radius ** 2) * height
    print("Cylinder's Volume: ", vol)  # Cylinder's Volume function


def square_prism_vol(length, height):
    vol = (1 / 3) * (length ** 2) * height
    print("Square prism's Volume: ", vol)  # Square's Prism Volume function


def ball_vol(radius):
    vol = (4 / 3) * (22 / 7) * (radius ** 3)
    print("Ball's Volume: ", vol)  # Ball's Volume function


print("--------------------------------------------------")
print("     Area and Volume Calculator                   ")
print("         by BlackBossX                            ")
print("             Visit for more: www.blackboss.xyz    ")
print("--------------------------------------------------")

print("Enter (1) Area Calculator")
print("Enter (2) Volume Calculator")
choice = int(input())

if choice == 1:
    print("")
    print("--------------------------------------------------")
    print("Enter (1) Triangle Area")
    print("Enter (2) Square Area")
    print("Enter (3) Circle Area")
    print("Enter (4) Sector Area")
    print("Enter (5) Parallelogram Area")
    print("Enter (6) Trapezoid Area")
    print("--------------------------------------------------")

    choice2 = int(input())

    if choice2 == 1:
        print("Enter Base Size: ")
        base = float(input())
        print("Enter Height Size: ")
        height = float(input())

        triangle_area(base, height)

    elif choice2 == 2:
        print("Enter Length: ")
        length = float(input())
        print("Enter Height: ")
        height = float(input())

        square_area(length, height)

    elif choice2 == 3:
        print("Enter Radius: ")
        radius = float(input())

        circle_area(radius)

    elif choice2 == 4:
        print("Enter Radius: ")
        radius = float(input())
        print("Enter Angle: ")
        angle = int(input())

        sector_area(radius, angle)

    elif choice2 == 5:
        print("Enter Base: ")
        base = float(input())
        print("Enter Height: ")
        height = float(input())

        parallelogram_area(base, height)

    elif choice2 == 6:
        print("Enter Base: ")
        base = float(input())
        print("Enter Height: ")
        height = float(input())
        print("Enter Top Bar: ")
        top_bar = float(input())

        trapezoid_area(base, height, top_bar)

    else:
        print("Enter Number was Invalid")
elif choice == 2:
    print("")
    print("--------------------------------------------------")
    print("Enter (1) Cube Volume")
    print("Enter (2) Cuboid Volume")
    print("Enter (3) Triangle Prism Volume")
    print("Enter (4) Cylinder Volume")
    print("Enter (5) Square Prism Volume")
    print("Enter (6) Ball Volume")
    print("--------------------------------------------------")

    choice2 = int(input())

    if choice2 == 1:
        print("Enter Length: ")
        length = float(input())

        cube_vol(length)

    elif choice2 == 2:
        print("Enter Base: ")
        base = float(input())
        print("Enter Height: ")
        height = float(input())
        print("Enter Width: ")
        width = float(input())

        cuboid_vol(base, height, width)

    elif choice2 == 3:
        print("Enter Base: ")
        base = float(input())
        print("Enter Height: ")
        height = float(input())
        print("Enter Length: ")
        length = float(input())

        triangle_prism_vol(base, height, length)

    elif choice2 == 4:
        print("Enter Radius: ")
        radius = float(input())
        print("Enter Height: ")
        height = float(input())

        cylinder_vol(radius, height)

    elif choice2 == 5:
        print("Enter Length: ")
        length = float(input())
        print("Enter Height: ")
        height = float(input())

        square_prism_vol(length, height)

    elif choice2 == 6:
        print("Enter Radius: ")
        radius = float(input())

        ball_vol(radius)

    else:
        print("Enter Number was Invalid")
else:
    print("Enter Number was Invalid")
