'''nativeVLAN = -9
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("This native VLAN and the data VLAN are different.")

nativeVLAN = 100
dataVLAN = 100
if nativeVLAN == dataVLAN or dataVLAN < 100:
    print("Éxito XD ")
else:
    print("Falla :'( ")

aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")

      
devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)

print(switches)

x = range(5,50,1)
for n in x:
    print(n,end="-")

x=input("Enter a number to count to: ")
x=int(x)

y=5
while y<=x:
    print(y)
    y=y+1

x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break

print("fuera")'''

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break

