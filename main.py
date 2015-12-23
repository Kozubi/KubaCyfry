__author__ = 'Marcin'

from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.label import Label
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
        self.NUMBER = random.choice(range(1, 10))
        self.sound = SoundLoader()
        self.startGame()
        self.insertWidgets()


    def insertWidgets(self):
        self.disabled = True # for initial run!
        self.popUp = self.popuper()
        self.popUp.open()
        if len(self.widgetList) > 1:
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
        "will tale random number and plays correct audio"
        print("wybierz cyfre")
        self.ppp = ModalView()
        self.NUMBER = random.choice(range(1, 10))
        # TODO wywalic clockera i zobaczyc czy przy sound player nie beda zachodzic na siebie
        self.clocker("pokaz_cyfre.wav", 2)
        self.clocker(self.sounds[self.NUMBER], 4)

    def popuper(self, *args):
        self.pop = ModalView()
        self.pop.background = "buttons/purple-button-hi.png"
        self.pop.add_widget(Label(text=str(self.NUMBER),
                                  font_size="100sp",))
        self.pop.size_hint = (.95,.95)
        return self.pop


    def callback(self, btn):
        """
        :param btn: here btn number will be taken to use it for sound
        :return:
        """
        #self.disabled = True
        if str(self.NUMBER) == btn.text:
            self.clocker("hurra.wav", -1)
        else:
           self.clocker("nie.wav", -1)
        self.startGame()
        self.insertWidgets()

    def soundPlayer(self, sound, *args):
        # function for playing sounds
        # will block main window where sound is played!
        self.player = self.sound.load("sounds/{}".format(sound))
        self.player.on_play = partial(self.PLAY, self.player.filename)
        self.player.on_stop = partial(self.STOP, self.player.filename)
        print('sounds/{}'.format(sound), sound)
        self.player.play()

    def PLAY(self, sound):
        # used to open and dismiss popups while specific sound is beign  played
        sound = sound.split("/")[-1]
        self.popUp.dismiss()
        if sound == "hurra.wav":
            self.ppp.add_widget(Label(text="HURRA"))
            self.ppp.open()
        if sound == "nie.wav":
            self.ppp.add_widget(Label(text="NIE"))
            self.ppp.open()
        if sound == "pokaz_cyfre.wav":
            self.ppp.dismiss()
            self.popUp.open()
        print("PLAYYYY", sound)

    def STOP(self, sound):
        sound = sound.split("/")[-1]
        if sound in self.sounds.values():
            self.disabled = False
            self.popUp.dismiss()

if __name__ == "__main__":
    class Main(App):
        def build(self):
            return MyApp()
    Main().run()
