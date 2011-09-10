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
from ArrayOfHexagons import ArrayOfHexagons
from ShapeFitter import ShapeFitter
from Shape import Shape
from ShapeManager import ShapeManager
from SvgWriter import SvgWriter
from ProgramData import VERSION, NAME

from math import sin, cos, tan, sqrt, pi
from random import randint
import random
import os.path
import time

class Test(object):        
    def everything(self):
        '''do some tests'''
        t1=time.time()
        a = ArrayOfHexagons()
        a.setRadius(25)
        a.addHexagon(0, 0)
        a.populate(6)

        #print a.hexagon(1, 1).distanceFrom(0, 0)
        #print a.hexagon(-2, 0).distanceFrom(0, 0)

        h = Shape()
        h.loadFromFile('sampleTiles/hexagon.tile')

        b = Shape()
        b.loadFromFile('sampleTiles/smallBend.tile')

        s = Shape()
        s.loadFromFile('sampleTiles/simple.tile')

        shapes = ShapeManager(h, b, s)

        #for i in shapes:
        #    print i

        #print shapes

        #a.hexagon(-1,-1).addShape(h)
        a.hexagon(1,1).addShape(h)
        a.hexagon(0,0).addShape(s)
        #a.hexagon(-2,0).addShape(b)

        a.hexagon(0,0).shape().rotate(4)

        #a.printArray()

        svg = SvgWriter()
        svg.offset(400,400)
        svg.rotate(0)
        for coordinates in a:
            svg.addHexagon(a.hexagon(coordinates[0], coordinates[1]))
        svg.write('hexagons.svg')

        #print shape 
        #shape.rotate(6)
        #print shape

        #sr = ShapeFitter(('a', '-', '-', '-', '-', '-'), ('+', '+', '+', 'A', '+', '+'))
        sr = ShapeFitter(a.hexagon(0,0).shape().sides(), a.gapEdges(0, 0))
        print 'need to rotate', sr.fit(), 'times'

        #print a.gapEdges(0, 0)
        t2=time.time()
        print 'time taken', t2-t1
        #for i in range(20):
        #    a.populate(1)
        #    print len(a), i
        
        
    def shapePoints(self):
        a = ArrayOfHexagons()
        a.setRadius(40)
        a.addHexagon(0, 0)
        a.populate(2)

        h = Shape()
        h.loadFromFile('sampleTiles/hexagon.tile')

        b = Shape()
        b.loadFromFile('sampleTiles/smallBend.tile')

        s = Shape()
        s.loadFromFile('sampleTiles/simple.tile')
        
        t = Shape()
        t.loadFromFile('sampleTiles/triangle.tile')
        
        c = Shape()
        c.loadFromFile('sampleTiles/cross.tile')
        
        p = Shape()
        p.loadFromFile('sampleTiles/prang.tile')
        
        ss = Shape()
        ss.loadFromFile('sampleTiles/singleSide.tile')

        shapes = ShapeManager(h, b, s)
        a.hexagon(-2,0).addShape(h)
        a.hexagon(0,0).addShape(b)
        #a.hexagon(0,0).shape().rotate(5)
        a.hexagon(-1,-1).addShape(b)
        a.hexagon(-1,-1).shape().rotate(3)
        a.hexagon(2,0).addShape(h)
        a.hexagon(1,1).addShape(c)
        a.hexagon(4,0).addShape(p)
        a.hexagon(1,-1).addShape(p)
        a.hexagon(1,-1).shape().rotate(5)
        a.hexagon(-1,1).addShape(ss)
        
        svg = SvgWriter()
        svg.offset(200,200)
        svg.rotate(0)
        for coordinates in a:
            svg.addHexagon(a.hexagon(coordinates[0], coordinates[1]))
        svg.write('hexagons.svg')
        
        print 'Done'
        
    def illustrateProblem(self):
        a = ArrayOfHexagons()
        a.setRadius(40)
        a.addHexagon(0, 0)
        a.populate(6)
        
        h = Shape()
        h.loadFromFile('sampleTiles/hexagon.tile')

        b = Shape()
        b.loadFromFile('sampleTiles/smallBend.tile')

        s = Shape()
        s.loadFromFile('sampleTiles/simple.tile')
        
        t = Shape()
        t.loadFromFile('sampleTiles/triangle.tile')
        
        c = Shape()
        c.loadFromFile('sampleTiles/cross.tile')
        
        p = Shape()
        p.loadFromFile('sampleTiles/prang.tile')
        
        ss = Shape()
        ss.loadFromFile('sampleTiles/singleSide.tile')
        
        a.hexagon(-12,0).addShape(h)
        a.hexagon(-8,0).addShape(b)
        a.hexagon(-4,0).addShape(s)
        a.hexagon(0,0).addShape(t)
        a.hexagon(4,0).addShape(c)
        a.hexagon(8,0).addShape(p)
        a.hexagon(12,0).addShape(ss)
        svg = SvgWriter()
        svg.offset(400,400)
        for coordinates in a:
            svg.addHexagon(a.hexagon(coordinates[0], coordinates[1]))
        svg.write('hexagons.svg')
        
        
        
if __name__ == '__main__':
    Test().shapePoints()
