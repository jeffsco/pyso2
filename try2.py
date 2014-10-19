import playlib
import math

def f(t, carry):
    return [math.sin(t * 440.0 * 2 * math.pi), 0]
def g(t, carry):
    return [math.sin(t * 440.0 * 1.0594630943592953 * 2 * math.pi), 0]

playlib.playsamp(playlib.samples(f, None, 1.0))
playlib.playsamp(playlib.samples(g, None, 1.0))
