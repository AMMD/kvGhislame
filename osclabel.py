import kivy
kivy.require('1.5.1')

from kivy.uix.label import Label

from osc import OscSender

class OscLabel(Label, OscSender):
    def control_cb(self, path, args):
        if re.search('127.0.0.1', src.get_url()):
            print "self-incoming message"
        else:
            print "OSC controlled"
            self.text = str(args[0])

    def on_touch_down(self, touch):
        print self.control_path
