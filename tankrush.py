def Trans_m(M):
    Trans = []
    for i in range(len(M[0])):
        Trans.append([])  
    for x in range(len(M[0])):
        for y in range(len(M)):
            Trans[x].append(M[y][x])
    return Trans
    


def TankRush(H1, W1, S1,  H2, W2, S2):
    s1 = S1.rsplit(' ')
    s2 = S2.rsplit(' ')
    elem = 0
    array_1 = []
    array_2 = []
    there = False
    for i in range(H1):
        array = []
        for j in range(W1):
            array.append(s1[i][j])
        array_1.append(array) 
    for i in range(H2):
        ar = []
        for j in range(W2):
            ar.append(s2[i][j])
        array_2.append(ar) 

    Trans_1 = Trans_m(array_1)
    Trans_2 = Trans_m(array_2)
   
    for i in range(W2):
        str_2 = ''.join(Trans_2[i])
        for j in range(W1):
            str_1 = ''.join(Trans_1[j])
            if str_1.count(str_2) == 1 and elem < W2:
                elem = elem + 1
                break
            elif str_1.count(str_2) ==  0 and  elem < W2:
                continue
    if elem == W2:
        there = True
    else:
        there = False
    return there