'''data = '    mi texto mi texto   '
data2 = '#'
print(data2+data+data2)
print('Texto sin espacios: ')
print(data2+data.strip()+data2)
print(len(data))
print(len(data.strip()))


data = 'mi texto'
data2 = 'MI TEXTO'
print(data.upper())
print(data2.lower())


data = 'mi texto mas extenso'
data2 = 'Mi Texto Mas Extenso X2'
print(data.capitalize())
print(data2.swapcase())

str1 = "México lindo y querido, si muero cerca de tí..."
print("texto original: ", str1)
str2 = str1[7:25]
print("Substring: ", str2) # lindo y querido, s
str2 = str1[7:]
print("Substring: ", str2) # lindo y querido, si muero cerca de tí...

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)'''


