#!/usr/bin/python

# Verbs extract conjug from GT input file
# Output conjug to tab delimeted db file
# Name: dedur@rumantsch.ch
# Date: 10.01.2016

def output_rec(nr, r, f):
    f.write('%s\t' % nr)
    tri = r[0] # infinitiv
    f.write('%s' % (tri[0]))
    for i in range(1,37):
	    tri = r[i]
	    if len(tri) != 3:
	    	print("***error*** ", r[i])
	    else:
	    	f.write('\t%s\t%s%s' % (tri[0],tri[1],tri[2]))
    tri = r[37] # pp_msg 
    f.write('\t%s%s' % (tri[1],tri[2]))
    tri = r[38] # pp_mpl
    f.write('\t%s%s' % (tri[1],tri[2]))
    tri = r[39] # pp_fsg
    f.write('\t%s%s' % (tri[1],tri[2]))
    tri = r[40] # pp_fpl
    f.write('\t%s%s' % (tri[1],tri[2]))
    tri = r[41] # aux_prf
    f.write('\t%s' % tri[1])
    tri = r[42] # gerundi
    f.write('\t%s\t%s%s\n' % (tri[0],tri[1],tri[2]))


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
            if not empty_lns.__contains__(ln_nr): # use only lines containing infos
                conjug.append(ln.split('\t'))
        else: # last line of conjugation reached
            output_rec(cnt, conjug, f_out)
            ln_nr = 0
            conjug = []
            cnt += 1
    f_in.close()
    f_out.close()
