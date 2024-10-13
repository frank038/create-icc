#!/usr/bin/env python3

# V. 0.1

import gi
gi.require_version('Colord', '1.0')
from gi.repository import Colord
from gi.repository import Gio
import os, sys

_file_name = "myicc.icc"

bb = Colord.Icc.new()
bb.create_default ()

# colorspace RGB
bb.set_colorspace(6)
# display kind
bb.set_kind(2)
# file name
bb.set_filename(_file_name)
#
# bb.set_version(2.1)

bb2 = Colord.Icc.new()
bb2.create_default ()

_arr = []
try:
    with open("data_array", "r") as ff:
        for lline in ff:
            _ll = [float(n) for n in lline.strip("\n").split(" ")]
            _arr.append(_ll)
except Exception as E:
    print("Error: ", str(E))
    sys.exit()

arr2 = []

_len_data = len(_arr[0])
if not len(_arr[0]) == len(_arr[1]) == len(_arr[2]):
    print("Data lenght error!")
    sys.exit()

for i in range(0,_len_data-1):
    ec = Colord.ColorRGB.new()
    ec.set(_arr[0][i],_arr[1][i],_arr[2][i])
    arr2.append(ec)

bb2.set_vcgt(arr2)
_curr_path = os.getcwd()
try:
    file2 = Gio.File.new_for_path(os.path.join(_curr_path, _file_name))
    bb2.save_file(file2, 0, None)
except Exception as E:
    print("Error: ", str(E))
    sys.exit()

print("Created.")
