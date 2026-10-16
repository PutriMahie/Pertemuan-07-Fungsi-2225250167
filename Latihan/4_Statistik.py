def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]

    for x in data:
        total += x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    rata = total / len(data)

    return minimum, maksimum, rata


data = [70, 80, 65, 90, 75]

mn, mx, rt = statistik(data)

print(f"Data: {data}")
print(f"Nilai minimum: {mn}")
print(f"Nilai maksimum: {mx}")
print(f"Nilai rata-rata: {rt}")