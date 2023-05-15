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
