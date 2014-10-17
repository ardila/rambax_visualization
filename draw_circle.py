import gizeh
import moviepy.editor as mpy
W,H = 128,128 # width, height, in pixels
duration = 2 # duration of the clip, in seconds
def make_frame(t):
    surface = gizeh.Surface(W,H)
    length = W*(1+(t*(duration-t))**2)/6
    #line = gizeh.polyline([(64,64),(70, 64)], xy=(64,64), stroke=(1,0,0), stroke_width=1)
    line = gizeh.polyline(points=[(64,64), (64+length,64), (40,40), (0,10)], stroke_width=3,
                     stroke=(1,0,0), fill=(0,1,0))
    line.draw(surface)
    return surface.get_npimage()
#def make_frame(t):
#    surface = gizeh.Surface(W,H)
#    radius = W*(1+ (t*(duration-t))**2 )/6
#    circle = gizeh.circle(radius, xy = (W/2,H/2), fill=(1,0,0))
#    circle.draw(surface)
#    return surface.get_npimage()
clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=15, opt="OptimizePlus", fuzz=10)
clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=15, opt="OptimizePlus", fuzz=10)
