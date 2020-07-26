def verification_of_initial_data(stroka):  #Проверяет строку на наличие недопустимых символов
    L = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', ',', '-']
    if stroka:
        for i in L:
            stroka = stroka.replace(i, '')
        if len(stroka) == 0:
            return True
    return False


def verification_of_initial_data1(stroka):  #Проверяет строку на наличие недопустимых символов
    L = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', ',', '.']
    if stroka == '':
        return True
    if stroka:
        for i in L:
            stroka = stroka.replace(i, '')
        if len(stroka) == 0:
            return True
    return False


def leftover_cables(stroka):
    stroka = stroka.replace(' ', '')
    list1 = stroka.split(',')
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    return list1


def list_of_floors_from_range(range_list, stroka):
    floor_list = []
    for x in range_list:
        x = x.replace(',', '')
        a = x.split('-')
        floor_list.extend(list(range(int(a[0]), int(a[1]) + 1)))
    list1 = stroka.split(',')
    if stroka:
        for x in list1:
            floor_list.append(int(x))
    floor_list.sort()
    return floor_list


def initial_data_processing(stroka):  # Выявляет диапазоны этажей, возвращает список этажей
    stroka = stroka.replace(' ', '')
    list1 = []
    while True:
        index_0 = stroka.find('-')
        if index_0 == -1:
            break
        flag = True
        i = 1
        while flag and (index_0 - i) >= 0:
            chr = stroka[index_0 - i]
            flag = chr.isdigit()
            i += 1
        if (index_0 - i) <= 0:
            i = 3
        index_min = index_0 - i + 2
        j = 1
        flag = True
        while flag and (index_0 + j) < len(stroka):
            chr = stroka[index_0 + j]
            flag = chr.isdigit()
            j += 1
        if (index_0 + j) >= len(stroka):
            j += 1
        index_max = index_0 + j - 1
        stroka1 = stroka[index_min:index_max]
        list1.append(stroka1)
        stroka = stroka.replace(stroka1, '')
    stroka = stroka.replace(',,', ',').lstrip(',').rstrip(',')
    floor_list = list_of_floors_from_range(list1, stroka)
    return floor_list


def calculation_of_initial_data(vysota, dlina, stoyak, stroka):  # 'stroka' -  текст обозначающий номер стояка
    floor_list = initial_data_processing(stoyak)
    if 1 in floor_list:
        floor_list.remove(1)
    dictionary = {}
    list1 = []
    for x in floor_list:
        if x == 1:
            a = dlina
        else:
            a = dlina + (x - 2) * vysota
        dictionary[a] = stroka + ' этаж ' + str(x)
        list1.append(a)
    return dictionary, list1

def calculation_of_all_initial_data(vysota, dlina, stoyak, dlina2=None, stoyak2=None):
    dictionary1, list1 = calculation_of_initial_data(vysota, dlina, stoyak, 'Стояк 1')
    if stoyak2:
        dictionary2, list2 = calculation_of_initial_data(vysota, dlina2, stoyak2, 'Стояк 2')
        list1 += list2
        dictionary2.update(dictionary1)
        dictionary1 = dictionary2
    return dictionary1, list1

def subsetsum(A, n):
    L = []
    for N in n:
        list1 = []
        res = {0: []}
        k = 3
        while not list1:
            for i in A:
                newres = dict(res)
                # print(newres)
                for v, l in res.items():
                    if v + i < (N - k):
                        newres[v + i] = l + [i]
                    elif (N - k) < v + i <= N:
                        # print('N = ', N)
                        list1.append(l + [i])
                        # return l + [i]
                res = newres
            if k < 15:
                k += 1
            elif k >= 15:
                k += 5
            elif k > 100:
                break
        L.append(list1)
    return L
    #return None


def proverka(a, b): #Проверяет входят ли члены одного списка в другой, список "а" может быть вложенным
    if type(a[0]) == list:
        for x in a:
            for i in b:
                if i in x:
                    return True
    else:
        for i in b:
            if i in a:
                return True
    return False

def perebor(list_1, list_2):  # Перебирает варианты из двух списков
    L = []
    flag = True if type(list_1[0][0]) == list else False
    for i in list_1:
        for j in list_2:
            if not proverka(i, j):
                if flag:
                    a = i[:]
                else:
                    a = [i]
                a += [j]
                L.append(a)
            else:
                continue
    return L

def iteration_over_all_values(list): #Перебирает все возможные варианты
    list1 = list[0]
    for i in range(1, len(list)):
        if not list1:
            return False
        list1 = perebor(list1, list[i])
    return list1


def sorty_2(list, list_b):    #Доделать для различного числа бухт
    summa = sum(list_b)
    list1 = list[:]
    list2 = []
    for i in range(len(list1)):
        x = 0
        for j in list1[i]:
            x += j if type(j) == int or type(j) == float else sum(j)
        list2.append([summa - x, i])
    list2.sort()
    list1 = []
    for i in list2:
        list1.append(list[i[1]])
    return list1


def vvod():
    dlina = input('Введите длину кабеля до второго этажа ')
    vysota = input('Введите высоту этажей ')
    etaji = input('Введите этажи ')
    buhty = input('Введите длины бухт ')
    dlina = int(dlina)
    vysota = int(vysota)
    buhty = list(map(int, buhty.split(', ')))
    l = list(map(int, etaji.split('-')))
    etaji = list(range(l[0], l[1] + 1))

    A = []
    for i in etaji:
        A.append(dlina + (i - 2) * vysota)
    return A, buhty

def vyvod(dictionary, list, buhty):
    print('list=', list)
    for i in range(len(buhty)):
        print(i)
        print('\n', 'Бухта ' + str(buhty[i]) + ' метров:')
        if type(list[0][i]) == int or type(list[0][i]) == float:
            for j in list[0]:
                print(j, 'm', dictionary[j])
            print('остаток с бухты: ', str(buhty[i] - sum(list[0])), 'м')
        else:
            for j in list[0][i]:
                print(j, 'm', dictionary[j])
            print('остаток с бухты: ', str(buhty[i] - sum(list[0][i])), 'м')


def vyvod1(dictionary, list, buhty, m):
    s = ''
    print('list=', list)
    for i in range(len(buhty)):
        s += 'Бухта ' + ' ' + str(buhty[i]) + ' метров:' + '\n'
        if type(list[m][i]) == int or type(list[m][i]) == float:
            for j in list[m]:
                s += str(j) + 'm' + ' ' + dictionary[j] + '\n'
            s += 'остаток с бухты: ' + str(buhty[i] - sum(list[m])) + 'м' + '\n'
        else:
            for j in list[m][i]:
                s += str(j) + 'm' + ' ' + dictionary[j] + '\n'
            s += 'остаток с бухты: ' + str(buhty[i] - sum(list[m][i])) + 'м' + '\n\n'
    return s


def main():
    v = 3
    d = 23.0
    d2 = None
    s = '1, 2, 3 - 13'
    s2 = None
    if not verification_of_initial_data(s):
        print('Недопустимые символы в списке этажей. Допускаются только: \n'
              'цифры, пробел, ",", "-"')
    else:
        dictionary, A = calculation_of_all_initial_data(v, d, s, d2, s2)
        print(dictionary)
        for x in dictionary:
            print(x, ' ', dictionary[x])
        # A = [27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69]
        n = [46, 70, 90]
        # A, n = vvod()
        L = subsetsum(A, n)
        if not L[0]:
            print('Не найден один из вариантов с заданным диапазоном остатков')
        else:
            m = iteration_over_all_values(L)
            if m:
                m = sorty_2(m, n)
                vyvod(dictionary, m, n)
            else:
                print('Невозможно подобрать этажи для всех бухт с заданным остатком')

if __name__ == '__main__':
    main()
