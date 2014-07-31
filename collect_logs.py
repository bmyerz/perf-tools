import glob
import subprocess
import re
import csv
import sys

burns = 0
if len(sys.argv) > 1:
    burns = int(sys.argv[1])

if filepat==0:
    fnpat = re.compile(r'([a-zA-Z]+[0-9]+).([a-zA-Z]+[0-9]+)')

with open ('logs.csv', 'w') as csvout:
    cw = csv.writer(csvout, delimiter=',')

    with open('header', 'r') as f:
        l = f.readline()
        cols = l.split()
        cols.append("host")
        cw.writerow(cols)

    for logfile in glob.glob("*.log"):
        with open(logfile, 'r') as f:
            lc = 0
            for l in f:
                lc+=1
                if lc <= burns: continue

                cols = l.split()
                hostname = fnpat.match(logfile).group(1)
                cols.append(hostname)
                cw.writerow(cols)

