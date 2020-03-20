#!/usr/bin/python

import os
import sys
import math

import colorsys



def halton(idx, base) :
	result = 0
	f = 1.0 / base
	i = idx
	while ( i > 0 ) :
		result += f * ( i % base )
		i = i / base
		f = f / base
	return result


mrg = 16
dim = 256-2*mrg
siz = dim+2*mrg

row = [ (1,1,1) for x in range(siz) ]
img = [ row+[] for x in range(siz) ]

accepted = []


def dump_img(name) :

	f = open( name, "w" )
	assert f
	f.write("P3\n%d %d\n255\n" % (siz,siz) )
	for y in range(siz) :
		for x in range(siz) :
			rgb = img[ y ][ x ]
			v0 = int(255.999 * rgb[0])
			v1 = int(255.999 * rgb[1])
			v2 = int(255.999 * rgb[2])
			f.write(str(v0)+" ")
			f.write(str(v1)+" ")
			f.write(str(v2)+" ")
		f.write("\n")
	f.close()


for i in range(51) :

	name = "images/out%04d.ppm" % ( i, )
	dump_img(name)

	x = halton( i, 2 )
	y = halton( i, 3 )
	ix = mrg + int( dim * x )
	iy = mrg + int( dim * y )
	rgb = colorsys.hsv_to_rgb( x, 1.0, 0.3 + 0.7 * y )
	for xx in range(-3,4) :
		for yy in range(-3,4) :
			img[ iy+yy ][ ix+xx ] = rgb


