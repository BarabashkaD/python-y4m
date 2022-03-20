import sys
import os
import y4m

all_frames = []
def process_frame(frame):
    # do something with the frame
    #pass
    print (frame.headers['W'],frame.headers['H'])
    all_frames.append(frame)



parser = y4m.Reader(process_frame, verbose=True)
# simulate chunk of data
with open('tests/akiyo_qcif.y4m',"rb") as f:
    ff = None
    while parser._count != 1:
        data = f.read(1024)
    #if not data:
    #    break
        ff = parser.decode(data)
    print (len(all_frames),all_frames[0].headers['H'], all_frames[0].headers['W'])