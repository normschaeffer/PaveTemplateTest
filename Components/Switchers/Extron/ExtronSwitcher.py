import socket

eol = '\r\n'

"""
Pynexsis class implementing Extron Switcher SIS for Extron XTP, DTP, and IN model video switchers
"""


class ExtronSwitcher:

    """
    Initialize switcher and connect to device
    Parameters:
        host (string) - hostname or ipaddress
        port (int) - default is 23, but device can be reconfigured by administrator to use different port
        username (string)  - can be blank - internally defaults to User
        password (string) - can be blank - internally defaults to user-level access

    Example:
    from ExtronSwitcher import ExtronSwitcher

    swt = ExtronSwitcher('192.168.1.50', 23, '','')

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

    def disconnect(self):
        s = self.s
        s.close()

    # endregion

    # region Send Command and Component Response
    def send_command(self, cmd):
        s = self.s
        s.send(bytes(cmd, 'utf-8'))

    def component_response(self) -> object:
        s = self.s
        device_response = s.recv(1024).decode('utf-8')
        return device_response

    # endregion

    # region Single Channel Switcher command
    def av_switch(self, swt_input):
        self.send_command(f'{swt_input}!' + eol)

    # endregion

    # region Crosspoint commands
    def av_xpoint(self, swt_input, swt_output) -> object:
        self.send_command(f'{swt_input}*{swt_output}!' + eol)
        return self.component_response()

    def av_xpoints(self, swt_input, swt_outputs):
        for swt_output in swt_outputs:
            self.av_xpoint(swt_input, swt_output)

    def av_xpoint_all(self, swt_input):
        self.send_command(f'{swt_input}*!' + eol)
        return self.component_response()

    def av_clear_all(self):
        self.send_command(f'0*!' + eol)
        self.component_response()

    def video_xpoint(self, swt_input, swt_output):
        self.send_command(f'{swt_input}*{swt_output}%' + eol)
        self.component_response()

    def video_xpoints(self, swt_input, swt_outputs):
        for swt_output in swt_outputs:
            self.audio_xpoint(swt_input, swt_output)
            self.component_response()

    def video_xpoint_all(self, swt_input):
        self.send_command(f'{swt_input}*%' + eol)
        self.component_response()

    def audio_xpoint(self, swt_input, swt_output):
        self.send_command(f'{swt_input}*{swt_output}$' + eol)
        self.component_response()

    def audio_xpoints(self, swt_input, swt_outputs):
        for swt_output in swt_outputs:
            self.audio_xpoint(swt_input, swt_output)
            self.component_response()

    def audio_xpoint_all(self, swt_input):
        self.send_command(f'{swt_input}*$' + eol)
        self.component_response()

    # endregion

    # region Get Crosspoint information
    def get_av_xpoint(self, channel):
        self.send_command(f'{channel}!' + eol)
        return self.component_response()

    def get_video_xpoint(self, channel):
        self.send_command(f'{channel}%' + eol)
        self.component_response()

    def get_audio_xpoint(self, channel):
        self.send_command(f'{channel}$' + eol)
        self.component_response()

    # endregion

    # region Mute Commands
    def video_mute_on(self, channel):
        self.send_command(f'{channel}*1B' + eol)
        self.component_response()

    def video_mute_off(self, channel):
        self.send_command(f'{channel}*0B' + eol)
        self.component_response()

    def audio_mute_on(self, channel):
        self.send_command(f'{channel}*1Z' + eol)
        self.component_response()

    def audio_mute_off(self, channel):
        self.send_command(f'{channel}*0Z' + eol)
        self.component_response()

    def mute_all_video(self):
        self.send_command('1*B' + eol)
        self.component_response()

    def unmute_all_video(self):
        self.send_command('0*B' + eol)
        self.component_response()

    def mute_all_audio(self):
        self.send_command('1*Z' + eol)
        self.component_response()

    def unmute_all_audio(self):
        self.send_command('0*Z' + eol)
        self.component_response()
    # endregion
