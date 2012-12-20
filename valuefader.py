import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, OptionProperty, NumericProperty, ReferenceListProperty, AliasProperty
from kivy.factory import Factory

class Fader(Slider):
    path = StringProperty('Fader')
    # Couleur
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    def get_value_pos(self):
        padding = self.padding
        x = self.x
        y = self.y
        nval = self.value_normalized
        if self.orientation == 'horizontal':
            return (x + padding + nval * (self.width - 2 * padding), y)
        else:
            return (x, y + padding + nval * (self.height - 2 * padding))

    def set_value_pos(self, pos):
        x = min(self.right - self.padding, max(pos[0], self.x + self.padding))
        y = min(self.top - self.padding, max(pos[1], self.y + self.padding))
        if self.orientation == 'horizontal':
            if self.width == 0:
                self.value_normalized = 0
            else:
                self.value_normalized = (x - self.x - self.padding) / float(self.width - 2 * self.padding)
        else:
            if self.height == 0:
                self.value_normalized = 0
            else:
                self.value_normalized = (y - self.y - self.padding) / float(self.height - 2 * self.padding)
    value_pos = AliasProperty(get_value_pos, set_value_pos,
                              bind=('x', 'y', 'width', 'height', 'min',
                                    'max', 'value_normalized', 'orientation'))



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
