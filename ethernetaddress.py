import struct


class EthernetAddress(object):
    @staticmethod
    def convert_string_to_binary(string):
        octets = string.split(':')
        assert len(octets) == 6
        return struct.pack('BBBBBB',
            int(octets[0],16), int(octets[1],16),
            int(octets[2],16), int(octets[3],16),
            int(octets[4],16), int(octets[5],16))

    def __init__(self, string):
        self.string = string
        self.addr = EthernetAddress.convert_string_to_binary(string)

    def __repr__(self):
        return '%s("%s")' % (self.__class__.__name__, self.string)

    def __str__(self):
        return self.addr
