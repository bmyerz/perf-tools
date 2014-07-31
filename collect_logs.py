import glob
import subprocess
import re
import csv

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
            for l in f:
                cols = l.split()
                hostname = fnpat.match(logfile).group(1)
                cols.append(hostname)
                cw.writerow(cols)

