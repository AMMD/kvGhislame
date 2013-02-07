import kivy
kivy.require('1.5.1')

import re

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty, BooleanProperty
from kivy.lang import Builder

from osc import OscSender

class Toggle(ToggleButton, OscSender):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    main_color = ReferenceListProperty(r, g, b)

    one_on_down = BooleanProperty()

    def control_cb(self, path, args, types, src):
#        if re.search('127.0.0.1', src.get_url()):
#            print "self-incoming message"
#        else:
            print "OSC controlled"
            if float(args[0]):
                self.state = 'down'
            else:
                self.state = 'normal'

    def state_to_args(self):
#        print self.one_on_down
        if self.one_on_down == True:
            if self.state == 'down':
                self.args = [1]
            else:
                self.args = [0]
        else:
            if self.state == 'down':
                self.args = [0]
            else:
                self.args = [1]            

class ToggleApp(App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        return Toggle(name="My Toggle", main_color=(1,0,0), app_name=self.name)

if __name__ == "__main__":
    ToggleApp().run()
