import socket

prefix = '\r*'
suffix = '#\r'

"""
EnkadiaPave(Python Audio Video Extensions) is an Audio Video Control library for AV system integrators. 

BenqBase is the EnkadiaPave class implementing Benq projectors. This module includes basic power on/off, input
selection, status functions and menu controls (arrows, enter, menu_off/on)
"""


class BenqBase:
    """
    Initialize projector and connect to device
    Parameters:
        host () - hostname or ipaddress
        port (int) - default is 23, but device can be reconfigured by administrator to use different port


    Example:
    from Components.Projectors.Benq.BenqBase import BenqBase

    projector = BenqBase('192.168.1.30', 8000, '','')

    """

    def __init__(self, host, port):
        self.s = socket.socket()
        self.host = host
        # TODO: Get correct port number
        self.port = port
        # TODO: Determine need for username and password
        # self.username = username
        # self.password = password
        self.connect()

    # region Connect / Disconnect

    """

    """

    def connect(self):
        s = self.s
        hostname = self.host
        port = self.port
        s.connect((hostname, port))

    def disconnect(self):
        s = self.s
        s.close()

    # endregion

    # region Send Command and Component Response
    def send_command(self, cmd):
        s = self.s
        s.send(bytes(cmd, 'utf-8'))

    def component_response(self):
        s = self.s
        device_response = s.recv(1024).decode('utf-8')
        # print(device_response)
        return device_response

    # endregion

    # region Power Commands

    def power_on(self):
        self.send_command(f'{prefix}pow=on{suffix}')
        return self.component_response()

    def power_off(self):
        self.send_command(f'{prefix}pow=off{suffix}')
        return self.component_response()

    def power_status(self):
        self.send_command(f'{prefix}pow=?{suffix}')
        return self.component_response()

    # endregion

    # region Projector Inputs

    def hdmi_input(self, proj_input):
        self.send_command(f'{prefix}sour=hdmi{proj_input}{suffix}')
        return self.component_response()

    def hd_baset_input(self, proj_input):
        self.send_command(f'{prefix}sour=hdbaset{proj_input}{suffix}')
        return self.component_response()

    def computer_rgb_input(self, proj_input):
        self.send_command(f'{prefix}sour=rgb{proj_input}{suffix}')
        return self.component_response()

    def dvi_input(self, proj_input):
        self.send_command(f"{prefix}sour=dvid{proj_input}{suffix}")
        return self.component_response()

    def display_port_input(self):
        self.send_command(f"{prefix}sour=dp{suffix}")
        return self.component_response()

    def sdi_input(self):
        self.send_command(f"{prefix}sour=sdi{suffix}")
        return self.component_response()

    def video_input(self):
        self.send_command(f"{prefix}sour=video{suffix}")
        return self.component_response()

    def component_input(self, proj_input):
        self.send_command(f"{prefix}sour=ypbr{proj_input}{suffix}")

    def composite_input(self):
        self.send_command(f"{prefix}sour=vid{suffix}")
        return self.component_response()

    def svideo_input(self):
        self.send_command(f"{prefix}sour=svid{suffix}")
        return self.component_response()

    def set_network_input(self):
        self.send_command(f"{prefix}sour=network{suffix}")
        return self.component_response()

    # endregion

    # region Set Mute
    def input_status(self):
        self.send_command(f"{prefix}sour=?{suffix}")
        return self.component_response()

    def mute_on(self):
        self.send_command(f"{prefix}blank=on{suffix}")
        return self.component_response()

    def mute_off(self):
        self.send_command(f"{prefix}blank=off{suffix}")
        return self.component_response()

    def mute_status(self):
        self.send_command(f"{prefix}blank=?{suffix}")
        return self.component_response()

    # endregion

    # region Admin functions

    def lamp_hours(self):
        self.send_command(f"{prefix}ltim=?{suffix}")
        return self.component_response()

    def lamp_hour_reset(self):
        self.send_command(f"{prefix}ltim=reset{suffix}")
        return self.component_response()

    def total_power_on_time(self):
        self.send_command(f"{prefix}tmhour=?{suffix})")
        return self.component_response()

    def model_name(self):
        self.send_command(f"{suffix}modelname=?{suffix}")
        return self.component_response()

    # endregion

    # region remote menu commands

    def menu_on(self):
        self.send_command(f"{prefix}menu=on{suffix}")
        return self.component_response()

    def menu_off(self):
        self.send_command(f"{prefix}menu=off{suffix}")
        return self.component_response()

    def arrow_up(self):
        self.send_command(f"{prefix}up{suffix}")
        return self.component_response()

    def arrow_down(self):
        self.send_command(f"{prefix}down{suffix}")
        return self.component_response()

    def arrow_left(self):
        self.send_command(f"{prefix}right{suffix}")
        return self.component_response()

    def arrow_right(self):
        self.send_command(f"{prefix}left{suffix}")
        return self.component_response()

    def menu_enter(self):
        self.send_command(f"{prefix}enter{suffix}")

    # endregion

    # region operation commands

    def position_front_table(self):
        self.send_command(f"{prefix}pp=FT{suffix}")
        return self.component_response()

    def position_front_ceiling(self):
        self.send_command(f"{prefix}pp=FC{suffix}")
        return self.component_response()

    def position_rear_table(self):
        self.send_command(f"{prefix}pp=RT{suffix}")
        return self.component_response()

    def position_rear_ceiling(self):
        self.send_command(f"{prefix}pp=RC{suffix}")
        return self.component_response()

    # endregion
