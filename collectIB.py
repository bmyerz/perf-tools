import subprocess
import time
import re
import sys

RX_bytes_pat = re.compile(r'RX bytes:(\d+)')
TX_bytes_pat = re.compile(r'TX bytes:(\d+)')

RX_packets_pat = re.compile(r'RX packets:(\d+)')
TX_packets_pat = re.compile(r'TX packets:(\d+)')

class Sampler:

  def __get_time__(self):
    return time.time()

  def __get_info__(self):
    ib_raw_string = subprocess.check_output('ifconfig 2>&1 2>/dev/null | grep -A7 ib0', shell=True)
    return ib_raw_string

  def __get_bytes__(self, ib_info_str):
    RX_bytes = int(RX_bytes_pat.search(ib_info_str).group(1))
    TX_bytes = int(TX_bytes_pat.search(ib_info_str).group(1))

    return RX_bytes, TX_bytes

  def __get_packets__(self, ib_info_str):
    RX_bytes = int(RX_packets_pat.search(ib_info_str).group(1))
    TX_bytes = int(TX_packets_pat.search(ib_info_str).group(1))

    return RX_bytes, TX_bytes

  def __init__(self):
    self.initial_time = self.__get_time__()
    ib_info_str = self.__get_info__()
    self.initial_RX_bytes, self.initial_TX_bytes = self.__get_bytes__(ib_info_str)
    self.initial_RX_packets, self.initial_TX_packets = self.__get_packets__(ib_info_str)
 
  def printHeader(self):
    print "timestamp", "RX_packets", "RX_bytes", "TX_packets", "TX_bytes"

  def printSample(self):
    timestamp = self.__get_time__() - self.initial_time

    ib_info_str = self.__get_info__()

    RX_bytes_now, TX_bytes_now = self.__get_bytes__(ib_info_str)
    RX_bytes = RX_bytes_now - self.initial_RX_bytes
    TX_bytes = TX_bytes_now - self.initial_TX_bytes
    
    RX_packets_now, TX_packets_now = self.__get_packets__(ib_info_str)
    RX_packets = RX_packets_now - self.initial_RX_packets
    TX_packets = TX_packets_now - self.initial_TX_packets

    print timestamp, RX_packets, RX_bytes, TX_packets, TX_bytes


if __name__ == '__main__':
  period = 1.0

  if len(sys.argv) > 1:
    period = float(sys.argv[1])

  s = Sampler()

  s.printHeader()

  while True:
    s.printSample()
    time.sleep(period)


