from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import logics

Window.size = (1080, 1920)

class Container(BoxLayout):

    def raschet(self):
        l = [self.dlina, self.stoyak, self.dlina2, self.stoyak2, self.vysota, self.dlina_b, self.etag,
             self.output_field, self.output_field2, self.cb]
        self.ob = logics.Obrabotka(l)
        self.flag1 = self.ob.flag1
        if not self.flag1:
            self.ob.vyvod()

    def next_set(self):
        if not self.flag1:
            self.ob.next()

    def previous_set(self):
        if not self.flag1:
            self.ob.previous()

class MyApp(App):
    def build(self):

        return Container()


if __name__ == '__main__':
    MyApp().run()