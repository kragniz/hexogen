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

import random

class ShapeManager(object):
    '''Manages Shapes'''
    
    # a bit pointless really, because it's just a list you can't remove items from
    def __init__(self, *args):
        '''Create a ShapeManager object, using all Shape objects given as arguments'''
        self._shapes = list(args)
        
        
    def __str__(self):
        return '(' + ', '.join([str(s) for s in self._shapes]) + ')'
    
    
    def __iter__(self):
        return iter(self._shapes)
    
    
    def __len__(self):
        return len(self._shapes)
    
    
    def add(self, shape):
        '''Add a shape to this manager'''
        self._shapes += [shape]
    
    
    def randomShape(self):
        '''Return a random shape from the available shapes'''
        return random.choice(self._shapes)
    
    
    def shapes(self):
        '''Return all the available shapes'''
        return tuple(self._shapes)
