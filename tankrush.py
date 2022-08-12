def Trans_m(M): # превращаем матрицу в транспонированную 
    Transpon_matr = [] # Trans - Transpon_matr
    for i in range(len(M[0])):
        Transpon_matr.append([])  
    for x in range(len(M[0])):
        for y in range(len(M)):
            Transpon_matr[x].append(M[y][x])
    return Transpon_matr
    


def TankRush(INP_HEIGHT_MAT_1, INP_WIDTH_MAT_1, INP_STR_MAT_1,  INP_HEIGHT_MAT_2, INP_WIDTH_MAT_2, INP_STR_MAT_2): # H1 -  INP_HEIGHT_MAT_1, W1 - INP_WIDTH_MAT_1, S1 - INP_STR_MAT_1,  H2 - INP_HEIGHT_MAT_2, W2 - INP_WIDTH_MAT_2, S2 - INP_STR_MAT_2
    input_str_1 = INP_STR_MAT_1.rsplit(' ') # s1 - input_str_1
    input_str_2 = INP_STR_MAT_2.rsplit(' ') # s2 - input_str_2
    elem = 0
    array_inp_str_1 = [] # array_1 - array_inp_str_1
    array_inp_str_2 = [] # array_2 - array_inp_str_2
    there = False
    for i_str in range(INP_HEIGHT_MAT_1): # i - i_str
        array = []
        for j_row in range(INP_WIDTH_MAT_1): # j - j_str
            array.append(input_str_1[i_str][j_str])
        array_inp_str_1.append(array) 
    for i in range(INP_HEIGHT_MAT_2):
        ar = []
        for j in range(INP_WIDTH_MAT_2):
            ar.append(s2[i][j])
        array_inp_str_2.append(ar) 

    TRANS_MATR_1 = Trans_m(array_inp_str_1)# Trans_1 - TRANS_MATR_1
    TRANS_MATR_2 = Trans_m(array_inp_str_2)# Trans_2 - TRANS_MATR_2
    for i in range(W2):
        str_2 = ''.join(TRANS_MATR_2[i])
        for j in range(INP_WIDTH_MAT_1):
            str_1 = ''.join(TRANS_MATR_1[j])
            if str_1.count(str_2) == 1 and elem < INP_WIDTH_MAT_2:
                elem = elem + 1
                break
            elif str_1.count(str_2) ==  0 and  elem < INP_WIDTH_MAT_2:
                continue
    if elem == INP_WIDTH_MAT_2:
        found = True # there-found
    else:
        found = False# there-found
    return found
