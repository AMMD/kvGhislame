import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from valuefader import ValueFader
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.factory import Factory
from kivy.lang import Builder



class Mute(ToggleButton):
    path = StringProperty('Mute')

class AudioStrip(Widget):
    path = StringProperty('Strip')
    name = StringProperty()
    valuefader = ObjectProperty(None)
    mute = ObjectProperty(None)
    name_s = ObjectProperty(None)



class AudioStripApp(App):
    def build(self):
        return AudioStrip(name="My Strip")

Builder.load_file('valuefader.kv')
Factory.register('ValueFader', ValueFader)
Factory.register('Mute', Mute)
if __name__ == '__main__':
    AudioStripApp().run()
