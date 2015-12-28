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
        self.WIDGET_LIST = [] # to store widget list
        self.RANDOM_NUMBER = random.choice(string.ascii_uppercase)

        #ModalView showing stuff to choose
        self.pop = ModalView(size_hint = (.5,.5))
        self.pop.auto_dismiss = False
        self.pop.add_widget(Button(text=str(self.RANDOM_NUMBER), on_press=self.pop.dismiss))

        for i in string.ascii_uppercase:
            x = random.uniform(0.1,0.99)
            y = random.uniform(0.1,0.99)
            z = random.uniform(0.1,0.99)

            btn = MyButton(text=str(i), on_press=self.checker)
            btn.background_color = (x,y,z,1)
            btn.background_normal = "buttons/purple-button-hi.png"
            self.add_widget(btn)
            self.WIDGET_LIST.append(btn)

        Clock.schedule_once(self.openP, 1) # TODO remove it when sound will be added


    def openP(self, *args):
        self.pop.open()


    def checker(self, btn):
        print("children", self.children)
        # will check is answer is correct and draw another popup
        if self.RANDOM_NUMBER == btn.text:
            print("WOHOOOO")
            self.s = self.SoundPlayer("hurra.wav")
        else:
            print("NOOOPE")
            self.s = self.SoundPlayer("nie.wav")
        for i in self.WIDGET_LIST:
            self.remove_widget(i)
        self.addWidgets()

    def SoundPlayer(self, sound):
        s = SoundLoader()
        s = s.load(sound)
        self.player.on_play = partial(self.PLAY, self.player.filename)
        self.player.on_stop = partial(self.STOP, self.player.filename)
        s.play()

    def PLAY(self, sound):
        pass


    def STOP(self, sound):
        pass

class MyApp(App):
    Window.fullscreen=False
    Window.size = (400,240)
    Window.title = "Apka"
    def build(self):
        return Alpha()

if __name__ == "__main__":
    MyApp().run()