#Input always into the form of string so first it's convert it
cpu = float(input("Enter the CPU: "))   # takie input from the user 

print(cpu)

if cpu > 50:
    print("Cpu over load")
elif cpu > 20 and cpu < 50:
    print("Send alart")    
else:
    print("CPU is normal")


if cpu > 20 and cpu < 50:
    print("Aleart")
