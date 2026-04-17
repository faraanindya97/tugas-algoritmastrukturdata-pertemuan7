def fibonacci(n):
    a, b = 1, 1
    hasil = []

    for i in range(n):
        hasil.append(a)
        a, b = b, a + b

    return hasil


def fibonacci_ke_n(n):
    a, b = 1, 1

    for i in range(n - 1):
        a, b = b, a + b

    return a


while True:
    print("\nmenu pilihan")
    print("1. Barisan Fibonacci")
    print("2. M kali N")
    print("0. Keluar")

    pilih = input("pilih menu : ")

    if pilih == "1":
        n = int(input("Masukkan Jumlah Suku : "))
        hasil = fibonacci(n)
        print(f"barisan fibonacci sebanyak {n} suku :")
        print(", ".join(map(str, hasil)))

    elif pilih == "2":
        m = int(input("Masukkan nilai M : "))
        n = int(input("Masukkan nilai N : "))
        hasil = m * n
        print(f"Hasil M kali N adalah : {hasil}")

    elif pilih == "0":
        print("Terima kasih")
        break

    else:
        print("Pilihan tidak tersedia")