#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import time

c = Camera()
img = c.getImage().save('Fotoloca.jpg')
time.sleep(2)

