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

from copy import copy
from math import sin, cos, tan, sqrt, pi

class Hexagon(object):
    '''Represents a single hexagon'''
    
    def __init__(self, u, v, r):
        '''Creates a new hexagon with centre (u, v) and radius r'''
        self._u = u
        self._v = v
        self._radius = r
        self._shape = None
        
        
    def __str__(self):
        return 'Hexagon at (%s, %s). Owns shape "%s"' % (self._u, self._v, self._shape)
        
        
    def hexagonalCoordinates(self):
        '''Return the hexagonal coordinates of this hexagon'''
        return (self._u, self._v)
        
        
    def cartesianCoordinates(self, u=None, v=None):
        '''Converts hexagonal coordinates (u, v) into cartesian
        coordinates (x, y). If coordinates are not specified, the
        coordinates of the hexagon are used'''
        r = self._radius
        
        if (u == None) and (v == None):
            u = self._u
            v = self._v
            
        return (u * r * cos(pi/6),
                -(v * (r + r * sin(pi/6))))
        
        
    def distanceFrom(self, u, v):
        '''Return the distance from another hexagon (u, v)'''
        xLocal, yLocal = self.cartesianCoordinates()
        xDistant, yDistant = self.cartesianCoordinates(u, v)
        # Pythagoras
        return sqrt( ((xLocal - xDistant)**2) + ((yLocal - yDistant)**2) )
        
        
    def getVertices(self):
        '''Return the coordinates for the vertices of this hexagon''' 
        r = self._radius
        x = self._u * r * cos(pi/6)
        y = -self._v * (r + r * sin(pi/6))
        
        return ( 
                 ( x , y + r ),
                 ( x + r * cos(pi/6), y + r * sin(pi/6) ),
                 ( x + r * cos(pi/6), (y - r * sin(pi/6) ) ),
                 ( x, y - r ),
                 ( x - r * cos(pi/6), y - r * sin(pi/6) ),
                 ( x - r * cos(pi/6), y + r * sin(pi/6) )
               )
               
               
    def getAdjacentHexagon(self, side):
        '''Return the hexagonal coordinates of the hexagon adjacent
        to the given side. The sides are counted clockwise from the
        upper right side'''
        
        u = self._u
        v = self._v
        
        if side == 1: return (u + 1, v + 1)
        elif side == 2: return (u + 2, v)
        elif side == 3: return (u + 1, v - 1)
        elif side == 4: return (u - 1, v - 1)
        elif side == 5: return (u - 2, v)
        elif side == 6: return (u - 1, v + 1)
        else: raise ValueError, 'Side value %s not valid' % side
        
        
    def surroundingShapeCoordinates(self):
        '''Return the pairs of coordinates belonging to the hexagons
        surrounding this hexagon which need a shape, and the type of 
        connector needed'''
        #TODO
        for side in self._shape.sides():
            print side
            
            
    def radius(self):
        return self._radius
        
        
    def addShape(self, shape):
        '''Attach a shape to this hexagon tile. Makes a copy of the shape. Returns the new shape'''
        self._shape = copy(shape) #Copy it (using copy.copy())
        self._shape.setRadius(self._radius)
        return self._shape
        
        
    def removeShape(self):
        '''Remove the shape from this hexagon'''
        self._shape = None
        
        
    def shape(self):
        '''Return the shape currently attached to this hexagon'''
        return self._shape
        
        
    def hasShape(self):
        '''Return whether this hexagon has a shape attached'''
        if self._shape: #FIXME make this neater!
            return True
        else:
            return False
        
        
def cartesianCoordinates(u, v, r):
        '''Converts hexagonal coordinates (u, v) into cartesian
        coordinates (x, y), with the radius r.
        (helper function to be imported)'''
            
        return (u * r * cos(pi/6),
                v * (r + r * sin(pi/6)))
