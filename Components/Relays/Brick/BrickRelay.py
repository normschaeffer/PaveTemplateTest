# TODO: Test actual unit for CRLF requirements

import socket
import time


class BrickRelay:
    """
    Initialize relay and connect to device
    Parameters:
        host (string) - hostname or ipaddress
        password (string)  - default is 123456

    Example:
    from Enkadia.Pave.Components.Relays.BrickRelay.BrickRelay import BrickRelay

    relay = BrickRelay('192.168.1.105' '','')

    """

    # will probably use constructor similar to following with TcpHelper is written and tested
    # def __init__(self, host, port, username, password):

    def __init__(self, host, password):
        self.s = socket.socket()
        self.host = host
        self.port = 5000
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
        # self.authenticate()

    def authenticate(self):
        response = self.component_response()
        if response.__contains__(b'login: '):
            self.send_command(f'{self.username}\r\n')
            self.send_command(f'{self.password}\r\n')

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
        print(device_response)
        return device_response

    # endregion

    # region Commands

    """
    Turn relay off

    Example:
        relay.off(1)
    """

    def off(self, relay_number):
        self.send_command(f'k0{relay_number}=0')
        self.component_response()

    """
    Turn relay on

    Example:
        relay.on(1)
    """

    def on(self, relay_number):
        self.send_command(f'k0{relay_number}=1')
        self.component_response()

    """
    Pulse relay

    Example:
        relay.pulse(1)
    """

    def pulse(self, relay_number):
        self.send_command(f'k0{relay_number}=4')
        self.component_response()

    """
    Set relay pulse time (in milliseconds)
      - pulse default is 1000ms

    Example:
        relay.set_pulse_time(2500)
    """

    def set_pulse_time(self, pulse_time):
        self.send_command(f'setpara[65]={pulse_time}')
        self.component_response()

    """
    Cycle (blink) relay
      - relay will pulse off and on until it receives a new command
      - Cycle time is based on pulse_time (default 1000ms)

    Example:
        relay.cycle

    """

    def cycle(self, relay_number):
        self.send_command(f'k0{relay_number}=6')
        self.component_response()

    """
    Set the length of time in milliseconds the cycle is on

    Example:
        relay.set_cycle_on_time(5000)
    """

    def set_cycle_on_time(self, cycle_on_time):
        self.send_command(f'setpara[65]={cycle_on_time}')
        self.component_response()

    """
    Set the length of time in milliseconds the cycle is off

    Example:
        relay.set_cycle_off_time(5000)
    """

    def set_cycle_off_time(self, cycle_off_time):
        self.send_command(f'setpara[66]={cycle_off_time}')
        self.component_response()

    """
    Read relay output status

    Example:
        relay.get_status(1)
    """

    def get_status(self, relay_number):
        self.send_command(f'k0{relay_number}=7')
        self.component_response()

    """
    Turn relays on in sequence with user-defined delay in milliseconds

    Example:
        relay.sequence_on([2, 8, 3], 1000)
    """

    def sequence_on(self, relays, delay):
        for relay in relays:
            self.send_command(f'k0{relay}=1')
            time.sleep(delay)
