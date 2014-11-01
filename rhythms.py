__author__ = 'ardila'

import numpy as np
from numpy import pi


class Rhythm(object):
   def __init__(self, repeats=2):
        for part in [self.mbalax, self.talmac, self.nyokos]:
            for stroke in part.keys():
                hits = np.array(part[stroke])
                if self.triple_meter == True:
                    hits = hits/3.
                hits = hits / 4. # 4 beats per cycle
                hits = hits * 2 * pi #1 measure per 2 pi radians
                final_hits = hits
                offsets = np.linspace(-(repeats-1)*2*pi, 0, repeats)
                # add repeats before start of video loop for burn-in
                part[stroke] = np.concatenate([repeat+offset for repeat, offset in zip([hits]*repeats, offsets)])


class Kaolak(Rhythm):
    triple_meter = False

    mbalax = {'ta': [1.5, 1.75, 3.5, 3.75],
              'gin': [.75, 2.75, 3],
              'pax': [0, 1.25, 2]}

    talmac = {'ta': [3.75],
              'gin': [0, 2],
              'tet': [.5, 2.5],
              'rwan': [1.5],
              'pax': [3]}

    nyokos = {'ta': [0, .75, 1.5, 2.75],
              'gin': [1, 3],
              'pax': [1.75]}


class Leumbel(Rhythm):
    triple_meter = True
    mbalax = {'ta': [0, 1, 3, 4, 6, 7, 9, 10],
              'gin': [2, 8],
              'pax': [5, 11]}

    talmac = {'ta': [5, 11],
              'gin': [0, 6],
              'tet': [1, 3, 7, 9]}

    nyokos = {'ta': [0, 2, 4, 8],
              'gin': [3, 9],
              'pax': [5]}


#Dude i actually don't know what baarmbaye is....
class Baarmbaye(Rhythm):
    triple = False
    mbalax = {'ta0'}

