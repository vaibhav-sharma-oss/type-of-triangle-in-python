import math
side=[]
angle=[]
a=0
s=0
sum=0

print('Write a program to find Type of triangle')

print('Angles of triangle')
for i in range(0,3):
    print('angle',i+1,end=':-')
    a=int(input())
    angle.append(a)

print('Measerment of sides')
for i in range(0,3):
    print('Side',i+1,end=':-')
    s=int(input())
    side.append(s)

print('hieght of triangle',end=':-')
h = eval(input())

for i in range(0,3):
    sum = sum + angle[i] 

for i in range(0,3):
    if sum == 180 :                                 
       if angle[i]==90 or angle[i+1]==90 or angle[i+2]==90:
            pas= 'RIGHT-ANGLE'     
            break
       if angle[i]==60 and angle[i+1]==60 and angle[i+2]==60 and side[i]==side[i+1]==side[i+2]:
            pas='EQUILATRAL'
            break   
       if angle[i]>90 or angle[i+1]>90 or angle[i+2]>90 and side[i]!=side[i+1] and side[i]!=side[i+2] and side[i+1]!=side[i+2] and angle[i]!=angle[i+1] and angle[i]!=angle[i+2] and angle[i+1]!=angle[i+2] :
            pas='OBTUSE'
            break 
       if side[i]==side[i+1] or side[i]==side[i+2] or side[i+1]==side[i+2] and angle[i]==angle[i+1] or angle[i]==angle[i+2] or angle[i+1]==angle[i+2] :
           pas='ISOSCELES'         
           break
       if side[i]!=side[i+1] and side[i]!=side[i+2] and side[i+1]!=side[i+2] and angle[i]!=angle[i+1] and angle[i]!=angle[i+2] and angle[i+1]!=angle[i+2] :
           pas='SCALENE'        
           break     
    else:
        print('From this angle which was given by you not possible')
        break


       
 

print('predict the type of triangle (EQUILATRAL , ISOSCELES , OBTUSE , RIGHT-ANGLE or SCALENE TRIANGL) ' ,end= ':- ')
pre=input()
if pas == pre:
     print('your pridiction is right. The triangle is :-',pas)
     print('Area of',pas,'triangle ')
     for i in range(0,3): 
         if pas == 'EQUILATRAL':
             area= (math.sqrt(3)/4)*pow(side[i],2)
             print('Area is :- ', area)
             break
         if pas == 'ISOSCELES':
             area = (side[i] * h)/2
             print('Area is :- ', area) 
             break 
         if pas == 'OBTUSE':
             area = (side[i] * h)/2
             print('Area is :- ', area)
             break
         if pas == 'RIGHT-ANGLE':
             area = (side[i] * h)/2
             print('Area is :- ', area)
             break
         if pas == 'SCALENE':
             area = (side[i] * h)/2
             print('Area is :- ', area)
             break
     print('perimeter of',pas,'triangle')
     for i in range(0,3): 
         if pas == 'EQUILATRAL':
             pre= 3*side[i]
             print('perimeter is :- ', pre)
             break
         if pas == 'ISOSCELES':
             pre = 2*side[i]+side[i+1]
             print('perimeter is :- ', pre) 
             break 
         if pas == 'OBTUSE':
             pre = side[i] + side[i+2] + side[i+1]
             print('perimeter is :- ', pre)
             break
         if pas == 'RIGHT-ANGLE':
             pre = side[i] +side[i+1] + (math.sqrt(pow(side[i],2)+pow(side[i+1],2) ))
             print('perimeter is :- ', pre)
             break
         if pas == 'SCALENE':
             pre = side[i] + side[i+2] + side[i+1]
             print('perimeter is :- ', pre)
             break
else:
     print('Sorry,your prediction is wrong ')
     print('the right answer is',pas)

