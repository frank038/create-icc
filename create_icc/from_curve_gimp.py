#!/usr/bin/env python3

# V. 0.1

import sys,os

# number of decimals
_precision = 4

if len(sys.argv) < 3 or sys.argv[1] in ["--help","-h"]:
    print('Usage: from_curve_gimp.py "file_name " "curve_name"')
    sys.exit()

_file_name = sys.argv[1]
if not os.path.exists(_file_name):
    print("File not found: ", _file_name)
    sys.exit()

_curve = sys.argv[2]
_n = 20+len(_curve)

# same values for all channels
_is_value = 0
if len(sys.argv) == 4:
    if sys.argv[3] == "value":
        _is_value = 1

my_curve = []
_found = 0
try:
    with open(_file_name, "r") as ff:
        for _lline in ff:
            if _lline[0:18] == '(GimpCurvesConfig ':
                if _lline[18:_n] == '"'+_curve+'"':
                    my_curve.append(_lline.strip("\n"))
                    _found = 1
            #
            if _found == 1:
                my_curve.append(_lline)
except Exception as E:
    print("Error: ", str(E))
    sys.exit()

if my_curve == []:
    print("Not found: ", _curve)
    sys.exit()
else:
    if _is_value:
        _value = my_curve[10][0:-3].lstrip(" ").rstrip("\n").rstrip(" ")
        #
        try:
            with open("data_array", "w") as ff:
                ff.write(" ".join(_value[13:].split(" "))+"\n")
                ff.write(" ".join(_value[13:].split(" "))+"\n")
                ff.write(" ".join(_value[13:].split(" "))+"\n")
        except Exception as E:
            print("Error: ", str(E))
            sys.exit()
    else:
        _red = my_curve[17][0:-3].lstrip(" ").rstrip("\n").rstrip(" ")
        _green = my_curve[24][0:-3].lstrip(" ").rstrip("\n").rstrip(" ")
        _blue = my_curve[31][0:-3].lstrip(" ").rstrip("\n").rstrip(" ")
        #
        try:
            with open("data_array", "w") as ff:
                ff.write(" ".join(_red[13:].split(" "))+"\n")
                ff.write(" ".join(_green[13:].split(" "))+"\n")
                ff.write(" ".join(_blue[13:].split(" "))+"\n")
        except Exception as E:
            print("Error: ", str(E))
            sys.exit()
    #
    print("Finished.")
