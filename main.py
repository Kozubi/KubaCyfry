__author__ = 'Marcin'

from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader, Sound
from kivy.clock import Clock
import random
from functools import partial


class MyApp(GridLayout):
    def __init__(self, *args):
        super(MyApp, self).__init__()
        self.rows, self.cols = [3, 3]
        self.padding = 5
        self.spacing = 5
        self.sounds = {1: "1.wav", 2: "2.wav", 3: "3.wav", 4: "4.wav", 5: "5.wav",
                       6: "6.wav", 7: "7.wav", 8: "8.wav", 9: "9.wav"}
        self.widgetList = []  # will store all buttons to easy remove
        self.block = False # for blocking overlaping sounds

        self.insertWidgets()
        self.startGame()

    def insertWidgets(self):
        self.disabled = True # for initial run!
        if len(self.widgetList) > 0:
            for item in self.widgetList:
                self.remove_widget(item)
        # TODO button colors - they are too dark
        self.btnColors = [(1, .2, .2, 1), (0, 1, 0, 1), (0, 0, 1, 1), (.6, 0, .4, 1),
                          (1, 0, 1, 1), (0, 1, 1, 1), (1, 1, 0, 1), (1, 1, .5, 1), (1, .5, 1, 1)]

        self.btnNUMBERS = [num for num in range(1,10)] # buttons numbers
        self.btnNUMBERScopy = [num for num in range(1,10)] # copy of list for random generating new number\
                                                            #  for each button

        for i in self.btnNUMBERS:
            currentNumber = random.choice(self.btnNUMBERScopy) # selects number for button text
            color = random.choice(self.btnColors) # select random color for new button
            self.btnColors.remove(color) # will remove color from colors list to avoid duplicated colors
            btn = Button(text=str(currentNumber), font_size="100sp", background_color=color,
                         on_release=self.callback)
            btn.background_normal= "buttons/purple-button-hi.png"
            btn.background_disabled_normal = "buttons/purple-button-hi.png"
            # TODO add down background color
            btn.background_down = "buttons/purple-button-hi.png"

            self.widgetList.append(btn) # will add button to this list - it used later for clearing Grid\
                                        #  from childrens
            self.add_widget(btn)
            self.btnNUMBERScopy.remove(currentNumber) # remove choosed number to avoid duplicated button numbers


    def clocker(self, sound, time, *args):
        Clock.schedule_once(partial(self.soundPlayer, sound), time)

    def startGame(self, *args):
        "will tale random numbet and plays correct audio"
        print("wybierz cyfre")
        self.NUMBER = random.choice(range(1, 10))
        # TODO dodac odtwarzanie dzwieku
        self.clocker("pokaz_cyfre.wav", 2)
        self.clocker(self.sounds[self.NUMBER], 4)


    def callback(self, btn):
        """
        :param btn: here btn number will be taken to use it for sound
        :return:
        """
        self.disabled = True
        if str(self.NUMBER) == btn.text:
            self.clocker("hurra.wav", -1)
        else:
           self.clocker("nie.wav", -1)

        self.startGame()
        self.insertWidgets()


    def soundPlayer(self, sound, *args):
        # function for playing sounds
        # will block main window where sound is played!
        if sound in ["hurra.wav", "nie.wav", "pokaz_cyfre.wav"]:
            self.disabled = True
        elif sound in self.sounds.values():
            # will unlock main window when number is played
            self.disabled = False

        print('sounds/{}'.format(sound), sound)
        self.player = SoundLoader().load("sounds/{}".format(sound))
        self.player.play()


if __name__ == "__main__":
    class Main(App):
        def build(self):
            return MyApp()
    Main().run()
