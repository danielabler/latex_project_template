#! /usr/bin/env python2
# -*- coding: iso-8859-1 -*-

# Copyright (c) 2012, Paul Hiemstra <paul@numbertheory.nl>, 
# Ronald van Haren <ronald@archlinux.org>.
# This file is part of scm-latexdiff.

# scm-latexdiff is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the Licence, or
# (at your option) any later version.

# scm-latexdiff is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os
from liblatexdiff import *

def scm_latexdiff(argv):
  ''' Calculate diff pdf between two latex files, either in hg, git, or a local file. '''
  showHelp(argv)
  git = gitOrHg()
  old_fileloc, new_fileloc = processCmdlineArgs(argv, git)
  old_texfile, new_texfile = dumpRepositoryVersion2tmp(old_fileloc, new_fileloc, git)
  createDiffTex(old_texfile, new_texfile, swaplocal = "local" in old_fileloc and not "local" in new_fileloc)
  os.chdir(compileFolder)
  removeTrailingNewlines(diffFile)
  compileDiffPdf(diffFile, diffFileLog)
  os.chdir('..')
  moveFiles()
  cleanAll()
  #cleanAllNonePDF()

  

  
if __name__ == "__main__":
  scm_latexdiff(sys.argv)

