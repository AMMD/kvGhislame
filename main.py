import kivy

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App
from kivy.lang import Builder

from osc import OscServer, OscSender
from audiostrip import AudioStrip
Builder.load_file('audiostrip.kv')


class MenuButton(ToggleButton):
    pass

class Menu(BoxLayout):
    mix_b = ObjectProperty(MenuButton)
    odr_b = ObjectProperty(MenuButton)


Builder.load_file('oscsender.kv')

class MainMix(Screen):
    drums = ObjectProperty(AudioStrip)
Builder.load_file('mainmix.kv')


class OrganicDrums(Screen):
    pass



class MainKvG(Widget):
    app_name = StringProperty()
    target = StringProperty()
    sm = ObjectProperty(ScreenManager)
    menu = ObjectProperty(Menu)
    mainmix = ObjectProperty(Screen)
    organicdrums = ObjectProperty(Screen)

    def change_tab(self, tab_name):
        self.sm.current = tab_name
        for child in self.children[:]:
            if isinstance(child, Menu):
                for kid in child.children[:]:
                    if (kid.text == tab_name) & isinstance(kid, MenuButton):
                        kid.state = 'down'



class kvGhislame(OscServer, App):
    title = "kvGhislame"

    def recurse_children(self, obj):
        for child in obj.children:
            print "New Child: " + str(type(child))
            if isinstance(child, OscSender):
                self.server.add_method(child.path, child.args_pattern, child.control_cb)
            self.recurse_children(child)

    def build_config(self, config):
        config.setdefaults('OSC', {
                'dest_host': 'osc.udp://127.0.0.1',
                'dest_port': '1234',
                'in_port': '9999'
         })

    def build_settings(self, settings):
        jsondata = """
[
    { "type": "title",
      "title": "kvGhislame" },

    { "type": "string",
      "title": "Destintion Host",
      "desc": "OSC destination host",
      "section": "OSC",
      "key": "dest_host"},

    { "type": "numeric",
      "title": "Destination Port",
      "desc": "OSC destination Port",
      "section": "OSC",
      "key": "dest_port" },

    { "type": "numeric",
      "title": "Control Port",
      "desc": "OSC control Port",
      "section": "OSC",
      "key": "in_port" }
]
"""
        settings.add_json_panel('kvGhislame',
                                self.config, data=jsondata)     

    def build(self):
        config = self.config
        print config.get('OSC', 'host')
        mainkvg = MainKvG()
        self.recurse_children(mainkvg)
        return mainkvg

if __name__ == "__main__":
    kvGhislame().run()
