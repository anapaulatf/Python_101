#### AULA 01
print("Hello World")

x = 1
print(x)

x = x + 1
print(x)

## CONDITIONAL
x = 30
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finish')

## REPETITION
n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')


## EXPRESSIONS

# input
nam = input('Who are you?')
print('Welcome', nam)

inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)


## Exercise 3
hrs = input("Horas: ")
rate = input("Taxa: ")
x = float(hrs)
y = float(rate)
price = x * y
print("Preço", price)

## MORE CONDITIONAL STATEMENTS

x = 10
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


x = 8
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
print('All done')

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')

## quiz
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)


## USING FUNCTIONS
def thing():
    print('Hello')
    print('Fun')

thing()


big = max('Hello world')
print(big)

sval = '123'
type(sval)

print(sval + 1) #é preciso converter para inter
print(int(sval) + 1)


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('fr')


def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print(x)


## LOOPS AND ITERATION
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)


n = 10
while n > 0:
    print('Lather')
    print('Rinse')
    break #Caso contrário, ele não para
print('Dry off')


n = 10
while n > 0:
    print('Bumbum')
    print('Tamtam')
    break

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


# Definite loop
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

amigos = ['Jo','Ge','Di']
for friend in amigos:
    print('Oi, ', friend)
print('Done!')

# Countiung loops
zork = 0 #zork é o 'count'
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

zork = 0 #zork é o 'count'
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# searching using boolean variable
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)


# finding the largest value so far
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)


# if you want the smallest so far
smallest_so_far = None #absence of a value
print('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)

## is e isnot é para True, False e None. Geralmente é mais forte do que ==
