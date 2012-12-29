import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.lang import Builder

from pad import Pad

class XyPad(Pad):
    name = StringProperty()
    name_w = ObjectProperty(None)

    # Axes
    x_name = StringProperty()
    x_name_w = ObjectProperty(None)
    y_name = StringProperty()
    y_name_w = ObjectProperty(None)
    y_name_s = ObjectProperty(None)



class XyPadApp(App):
    def build(self):
        return XyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y');

Builder.load_file('pad.kv')
if __name__ == '__main__':
    XyPadApp().run()
