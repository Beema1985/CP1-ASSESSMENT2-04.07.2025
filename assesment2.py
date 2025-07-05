#Assesment3-04.07.2025 print the series 1 4 7...40

#for i in range(1,41,3):
 #   print(i,end=' ')









##Assesment2-04.07.2025-Harini Priya.K
#Write a program that gets 2 inputs from user, starting  and ending value and print the number that are divisible by 11

    

x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))

for i in range(x,y):
    if i % 11 == 0:      
         print('Numbers divisible by 11 between',x, 'and', y,':',i)
 
