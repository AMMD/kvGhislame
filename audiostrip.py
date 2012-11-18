import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from valuefader import ValueFader
from valuepanner import ValuePanner
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty
from kivy.factory import Factory
from kivy.lang import Builder



class Mute(ToggleButton):
    path = StringProperty('Mute')

class AudioStrip(Widget):
    path = StringProperty('Strip')
    name = StringProperty()
    gainfader = ObjectProperty(None)
    panfader = ObjectProperty(None)
    mute = ObjectProperty(None)
    name_s = ObjectProperty(None)
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)



class AudioStripApp(App):
    def build(self):
        return AudioStrip(name="My Strip", color = (1, 0.5, 0.5))

Builder.load_file('valuefader.kv')
Factory.register('ValueFader', ValueFader)
Builder.load_file('valuepanner.kv')
Factory.register('ValuePanner', ValuePanner)
Factory.register('Mute', Mute)
if __name__ == '__main__':
    AudioStripApp().run()
