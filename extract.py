#!/usr/bin/python

# Verbs extract conjug from GT input file
# Output conjug to tab delimeted db file
# Name: dedur@rumantsch.ch
# Date: 09.01.2016

from string import *
import sys

def output_rec(nr, r, f):
    f.write('%s\t' % nr)
    tri = r[0]
    f.write('%s' % (tri[0]))
    for i in range(1,37):
	    tri = r[i]
	    if len(tri) != 3:
	    	print("***error*** ", r[i])
	    else:
	    	f.write('\t%s\t%s\t%s' % (tri[0],tri[1],tri[2]))
    tri = r[37]
    f.write('\t%s\t%s' % (tri[1],tri[2]))
    tri = r[38]
    f.write('\t%s\t%s' % (tri[1],tri[2]))
    tri = r[39]
    f.write('\t%s\t%s' % (tri[1],tri[2]))
    tri = r[40]
    f.write('\t%s\t%s' % (tri[1],tri[2]))
    tri = r[41]
    f.write('\t%s' % tri[1])
    tri = r[42]
    f.write('\t%s\t%s\t%s\n' % (tri[0],tri[1],tri[2]))


if __name__ == '__main__':
    f_in=open("../data/verbs_va.txt", mode='r', encoding="utf-8")
    lines=f_in.readlines()
    print("  ", len(lines), "lines read.")
    f_out = open('verbs_va.txt', 'w', encoding="utf-8")

    empty_lns = set([2, 9, 16, 23, 30, 37, 44, 49, 51])
    ln_nr = 0
    conjug = []
    cnt = 0
    for line in lines:
        ln_nr += 1
        if ln_nr < 53:

            ln = line.rstrip('\n')
            # if not((ln_nr==2) or (ln_nr==9) or (ln_nr==16) or (ln_nr==23) or (ln_nr==30) or (ln_nr==37) or (ln_nr==44) or (ln_nr==49) or (ln_nr==51)):
            if not empty_lns.__contains__(ln_nr):
                conjug.append(ln.split('\t'))
        else:
            # last line of conjugation reached
            output_rec(cnt, conjug, f_out)
            ln_nr = 0
            conjug = []
            cnt += 1
    f_in.close()
    f_out.close()
