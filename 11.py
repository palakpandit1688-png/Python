#P1_Write a program to demonstrate conditional statements using if if-else and if-elif-else.

#if statement
num=(int(input("Enter number :")))

if num>0:
    print("Number is positive")

#if-else statement
    if num %2==0:
            print("Even number")

    else:
        print("Odd number")

#if-elif-else statement
marks=((int(input("Enter Marks:"))))

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")
        


