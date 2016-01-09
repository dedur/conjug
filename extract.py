#!/usr/bin/python
# -*- coding: utf-8 -*-

# Verbs extract conjug from GT input file
# Output conjug to tab delimeted db file
# Name: dedur@rumantsch.ch
# Date: 31.07.2015

from string import *
import sys

def output_rec(r):
    tri = r[0]
    print('%s' % (tri[0]), end="")
    for i in range(1,37):
	    tri = r[i]
	    if len(tri) != 3:
	    	print("***error*** ", r[i])
	    else:
	    	print('\t%s\t%s\t%s' % (tri[0],tri[1],tri[2]), end="")
    tri = r[37]
    print('\t%s\t%s' % (tri[1],tri[2]), end="")
    tri = r[38]
    print('\t%s\t%s' % (tri[1],tri[2]), end="")
    tri = r[39]
    print('\t%s\t%s' % (tri[1],tri[2]), end="")
    tri = r[40]
    print('\t%s\t%s' % (tri[1],tri[2]), end="")
    tri = r[41]
    print('\t%s' % tri[1], end="")
    tri = r[42]
    print('\t%s\t%s\t%s' % (tri[0],tri[1],tri[2]))


if __name__ == '__main__':
    fln=open("../data/verbs_va.txt", mode='r', encoding="utf-8")
    lines=fln.readlines()
    print("  ", len(lines), "lines read.")
    sys.stdout = open('verbs_va.txt', 'w', encoding="utf-8")

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
            print(cnt, "\t", end="")
            output_rec(conjug)
            ln_nr = 0
            conjug = []
            cnt += 1
