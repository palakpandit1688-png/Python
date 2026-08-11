#Write a program to illustrate variable scope using local global and nonlocal variables.

x = 10          #Global 
def outer():
    y = 20      # Local variable of outer()

    def inner():
        nonlocal y
        global x

        y = 30   # Changes outer()'s variable
        x = 40   # Changes global variable

        print("Inside inner function:")
        print("Global x =", x)
        print("Nonlocal y =", y)

    inner()

    print("Inside outer function:")
    print("Nonlocal y =", y)


outer()

print("Outside all functions:")
print("Global x =", x)
