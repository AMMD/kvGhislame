import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty, BooleanProperty, AliasProperty
from kivy.lang import Builder

from osc import OscSender

class Push(Button, OscSender):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    main_color = ReferenceListProperty(r, g, b)

    one_on_down = BooleanProperty()

    def control_cb(self, path, args, types, src):
        if re.search('127.0.0.1', src.get_url()):
            print "self-incoming message"
        else:
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

    def set_hsv_triplet(self, value):
        self.main_color = colorsys.hsv_to_rgb(value[0], value[1], value[2])

    def get_hsv_triplet(self):
        return(colorsys.rgb_to_hsv(self.main_color[0], self.main_color[1], self.main_color[2]))
    hsv = AliasProperty(get_hsv_triplet, set_hsv_triplet, bind=('main_color',))



class PushApp(App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        return Push(name="My Push", main_color=(1,0,0), app_name=self.name)

if __name__ == "__main__":
    PushApp().run()
