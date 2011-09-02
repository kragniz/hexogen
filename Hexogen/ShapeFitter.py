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

from Shape import Shape
from random import randint

class ShapeFitter(object):
    '''Find the amount to rotate a shape to fit into a gap'''
    
    def __init__(self, shapeSides, gapSides):
        self._shape = Shape(shapeSides, 'shape being rotated')
        self._gapSides = gapSides
        
        
    def fit(self, random=True):
        '''Rotate the shape around until it fits the gap. Random by default to avoid bias'''
        orientationsChecked = []
        timesRotated = 0
        
        if random: #give the shape a random offset
            rotateNumber = randint(0, 5)
            timesRotated += rotateNumber
            self._shape.rotate(rotateNumber) 
        else:
            rotateNumber = 1
            
        if not self._fits():
            while (len(orientationsChecked) < 6):
                if not self._fits():
                    if random: #rotateNumber defaults to 1 if not random
                        rotateNumber = randint(1, 5)                        
                    timesRotated += rotateNumber
                    self._shape.rotate(rotateNumber) 
                    if self._shape.sides() not in orientationsChecked:
                        if self._fits():
                            return timesRotated % 6
                        else:
                            orientationsChecked += [self._shape.sides()]
        else:
            return timesRotated % 6 #if it already fits
        
        
    def _fits(self):
        '''Return True if the shape fits in the gap'''
        passed = True
        for i in range(len(self._shape.sides())): #TODO make Shape iterative
            if self._gapSides[i] != '+': # '+' means an empty hexagon (with no shape attached), so any tile can be adjacent to its sides
                if self._gapSides[i] != self._shape.sides()[i].swapcase(): #swap the case, meaning only side A can connect to side a and vice versa
                    passed = False
        return passed
