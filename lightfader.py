import kivy
kivy.require('1.5')

from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout

from valuefader import ValueFader
from push import Push

class LightFader(ValueFader):
    old_value = NumericProperty()
    flash = ObjectProperty(Push)


