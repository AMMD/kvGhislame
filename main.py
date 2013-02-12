import kivy

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty
from kivy.app import App
from kivy.lang import Builder

from osc import OscServer, OscSender

from osclabel import OscLabel
Builder.load_file('osclabel.kv')
from audiostrip import AudioStrip
Builder.load_file('audiostrip.kv')
from xypad import XyPad
Builder.load_file('xypad.kv')

class MenuButton(ToggleButton):
    pass

class Menu(BoxLayout):
    mix_b = ObjectProperty(MenuButton)
    odr_b = ObjectProperty(MenuButton)


Builder.load_file('oscsender.kv')

class MainMix(Screen):
    organicdrums = ObjectProperty(AudioStrip)
    basses = ObjectProperty(AudioStrip)
    guitares = ObjectProperty(AudioStrip)
    saxophones = ObjectProperty(AudioStrip)
    vocals = ObjectProperty(AudioStrip)
    mxsynths = ObjectProperty(AudioStrip)
    mxdrums = ObjectProperty(AudioStrip)
    nycomp = ObjectProperty(AudioStrip)
    drloop = ObjectProperty(AudioStrip)
    fxs = ObjectProperty(AudioStrip)
    mainmix = ObjectProperty(AudioStrip)

Builder.load_file('mainmix.kv')


class OrganicDrums(Screen):
    kick1 = ObjectProperty(AudioStrip)
    kick2 = ObjectProperty(AudioStrip)
    snare_t = ObjectProperty(AudioStrip)
    tom1 = ObjectProperty(AudioStrip)
    tom2 = ObjectProperty(AudioStrip)
    tom3 = ObjectProperty(AudioStrip)
    tom4 = ObjectProperty(AudioStrip)
    ohs = ObjectProperty(AudioStrip)
    toms = ObjectProperty(AudioStrip)
    organicdrums = ObjectProperty(AudioStrip)
                             
Builder.load_file('organicdrums.kv')

class Basses(Screen):
    basse = ObjectProperty(AudioStrip)
    grotterie = ObjectProperty(AudioStrip)
    mxbass = ObjectProperty(AudioStrip)
    bassfx = ObjectProperty(AudioStrip)

    basses = ObjectProperty(AudioStrip)

Builder.load_file('basses.kv')

class Guitares(Screen):
    pass

class Saxophones(Screen):
    saxophone = ObjectProperty(AudioStrip)
    saxfx = ObjectProperty(AudioStrip)

    saxophones = ObjectProperty(AudioStrip)

Builder.load_file('saxophones.kv')

class Vocals(Screen):
    vocalsorl = ObjectProperty(AudioStrip)
    vocalssouv = ObjectProperty(AudioStrip)
    vocalsyula = ObjectProperty(AudioStrip)
    vocalsfx = ObjectProperty(AudioStrip)

    vocals = ObjectProperty(AudioStrip)

Builder.load_file('vocals.kv')

class MxSynths(Screen):
    mxbass = ObjectProperty(AudioStrip)
    mxchords = ObjectProperty(AudioStrip)
    mxlead = ObjectProperty(AudioStrip)
    mxctlead = ObjectProperty(AudioStrip)
    mxsamples = ObjectProperty(AudioStrip)

    mxsynths = ObjectProperty(AudioStrip)

Builder.load_file('mxsynths.kv')

class MxDrums(Screen):
    mxkicks = ObjectProperty(AudioStrip)
    mxsnares = ObjectProperty(AudioStrip)
    mxcymbs = ObjectProperty(AudioStrip)
    mxcont = ObjectProperty(AudioStrip)

    mxdrums = ObjectProperty(AudioStrip)

Builder.load_file('mxdrums.kv')

#class NyComp(Screen):
#    pass

class Fxs(Screen):
    pass

#class DrumLoop(Screen):
#    pass

class MonitorOrl(Screen):
    mainmix = ObjectProperty(AudioStrip)
    basse = ObjectProperty(AudioStrip)
    guitares = ObjectProperty(AudioStrip)
    vocals = ObjectProperty(AudioStrip)
    organicdrums = ObjectProperty(AudioStrip)
    droiture = ObjectProperty(AudioStrip)

Builder.load_file('monitororl.kv')

class MonitorSouv(Screen):
    mainmix = ObjectProperty(AudioStrip)
    saxophones = ObjectProperty(AudioStrip)
    vocals = ObjectProperty(AudioStrip)
    organicdrums = ObjectProperty(AudioStrip)
    droiture = ObjectProperty(AudioStrip)

Builder.load_file('monitorsouv.kv')

class MonitorYula(Screen):
    mainmix = ObjectProperty(AudioStrip)
    kick1 = ObjectProperty(AudioStrip)
    organicdrums = ObjectProperty(AudioStrip)
    droiture = ObjectProperty(AudioStrip)

Builder.load_file('monitoryula.kv')

class VCO(BoxLayout):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

Builder.load_file('vco.kv')

class VCF(BoxLayout):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

Builder.load_file('vcf.kv')

class Envelop(BoxLayout):
    name = StringProperty()

class AdvEnvelop(BoxLayout):
    name = StringProperty()

class MxBass(Screen):
    vco1 = ObjectProperty(VCO)
    vco2 = ObjectProperty(VCO)
    vco3 = ObjectProperty(VCO)
    vco4 = ObjectProperty(VCO)
    vcf = ObjectProperty(VCF)
    env = ObjectProperty(Envelop)
    advenv = ObjectProperty(AdvEnvelop)

Builder.load_file('mxbass.kv')

class MxChords(Screen):
    pass

class MxLead(Screen):
    pass

class MxCtLead(Screen):
    pass

class SooperLooper(Screen):
    pass

class BassFx(Screen):
    pass

class VocalsFx(Screen):
    pass

class Qlc(Screen):
    pass

class Lives(Screen):
    pass


class MainKvG(Widget):
    app_name = StringProperty()

    container = ObjectProperty()

    tunename = ObjectProperty()

    sm = ObjectProperty(ScreenManager)
    menu = ObjectProperty(Menu)

    mainmix = ObjectProperty(MainMix)
    organicdrums = ObjectProperty(OrganicDrums)
    basses = ObjectProperty(Basses)
    guitares = ObjectProperty(Guitares)
    saxophones = ObjectProperty(Saxophones)
    vocals = ObjectProperty(Vocals)
    mxsynths = ObjectProperty(MxSynths)
    mxdrums = ObjectProperty(MxDrums)
    fxs = ObjectProperty(Fxs)
    monitororl = ObjectProperty(MonitorOrl)
    monitorsouv = ObjectProperty(MonitorSouv)
    monitoryula = ObjectProperty(MonitorYula)
    mxbass = ObjectProperty(MxBass)
    mxchords = ObjectProperty(MxChords)
    mxlead = ObjectProperty(MxLead)
    mxctlead = ObjectProperty(MxCtLead)
    sooperlooper = ObjectProperty(SooperLooper)
    bassxx = ObjectProperty(BassFx)
    vocalsfx = ObjectProperty(VocalsFx)
    qlc = ObjectProperty(Qlc)
    lives = ObjectProperty(Lives)
    

    def change_tab(self, tab_name):
        self.sm.current = tab_name
        for child in self.children[0].children[:]:
            if isinstance(child, Menu):
                for kid in child.children[:]:
                    if (kid.text == tab_name) & isinstance(kid, MenuButton):
                        kid.state = 'down'



class kvGhislame(OscServer, App):
    title = "kvGhislame"

    def recurse_children(self, obj):
        for child in obj.children:
#            print "New Child: " + str(type(child))
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
