import gizeh
import numpy as np
import moviepy.editor as mpy
from rhythms import Kaolak, Leumbel
from numpy import pi
time_multiples = [1, 2, 4, 6]
W, H = 256, 256 # width, height, in pixels of one window. Total size is W*len(time_multiples), H*len(parts)
duration = 3 # duration of the clip, in seconds

rhythm = Kaolak()
parts = ['mbalax', 'talmac', 'nyokos']

stroke_colors = {'gin': [1, 0, 0],
                 'ta': [0, 1, 0],
                 'pax': [1, 1, 0],
                 'rwan': [.5, 1, 0],
                 'tet': [1, 1, 1]}

stroke_names = stroke_colors.keys()
stroke_offset_magnitude = .01
offsets = np.linspace(-stroke_offset_magnitude, stroke_offset_magnitude, len(stroke_names)) - pi/2
stroke_offsets = {stroke: offset for stroke, offset in zip(stroke_names, offsets)}

fade = np.pi

def ray(R, theta, center, **kw):
    x,y = center
    dx,dy = gizeh.polar2cart(R, theta)
    return gizeh.polyline(points=[(x,y), (x+dx,y+dy)], **kw)




def spinner(t, time_multiple, center, surface, R, hits, phase_offset, stroke_color):
    theta = t/duration*2*np.pi*time_multiple
    for hit in hits:
        hit = hit*time_multiple
        if theta>hit:
            intensity = np.exp((hit-theta)/fade/time_multiple)
            stroke = np.array(stroke_color)*intensity
            if intensity > .01:
                ray(R, hit+phase_offset, center, stroke_width=1, stroke=tuple(stroke)).draw(surface)


rows = len(time_multiples)
columns = len(parts)



def make_frame(t):
    surface = gizeh.Surface(W*columns, H*rows)
    xcenters = np.linspace(W/2, (columns-1)*W + W/2, columns)
    ycenters = np.linspace(H/2, (rows-1)*H + H/2, rows)
    for ycenter, time_multiple in zip(ycenters, time_multiples):
        for xcenter, part in zip(xcenters, parts):

            part = getattr(rhythm, part)
            for stroke in part.keys():
                stroke_color = stroke_colors[stroke]
                hits = part[stroke]
                phase_offset = stroke_offsets[stroke]
                spinner(t, time_multiple, (xcenter, ycenter), surface, W/2, hits, phase_offset, stroke_color)
    return surface.get_npimage()


clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle_LEUMBEL.gif",fps=60, opt="OptimizePlus", fuzz=10)
