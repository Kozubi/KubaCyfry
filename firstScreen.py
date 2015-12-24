from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from main import MyApp

"""
Main screen for future options (like other games)
"""
class Splash(GridLayout):
    def __init__(self):
        super(Splash, self).__init__()
        self.rows, self.cols = [1,2]

        btn1 = Button(text="1", on_press=self.callback)
        btn2 = Button(text="2", on_press=self.Pop)

        self.add_widget(btn1)
        self.add_widget(btn2)

    def callback(self, *args):
        self.clear_widgets()
        self.add_widget(MyApp())

    def Pop(self, *args):
        print(2)
        myPop = Popup()
        myPop.on_touch_move= self.mrrr
        myPop.open()

    def mrrr(self, *args):
        print("MRRRRRR", args)


if __name__ == "__main__":
    class MyApp2(App):
        def open_settings(self, *largs):
            pass
        def build(self):
            return Splash()

    app = MyApp2()
    app.run()