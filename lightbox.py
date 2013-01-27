import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.lang import Builder

from lightxypad import LightXyPad
from valuefader import ValueFader
from toggle import Toggle

class LightBox(LightXyPad):
    main_dimmer_fader = ValueFader()

    r_fader = ValueFader()
    g_fader = ValueFader()
    b_fader = ValueFader()

    custom_color_a = Toggle()
    custom_color_2 = Toggle()
    custom_color_3 = Toggle()
    custom_color_4 = Toggle()
    custom_color_5 = Toggle()
    custom_color_6 = Toggle()
    custom_color_7 = Toggle()
    custom_color_8 = Toggle()

# TODO Flash
# TODO Link
# TODO Develop

Builder.load_file('valuefader.kv')
Builder.load_file('toggle.kv')
Builder.load_file('lightxypad.kv')

class LightBoxApp(App):
    def build(self):
        return LightBox(name="Ducul", color=(1, 1, 0))


if __name__ == '__main__':
    LightBoxApp().run()


