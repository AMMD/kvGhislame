import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from fader import Fader
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.factory import Factory
from kivy.lang import Builder



class Mute(ToggleButton):
    path = StringProperty('Mute')

class AudioStrip(Widget):
    path = StringProperty('Strip')
    fader = ObjectProperty(None)
    mute = ObjectProperty(None)

class AudioStripApp(App):
    def build(self):
        return AudioStrip()

Builder.load_file('fader.kv')
Factory.register('Fader', Fader)
Factory.register('Mute', Mute)
if __name__ == '__main__':
    AudioStripApp().run()
