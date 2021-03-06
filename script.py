import pathmap
import image2bin
import time

i2b = image2bin.im2bin()
PathMap = pathmap.PathMap(i2b)
PathMap.fwrite_path("path.txt")
f_interrupt = open("interrupt.txt",'w')
f_interrupt.write("0")
f_interrupt.close()

while 1:
    time.sleep(1)
    i2b.update()
    if PathMap.need_update(i2b):
        f_interrupt = open("interrupt.txt",'w')
        f_interrupt.write("1")
        f_interrupt.close()
        print "path update"
        PathMap.update(i2b)
    else:
        f_interrupt = open("interrupt.txt",'w')
        f_interrupt.write("0")
        f_interrupt.close()
    PathMap.barriers = i2b.barriers

