n = int(input("Masukkan jumlah bilangan Fibonacci: "))

a, b = 0, 1
count = 0

print("Deret Fibonacci:")
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1