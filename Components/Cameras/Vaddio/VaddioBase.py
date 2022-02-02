# TODO: Check response for password prompt
# TODO: Add component response to all functions

import socket
import time

# region Camera properties
eol = '\r\n'
min_speed = 1
max_pan_speed = 24
max_tilt_speed = 20
max_zoom_speed = 7
max_focus_speed = 8
# endregion

"""
EnkadiaPave(Python Audio Video Extensions) is an Audio Video Control library for AV system integrators. 

VaddioBase is the EnkadiaPave class implementing Vaddio RoboShot and ConferenceShot cameras. This module includes basic
PTZF movement and ability to set and recall presets
"""


class VaddioBase:
    """
    Initialize camera and connect to device

    :param host: hostname or ipaddress
    :type host: string
    :param port: set device port default is 23, but device can be reconfigured by administrator to use different port
    :type port: int
    :param username: add username for login; an empty string my be used for default User
    :type username: string
    :param password: add password for login: - an empty string my be used for default user-level access
    :type password: string

    Example:
    from Enkadia.Pave.Components.Cameras.Vaddio.VaddioBase import VaddioBase

    camera1 = VaddioBase('192.168.1.200', 23, 'user','password')

    """

    def __init__(self, host, port, username, password):
        self.s = socket.socket()
        self.host = host
        self.port = port or 23
        self.username = username
        self.password = password
        self.connect()

    # region Connect / Disconnect

    """

    """

    def connect(self):
        s = self.s
        hostname = self.host
        port = self.port
        s.connect((hostname, port))
        time.sleep(.5)
        self.authenticate()

    def authenticate(self):
        response = self.component_response()
        if response.__contains__(b'login: '):
            self.send_command(f'{self.username}\r\n')
            time.sleep(.5)
            self.send_command(f'{self.password}\r\n')
            time.sleep(.5)

    def disconnect(self):
        s = self.s
        s.close()

    # endregion

    # region Send Command and Component Response
    def send_command(self, cmd):
        time.sleep(.25)
        s = self.s
        s.send(bytes(cmd, 'utf-8'))

    def component_response(self) -> object:
        s = self.s
        while True:
            device_response = s.recv(8196).hex()
            if not device_response:
                break
            device_response = bytes.fromhex(device_response)
            print(device_response)
            return device_response

    # endregion

    # region Stop and Home commands
    """
    Send stop command to camera, returns OK if successful
    """

    def stop(self):
        self.send_command('camera pan stop' + eol)
        self.send_command('camera zoom stop' + eol)
        self.send_command('camera tilt stop' + eol)

    """
    Send camera to home position, returns OK if successful
    """

    def home(self):
        self.send_command('camera home' + eol)

    # endregion

    # region PTZ commands

    """
    Pan camera right at the default speed
    """
    def pan_right(self):
        self.send_command('camera pan right' + eol)

    """"
    Pan camera right at user-defined speed
    :param speed: set pan speed 1-24
    :type speed: int
    """
    def pan_right_at_speed(self, speed):
        if speed > max_pan_speed:
            speed = str(max_pan_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera pan right {speed}' + eol)

    """
    Pan camera left at the default speed
    """
    def pan_left(self):
        self.send_command('camera pan left' + eol)

    """"
    Pan camera left at user-defined speed
    :param speed: set pan speed 1-24
    :type speed: int
    """
    def pan_left_at_speed(self, speed):
        if speed > max_pan_speed:
            speed = str(max_pan_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera pan left {speed}' + eol)

    """
    Tilt camera up at the default speed
    """
    def tilt_up(self):
        self.send_command('camera tilt up' + eol)

    """"
    Tilt camera up at user-defined speed
    :param speed: set tilt speed 1-20
    :type speed: int
    """
    def tilt_up_at_speed(self, speed):
        if speed > max_tilt_speed:
            speed = str(max_tilt_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera tilt up {speed}' + eol)

    """
    Tilt camera down at the default speed
    """
    def tilt_down(self):
        self.send_command('camera tilt down' + eol)

    """"
    Tilt camera down at user-defined speed
    :param speed: set tilt speed 1-20
    :type speed: int
    """
    def tilt_down_at_speed(self, speed):
        if speed > max_tilt_speed:
            speed = str(max_tilt_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera tilt down {speed}' + eol)

    """
    Zoom camera in at the default speed
    """
    def zoom_in(self):
        self.send_command('camera zoom in' + eol)

    """"
    Zoom camera in at user-defined speed
    :param speed: set zoom speed 1-7
    :type speed: int
    """
    def zoom_in_at_speed(self, speed):
        if speed > max_zoom_speed:
            speed = str(max_zoom_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera zoom in {speed}' + eol)

    """
    Zoom camera out at the default speed
    """
    def zoom_out(self):
        self.send_command('camera zoom out' + eol)

    """"
    Zoom camera out at user-defined speed
    :param speed: set zoom speed 1-7
    :type speed: int
    """
    def zoom_out_at_speed(self, speed):
        if speed > max_zoom_speed:
            speed = str(max_zoom_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera zoom out {speed}' + eol)

    """
    Set camera focus near at the default speed
    """
    def focus_near(self):
        self.send_command('camera focus near' + eol)

    """"
    Set camera focus near at user-defined speed
    :param speed: set focus speed 1-8
    :type speed: int
    """
    def focus_near_at_speed(self, speed):
        if speed > max_focus_speed:
            speed = str(max_focus_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera focus near {speed}' + eol)

    """
    Set camera focus far at the default speed
    """
    def focus_far(self):
        self.send_command('camera focus far' + eol)

    """"
    Set camera focus far at user-defined speed
    :param speed: set focus speed 1-8
    :type speed: int
    """
    def focus_far_at_speed(self, speed):
        if speed > max_focus_speed:
            speed = str(max_focus_speed)
        if speed < min_speed:
            speed = str(min_speed)
        self.send_command(f'camera focus far {speed}' + eol)

    # endregion

    # region Presets

    """
    Get camera preset
    :param preset: get camera preset 1-16
    :type preset: int
    """
    def get_preset(self, preset):
        self.send_command(f'camera preset recall {preset}' + eol)

    """
    Set camera preset
    :param preset: get camera preset 1-16
    :type preset: int
    """
    def set_preset(self, preset):
        self.send_command(f'camera preset store {preset}' + eol)

    # endregion

    # region Toggle Standby / Auto focus commands

    """
    Toggle camera standby off/on
    """
    def toggle_standby(self):
        self.send_command('camera standby toggle' + eol)

    """
    Set focus to auto
    """
    def auto_focus_on(self):
        self.send_command('camera focus mode auto' + eol)

    """
    Set focus to manual
    """
    def auto_focus_off(self):
        self.send_command('camera focus mode manual' + eol)

    # endregion
