__author__ = 'Marcin'

from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random


class MyApp(GridLayout):
    def __init__(self, *args):
        super(MyApp, self).__init__()

        self.sounds = {1: "1.mp3", 2: "2.mp3", 3: "3.mp3", 4: "4.mp3", 5: "5.mp3",
                       6: "6.mp3", 7: "7.mp3", 8: "8.mp3", 9: "9.mp3"}

        self.rows, self.cols = [3, 3]
        self.padding = 5
        self.spacing = 5
        self.widgetList = []  # will store all buttons tp easy remove
         # numbers for buttons
        self.startGame()
        self.insertWidgets()

    def insertWidgets(self):
        if len(self.widgetList) > 0:
            for item in self.widgetList:
                self.remove_widget(item)
        # TODO button colors - they are too dark
        self.btnColors = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (.6, 0, .4, 1),
                          (1, 0, 1, 1), (0, 1, 1, 1), (1, 1, 0, 1), (1, 1, .5, 1), (1, .5, 1, 1)]

        self.btnNUMBERS = [num for num in range(1,10)]
        self.btnNUMBERScopy = [num for num in range(1,10)]

        for i in self.btnNUMBERS:
            currentNumber = random.choice(self.btnNUMBERScopy)
            color = random.choice(self.btnColors)
            self.btnColors.remove(color)
            btn = Button(text=str(currentNumber), font_size="45sp", background_color=color,
                         on_press=self.callback)
            self.widgetList.append(btn)
            self.add_widget(btn)
            self.btnNUMBERScopy.remove(currentNumber)

    def startGame(self, *args):
        "will tale random numbet and plays correct audio"

        print("wybierz cyfre")
        self.NUMBER = random.choice(range(1, 10))
        print(self.NUMBER, self.sounds[self.NUMBER])

    def callback(self, btn):
        """
        :param btn: here btn number will be taken to use it for sound
        :return:
        """
        if str(self.NUMBER) == btn.text:
            print("HURRA")

        else:
            print("TO NIE TO")
        self.startGame()
        self.insertWidgets()


class Main(App):
    def btnCallback(self, *args):
        print(args)

    def build(self):
        return MyApp()


Main().run()
