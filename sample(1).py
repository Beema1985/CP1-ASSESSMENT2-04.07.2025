##import My_math
##print("Enter your choice:1.addition;2.division;3.multiplication;4.exit")
##n=int(input("Enter your choice as 1,2,3,4:"))
##if n==1:
##    My_math.my_sum()
##elif n==2:
##    My_math.my_dev()
##elif n==3:
##    My_math.my_mul()
##else:
##    print("Invalid input")
##break
##Assesment2-04.07.25-sarveshwaran


a=int(input("Enter the staring value"))
b=int(input("Enter the ending value"))
for i in range(a,b+1):
    if i%11==0:
        print (i)
