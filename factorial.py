num = int(input())
ans=1

#for i in range(2,num+1):
 #   ans=ans*i
#print(ans)

# using recursion
def factorial(num):
    if num ==1 or num==0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(num))



