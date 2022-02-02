# region import statements

import time

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Components.Relays.Brick.BrickRelay import BrickRelay
from Components.Switchers.Extron.ExtronSwitcher import ExtronSwitcher
from Components.Projectors.Benq.BenqBase import BenqBase

# endregion

# region Set Configuration

Config.set('graphics', 'width', '1800')
Config.set('graphics', 'height', '1200')
Config.set('graphics', 'borderless', '1')


# Config.set('graphics', 'show_cursor', '1') # 0 - off, 1 - on

# endregion

# region Instantiate screens and screen manager

class Home(Screen):
    pass


class Lighting(Screen):
    pass


class Content(Screen):
    pass


"""
class CameraControl(Screen):
    pass
"""


class WindowManager(ScreenManager):
    pass


# endregion

# region Load and initialize kv files to run in the app class

# IMPORTANT: The base style must be loaded before adding the layouts files
Builder.load_file("kv_files/CoeBaseStyles.kv")  # Base stylesheets -- !!!! LOAD THIS FIRST !!!!
# Builder.load_file("kv_files/PtzLayout.kv")  # camera PTZ controls layout
Builder.load_file("kv_files/ContentSourceLayout.kv")  # 3 x 1 simple video switcher layout
Builder.load_file("kv_files/LightingLayout.kv")  # lighting controls layout
Builder.load_file("kv_files/SplashLayout.kv")  # splash screen

coe_base = Builder.load_file("kv_files/CoeBaseLayouts.kv")  # load the main screen layouts for the controller

# endregion

# region Instantiate components

relay = BrickRelay("192.168.1.105", "")  # requires ip address, port is fixed at nnnn
projector1 = BenqBase("192.168.1.30", 8000)  # user and password authentication not implemented in BenqBase
projector2 = BenqBase("192.168.1.31", 8000)
swt = ExtronSwitcher("192.168.1.50", 23, "", "")  # user and password are optional / defaults to simple User profile

# endregion


class Nh133Control(App):
    def build(self):
        return coe_base

    # region Startup / Shutdown sequences / KeepAlive function

    def system_power(self, instance, value):
        if value == 'down':
            self.system_startup()
        else:
            self.system_shutdown()

    def system_startup(self):
        projector1.power_on()
        projector2.power_on()

    def system_shutdown(self):
        projector1.power_off()
        projector2.power_off()

    def keep_alive(self):
        print(f'Projector 1 status: {projector1.power_status()}')
        print(f'Projector 2 status: {projector2.power_status()}')
        print(swt.get_av_xpoint(1))  # sends request to return version information

    Clock.schedule_interval(keep_alive, 2.0)

    # endregion

    # region Select Content

    def pc_source(self):
        swt.av_xpoints(1, [1, 2, 3])

    def hdmi_source(self):
        swt.av_xpoints(2, [1, 2, 3])

    def airtame_source(self):
        swt.av_xpoints(3, [1, 2, 3])

    # endregion

    # region Lighting commands

    def student_lights_on(self):
        relay.on(3)
        time.sleep(.5)
        relay.on(4)

    def student_lights_off(self):
        relay.off(3)
        relay.off(4)

    def student_lights_50(self):
        relay.on(3)
        relay.off(4)

    def instructor_lights_off(self):
        relay.off(2)

    def instructor_lights_on(self):
        relay.on(2)

    def wall_wash_on(self):
        relay.off(1)  # wall wash relay is Normally Closed so will come on when relay is in off position

    def wall_wash_off(self):
        relay.on(1)  # wall wash relay is Normally Closed so will turn off when relay is set to on position

    def all_lights_on(self):
        relay.off(1)  # wall wash relay is Normally Closed so will come on when relay is in off position
        relay.on(2)
        relay.on(3)
        relay.on(4)

    def room_empty(self):
        relay.off(2)
        relay.off(1)  # wall wash relay is Normally Closed so will come on when relay is in off position
        relay.off(3)
        relay.off(4)
    # endregion


# region App Launcher

if __name__ == '__main__':
    Nh133Control().run()

# endregion
