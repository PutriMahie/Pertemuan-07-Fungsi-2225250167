def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


n = 10
hasil = jumlah_n(n)

print(f"Jumlah bilangan 1 sampai {n} adalah {hasil}")