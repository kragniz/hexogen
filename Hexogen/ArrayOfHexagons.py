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

from Hexagon import Hexagon

class ArrayOfHexagons(object):
    '''Manages an array of the Hexagon object'''
    
    def __init__(self):
        self._array = {} #the dictionary used for saving the hexagons. Uses a two-part tuple (u, v) as the key
        self._radius = 1 
        self.debugMessages = False
        
        
    def __len__(self):
        return len(self._array)
    
    
    def __iter__(self):
        return iter(self._array)
        
        
    def hexagon(self, u, v):
        '''Return the hexagon at the location (u, v)'''
        return self._array[(u, v)]
     
     
    def setRadius(self, r):
        self._radius = r
        
        
    def printArray(self):
        print len(self._array), 'hexagons in the array'
        for k in self._array:
            print self._array[k]
            
            
    def findClosest(self, *args):
        '''Finds the closest tile to the centre (0, 0) from a set of coordinates'''
        pass #TODO
        
        
    def hasHexagonAt(self, u, v):
        '''Return whether this array has a hexagon at the point (u, v)'''
        return self._array.has_key((u, v))
        #a.printArray()
        
        
    def populate(self, depth):
        '''Populates the array'''
        doneHexagons = [] #save the hexagons known to have all faces joined to another hexagon
        
        for n in range(depth):
            temporaryArray = dict(self._array) # make a copy of the dictionary. 
                                               # Just doing temporaryArray = self._array does not work
                                               # because this creates a new pointer to the same memory
                                               # location instead of copying the memory content
            
            for u, v in temporaryArray: #iterate through each hexagon
                if (u, v) not in doneHexagons:
                    currentHexagon = self.hexagon(u, v)
                    for face in range(1, 7): #iterate through each face of the hexagon
                        uface, vface = currentHexagon.getAdjacentHexagon(face)
                        if not self.hasHexagonAt(uface, vface):
                            self.addHexagon(uface, vface)
                    doneHexagons += [(u, v)]
        
        
    def addHexagon(self, u, v):
        if not self.hasHexagonAt(u, v):
            self._array[(u, v)] = Hexagon(u, v, self._radius)
        else:
            raise ValueError, 'These coordinates are already used'
            
            
    def gapEdges(self, u, v):
        '''Finds each type of face around a hexagon with no shape'''
        faces = [4, 5, 6, 1, 2, 3] #the face number of the face adjacent to this hexagons face number [index+1]
        edges = []
        hexagon = self.hexagon(u, v)
        for f in range(6):
            hexu, hexv = self.hexagon(u, v).getAdjacentHexagon(f+1)
            if self.hasHexagonAt(hexu, hexv):
                shape = self.hexagon(hexu, hexv).shape()
                if shape != None:
                    edges += [shape.side(faces[f])]
                else:
                    edges += ['+']
            else:
                edges += ['+']
        return tuple(edges)
