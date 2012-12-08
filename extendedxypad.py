import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty

from valuefader import Fader
from xypad import XyPad

class ExtendedXyPad(XyPad):
    xfader = ObjectProperty(None)
    yfader = ObjectProperty(None)


class ExtendedXyPadApp(App):
    def build(self):
        return ExtendedXyPad(color=(1,0,0), name='My Xtended XY Pad', x_name='X', y_name='Y')


#Factory.register('XyPad', XyPad)
Factory.register('Fader', Fader)
Builder.load_file('xypad.kv')
Builder.load_file('valuefader.kv')

if __name__ == '__main__':
    ExtendedXyPadApp().run()
