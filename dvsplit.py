import sys
import os
import y4m
import copy

dumpers = []
outfds = []
outfds.append(open('dump.y4m',"wb"))
def process_frame(frame):
    outbuf = bytes()
    number_of_slices = 4
    indx = 0
    frame_header = copy.copy(frame.headers)
    #frame_header['W'] //= 2
    frame_header['H'] //= number_of_slices
    
    size_slice = frame.headers['W'] * (frame.headers['H'] //number_of_slices)

    offset_Y = size_slice * indx
    offset_U = offset_Y + frame.headers['W'] * frame.headers['H']
    offset_V = offset_U + (frame.headers['W'] * frame.headers['H'])//4
    
    outbuf += frame.buffer[offset_Y:offset_Y+size_slice]
    size_slice //= 4
    outbuf += frame.buffer[offset_U:offset_U+size_slice]
    outbuf += frame.buffer[offset_V:offset_V+size_slice]
    
    dumpers[0].encode(y4m.Frame(outbuf,frame_header,frame.count))


dumpers.append(y4m.Writer(outfds[0], verbose=True))
parser = y4m.Reader(process_frame, verbose=True)
# simulate chunk of data
with open('tests/akiyo_qcif.y4m',"rb") as f:
    ff = None
    while parser._count != 100:
        data = f.read(1024)
        if not data:
            break
        ff = parser.decode(data)
