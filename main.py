done = False
p = 1

while not done:
    n = int(input("nr = "))

    if n < 100:
        done = True
    else:
        s = 0
        while n != 0:
            s = s + n % 10
            n = n // 10
            
        p *= s

        print(f"suma cifrelor nr = {s}")

print(f"produsul = {p}")

# se citesc nr atat tim cat sunt mai mari decat 100, sa se calculeze
# si afiseze pt fiecare nr suma cifrelor, apoi la final sa se afiseze produsul sumelor
