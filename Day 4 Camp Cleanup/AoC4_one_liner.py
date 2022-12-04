# This is for scientific purpose only. Don't try it in production!
with open("input.txt", "r") as oFile:
    suma = 0
    for line in oFile:
        if set(range(int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[:2][0]), int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[:2][1]) + 1)).issubset(set(range(int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[2:][0]), int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[2:][1]) + 1))) or set(range(int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[2:][0]), int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[2:][1]) + 1)).issubset(set(range(int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[:2][0]), int(line.replace('-', ' ').replace(',', ' ').replace('\n', '').split(' ')[:2][1]) + 1))):
            suma += 1

    print(suma)
