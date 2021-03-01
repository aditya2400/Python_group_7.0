
weights = [70,80,45,50]

a = sum(weights)
mean = a/4
print("The list of Weights  is     ",weights)
print("The sum Of the weights is   ",a)
print("the mean of the weights  is ",mean)
        
while(1):
    
    print('''

1.change weights
2.exit
 ''')
    
    ch =  int(input("Enter the Choice"))
    
    
        
    if ch == 1:
        c  = int(input("enter which one"))
        d = int (input("enter the weight"))
        weights[c] = d
        a = sum(weights)
        mean = a/4
        print("The list of Weights after change is        ",weights)
        print("The sum Of the weights is                  ",a)
        print("the mean of the weights after changeing is ",mean)
    else:
        exit()
