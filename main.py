import os

import re

import liblo as _liblo

import kivy

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.stencilview import StencilView
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty
from kivy.app import App
from kivy.lang import Builder

from osc import OscServer, OscSender

from osclabel import OscLabel
Builder.load_file('osclabel.kv')
from audiostrip import AudioStrip
Builder.load_file('audiostrip.kv')
from xypad import XyPad
#Builder.load_file('xypad.kv')
from toggle import Toggle
#Builder.load_file('toggle.kv')
from push import Push
#Builder.load_file('push.kv')
from valuefader import ValueFader
#Builder.load_file('valuefader.kv')
from lightbox import LightBox
Builder.load_file('lightbox.kv')
from lightfader import LightFader
Builder.load_file('lightfader.kv')
#from lightstrip import LightStrip
#Builder.load_file('lightstrip.kv')


class MenuButton(ToggleButton):
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    main_color = ReferenceListProperty(r, g, b)

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
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

Builder.load_file('env.kv')

class AdvEnvelop(BoxLayout):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

Builder.load_file('advenv.kv')

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
    vco1 = ObjectProperty(VCO)
    vco2 = ObjectProperty(VCO)
    vco3 = ObjectProperty(VCO)
    vcf = ObjectProperty(VCF)
    advenv1 = ObjectProperty(AdvEnvelop)
    advenv2 = ObjectProperty(AdvEnvelop)
    noise = ObjectProperty(XyPad)

Builder.load_file('mxchords.kv')


class MxLead(Screen):
    vco1 = ObjectProperty(VCO)
    vco2 = ObjectProperty(VCO)
    vco3 = ObjectProperty(VCO)
    vcf = ObjectProperty(VCF)
    advenv1 = ObjectProperty(AdvEnvelop)
    advenv2 = ObjectProperty(AdvEnvelop)
    noise = ObjectProperty(XyPad)

Builder.load_file('mxlead.kv')


class MxCtLead(Screen):
    vco1 = ObjectProperty(VCO)
    vco2 = ObjectProperty(VCO)
    vco3 = ObjectProperty(VCO)
    vco4 = ObjectProperty(VCO)
    vcf = ObjectProperty(VCF)
    slew = ObjectProperty(XyPad)

Builder.load_file('mxctlead.kv')


class Loop(BoxLayout):
    play = ObjectProperty(Toggle)
    record = ObjectProperty(Toggle)
    overdub = ObjectProperty(Toggle)
    pause = ObjectProperty(Toggle)
    multiply = ObjectProperty(Toggle)
    reverse = ObjectProperty(Toggle)
    undo = ObjectProperty(Push)
    redo = ObjectProperty(Push)
    mute = ObjectProperty(Toggle)
    once = ObjectProperty(Toggle)
    twice = ObjectProperty(Toggle)
    halfth = ObjectProperty(Toggle)
    play_sync = ObjectProperty(Toggle)
    sync = ObjectProperty(Toggle)
    trig = ObjectProperty(Toggle)
    wet = ObjectProperty(ValueFader)
    dry = ObjectProperty(ValueFader)
    rate = ObjectProperty(ValueFader)

    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

Builder.load_file('loop.kv')


class SooperLooper(Screen):
    drums = ObjectProperty(Loop)
    bass = ObjectProperty(Loop)
    guitar = ObjectProperty(Loop)
    vocals = ObjectProperty(Loop)
    bpm = ObjectProperty(ValueFader)

Builder.load_file('sooperlooper.kv')


class BassFx(Screen):
    chorus = ObjectProperty(BoxLayout)
    revdelay = ObjectProperty(BoxLayout)
    pitchshifter = ObjectProperty(BoxLayout)
    reverb = ObjectProperty(BoxLayout)
    vcf = ObjectProperty(BoxLayout)
    
Builder.load_file('bassfx.kv')


class VocalsFx(Screen):
    pitchshifter_left = ObjectProperty(BoxLayout)
    pitchshifter_right = ObjectProperty(BoxLayout)
    disintegrator = ObjectProperty(BoxLayout)
    cscape = ObjectProperty(BoxLayout)

Builder.load_file('vocalsfx.kv')


class LightStrip(BoxLayout):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    path = StringProperty()
    control_path = StringProperty()
    target = StringProperty()
    osc_name = StringProperty()

    lightbox = ObjectProperty(LightBox)
    button = ObjectProperty(Button)
    stencil = ObjectProperty(StencilView)

    def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
#             print "Touch " + self.name + ": True"
#             touch.grab(self.lightbox.xypad)
#             self.lightbox.xypad.on_touch_down(touch)
#             print touch.grab_current
# #            return True
#         else:
            return super(BoxLayout, self).on_touch_down(touch)
    

class Qlc(Screen):
    barres = ObjectProperty(LightStrip)
    orl64 = ObjectProperty(LightStrip)
    souv64 = ObjectProperty(LightStrip)
    yula64 = ObjectProperty(LightStrip)
    orl36top = ObjectProperty(LightStrip)
    orl36bottom = ObjectProperty(LightStrip)
    lointains = ObjectProperty(LightStrip)
    occuloques = ObjectProperty(LightStrip)
    yula36tub = ObjectProperty(LightStrip)
    yula36ext = ObjectProperty(LightStrip)
    yula36int = ObjectProperty(LightStrip)
    # barres_st = ObjectProperty(StencilView)
    # orl64_st = ObjectProperty(StencilView)
    # souv64_st = ObjectProperty(StencilView)
    # yula64_st = ObjectProperty(StencilView)
    # orl36top_st = ObjectProperty(StencilView)
    # orl36bottom_st = ObjectProperty(StencilView)
    # lointains_st = ObjectProperty(StencilView)
    # occuloques_st = ObjectProperty(StencilView)
    # yula36tub_st = ObjectProperty(StencilView)
    # yula36ext_st = ObjectProperty(StencilView)
    # yula36int_st = ObjectProperty(StencilView)
    smoke = ObjectProperty(Push)
    grada1 = ObjectProperty(LightFader)
    grada2 = ObjectProperty(LightFader)
    grada3 = ObjectProperty(LightFader)
    grada4 = ObjectProperty(LightFader)
    grada5 = ObjectProperty(LightFader)
    grada6 = ObjectProperty(LightFader)
    fade = ObjectProperty(ValueFader)
    hold = ObjectProperty(ValueFader)
    chase1 = ObjectProperty(Toggle)
    chase2 = ObjectProperty(Toggle)
    chase3 = ObjectProperty(Toggle)
    chase4 = ObjectProperty(Toggle)
    chase5 = ObjectProperty(Toggle)
    chase7 = ObjectProperty(Toggle)
    chase8 = ObjectProperty(Toggle)
    chase9 = ObjectProperty(Toggle)
    chase10 = ObjectProperty(Toggle)
    chase11 = ObjectProperty(Toggle)
    chase12 = ObjectProperty(Toggle)
    blackout = ObjectProperty(Toggle)
    smoke = ObjectProperty(Push)
    barled_on = ObjectProperty(Toggle)

    stf = ObjectProperty(StencilView)
    tmp_s = ObjectProperty(StencilView)

    lightsm = ObjectProperty(ScreenManager)
    main_s = ObjectProperty(Screen)
    front_s = ObjectProperty(Screen)


    def zoom_strip(self, obj):
        parent = obj.parent
        obj.parent.remove_widget(obj)
        self.stf.add_widget(obj)
        obj.width = self.width
        obj.height = self.stf.height
        obj.pos = self.pos
        self.tmp_s = parent
        self.lightsm.current = 'front'

    def restore_zoomed_strip(self):
        for child in self.stf.children[:]:
            self.stf.remove_widget(child)
#            child.width = self.tmp_s.width
            child.pos = self.tmp_s.pos
            child.height = self.tmp_s.height
            self.tmp_s.add_widget(child)
            self.lightsm.current = 'main'

Builder.load_file('qlc.kv')

class Lives(Screen):
    pass
Builder.load_string("""
<Lives>:
    ToggleButton:
        text: "test"
        main_color: 1, 1, 1
        on_press:
            print "sent"
""")


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save_all = ObjectProperty(None)
    save_this = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

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
    bassfx = ObjectProperty(BassFx)
    vocalsfx = ObjectProperty(VocalsFx)
    qlc = ObjectProperty(Qlc)
    lives = ObjectProperty(Lives)

# Internal binds
    m2o_organicdrums_gain = NumericProperty()
    o2m_organicdrums_gain = NumericProperty()

    m2b_basses_gain = NumericProperty()
    b2m_basses_gain = NumericProperty()

    m2s_saxophones_gain = NumericProperty()
    s2m_saxophones_gain = NumericProperty()

    m2v_vocals_gain = NumericProperty()
    v2m_vocals_gain = NumericProperty()

    m2s_mxsynths_gain = NumericProperty()
    s2m_mxsynths_gain = NumericProperty()

    m2d_mxdrums_gain = NumericProperty()
    d2m_mxdrums_gain = NumericProperty()

    m2s_sooperlooper_drums_gain = NumericProperty()
    s2m_sooperlooper_drums_gain = NumericProperty()

#    def bind_strips(self, obj1, obj2):
#        obj2.gainfader.value = obj1.gainfader.value

    def change_tab(self, tab_name):
        self.sm.current = tab_name
        for child in self.children[0].children[:]:
            if isinstance(child, Menu):
                for kid in child.children[:]:
                    if (kid.text == tab_name) & isinstance(kid, MenuButton):
                        kid.state = 'down'


    def dismiss_popup(self):
        pass
#       self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, filename):
        with open(os.path.join(path, filename)) as stream:
            print stream.readline().rstrip('\n').replace("%", "") + "read!"
            header = stream.readline().rstrip('\n').split(" ")
            target_idx = header.index("target")
            path_idx = header.index("path")
            args_pattern_idx = header.index("args_pattern")
            args_idx = header.index("args")

            for line in stream:
                data = line.rstrip('\n').split(" ")
                i = 0
                format_args = []
                for arg in data[args_idx].split(","):
                    if data[args_pattern_idx][i] == 's':
                        format_args.append(arg)
                    if data[args_pattern_idx][i] == 'i':               
                        format_args.append(int(arg))
                    if data[args_pattern_idx][i] == 'f':
                        format_args.append(float(arg))
                    i = i+1
                _liblo.send(data[target_idx], data[path_idx], *format_args)
                _liblo.send("9999", data[path_idx] + "/load", *format_args)

        self.dismiss_popup()

    def recursively_save_children(self, obj, stream):
        for child in obj.children:
            if isinstance(child, OscSender):
                if re.search("Tune", child.path):
                    pass
                else:
                    if child.osc_name != '':
                        args_pattern = child.args_pattern[2:]
                    else:
                        args_pattern = child.args_pattern[1:]
#                    print args_pattern + " /  " + child.args_pattern + " / " + str(child.args)
                    stream.write(child.target + " " + child.control_path + " " + args_pattern + " ")

                    i = 0
                    for a in child.args:
#                    if (a == '') & (child.args_pattern[i] != 's'):
#                        a = 0
                        if i > 0:
                            if (i != len(child.args) - 1):
                                stream.write(str(a) + ",")
                            else:
                                stream.write(str(a))
                        i = i+1
                    stream.write("\n")
            self.recursively_save_children(child, stream)

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write("%%% " + filename + " %%%\n" + "target path args_pattern args\n" )
            self.recursively_save_children(self, stream)


        self.dismiss_popup()





class kvGhislame(OscServer, App):
    title = "kvGhislame"
    osc_methods_file = open(os.path.join("./", "osc_methods.kvg"), 'w')
    osc_methods_file.write("%%% List of OSC methods registered %%%\n")

    def recurse_children(self, obj):

        for child in obj.children:
            #            print "New Child: " + str(type(child))
            if isinstance(child, OscSender):

                if child.osc_name != "":
                    args_pattern = child.args_pattern[2:]
                else:
                    args_pattern = child.args_pattern[1:]
                self.osc_methods_file.write("\n--\n")
                self.server.add_method(child.control_path, args_pattern, child.control_cb)
                self.osc_methods_file.write(child.control_path + " , " + args_pattern + "\n")
                self.server.add_method(child.control_path + "/load", args_pattern, child.control_cb)
                self.osc_methods_file.write(child.control_path + "/load , " + args_pattern + "\n")
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
        for screen in mainkvg.sm.screen_names:
            print screen + ": OSC ready"
            mainkvg.sm.current = screen
            self.recurse_children(mainkvg)
        mainkvg.sm.current = "Main Mix"
        return mainkvg

if __name__ == "__main__":
    kvGhislame().run()


