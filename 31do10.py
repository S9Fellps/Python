"""
import keyword #serve para aparecer todas as chaves de comando que tem
print (keyword.kwlist)

#---------------------------------------------------------

x= 'hello world'
print (x)

y= 3
print (y)

#---------------------------------------------------------

b= 4
b='sally' #ele esta substituindo, e nao dando prioridade 
print (b)

#---------------------------------------------------------

x= str(3) # x vai vira '3'
y= int(3) # y vai vira 3
z= float(3) # z vai vira 3.0
print (x, y, z)

#---------------------------------------------------------

x= 5
y='john'
print(type(x))
print (type(y))

#---------------------------------------------------------

a= 4
A= 'sally' 

print (a)
print (A)

#---------------------------------------------------------

x,y,z = 'Laranja', 'Banana', 'Maça'
print (x)
print (y)
print (z)

#---------------------------------------------------------

x=y=z= 'manga'
print (x)
print (y)
print (z)

#---------------------------------------------------------

fruits= ['apple', 'banana', 'cherry']

x,y,z = fruits

print (x)
print (y)
print (z)

#---------------------------------------------------------

x='maravilhoso'
def myfunc():
    print ('python is '+x)
    
myfunc()

#---------------------------------------------------------

x='maravilhoso'
def myfunc():
    x='dificil' # por estar aqui dentro ela vira uma variavel local
    print ('python is '+x)
    
myfunc()

print ('python is '+x)

#---------------------------------------------------------

def myfunc():
    global x
    x='fantastico'
    
myfunc()

print ('python is '+x)

#---------------------------------------------------------

username= input('Nome')
print ('O seu nome é: '+username)

#---------------------------------------------------------

price= 59

txt = f'The price is {price:.2f} dollars' #o 'f' que vem antes é o mesmo do ${} no html, e o '.2f' é o das casas deciamis que é para ter 

print (txt)

"""

