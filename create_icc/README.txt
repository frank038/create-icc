Launch the program 
create_icc.py
to create the file myicc.icc in this folder
using the file data_array. To be used with monitors.

Required:
python3
Colord
Gio

The file data_array can be created in all ways you may want.
Each line in it is an arbitrary amount of points of a curve, 
one line for each colour, red, green and blue, in this order.
Each line must be terminated by the newline.
The number of points of each colour curve must be large enough (256), 
but should work with a less amount of points, at least 21.

The program from_curve_gimp.py uses the colour curve created with Gimp.
Once the curve has been created, save it with the name "whateveryouwant".
Copy the file GimpCurvesConfig.settings from the directory 
HOME/.config/GIMP/2.10/filters
in this folder and launch 
from_curve_gimp.py GimpCurvesConfig.settings "whateveryouwant"
to create the file data_array, if the curve has been created 
for each colour channel.
For the only Value channel, use the following command:
from_curve_gimp.py GimpCurvesConfig.settings "whateveryouwant" value
and in this case the same points will be used for all colours.
