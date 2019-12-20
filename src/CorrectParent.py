#!/usr/bin/env python

import sys
import re

readsFile = sys.argv[1]

#input: annotation column from gff3 file (9th column)
#output: corrected annotation column from gff3 file

out= open("CorParent.out","w+")
f= open(readsFile,"r+")
for line in f:
        line2 = line.rstrip('\n').split('\t')
        if "exon" in line2[0]:
                split=list(filter(None,re.split('(:)|(-)|(;)',line2[0])))
                split[10] = split[2]
                out.write("".join(split) + "\n")
        else:
                out.write(line2[0] + "\n")                      
out.close()
