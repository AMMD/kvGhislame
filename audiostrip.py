import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty, OptionProperty
from kivy.factory import Factory
from kivy.lang import Builder

from valuefader import ValueFader
from toggle import Toggle

#class Mute(ToggleButton):
 #   path = StringProperty('Mute')

class AudioStrip(Widget):
    path = StringProperty('Strip')
    base_path = StringProperty()
    name = StringProperty()
    gainfader = ObjectProperty(ValueFader)
    panfader = ObjectProperty(ValueFader)
    mute = ObjectProperty(Toggle)
    app_name = StringProperty()

    mute_mode = OptionProperty('mute', options=('on', 'mute'))

#    mute = ObjectProperty(None)
#    name_s = ObjectProperty(None)
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)



class AudioStripApp(App):
    name = StringProperty()
    name = 'kvGhislame'
    def build(self):
        return AudioStrip(name="My Strip", color = (1, 0.5, 0.5), app_name=self.name)

Builder.load_file('toggle.kv')
Builder.load_file('valuefader.kv')
#Factory.register('ValueFader', ValueFader)
#Factory.register('Mute', Mute)
if __name__ == '__main__':
    AudioStripApp().run()
