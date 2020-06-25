n=list(input("Enter the Binary value:"))
value=0
for i in range(len(n)):
    digit=n.pop()
    if digit=='1':
        value=value+pow(2,i)
print("The Decimal Value of the number is",value)