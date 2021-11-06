num1=[1,2,3,4,5]
num2=[0,0,0,0,0]
def med(num1, num2):
    sor=sorted(num1+num2)
    if len(sor)==0:
        a=sor
    elif len(sor) %2==1:
        a = s[len(sor)//2]
    else:
        a = (s[len(sor)//2] + s[len(sor)//2 - 1]) /2
    return a
print(med(num1, num2))
