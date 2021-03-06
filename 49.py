def bin(n):
    if(n>1):
        bin(n//2)
    print(n%2,end="")
n=int(input("enter value "))
bin(n)
print()