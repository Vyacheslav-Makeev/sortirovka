import sortirovka
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)


class RaschetApp(App):
    #def callback(self, instance):
        #pass

    def build(self):
        self.qwerty = Raschet()
        bl = BoxLayout(orientation='vertical')
        bl0 = BoxLayout(size_hint=(1, 0.08))
        lb1 = Label(text='2 этаж, м:', font_size=40, size_hint=(0.022, 1))
        lb2 = Label(text='Этажи, через запятую или дефис:', font_size=40, size_hint=(0.1, 1),
                    halign='left', valign='center')
        bl0.add_widget(lb1)
        bl0.add_widget(lb2)

        bl1 = BoxLayout(size_hint=(1, 0.07))
        ti0 = TextInput(font_size=50, size_hint=(0.022, 1), multiline=False)    # Второй этаж
        ti1 = TextInput(font_size=50, size_hint=(0.1, 1), multiline=False)     # Этажи
        bl1.add_widget(ti0)
        bl1.add_widget(ti1)

        bl2 = BoxLayout(size_hint=(1, 0.07))
        ti2 = TextInput(font_size=50, size_hint=(0.022, 1), multiline=False)    # Второй этаж
        ti3 = TextInput(font_size=50, size_hint=(0.1, 1), multiline=False)     # Этажи
        bl2.add_widget(ti2)
        bl2.add_widget(ti3)

        bl4 = BoxLayout()
        lb6 = Label(font_size=40, halign='left', valign='top')
        lb6.bind(size=lb6.setter('text_size'))
        lb3 = Label(font_size=40, halign='left', valign='top')
        lb3.bind(size=lb3.setter('text_size'))
        bl4.add_widget(lb3)
        bl4.add_widget(lb6)

        bl5 = BoxLayout(size_hint=(1, 0.08))
        lb4 = Label(text='Высота этажей, м:', font_size=40, size_hint=(0.01, 1))
        lb5 = Label(text='Длины бухт, м:', font_size=40, size_hint=(0.01, 1))
        bl5.add_widget(lb4)
        bl5.add_widget(lb5)

        bl6 = BoxLayout(size_hint=(1, 0.08))
        ti4 = TextInput(text='3', font_size=50, size_hint=(0.02, 1), multiline=False)    # Высота этажей
        ti5 = TextInput(font_size=50, size_hint=(0.02, 1), multiline=False)    # Длины бухт
        bl6.add_widget(ti4)
        bl6.add_widget(ti5)

        L = [ti0, ti1, ti2, ti3, ti4, ti5, lb3, lb6]

        bl3 = BoxLayout(size_hint=(1, 0.08))
        bt0 = Button(text='Расчет')
        bt0.on_press = lambda: self.qwerty.receiving_and_processing_data(L)
        bt1 = Button(text='Вперед')
        bt1.on_press = lambda: self.qwerty.next_set(lb3)
        bt2 = Button(text='Назад')
        bt2.on_press = lambda: self.qwerty.previous_set(lb3)
        bl3.add_widget(bt0)
        bl3.add_widget(bt1)
        bl3.add_widget(bt2)

        bl.add_widget(bl0)
        bl.add_widget(bl1)
        bl.add_widget(bl2)
        bl.add_widget(bl5)
        bl.add_widget(bl6)
        bl.add_widget(bl3)
        bl.add_widget(bl4)


        return bl


class Raschet():
    dlina1 = 0
    dlina2 = 0
    vysota = 0
    etagi1 = ''
    etagi2 = ''
    buhty = ''
    A = ''
    dictionary = {}
    m = []
    flag = True
    k = 0
    def receiving_and_processing_data(self, L1):
        s = 'Длины, этажи:\n'
        ekran = L1[6]
        ekran2 = L1[7]
        if L1[0].text and sortirovka.verification_of_initial_data1(L1[0].text):
            self.dlina1 = float(L1[0].text)
        else:
            self.flag = False
        etagi1 = L1[1].text
        if sortirovka.verification_of_initial_data1(L1[2].text):
            self.dlina2 = float(L1[2].text) if L1[2].text != '' else None
        else:
            self.flag = False
        etagi2 = L1[3].text if L1[3].text != '' else None
        if L1[4].text and sortirovka.verification_of_initial_data1(L1[4].text):
            self.vysota = int(L1[4].text)
        else:
            self.flag = False
        if L1[5].text and sortirovka.verification_of_initial_data1(L1[5].text):
            self.buhty = sortirovka.leftover_cables(L1[5].text)
        else:
            self.flag = False


        if not sortirovka.verification_of_initial_data(etagi1):
            ekran.text = ('Недопустимые символы\nв списке этажей.\nДопускаются только: \n'
                  'цифры, пробел, ",", "-"')
        elif etagi2 and not sortirovka.verification_of_initial_data(etagi2):
            ekran.text = ('Недопустимые символы\nв списке этажей.\nДопускаются только: \n'
                          'цифры, пробел, ",", "-"')
        elif not self.flag:
            ekran.text = ('Недопустимые символы\nв списке этажей.\nДопускаются только: \n'
                          'цифры, пробел, ","')
        else:
            self.dictionary, self.A = sortirovka.calculation_of_all_initial_data(self.vysota, self.dlina1, etagi1,
                                                                                 self.dlina2, etagi2)
            for x in self.dictionary:
                s += str(x) + 'м' + ' ' + self.dictionary[x] + '\n'
            ekran2.text = s
            self.L = sortirovka.subsetsum(self.A, self.buhty)
            if not self.L[0]:
                ekran.text = 'Не найден один из вариантов\nс заданным диапазоном остатков'
            else:
                self.m = sortirovka.iteration_over_all_values(self.L)
                if self.m:
                    self.m = sortirovka.sorty_2(self.m, self.buhty)
                    ekran.text = sortirovka.vyvod1(self.dictionary, self.m, self.buhty, 0)
                else:
                    ekran.text = 'Невозможно подобрать этажи\nдля всех бухт с заданным\nостатком'
    def next_set(self, ekran):
        if self.k < len(self.m) - 1:
            self.k += 1
        ekran.text = sortirovka.vyvod1(self.dictionary, self.m, self.buhty, self.k)

    def previous_set(self, ekran):
        if self.k > 0:
            self.k -= 1
        ekran.text = sortirovka.vyvod1(self.dictionary, self.m, self.buhty, self.k)



if __name__ == '__main__':
    RaschetApp().run()