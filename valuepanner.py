import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.factory import Factory

class Panner(Slider):
    path = StringProperty('Fader')
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)
#    def on_touch_move(self, touch):
#        app = App.get_running_app()
#        app.send_message()

class ValuePanner(Widget):
    panner = ObjectProperty(None)
    name_p = ObjectProperty(None)
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)
    max = NumericProperty()
    min = NumericProperty()
    step = NumericProperty()

class ValuePannerApp(App):
    def build(self):
        return ValuePanner(name='My Panner', max=100, min=0, color=(1, 0.5, 0.5))

Factory.register('Panner', Panner)
if __name__ == "__main__":
    ValuePannerApp().run()
