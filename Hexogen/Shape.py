#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2011 Louis Taylor <kragniz@gmail.com> 
#  
#  This file is part of Hexogen                             
#                                                                             
#  This program is free software: you can redistribute it and/or modify         
#  it under the terms of the GNU General Public License as published by         
#  the Free Software Foundation, either version 3 of the License, or            
#  (at your option) any later version.                                          
#                                                                             
#  This program is distributed in the hope that it will be useful,              
#  but WITHOUT ANY WARRANTY; without even the implied warranty of               
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                
#  GNU General Public License for more details.                                 
#                                                                            
#  You should have received a copy of the GNU General Public License            
#  along with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.txt 

from Hexagon import cartesianCoordinates
from math import sin, cos, pi

class Shape(object):
    '''Represents a single matchable shape'''
    
    def __init__(self, sideData=(), name='', radius=1):
        self._matchableSides = sideData
        self._name = name
        self._radius = radius
        self._colour = None
        
        
    def __str__(self):
        '''Return a nice string representation of the shape'''
        return self._name + ' : [' + ''.join(self._matchableSides) + ']'
    
    
    def __len__(self):
        '''Return the number of non-empty faces on this shape'''
        return len([c for c in self._matchableSides if c != '-'])
        
        
    def side(self, side):
        '''Return a string containing the type of face specified by face'''
        return self._matchableSides[side-1]
        
        
    def sides(self):
        '''Return a tuple containing side data'''
        return self._matchableSides
    
    
    def color(self):
        '''Return the colour of the shape (using the American spelling for consistency with CSS)'''
        return self._colour
        
        
    def loadFromFile(self, tileFileName):
        '''Load data about this tile from a file'''
        tileFileLines = open(tileFileName, 'r').readlines()
        data = []
        for line in tileFileLines:
            #print line
            if '#' in line: #handle some comments
                data += [line[:line.index('#')].strip()] #allow the comment to start on a line of code
            else:
                data += [line.strip()]
        while '' in data:
            data.remove('')
        
        if data[0].lower() != '[tile definition]':
            raise ValueError, 'This file does not seem to be a Shape definition file (must start with \'[tile definition]\')'
        else:
            data = data[1:] #remove this data, as it is now useless
            
        foundSides = {}
        for i in range(len(data)):
            if data[i].lower().startswith('name'):
                self._name = data[i][5:]
                
            if data[i].lower().startswith('color'):
                nonHexDigits = 0
                hexDigits = '123456789ABCDEF'
                for c in data[i][6:].upper():
                    if c not in hexDigits:
                        nonHexDigits += 1
                if nonHexDigits > 0:
                    #It's not hex.
                    self._colour = data[i][6:]
                else:
                    #must be hex, lets add a hash in front (for CSS stuff)
                    self._colour = '#' + data[i][6:]
                        
            if data[i].lower().startswith('side-'):
                foundSides[int(data[i][5])] = data[i][ data[i].index('=') + 1 :].strip()
                
        '''for k in foundSides:
            value = foundSides[k]
            if value == 'none': foundSides[k] = 0
            elif value == 'double': foundSides[k] = 2
            elif value == 'out': foundSides[k] = 1
            elif value == 'in': foundSides[k] = -1
            else:
                foundSides[k] = 0 #assume it's blank'''
        
        self._matchableSides = tuple(foundSides.values())
        
        
    def rotate(self, n): 
        '''Rotate the shape n times, with n being pi/3 radians'''
        sides = list(self._matchableSides)
        for i in range(n):
            sides[0] = self._matchableSides[-1]
            for j in range(len(sides)-1):
                sides[j+1] = self._matchableSides[j]
            self._matchableSides = tuple(sides)
            
            
    def setRadius(self, radius):
        '''Set the radius of the shape'''
        self._radius = radius
            
            
    def getVertices(self, controlPoints=False):
        '''Return the vertices making up this shape'''
        points = {}
        controlPoints = {}
        r = self._radius
        d1 = 0.15 * r #diameter of the extrusions from the shape
        d2 = 2 * d1 #length of the control points
        d3 = 6 #length of triangle extending out of one-way sides
        
        #two points on the edge of a hexagon, the top one and the next one along (clockwise)
        x1, y1 = 0, r
        x2, y2 = r * cos(pi/6), r * sin(pi/6)
        #midpoint between these two points
        xm, ym = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        #the two points d1 units away from the midpoint
        x1, y1 = xm - d1 * cos(pi/6), ym + d1 * sin(pi/6)
        x2, y2 = xm + d1 * cos(pi/6), ym - d1 * sin(pi/6)
        #the sticking in and sticking out bits for one-way sides
        xso, yso = (xm + d3 * cos(pi/3), ym + d3 * sin(pi/3)) #sticky-out
        xsi, ysi = (xm - d3 * cos(pi/3), ym - d3 * sin(pi/3)) #sticky-in
        print self._matchableSides
        
        if self._matchableSides[0] != '-':
            #main two points, with the 
            m1, m2, m3, m4 = (x1, y1), (x2, y2), (xso, yso), (xsi, ysi)
            #control points for some nice smooth lines
            xc1, yc1 = m1[0] - d2 * sin(pi/6),  m1[1] - d2 * cos(pi/6)
            xc2, yc2 = m2[0] - d2 * sin(pi/6),  m2[1] - d2 * cos(pi/6)
            points[0] = ( m1, m2, m3, m4 )
            controlPoints[0] = ( (xc1, yc1), (xc2, yc2) )
            
        if self._matchableSides[1] != '-':
            m1, m2, m3, m4 = (r * cos(pi/6), d1), (r * cos(pi/6), -d1), (r * cos(pi/6) + d3, 0), (r * cos(pi/6) - d3, 0)
            xc1, yc1 = m1[0] - d2,  m1[1]
            xc2, yc2 = m2[0] - d2,  m2[1]
            points[1] = ( m1, m2, m3, m4 )
            controlPoints[1] = ( (xc1, yc1), (xc2, yc2) )
            
        if self._matchableSides[2] != '-':
            m1, m2, m3, m4 = (x2, -y2), (x1, -y1), (xso, -yso), (xsi, -ysi)
            xc1, yc1 = m1[0] - d2 * sin(pi/6),  m1[1] + d2 * cos(pi/6)
            xc2, yc2 = m2[0] - d2 * sin(pi/6),  m1[1] + d2 * cos(pi/6) - d1 #wtf, why does this work?
            points[2] = ( m1, m2, m3, m4 )
            controlPoints[2] = ( (xc1, yc1), (xc2, yc2) )
            
        if self._matchableSides[3] != '-':
            m1, m2, m3, m4 = (-x1, -y1), (-x2, -y2), (-xso, -yso), (-xsi, -ysi)
            xc1, yc1 = m1[0] + d2 * sin(pi/6),  m1[1] + d2 * cos(pi/6)
            xc2, yc2 = m2[0] + d2 * sin(pi/6),  m2[1] + d2 * cos(pi/6)
            points[3] = ( m1, m2, m3, m4 )
            controlPoints[3] = ( (xc1, yc1), (xc2, yc2) )
        
        if self._matchableSides[4] != '-':
            m1, m2, m3, m4 = (-r * cos(pi/6), -d1), (-r * cos(pi/6), d1), (-r * cos(pi/6) - d3, 0), (-r * cos(pi/6) + d3, 0)
            xc1, yc1 = m1[0] + d2,  m1[1]
            xc2, yc2 = m2[0] + d2,  m2[1]
            points[4] = ( m1, m2, m3, m4 )
            controlPoints[4] = ( (xc1, yc1), (xc2, yc2) )
            
        if self._matchableSides[5] != '-':
            m1, m2, m3, m4 = (-x2, y2), (-x1, y1), (-xso, yso), (-xsi, ysi)
            xc1, yc1 = m1[0] + d2 * sin(pi/6),  m1[1] - d2 * cos(pi/6)
            xc2, yc2 = m2[0] + d2 * sin(pi/6),  m2[1] - d2 * cos(pi/6)
            points[5] = ( m1, m2, m3, m4 )
            controlPoints[5] = ( (xc1, yc1), (xc2, yc2) )
            
        if controlPoints:
            return points, controlPoints
        else:
            return points.values()
    
    
    def name(self):
        return self._name
