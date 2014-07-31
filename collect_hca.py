# replacement for collectl when I'm not allowed to use it

import subprocess
import socket
import time
import sys

samples = -1
if len(sys.argv) > 1:
    samples = int(sys.argv[1])
logfilen = socket.gethostname()+'.log'
if len(sys.argv) > 2:
    logfilen = sys.argv[2]
sc = 0

ctr_path = '/sys/class/infiniband/mlx4_0/ports/1/counters/'
counters = ['port_rcv_data', 'port_rcv_packets', 'port_xmit_data', 'port_xmit_packets', 'port_xmit_discards']

interval = 1
mark_resets = False

def get_counters():
    return [int(subprocess.check_output(['cat', ctr_path+ctr_name])) for ctr_name in counters]

with open(logfilen, 'w') as fout:
    fout.write(" ".join(['time']+counters) + '\n')

    last = get_counters()
    last_time = time.time()

    while(samples==-1 or sc < samples):
        sc+=1
        current = get_counters()
        current_time = time.time()

        # take the delta and account for external collectl resets
        delta = [float(c - l if c-l>=0 else c)/(current_time-last_time) for (c,l) in zip(current, last)]
        
        if mark_resets:
            reset_occurred = any([c-l < 0 for (c,l) in zip(current,last)])
            if reset_occurred: print "RESET"

        outputs = [current_time] + delta

        fout.write(" ".join([str(x) for x in outputs]) + '\n')
        fout.flush() # I want it now!
        time.sleep(1)

        last = current
        last_time = current_time


