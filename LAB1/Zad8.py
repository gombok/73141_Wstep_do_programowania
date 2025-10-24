#Amelia Kawik 73141

print("Zadanie ósme")

a = float(input("\nPodaj a: "))

b = float(input("\nPodaj b: "))

c = float(input("\nPodaj c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    
    x2 = (-b - delta**0.5) / (2*a)
    
    print("\nRównanie ma dwa różne rozwiązania:")
    
    print("x1 =", x1)
    
    print("x2 =", x2)
    
elif delta == 0:
    
    x = -b / (2*a)
    
    print("\nRównanie ma jedno podwójne rozwiązanie:")
    
    print("x =", x)
    
else:
    
    print("\nRównanie nie ma rozwiązań rzeczywistych.")

#Amelia Kawik 73141

