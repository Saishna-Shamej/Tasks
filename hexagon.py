def print_honeycomb(rows, cols):
    hexagon_height = 3  # number of lines used

    for n in range(rows):
        if n % 2 == 1:
            indent = " "
        else:
            indent = ""

        for i in range(hexagon_height):
            for j in range(cols):
                if i == 0:
                    print(indent + "  ___  ", end="")
                elif i == 1:
                    print(indent + " /   \\ ", end="")
                elif i == 2:
                    print(indent + " \\___/ ", end="")
            print()

print("Input 1")
print_honeycomb(3, 5)
print()
print("Input 2")
print_honeycomb(4, 7)
