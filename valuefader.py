import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, OptionProperty, NumericProperty, ReferenceListProperty
from kivy.factory import Factory

class Fader(Slider):
    path = StringProperty('Fader')
    # Couleur
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

class ValueFader(Widget):
    fader = ObjectProperty(None)
    name_f = ObjectProperty(None)
    name = StringProperty()

    # Couleur
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)
    
    # Fader settings
    orientation = OptionProperty('horizontal', options=('vertical', 'horizontal'))
    max = NumericProperty()
    min = NumericProperty()
    # (require 1.4.2) step = NumericProperty()    

class ValueFaderApp(App):
    def build(self):
        return ValueFader(name='My Fader', orientation='horizontal', color=(1,0.5,0.5))

Factory.register('Fader', Fader)
if __name__ == "__main__":
    ValueFaderApp().run()
