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
##
## 
##  TODO:
##  1. Place a randomly chosen tile in the center of the grid.
##
##  2. Make a list of empty locations in the grid with abutting non-empty
##  edges. If there are no such locations, halt. Otherwise, if there are
##  any sites where only either one or zero types of tile could be added,
##  restrict the list to just these sites. From the list, choose the
##  location closest to the center of the assemblage.
##
##  3. If there is no tile that fits at that location, or if it can be
##  determined that for any tile that might be added the assemblage
##  will become non-completable (see next section), perform
##  backtracking. That is, remove some number of tiles from the
##  assemblage in the reverse order to which they were added (see the
##  section after next).
##
##  4. Otherwise choose a tile at random from the remaining possibilities,
##  and put it at the location.
##
##  5. Go to step 2.
##
##
## **STEPS** (or 'things needed')
##  Place tile at a location.  DONE
##  Make a list of empty locations in the grid with abutting non-empty edges. TODO
##      + Make a list of all the tiles. DONE
##
##  Find the number of types of tile will fit in a site. TODO
##      + Make a list of all the tiles available. DONE
##      + Test if a tile fits in a site DONE
##
##  Choose the location closest to the centre of the assemblage from a list of sites. TODO
##
##  Backtrack. TODO
##      + Calculate how many tiles to remove. TODO
##      + Remove tile DONE
##
##  Choose a tile at random from the available tiles DONE
##
##  Create a hash table of non-completable areas TODO
##      + Create class TODO
##      + Defined by the edge of the area. Hash this and add it to the table

from Hexogen import Testing
        
if __name__ == '__main__':
    Testing.Test().shapePoints()
