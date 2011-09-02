#!/usr/bin/env python
# -*- coding: utf-8 -*-
# see http://docs.python.org/distutils/

from distutils.core import setup
from Hexogen import ProgramData
setup(name = ProgramData.NAME,
      version = ProgramData.VERSION,
      description = 'A small program used to generate images from a set of tiles',
      long_description = '''The objective is to find a connected structure
composed only of pieces from a specified set. Pieces are based on squares or
hexagons with edges of various types. An edge of a certain type may only abut
edges of some other certain type. Some edges of a piece may be “empty”, and
these edges do not need to abut another piece. All other edges must abut an
appropriate opposite edge. Pieces may be rotated, but not flipped.''',
      author = 'Louis Taylor',
      author_email = 'kragniz@gmail.com',
      #url = 'nothing yet',
      license = 'GPL v3 or later',
      packages = ['hexogen'],
      scripts = ['hexogen'],
      platform = 'Any'
      #data_files = [
      #  ('nothing yet', ['nothing yet']),
      #  ]
      )
