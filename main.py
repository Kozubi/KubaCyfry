__author__ = 'Marcin'

from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random
from functools import partial

class MyApp(GridLayout):
    def __init__(self, *args):
        super(MyApp, self).__init__()
        self.rows, self.cols = [3, 3]
        self.padding = 5
        self.spacing = 5

        self.sounds = {1: "1.mp3", 2: "2.mp3", 3: "3.mp3", 4: "4.mp3", 5: "5.mp3",
                       6: "6.mp3", 7: "7.mp3", 8: "8.mp3", 9: "9.mp3"}

        self.widgetList = []  # will store all buttons tp easy remove

        self.startGame()
        self.insertWidgets()

    def insertWidgets(self):
        if len(self.widgetList) > 0:
            for item in self.widgetList:
                self.remove_widget(item)
        # TODO button colors - they are too dark
        self.btnColors = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (.6, 0, .4, 1),
                          (1, 0, 1, 1), (0, 1, 1, 1), (1, 1, 0, 1), (1, 1, .5, 1), (1, .5, 1, 1)]

        self.btnNUMBERS = [num for num in range(1,10)] # buttons numbers
        self.btnNUMBERScopy = [num for num in range(1,10)] # copy of list for random generating new number\
                                                            #  for each button

        for i in self.btnNUMBERS:
            currentNumber = random.choice(self.btnNUMBERScopy) # selects number for button text
            color = random.choice(self.btnColors) # select random color for new button
            self.btnColors.remove(color) # will remove color from colors list to avoid duplicated colors
            btn = Button(text=str(currentNumber), font_size="45sp", background_color=color,
                         on_press=self.callback)
            btn.background_normal= "buttons/purple-button-hi.png"
            self.widgetList.append(btn) # will add button to this list - it used later for clearing Grid\
                                        #  from childrens
            self.add_widget(btn)
            self.btnNUMBERScopy.remove(currentNumber) # remove choosed number to avoid duplicated button numbers

    def startGame(self, *args):
        "will tale random numbet and plays correct audio"

        print("wybierz cyfre")
        self.NUMBER = random.choice(range(1, 10))
        # TODO dodac odtwarzanie dzwieku
        print(self.NUMBER, self.sounds[self.NUMBER])

    def callback(self, btn):
        """
        :param btn: here btn number will be taken to use it for sound
        :return:
        """
        if str(self.NUMBER) == btn.text:
            Clock.schedule_once(partial(self.soundPlayer, "hurra.mp3"))

        else:
            Clock.schedule_once(partial(self.soundPlayer, "to_nie.mp3"))
        self.startGame()
        self.insertWidgets()

    def soundPlayer(self, sound, *args):
        # function for playing sounds
        player = SoundLoader.load(sound)
        player.play()
        Clock.unschedule(self.soundPlayer)

class Main(App):
    def btnCallback(self, *args):
        print(args)

    def build(self):
        return MyApp()


Main().run()
