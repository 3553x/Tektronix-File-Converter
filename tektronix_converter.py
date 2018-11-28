#!/usr/bin/python3
import struct, sys

CURVE_START = b":CURVE #"
PREAMBLE_START = b":WFMPRE:"


def convert(data):

  if(CURVE_START not in data):
    raise Exception("No curve data found")
  if(PREAMBLE_START not in data):
    raise Exception("No preamble found")

  preamble_start = data.index(PREAMBLE_START)
  preamble_end = data.index(CURVE_START)

  curve_start = preamble_end
  #We assume data follow preamble

  preamble = data[preamble_start + len(PREAMBLE_START):preamble_end]
  curve = data[curve_start + len(CURVE_START):]

  preamble_fields = {field[:field.index(b" ")] : field[field.index(b" ") + 1:] for field in preamble.split(b";")[:-1]}
  

  x_factor = float(preamble_fields[b"XINCR"])
  x_zero = float(preamble_fields[b"XZERO"])

  y_factor = float(preamble_fields[b"YMULT"])
  y_offset = float(preamble_fields[b"YOFF"])
  y_zero = float(preamble_fields[b"YZERO"])
  
  size_len = int(chr(curve[0]))
  size = int(curve[1: 1+size_len])

  csv = ""
  
  x = x_zero
  
  for sample in struct.iter_unpack(">h", curve[size_len + 1: size_len + 1 + size]):
    csv += "%g,%g\n" % (x, (sample[0] - y_offset) * y_factor + y_zero)
    x += x_factor

  return csv


if(__name__ == "__main__"):
  if(len(sys.argv) != 2):
    raise Exception("Please pass a filename as input")

  with open(sys.argv[1], 'rb') as f:
    data = f.read()
  print(convert(data))
