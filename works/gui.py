import logics
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.checkbox import CheckBox
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 1920)


class RaschetApp(App):
    #def callback(self, instance):
        #pass

    def build(self):
        self.qwerty = logics.Posrednik()
        bl = BoxLayout(orientation='vertical')
        bl0 = BoxLayout(size_hint=(1, 0.08))
        lb1 = Label(text='Длина, м:', font_size=40, size_hint=(0.022, 1))
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
        lb3.text = '''Инструкция:
        Если МУС на последнем этаже - поставить галочку.
        "Этаж" - номер этажа до которого измерена длина, общий на 2 стояка.
        "Длина" - длина кабеля на выбранный этаж.
        "Этажи" - перечислить нужные этажи, через запятую или дефис (например 3, 5, 7-12).
        "Высота этажей" - высота типичного этажа. Десятичные дроби записывать через ".", а не ",".
        "Длины бухт" - перечислить длины бухт через запятую.
        '''
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

        bl10 = BoxLayout(size_hint=(1, 0.08))
        lb10 = Label(text='Если МУС на последнем этаже:', font_size=40, size_hint=(0.4, 1),
                    halign='left', valign='center')
        cb = CheckBox(color=(1, 1, 1, 3), size_hint=(0.003, 1))
        lb11 = Label(text='Этаж: ', font_size=40, size_hint=(0.1, 1),
                    halign='left', valign='center')
        ti10 = TextInput(font_size=50, size_hint=(0.15, 1), multiline=False)

        L = [ti0, ti1, ti2, ti3, ti4, ti5, lb3, lb6, ti10, cb]

        bl3 = BoxLayout(size_hint=(1, 0.08))
        bt0 = Button(text='Расчет')
        bt0.on_press = lambda: self.qwerty.raschet(L)
        bt1 = Button(text='Вперед')
        bt1.on_press = lambda: self.qwerty.next_set()
        bt2 = Button(text='Назад')
        bt2.on_press = lambda: self.qwerty.previous_set()
        bl3.add_widget(bt0)
        bl3.add_widget(bt1)
        bl3.add_widget(bt2)

        bl10.add_widget(lb10)
        bl10.add_widget(cb)
        bl10.add_widget(lb11)
        bl10.add_widget(ti10)

        bl.add_widget(bl10)
        bl.add_widget(bl0)
        bl.add_widget(bl1)
        bl.add_widget(bl2)
        bl.add_widget(bl5)
        bl.add_widget(bl6)
        bl.add_widget(bl3)
        bl.add_widget(bl4)

        return bl

if __name__ == '__main__':
    RaschetApp().run()
