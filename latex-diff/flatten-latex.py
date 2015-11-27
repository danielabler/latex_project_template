# -*- coding: utf-8 -*-
#
#
# flatten-latex.py
#
# purpose:  Make one big tex file to use with latexdiff
# author:   Filipe P. A. Fernandes
# e-mail:   ocefpaf@gmail
# web:      http://ocefpaf.tiddlyspot.com/
# created:  11-Jun-2012
# modified: Wed 19 Sep 2012 12:06:46 PM BRT
#
# obs:
# http://dropbearcode.blogspot.com/2011/09/multiple-file-latex-diff.html

import os
import re
import sys


inputPattern = re.compile('\\input{(.*)}')


def flattenLatex(rootFilename):
    dirpath, filename = os.path.split(rootFilename)
    with open(rootFilename, 'r') as fh:
        for line in fh:
            match = inputPattern.search(line)
            if match:
                newFile = match.group(1)
                if line.startswith('%'):
                    sys.stdout.write(line)
                elif newFile.endswith('sty'):
                    sys.stdout.write(line)                    
                else:
                    if not newFile.endswith('tex'):
                        newFile += '.tex'
                    flattenLatex(os.path.join(dirpath, newFile))
            else:
                sys.stdout.write(line)

if __name__ == "__main__":
    flattenLatex(sys.argv[1])

"""
Merge multiple files into the old and current versions of the document
flatten-latex ${DIFFTREE}/thesis.tex > old.tex
flatten-latex ${WORKINGTREE}/thesis.tex > cur.tex

# Produce the marked up document.
latexdiff old.tex cur.tex > tmp.tex

# Fix line ending problem introduced by latexdiff.
sed 's/^M//' tmp.tex > diff.tex
"""

