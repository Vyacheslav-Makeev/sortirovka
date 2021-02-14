

import time
class IncomingData:

    '''def verification_of_initial_data(self, stroka, valid_characters):
        """Проверяет на наличие недопустимых симвлов"""
        if stroka:
            for i in valid_characters:
                stroka = stroka.replace(i, '')
            stroka = stroka.replace(' ', '')
            if len(stroka) == 0:
                return False
        return True'''

    def separate_by_comma(self, stroka):
        """разбивает полученную строку в список по запятым и пробелам, удаляет пустые значения"""
        stroka = stroka.replace('-', ' - ').replace(' ', ',')
        list1 = stroka.split(',')
        list1 = [x for x in list1 if x != '']
        return list1


class LeftoverCables(IncomingData):
    """возвращает список длин бухт из полученной строки и сортирует список по возрастанию"""
    valid_characters = '1234567890,.'

    def __init__(self, stroka):
        self.list1 = self.separate_by_comma(stroka)
        self.leftover_cables()
        self.list1.sort()

    def leftover_cables(self):
        for i in range(len(self.list1)):
            self.list1[i] = float(self.list1[i])

    def return_val(self):
        return self.list1


class FloorList(IncomingData):
    """Выявляет этажи, рассчитывает длины. Выдает словарь формата 'длина: этаж, стояк' и список длинн
        если какие то длины совпадают, то в словаре остается только одна длина, вторая не учитывается"""
    valid_characters_stoyak = '1234567890,-'
    valid_characters_etag = '1234567890'
    valid_characters_dlina = '1234567890.'

    def __init__(self, stoyak, stoyak2=None, flag=False):
        """
        :param vysota: высота типового этажа, int
        :param dlina: измеренная длина до этажа, int
        :param stoyak: список этажей (строка), str
        :param flag: если True - МУС на верху, bool
        :param etag: этаж до которого измерена длина, int
        :param dlina2:
        :param stoyak2:
        """
        self.flag = flag
        self.stoyak = self.separate_by_comma(stoyak)
        self.floor_list1 = self.getting_list_of_floors(self.stoyak)
        self.floor_list2 = None
        if stoyak2:
            self.stoyak2 = self.separate_by_comma(stoyak2)
            self.floor_list2 = self.getting_list_of_floors(self.stoyak2)

    def list_of_floors_from_range(self, floor_range):
        """Выдает список этажей из полученного диапазона этажей"""
        min_floor = int(floor_range[0])
        max_floor = int(floor_range[2])
        if min_floor > max_floor:
            min_floor, max_floor = max_floor, min_floor
        floor_range_list = list(range(min_floor, max_floor + 1))
        return floor_range_list

    def getting_list_of_floors(self, list1):
        """Выдает список этажей"""
        floor_number_list = []
        while '-' in list1:
            if list1[0] == '-':
                del list1[0]
            if list1[-1] == '-':
                del list1[-1]
            if '-' in list1:
                num = list1.index('-')
                floor_number_list += self.list_of_floors_from_range(list1[num-1: num+2])
                del list1[num-1: num+2]
        for i in list1:
            floor_number_list.append(int(i))
        floor_number_list = sorted(list(set(floor_number_list)))
        return floor_number_list

    def calculation_of_initial_data(self, vysota, dlina, floor_list, stroka, floor):  # 'stroka' -  текст обозначающий номер стояка
        """Рассчитывает длины до каждого этажа из полученного списка.
        Выдает словарь формата 'длина: этаж, стояк' и список длинн"""
        if 1 in floor_list:
            floor_list.remove(1)
        dictionary = {}
        list1 = []
        floor = int(floor)
        dlina = int(dlina)
        vysota = int(vysota)
        for x in floor_list:
            if self.flag:
                a = dlina + (floor - x) * vysota
            else:
                a = dlina + (x - floor) * vysota
            dictionary[a] = stroka + ' этаж ' + str(x)
            list1.append(a)
        return dictionary, list1

    def calculation_of_all_initial_data(self, vysota, dlina, etag, dlina2):
        dictionary1, list1 = self.calculation_of_initial_data(vysota, dlina, self.floor_list1, '- стояк 1', etag)
        if self.floor_list2:
            dictionary2, list2 = self.calculation_of_initial_data(vysota, dlina2, self.floor_list2, '- стояк 2', etag)
            list1 += list2
            dictionary2.update(dictionary1)
            dictionary1 = dictionary2
        return dictionary1, list1

    def return_val(self,vysota, dlina, etag='2', dlina2=None):
        """
        :param vysota: высота типового этажа, int
        :param dlina: измеренная длина до этажа, int
        :param etag: этаж до которого измерена длина, int
        :param dlina2:
        """
        self.dictionary_all, self.list_all = self.calculation_of_all_initial_data(vysota, dlina,etag, dlina2)
        return self.dictionary_all, self.list_all


class Raschet():

    def __init__(self, dlina_k, dlina_b):
        self.dlina_k = dlina_k  # длины до этажей
        self.dlina_b = dlina_b
        self.list = []
        self.list1 = []  # для созданных наборов

    def subsetsum(self):
        print('Start subsetsum: ', time.ctime())
        for N in self.dlina_b:
            res = {0: []}
            list1 = []
            k = 0
            A_min = min(self.dlina_k)
            k_max = N - A_min
            while k <= k_max:
                for i in self.dlina_k:
                    newres = dict(res)
                    for v, l in res.items():
                        if v + i < (N - k):
                            newres[v + i] = l + [i]
                        elif (N - k) <= v + i <= N:
                            if l:
                                l = list(set(l))
                                l.sort()
                            list1.append(l + [i]) if i not in l else list1.append(l)
                    res = newres
                if k < 10:
                    k += 5
                elif k >= 10:
                    k += 5

            self.list.append(list1)
        for i in range(len(self.list)):  # удаляет дубликаты в каждом из списков
            self.list[i] = list(set(tuple(sorted(sub)) for sub in self.list[i]))
            self.list[i] = [list(sub) for sub in self.list[i]]
        #print(len(self.list[4]))
        #print(self.list[4])
        print('Stop subsetsum: ', time.ctime())


    def proverka(self, a, b):  # Проверяет входят ли члены одного списка в другой, список "а" может быть вложенным
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

    def perebor(self, list_1, list_2):  # Перебирает варианты из двух списков и составляет из них наборы
        print('Start perebor: ', time.ctime())
        L = []
        flag = True if type(list_1[0][0]) == list else False
        for i in list_1:
            for j in list_2:
                if not self.proverka(i, j):
                    if flag:
                        a = i[:]
                    else:
                        a = [i]
                    a += [j]
                    L.append(a)
                else:
                    continue
        print('Stop  perebor: ', time.ctime())
        return L


    def iteration_over_all_values(self):  # Перебирает все возможные варианты
        print('Start iteration_over_all_values: ', time.ctime())
        self.list1 = self.list[0]
        for i in range(1, len(self.list)):   # вернуть for i in range(1, len(self.list)):
            print(len(self.list[i]))
            if not self.list1:
                return False
            self.list1 = self.perebor(self.list1, self.list[i])
        print('Stop iteration_over_all_values: ', time.ctime())

    def sorty_2(self):  # Доделать для различного числа бухт
        print('Start sorty_2: ', time.ctime())
        summa = sum(self.dlina_b)
        list1 = self.list1[:]
        list2 = []
        for i in range(len(list1)):
            x = 0
            for j in list1[i]:
                x += j if type(j) == int or type(j) == float else sum(j)
            list2.append([summa - x, i])
        list2.sort()
        list1 = []
        for i in list2:
            list1.append(self.list1[i[1]])
        self.list1 = list1
        print('Stop sorty_2: ', time.ctime())

    def return_val(self):
        self.subsetsum()
        self.iteration_over_all_values()
        self.sorty_2()
        return self.list1


class Obrabotka():
    valid_characters_stoyak = '1234567890,-'
    valid_characters_etag = '1234567890'
    valid_characters_dlina = '1234567890.'
    valid_characters_b = '1234567890.,'
    def __init__(self, a):
        self.flag1 = False
        self.dlina = a[0].text
        self.stoyak = a[1].text
        self.dlina2 = a[2].text
        self.stoyak2 = a[3].text
        self.vysota = a[4].text
        self.dlina_b = a[5] .text    # список длин бухт
        self.etag = a[6].text
        self.output_field = a[7]
        self.output_field2 = a[8]
        self.cb = a[9].active

        self.nabor = []    #готовый набор (распределение бухты по этажам)
        self.nabor_dlin = []    #списки длинн распределенные по бухтам
        self.number = 0         # номер набора

        # Проверка корректности введенных данных
        self.verification_of_initial_data(self.dlina, self.valid_characters_dlina)
        self.verification_of_initial_data(self.stoyak, self.valid_characters_stoyak)
        self.verification_of_initial_data(self.vysota, self.valid_characters_etag)
        self.verification_of_initial_data(self.dlina_b, self.valid_characters_b)
        self.verification_of_initial_data(self.etag, self.valid_characters_etag)
        if self.dlina2:
            self.verification_of_initial_data(self.dlina2, self.valid_characters_dlina)
        if self.stoyak2:
            self.verification_of_initial_data(self.stoyak2, self.valid_characters_stoyak)
        if self.flag1:
            return

        self.dlina_b = LeftoverCables(self.dlina_b).return_val()
        floor_list = FloorList(self.stoyak, self.stoyak2, self.cb)
        self.dictionary_all, self.list_all = floor_list.return_val(self.vysota, self.dlina, self.etag, self.dlina2)
        self.nabor_dlin = Raschet(self.list_all, self.dlina_b).return_val()


    def verification_of_initial_data(self, stroka, valid_characters):
        """Проверяет на наличие недопустимых симвлов"""
        if stroka:
            for i in valid_characters:
                stroka = stroka.replace(i, '')
            stroka = stroka.replace(' ', '')
            if len(stroka) == 0:
                return
        self.output_field.text = 'недопустимые символы:\n %s\nдопускаются только:\n%s' % (stroka, valid_characters)
        self.flag1 = True

    def vyvod(self):
        s = ''
        for i in range(len(self.dlina_b)):
            s += 'Бухта %s метров:\n' % str(self.dlina_b[i])
            summa = 0
            if not self.nabor_dlin:
                self.output_field.text = 'Невозможно подобрать длины для всех бухт'
                return
            if type(self.nabor_dlin[self.number][i]) == list:
                for k in self.nabor_dlin[self.number][i]:
                    summa += k
                    s += str(k) + 'м ' + self.dictionary_all[k] + '\n'
            else:
                for k in self.nabor_dlin[self.number]:
                    summa += k
                    s += str(k) + 'м ' + self.dictionary_all[k] + '\n'
            s += 'Остаток с бухты: %sм\n\n' % str(self.dlina_b[i] - summa)
        self.output_field.text = s
        s1 = ''
        for i in self.dictionary_all:
            s1 += str(i) + 'м' + ' ' + self.dictionary_all[i] + '\n'
        self.output_field2.text = s1
        print(s)

    def next(self):
        if self.number < len(self.nabor_dlin):
            self.number += 1
            self.vyvod()
        else:
            return

    def previous(self):
        if self.number > 0:
            self.number -= 1
            self.vyvod()
        else:
            return

if __name__ == '__main__':

    dlina = '12'
    stoyak = '3-15'
    dlina2 = None
    stoyak2 = None
    vysota = '3'
    dlina_b = '67'
    etag = '2'
    L = [dlina, stoyak, dlina2, stoyak2, vysota, dlina_b, '', '', etag, False]

