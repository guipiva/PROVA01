a = 80000
b = 200000
anos = 0
hab1 = 0.03
hab2 = 0.015
while a < b:
    anos += 1
    a = a + (a * hab1)
    b = b + (b * hab2)
if a >= b:
    print(f"Em {anos} a populacao {a} ira ultrapassar a {b} em {anos} anos")

    print(f"Quantidade da populacao {a:.2f} em {anos} anos")

    print(f"Quantidade da populacao {b:.2f} em {anos} anos")



