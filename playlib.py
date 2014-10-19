import struct
from subprocess import call

def play(f, duration):
    steps = int(duration * 44100)
    with open('/tmp/test.raw', 'wb') as rawf:
        carry = None
        for i in range(0, steps):
            [w, carry] = f(i/44100.0, carry)
            rawf.write(struct.pack('h', int(32767.0 * w)))
    call(['play', '-r44100', '-b16', '-c1', '-esig', '/tmp/test.raw'])

def samples(f, duration):
    res = []
    steps = int(duration * 44100)
    carry = None
    for i in range(0, steps):
        [w, carry] = f(i/44100.0, carry)
        res.append(w)
    return res

def playsamp(samples):
    with open('/tmp/test.raw', 'wb') as rawf:
        for s in samples:
            rawf.write(struct.pack('h', int(32767.0 * s)))
    call(['play', '-r44100', '-b16', '-c1', '-esig', '/tmp/test.raw'])
