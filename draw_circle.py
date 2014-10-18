import gizeh
import numpy as np
import moviepy.editor as mpy
subdivisions = [2, 1,  .5]
W,H = 128*len(subdivisions),128 # width, height, in ixels
duration = 3 # duration of the clip, in seconds
cycles = 4  #duration of the clip in cycles
hits = np.array([0, .75, 1.5, 1.75, 2, 2.75, 3.0, 3.5, 3.75])*2*np.pi
ta = np.array([ 1.5, 1.75, 3.5, 3.75])*2*np.pi
gin = np.array([.75, 2.75, 3])*2*np.pi
pax = np.array([0, 1.25, 2])*2*np.pi
hits = {}
hits[0] = ta
hits[1] = gin
hits[2] = pax
#add hits at beginning to get burn in
for channel in hits.keys():
    hits[channel] = np.concatenate([hits[channel], hits[channel]+(cycles*2*np.pi)])
print hits
fade = 2*np.pi
def ray(R, theta, center, **kw):
    x,y = center
    dx,dy = gizeh.polar2cart(R, theta)
    return gizeh.polyline(points=[(x,y), (x+dx,y+dy)], **kw)

blank = gizeh.Surface(W,H).get_npimage()
surface = gizeh.Surface(W,H)


def spinner(t, center, subdivision, R, channel):
#    image = blank 
    theta = (t+duration)/duration*2*np.pi*cycles*subdivision 
    for hit in hits[channel]:
        hit = hit*subdivision
        #surface = gizeh.Surface(W,H)
        if theta>hit:
            i = np.exp((hit-theta)/fade/subdivision)
            stroke = np.array({0:[0,1,0], 1:[1,0,0], 2:[1,1,0]}[channel])
            stroke = stroke*i
            ray(R, hit-(np.pi/2), center, stroke_width=1, stroke=tuple(stroke)).draw(surface)
 #           image += surface.get_npimage()
  #  return image
    #ray(R, theta, center, stroke_width=1, stroke=(1,1,0)).draw(surface) 

def make_frame(t):
    image = blank
    xcenter = 64
    ycenter = 64
    for i, subdivision in enumerate(reversed(subdivisions)): 
       for channel in hits.keys(): 
            spinner(t, (xcenter, ycenter), subdivision, 64, channel )         
       xcenter+=128
       # ycenter += 128
       # xcenter = 64
        
      
   # for i in range(image.shape[2]):
#	image[:,:,i] = np.max(image[:,:,i])
#    return image 
    return surface.get_npimage()
clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=60, opt="OptimizePlus", fuzz=10)
