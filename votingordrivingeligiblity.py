#Create a Scala program to check if a person is eligible to vote (age greater than or equal to 18) or
#eligible to drive (age greater than or equal to 16).

n= int(input())

if (n >=18):
    print("able to vote and drive")
elif(n>=16 and n<18):
    print("able to drive but cannot vote")
else:
    print("not eligible to vote or drive")