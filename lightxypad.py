import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.lang import Builder

from xypad import XyPad

class LightXyPad(XyPad):

class LightXyPadApp(App):
    def build(self):
        return LightXyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y');

Factory.register('Pad', Pad)
Builder.load_file('pad.kv')
if __name__ == '__main__':
    XyPadApp().run()
