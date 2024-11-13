#!/usr/bin/python3.8
from PIL import Image
import re
import os
import argparse
import joblib
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split

def cut_image( image, row, col ):
	width, height = image.size
	item_width = float( width / col )
	item_height = float( height / row )
	box_list = []
	image_list = []
	
	for i in range( 0, row ):
		for j in range( 0, col ):
			box = ( j*item_width, i*item_height, (j+1)*item_width, (i+1)*item_height )
			box_list.append( box )
	
	for box in box_list:
		box = image.crop( box )
		box = box.crop( ( 5, 5, 25, 25 ) )
		image_list.append( box )
	
	return image_list

def save_images( image_list ):
	letter = [ chr(i) for i in range( ord("A"), ord("Q") ) ]
	for k in range( 0, len( image_list ) ):
		row = int( ( k + 1 ) / 24 ) - 1
		col = ( k + 1 ) % 24
		if col == 0:
			loc = letter[ row ] + '24'
		else:
			loc = letter[ row + 1 ] + str( col )
		image_list[ k ].save( loc + '.jpg' )

if __name__ == '__main__':
	parser = argparse.ArgumentParser( description='########\nGreen-Yellow Ranking\n#########\n' )
	parser.add_argument( '-i', '--input', dest='input', metavar='', required=True, help='input image' )
	parser.add_argument( '-o', '--output', dest='output', metavar='', help='output table (default {inputName}.tsv)' )
	parser.add_argument( '-p','--pixel', dest='pixel', metavar='', type=int, default=30, help='pixels used to calculate the final value' )
	
	args = parser.parse_args()
	
	if not args.output:
		if '.png' in args.input:
			args.output = args.input.replace( '.png', '.tsv' )
		else:
			args.output = args.input + '.tsv'
	
	img = Image.open( args.input )
	
	cropped = img.crop( ( 277.3, 225.3, 998.4, 702.7 ) )  # (left, upper, right, lower)
	image_list = cut_image( cropped, 16, 24 )
	
	
	Final_score = {}
	
	clf = joblib.load( 'model.svm.linear.pkl' )
	
	p = 1
	for i in image_list:
		score = []
		for y in range( i.size[1] ):
			for x in range( i.size[0] ):
				pix = i.getpixel( ( x, y ) )
				score.append( clf.predict( [[ pix[0], pix[1], pix[2] ] ] ).item() )
		score.sort()
		Final_score[ p ] = float( sum( score[ -args.pixel: ] ) / args.pixel )
		p += 1
		
	with open( args.output, 'w' ) as out:
		letter = [ chr(i) for i in range( ord("A"), ord("Q") ) ]
		for k in Final_score:
			row = int( k / 24 ) - 1
			col = k % 24
			if col == 0:
				loc = letter[ row ] + '24'
			else:
				loc = letter[ row + 1 ] + str( col )
			out.write( loc + '\t' + str( Final_score[ k ] ) + '\n' )
	
