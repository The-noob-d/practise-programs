#Write a function to check if a given number is both even and positive.

number = int(input())

if number %2 == 0 and number >=0:
    print("number is even and positive")
else:
    print("number is not even or positive")