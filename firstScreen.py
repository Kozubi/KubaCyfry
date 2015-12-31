from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from main import MyApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

"""
Main screen for future options (like other games)
"""
class Splash(Screen):
    def __init__(self, **kwargs):
        super(Splash, self).__init__(**kwargs)

        self.grid = GridLayout(cols = 2, rows = 2)
        btn1 = Button(text="1")
        btn1.on_press = self.prin
        self.grid.add_widget(btn1)

        btn2 = Button(text="2")
        btn2.on_press = self.switchToNumbers
        self.grid.add_widget(btn2)
        self.add_widget(self.grid)

    def prin(self, *args):

        self.parent.current = "first"

        # TODO here will be alphabet

    def switchToNumbers(self, *args):
        self.parent.current = "numbers"
        APP_NUM.firstPopup()
       # APP_NUM.insertWidgets()


class NumScreen(Screen):
    def __init__(self, **kwargs):
        super(NumScreen, self).__init__(**kwargs)
        global APP_NUM # need to run in prin2 screen
        APP_NUM = MyApp()
        self.add_widget(APP_NUM)


if __name__ == "__main__":

    class MyApp2(App):

        def keyHandler(self, window, key, *args):
            # function to ovveride ESC button
            if key == 27:
                APP_NUM.killAll()
                self.root.current = "first"
                APP_NUM.numberPopUp.dismiss()
                APP_NUM.temp_popup.dismiss()
                # TODO DOROBIC ZEBY ON PRZLACZANIE SIE KASOWAL POPUPY
                # TODO will need to kill NumberApp when closing - add function in my app to kill it!!
                return True

        def open_settings(self, *largs):
            pass


        def build(self):
            Window.fullscreen=False
            Window.size = (400,240)

            Window.bind(on_keyboard=self.keyHandler)
            self.root = ScreenManager()
            self.root.add_widget(Splash(name="first"))
            self.root.add_widget(NumScreen(name="numbers"))
            self.root.current = "first"
            return self.root

    app = MyApp2()
    app.run()