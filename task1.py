print(103993/33102)#рациональное приближение с тосностью до 9 знака.
print((4/1)-(4/3)+(4/5)-(4/7)+(4/9)-(4/11)+(4/13)-(4/15)+(4/17)-(4/19)+(4/21)-(4/23)+(4/25)-(4/27)+(4/29))#ряд Лейбница, бесконечный ряд чем длиннее тем точнее дает значение, но так то чепуха
print(3+4/(2*3*4)-4/(4*5*6)+4/(6*7*8)-4/(8*9*10)+4/(10*11*12)-4/(12*13*14)+4/(14*15*16)-4/(16*17*18))#ряд Нилоканта , та же проблема что и с рядом Лейбница однако точность вычислений выше при меньшем колличестве итераций
for i in range (1,1000):
    A=3
    B=2
    C=3
    D=4
    if i%2!=0:
        A+=4/(B*C*D)
        B+=2
        C+=2
        D+=2
    else :
        A-=4/(B*C*D)
        B+=2
        C+=2
        D+=2
        
print (A)#как видно ряд нилоканта при ста итерациях не дает высокой точности 
Inp=int(input("введите точность после запятой для пи:"))
Pi=103993/33102
print(round(Pi,Inp))#эта гадость округляет
pi=str(Pi)
for i in range (Inp+2):
 print(pi[i],end="")#так лучше)