print("Enter any 10 numbers")
sum=0
avg=0
for i in range(1,11):
    n=int(input("> "))
    sum=sum+n
avg=sum/10
print("The sum of entered 10 numbers is",sum)
print("And their Average is",avg)