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

from ProgramData import VERSION, NAME

class SvgWriter(object):
    '''Create and save svg files'''
    
    def __init__(self):
        self.header = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created by {programName} {programVersion} -->
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   width="1000px"
   height="1000px">
  <metadata>
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillINAMEmage" />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs>
    <style type="text/css"><![CDATA[
      path.white {{
        fill: {white[fill]};
        stroke: {white[stroke]};
        stroke-width: {white[stroke-width]}
      }}

      path.shape-removed {{
        fill: {shapeRemoved[fill]};
        stroke: {shapeRemoved[stroke]};
        stroke-width: {shapeRemoved[stroke-width]};
      }}
      
      path.shape-new {{
        fill: {shapeNew[fill]};
        stroke: {shapeNew[stroke]};
        stroke-width: {shapeNew[stroke-width]};
      }}    

      path.blue {{
        fill: {blue[fill]};
        stroke: {blue[stroke]};
        stroke-width: {blue[stroke-width]};
      }}      
      
      path.shape {{
        fill: red;
        stroke: white;
        stroke-width: 0.5;
      }}      
      
      text {{
        font-family: Monospace;
        fill: black;
        text-anchor: middle;
      }}
      
    ]]></style>
  </defs>
  <g transform="translate({offsetX}, {offsetY}) rotate({angle})">
    <g id="MainLayer">
'''

        self.footer = '''      </g>
  </g>
</svg>'''
        
        self.hexagonXml = '''        <path id="Hexagon {pathNumber}" class= "{hexagonType}" d="{points}"/>
'''
        self.tileXml = '''        <g transform="translate({x:0.2f}, {y:0.2f})">
          <path id="{tileName}"
                class= "shape"
                d="{points}"/>
          <text font-size="3">
            {tileName}
          </text>
        </g>
'''
        self.hexagons = []
        self.tiles = []
        
        self._offsetX = 0
        self._offsetY = 0
        self._rotateAngle = 0
        
        #style variables        
        self._white = {'fill': 'white', 'stroke': 'black', 'stroke-width': '0.5'}
        self._blue = {'fill': 'lightblue', 'stroke': 'black', 'stroke-width': '0.5'}
        self._shapeRemoved = {'fill': '#FF5050', 'stroke': 'black', 'stroke-width': '0.5'}
        self._shapeNew = {'fill': 'greenyellow', 'stroke': 'black', 'stroke-width': '0.5'}
        
        
    def offset(self, x, y):
        '''Set the amount of offsetting required'''
        self._offsetX = x
        self._offsetY = y
        
        
    def rotate(self, angle):
        '''Rotate the image by a number of degrees'''
        self._rotateAngle = angle
        
    
    def _dp(self, f):
        '''Round the float f to 2 d.p. and return the string of this value'''
        return format(f, '.2f')
    
    
    def _point(self, p):
        '''Return a nice string rep. of a two value tuple, rounded to 2 d.p.
        (324.344434, 23.536535) => "324.34, 23.54"'''
        return str( (self._dp(p[0]), self._dp(p[1])) )[1:-1].replace("'", '')


    def addHexagon(self, hexagon):
        '''Add a hexagon to the SVG file'''
        if hexagon.hasShape():
            hexagonType = 'blue'
        else:
            hexagonType = 'white'
            
        point = self._point
        if hexagon.hasShape():
            s= ''
            firstSide = -1
            plotEndNext = 0
            numberOfSides = len(hexagon.shape())
            sidesPlotted = 0
            lastPlottedSide = None
            shapePoints, shapeControlPoints = hexagon.shape().getVertices()
            for i in range(6):
                if shapePoints.has_key(i):
                    sidesPlotted += 1
                    if sidesPlotted+1 == numberOfSides:
                            #next side must be the last one
                            plotEndNext = 1
                            
                    if not (firstSide + 1):
                        #must be the first side
                        s += 'M ' + point(shapePoints[i][0]) + ' L '
                        s += point(shapePoints[i][1])
                        
                        firstSide = i
                        lastPlottedSide = i
                        if plotEndNext == 1: plotEndNext = 2
                        print 'face', i, 'is at the start'
                        
                    else:
                        if plotEndNext == 2:
                            print 'face', i, 'is at the end'
                            s += ' C ' + point(shapeControlPoints[i][1]) + ' '
                            s += point(shapeControlPoints[firstSide][0]) + ' '
                            s += point(shapePoints[firstSide][0]) + ' z '
                        else:
                            #side must be 'normal' (not at the beginning or end)
                            print 'face', i, 'is in the middle'
                            
                            s += ' C ' +  point(shapeControlPoints[lastPlottedSide][1] ) + ' '
                            s += point(shapeControlPoints[i][0]) + ' '
                            s += point(shapePoints[i][0]) + ' L '
                            s += point(shapePoints[i][1])
                            
                            lastPlottedSide = i
                            if plotEndNext == 1: plotEndNext = 2
                    
            tilePoints = s #do this to keep the above (more) readable
            print tilePoints
            x, y = hexagon.cartesianCoordinates()
            self.tiles += [self.tileXml.format(points=tilePoints, x=x, y=y,
                                               tileName=hexagon.shape().name())]
            
        # round them floats! (2 d.p.)
        hexagonPoints = tuple( [ str( (format(p[0], '.2f'), format(p[1], '.2f')) )[1:-1] for p in hexagon.getVertices() ] ) # Convert a tuple containing 6 
                                                                       # two-part tuples into a list 
                                                                       # containing pairs of coordinates
                                                                       # in string form (like '234, 132'),
                                                                       # rounded to 2 d.p.    
        #format them points!
        hexagonShapePonts = 'M {0[0]} L {0[1]} L {0[2]} L {0[3]} L {0[4]} L {0[5]} z'.format(hexagonPoints).replace("'", '')
        #add all the data to the block of shape xml, then add it to the list of hexagons 
        self.hexagons += [self.hexagonXml.format(
                        points = hexagonShapePonts,
                        pathNumber = hexagon.hexagonalCoordinates(),
                        hexagonType = hexagonType)]
                        
                        
    def svgDocument(self):
        '''Return the entire SVG document as a string'''
        return self.header.format(offsetX = self._offsetX,
                                  offsetY = self._offsetY,
                                  angle = self._rotateAngle,
                                  
                                  #program info constants
                                  programName = NAME,
                                  programVersion = VERSION,
                                  
                                  #style stuff
                                  white = self._white,
                                  shapeRemoved = self._shapeRemoved,
                                  shapeNew = self._shapeNew,
                                  blue = self._blue) + \
                                  ''.join(self.hexagons) + \
                                  ''.join(self.tiles) + \
                                  self.footer
        
        
    def write(self, filename):
        '''Write the SVG file to the path specified'''
        svg = self.svgDocument()#self.header + ''.join(self.hexagons) + self.footer
        svgFile = open(filename, 'w')
        svgFile.writelines(svg)
        svgFile.close()
