"""
Miniproject #2: Area & Volume Calculator
"""
import math

# check if numbers are > 0
def get_number(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Value must be greater than 0")
                continue
            return val
        except ValueError:
            print("Please enter a number")

# area calculator functions
def area_triangle(base, height):
    return base * height * 0.5

def area_circle(radius):
    return math.pi * radius**2

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_rhombus(diag1, diag2):
    return diag1 * diag2 * 0.5

def area_parallelogram(base, height):
    return base * height

# volume calculator functions
def volume_pyramid(base_side, height):
    return (base_side**2) * height * (1/3)

def volume_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height

def volume_cube(side):
    return side ** 3

def volume_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def volume_prism(side, width, height):
    return side * width * height

# mapping
shapes_2d = {
    "triangle": area_triangle,
    "circle": area_circle,
    "square": area_square,
    "rectangle": area_rectangle,
    "rhombus": area_rhombus,
    "parallelogram": area_parallelogram
}

shapes_3d = {
    "pyramid": volume_pyramid,
    "cone": volume_cone,
    "sphere": volume_sphere,
    "cube": volume_cube,
    "cylinder": volume_cylinder,
    "rectangular_prism": volume_prism
}

shape_inputs = {
    "triangle": ["base", "height"],
    "circle": ["radius"],
    "square": ["side"],
    "rectangle": ["length", "width"],
    "rhombus": ["diag1", "diag2"],
    "parallelogram": ["base", "height"],
    "pyramid": ["base_side", "height"],
    "cone": ["radius", "height"],
    "sphere": ["radius"],
    "cube": ["side"],
    "cylinder": ["radius", "height"],
    "rectangular_prism": ["side", "width", "height"]
}

while True:
    # user input
    print("--- ShapeMath ---")
    category = input("Choose category (2D / 3D) or 'exit': ").lower().strip()
    if category == "exit":
        print("User exited.")
        break
    elif category == "2d":
        print(f"Available 2D shapes: {', '.join(shapes_2d.keys())}")
        choice = input("Enter shape name: ").lower().strip()
        if choice in shapes_2d:
            requirements = shape_inputs[choice]
            values = []
            for item in requirements:
                num = get_number(f"Enter {item}: ")
                values.append(num)
            result = shapes_2d[choice](*values)
            print(f"--- Result: {result:.2f} square units ---")
        else:
            print("Shape not found!")
    elif category == "3d":
        print(f"Available 3D shapes: {', '.join(shapes_3d.keys())}")
        choice = input("Enter shape name: ").lower().strip()
        if choice in shapes_3d:
            requirements = shape_inputs[choice]
            values = []
            for item in requirements:
                num = get_number(f"Enter {item}: ")
                values.append(num)
            result = shapes_3d[choice](*values)
            print(f"--- Result: {result:.2f} cubic units ---")
    else:
        print("Please enter either 'exit' or '2D' or '3D'")
        continue