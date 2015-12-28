__author__ = 'Marcin'

from kivy.app import App
#from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random
from functools import partial
from time import sleep


class MyApp(GridLayout):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
        self.rows, self.cols = [3, 3]
        self.padding = 5
        self.spacing = 5
        self.sounds = {1: "1.wav", 2: "2.wav", 3: "3.wav", 4: "4.wav", 5: "5.wav",
                       6: "6.wav", 7: "7.wav", 8: "8.wav", 9: "9.wav"}
        self.widgetList = []  # will store all buttons to easy remove
        self.block = False # for blocking overlaping sounds

        self.sound = SoundLoader()
        #self.firstPopup()

        #self.insertWidgets()

    def firstPopup(self, *args):
        frstPop = ModalView()
        btnStart = Button(text="Zaczynamy!", on_press=frstPop.dismiss)
        frstPop.add_widget(btnStart)
        frstPop.on_dismiss =  self.insertWidgets
        frstPop.open()


    def insertWidgets(self):
        self.disabled = True # for initial run!
        self.NUMBER = random.choice(range(1,10))
        self.HurrayOhNoes = ModalView(auto_dismiss = False, size_hint=(.8,.8),
                                      background="")
        self.clocker("pokaz_cyfre.wav", 1)
        self.clocker(self.sounds[self.NUMBER], 4)

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
                         on_press=self.callback)
            btn.background_normal= "buttons/purple-button-hi.png"
            btn.background_disabled_normal = "buttons/purple-button-hi.png"
            btn.background_down = "buttons/purple-button-hi.png"
            self.widgetList.append(btn) # will add button to this list - it used later for clearing Grid\
                                        #  from childrens
            self.add_widget(btn)
            self.btnNUMBERScopy.remove(currentNumber) # remove choosed number to avoid duplicated button numbers

        # popup with number for presentation
        self.numberPopUp = ModalView(auto_dismiss = False, background = "buttons/purple-button-hi.png", size_hint = (.7,.7))
        self.numberPopUp.add_widget(Label(text=str(self.NUMBER),
                                  font_size="250sp",))


    def clocker(self, sound, time, *args):
        Clock.schedule_once(partial(self.soundPlayer, sound), time)


    def callback(self, btn):
        """ here btn number will be taken to use it for sound """
        #self.disabled = True
        if str(self.NUMBER) == btn.text:
            self.clocker("hurra.wav", -1)
        else:
           self.clocker("nie.wav", -1)
        #self.startGame()
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
        #self.numberPopUp.dismiss()
        if sound == "hurra.wav":
            pic = random.choice(('images/happy.jpg', 'images/happy-face.jpg',
            'images/Peppa-happy.jpg'))
            self.numberPopUp.dismiss()
            self.HurrayOhNoes.add_widget(Image(source=pic))
            self.HurrayOhNoes.open()

        if sound == "nie.wav":
            self.numberPopUp.dismiss()
            pic='images/peppaSad.png'
            self.HurrayOhNoes.add_widget(Image(source=pic))  #add_widget(Image(source="images/sad.jpg", keep_ration=False))
            #self.HurrayOhNoes.size_hint = (.5,.8)
            self.HurrayOhNoes.open()
        
        if sound == "pokaz_cyfre.wav":
            sleep(.7)
            self.temp_popup = ModalView(auto_dismiss = False, background="images/question.png",
                                        size_hint=(.6,.5))
            self.HurrayOhNoes.dismiss()
            #self.temp_popup.add_widget(Image(source="images/question.png", keep_ration=False))
            self.temp_popup.open()
            #self.numberPopUp.open()

        if sound in self.sounds.values():
            self.temp_popup.dismiss()
            self.numberPopUp.open()


    def STOP(self, sound):
        sound = sound.split("/")[-1]
        if sound in self.sounds.values():
            self.disabled = False
            sleep(1)
            self.numberPopUp.dismiss()


# if __name__ == "__main__":
#     class Main(App):
#         Window.fullscreen=False
#         def open_settings(self, *largs):
#             pass
#         def on_pause(self):
#             True
#
#         def build(self):
#             return MyApp()
#     Main().run()
