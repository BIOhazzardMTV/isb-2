import math
with open("GPSCH.txt", mode='r', encoding='UTF-8') as text:
    reader = text.read()
    dic = {}
    lst = []
    lst2 = []
    z = 0
    x = 0
    count = 0
    for i in reader:
        dic[z] = reader[count:count + 8]
        lst.append(i)
        lst2.append(i)
        x += 1
        if x == 8:
            z += 1
            count += 8
            x = 0
    print(dic)
    print(lst)
    lst = list(map(int, lst))
    lst2 = list(map(int, lst))
    print(lst2)

    # Частотный побитовый тест.
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = -1
    print(lst)
    print(sum(lst))
    S1 = (-1/math.sqrt(128))*sum(lst)
    print(S1)  # 1.0606601717798212
    P1 = math.erfc(S1/math.sqrt(2))
    print(P1)  # 0.2888443663464849

    # Тест на одинаковые подряд идущие биты.
    S2 = (1 / 128) * sum(lst2)
    print(S2)
    if abs(S2 - 0.5) < 2 / math.sqrt(128):
        print("Good :)")
    else:
        print("Bad :(")
    ri = []
    for i in range(len(lst2) - 1):
        if lst2[i] == lst2[i + 1]:
            ri.append(0)
        else:
            ri.append(1)
    print(ri)
    Vn = sum(ri)
    print(Vn)
    P2 = math.erfc((abs(Vn - 2 * 128 * S2 * (1 - S2))) / (2 * math.sqrt(2 * 128) * S2 * (1 - S2)))
    print(P2)  # 0.42870928611174086

    # Тест на самую длинную последовательность единиц в блоке.
    lst3 = []
    for k, v in dic.items():
        max2 = 1
        for i in range(len(v)):
            max1 = 0
            if v[i] == "1":
                z = i
                while v[z: z + 1] == "1":
                    z += 1
                    max1 += 1
            if max1 > max2:
                max2 = max1
        lst3.append(max2)
    print(lst3)
    v1 = lst3.count(1)
    v2 = lst3.count(2)
    v3 = lst3.count(3)
    v4 = lst3.count(4) + lst3.count(6)
    X2 = 0
    X2 += ((v1 - 16 * 0.2148) ** 2) / (16 * 0.2148)
    X2 += ((v2 - 16 * 0.3672) ** 2) / (16 * 0.3672)
    X2 += ((v3 - 16 * 0.2305) ** 2) / (16 * 0.2305)
    X2 += ((v4 - 16 * 0.1875) ** 2) / (16 * 0.1875)
    print(X2)  # 0.90045395
