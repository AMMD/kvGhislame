import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory

class InnerBox(Widget):
    h = NumericProperty()
    s = NumericProperty()
    v = NumericProperty()
    color = ReferenceListProperty(h, s, v)

class XyPad(Widget):
    innerbox = ObjectProperty(None)
    path = StringProperty('xypad')

class XyPadApp(App):
    def build(self):
        return XyPad();

Factory.register('InnerBox', InnerBox)
if __name__ == '__main__':
    XyPadApp().run()
