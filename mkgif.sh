#!/bin/sh

convert -delay 20 -loop 0 images/*.ppm images/anim.gif
#convert anim.gif -fuzz 3% -layers Optimize optim.gif

