from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
import random
from functools import partial
from time import sleep
import string


kv = """
<MyButton>:
    font_size: "50sp"
    background_color: (.7,.1,.1,.9)
"""

Builder.load_string(kv)

class MyButton(Button):
    pass

class Alpha(GridLayout):
    def __init__(self, *args):
        super(Alpha, self).__init__(*args)
        # a bit of layout
        self.cols, self.rows = 5,6
        self.spacing = 2
        self.padding = 5

        self.addWidgets()



    def addWidgets(self, *args):
        self.RANDOM_NUMBER = random.choice(string.ascii_uppercase)

        #ModalView showing stuff to choose
        self.pop = ModalView(size_hint = (.5,.5))
        self.pop.auto_dismiss = False
        self.pop.add_widget(Label(text=str(self.RANDOM_NUMBER)))

        for i in string.ascii_uppercase:
            self.add_widget(MyButton(text=str(i), on_press=self.pop.open))

        Clock.schedule_interval(self.openP, 3) # TODO remove it when sound will be added

    def openP(self, *args):
        self.pop.open()

    def checker(self, *args):
        # will check is answer is correct and draw another popup
        if self.RANDOM_NUMBER ==


class MyApp(App):
    Window.fullscreen=False
    Window.title = "Apka"
    def build(self):
        return Alpha()

if __name__ == "__main__":
    MyApp().run()