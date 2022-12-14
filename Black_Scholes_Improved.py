import math


print("Please enter the stock price")
p = float(input())

print("Please enter the strike price")
s = float(input())

print("How many days until expiration?")
t = float(input()/365)

print("Current risk-free interest rate")
r = float(input())

print("Volatility measured by annual standard deviation")
v = float(input())

#Formula for d1
A = math.log(p/s) #1st part of the numerator
B = ((r + ((v ** 2)/2)) * t) #2nd part of the numerator  
C = (v * math.sqrt(t)) #the denominator

d1 = ((A + B) / C)
d2 = float(d1 - C) 


#Formula for y1
E = float(.2316419 * abs(d1))
y1 = float((1 / (1 + E))) 
 
#Formula for y2
F = float(.2316419 * abs(d2))
y2 = float((1 / (1 + F)))


#Formula for z1
G = (-1 * ((d1 ** 2)/2))
z1 = float(.3989423 * (math.exp(G)))  

#Formula for z2
H = (-1 * ((d2 ** 2)/2))
z2 = float(.3989423 * (math.exp(H))) 


I = 1.330274 * (y1 ** 5)
J = 1.821256 * (y1 ** 4)
K = 1.781478 * (y1 ** 3)
L = .356538 * (y1 ** 2)
M = .3193815 * y1 
x1 = 1 - (z1 * (I - J + K - L + M))


I1 = 1.330274 * (y2 ** 5)
J1 = 1.821256 * (y2 ** 4)
K1 = 1.781478 * (y2 ** 3)
L1 = .356538 * (y2 ** 2)
M1 = .3193815 * y2 
x2 = 1 - (z2 * (I1 - J1 + K1 - L1 + M1))


d3 = 1 - x1
d4 = 1 - x2


N = (-1 * r * t)
O = p * x1
O1 = p * d3
P = s * math.exp(N) * x2
PP = s * math.exp(N)
P1 = s * math.exp(N) * d4

#This uses d3 and d4 because d1 and d2 are less than 0
if d1 < 0 and d2 < 0:
    Vc = O1 - P1
    Vp = Vc + PP - p
    Answer1 = input('Would you like to figure out the value of a Call, Put, or Both? ')
    if Answer1 == 'Put':
        print('Option Price (Put) = '+ str(Vp))
    if Answer1 == 'Call':
        print('Option Price (Call) = '+ str(Vc))
    elif Answer1 == 'Both':
        print('Option Price (Call) = '+ str(Vc))
        print('Option Price (Put) = '+ str(Vp))

#This uses x1 and x2 because d1 and d2 are greater than 0
if d1 > 0 and d2 > 0:
    Vc = O - P
    Vp = Vc + PP - p
    Answer1 = input('Would you like to figure out the value of a Call, Put, or Both? ')
    if Answer1 == 'Put':
        print('Option Price (Put) = '+ str(Vp))
        
    if Answer1 == 'Call':
        print('Option Price (Call) = '+ str(Vc))
        
    elif Answer1 == 'Both':
        print('Option Price (Put) = '+ str(Vp))
        print('Option Price (Call) = '+ str(Vc))
        
#This uses x1 and d4
if d1 > 0 and d2 < 0:
    Vc = O - P1
    Vp = Vc + PP - p
    Answer1 = input('Would you like to figure out the value of a Call, Put, or Both? ')
    if Answer1 == 'Put':
        print('Option Price (Put) = '+ str(Vp))

    if Answer1 == 'Call':
        print('Option Price (Call) = '+ str(Vc))
        
    elif Answer1 == 'Both':
        print('Option Price (Put) = '+ str(Vp))
        print('Option Price (Call) = '+ str(Vc))
        
#This uses d3 and x2
if d1 < 0 and d2 > 0:
    Vc = O1 - P
    Vp = Vc + PP - p 
    Answer1 = input('Would you like to figure out the value of a Call, Put, or Both? ')
    if Answer1 == 'Put':
        print('Option Price (Put) = '+ str(Vp))

    if Answer1 == 'Call':
        print('Option Price (Call) = '+ str(Vc))
        
    elif Answer1 == 'Both':
        print('Option Price (Put) = '+ str(Vp))
        print('Option Price (Call) = '+ str(Vc))
