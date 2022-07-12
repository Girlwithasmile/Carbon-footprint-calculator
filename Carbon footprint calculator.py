import math
N = int(input('Enter no. of people in your house'))

#Carbon footprint due to lights
Q1 = int(input("How many lights do you have?"))
Q2 = int(input("Power in watt?"))
Q3 = int(input("How many hours do you use them?"))
sum1 = Q1*Q2*Q3/N

#Carbon footprint due to fans
Qno1 = int(input("How many fans do you have?"))
Qno2 = int(input("Power in watt?"))
Qno3 = int(input("How many hours do you use them?"))
sum2 = Qno1*Qno2*Qno3/N

#Carbon footprint due to AC
Qs1 = int(input("How many AC do you have?"))
Qs2 = int(input("Power in watt?"))
Qs3 = int(input("How many hours do you use them?"))
sum3 = Qs1*Qs2*Qs3/N

#initializing variable mode
mode = 0
Y = 0
Qsn1 = int(input('How far is your home from scchool/college/office?'))
Qsn2 = int(input('How do you travel? 1Train 2Bus 3Private car 4Rickshaw 5Walking 6Metro'))
if Qsn2 == 1:
       mode = 41
elif Qsn2 == 2:
       mode = 50
elif Qsn2 == 3:
      p= input('Do you car-pool?Y or N')
      if p == Y:
           mode = 55.5
      else:
       mode = 111
elif Qsn2 == 4:
       mode = 95
elif Qsn2 == 5:
       mode = 0
elif Qsn2 == 6:
       mode = 70
else:
       print('Invalid')

sum4 = Qsn1*mode

#initializing re variable
re = 0
Qsno1 = int(input('What do u give for recycling? 1Newspapers 2Wet waste 3Plastic'))
if Qsno1 == 1:
       re = 7
elif Qsno1 == 2:
       re = 8
elif Qsno1 == 3:
       re = 10

#Total carbon footprint of a person is given by variable sum
sum = (sum1 + sum2 + sum3 + sum4 - re ) 
print("Your carbon footprint is", sum)  

#using while loop we print instructions according to range of sum
while (sum < 5000):
    if (sum < 2000):
        print("You are living a good life without much damage to nature!Try and maintain this and even better life style. Feel free to have a look at our solutions.")
        break
    else:
        print("You have a high carbon footprint. Try and implement suggestions provided to reduce yours and live a better lifestyle")
        break
else:
    print("Take actions immediately! You are consuming hell lot of resources!")

#Customised solutions and suggestions
print("Suggestions to reduce carbon footprint:")
if sum1 > 2000:
       print('You can reduce your lights usage, switch them off when there is enough light, use more natural light.')
elif sum2 > 4000:
       print('You can reduce your fan usage by letting natural air in.')
elif sum3 > 2000:
       print('You can reduce use and pressure on AC by letting natural air or making use of fan, cooler.')
elif Qsn2 == 3:
       print('You can try to walk for short distances or use public transport, car-pooling whenever possible.')
else:
       print('Good going!You can try and implement general solutions wherever required and possible.')
