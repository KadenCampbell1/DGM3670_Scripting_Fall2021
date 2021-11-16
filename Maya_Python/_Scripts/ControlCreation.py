"""Control Creation creates a circle at a location and orientation based upon selection.

Function receives a string "Red" or int and changes the circle's color to indicated color.
importing a copy of CreateNullParent from 'C:\Users\Xmen9\Documents\maya\scripts'

Functions:
color_picker(sels, color) -- Overrides the color of selected shape nodes
create_control(color) -- Creates circle control with selected object(s) orientation, location, and name
"""

import maya.cmds as cmds
from CreateNullParent import create_null_parent


def color_picker(sels=None, color="Red"):
    """Overrides the color of selected shape nodes

    Notable Colors:
    0 -- None
    1 -- Black
    2 -- Grey
    5 -- Blue
    13 -- Red
    17 -- Yellow
    23 -- Green

    arguments:
    sels -- type list
    color -- type string or int
    """

    if not sels:
        # sets sels to selection
        # allows color_picker() to run independently
        sels = cmds.ls(sl=True)

    if isinstance(color, str):
        # Determines if color is a string and chooses int corresponding to that color.
        # Otherwise function uses raw color data.

        if color == "None":
            color = 0
        if color == "Black":
            color = 1
        if color == "Grey":
            color = 2
        if color == "Blue":
            color = 5
        if color == "Red":
            color = 13
        if color == "Yellow":
            color = 17
        if color == "Green":
            color = 23

    for sel in sels:
        # Runs through each selection enabling color override and setting color from color input
        sel = cmds.listRelatives(sel, children=True)
        cmds.setAttr(f"{sel[0]}.overrideEnabled", 1)
        cmds.setAttr(f"{sel[0]}.overrideColor", color)


def create_control(color):
    """Creates circle control with selected object(s) orientation

    Control created at each selected objects position and orientation.
    Control will then be renamed with suffix _Ctrl. Renaming will replace
    object's existing suffix (i.e. Head_Geo -> Head_Ctrl). If there is no
    selection a default name ending in _Ctrl will be used.
    create_control() will call color_picker().

    arguments:
    color -- type string or int
    """

    sels = cmds.ls(sl=True)
    name = None
    location = None
    temp_lyst = []
    parent_lyst = []

    if not sels:
        # with no selection a control will be created at the origin named Root_Ctrl
        name = "Root_Ctrl"
        location = (0, 0, 0)
        curve = cmds.circle(c=location, n=name, normal=(0, 1, 0))
        temp_lyst.append(curve)
        parent_lyst.append(curve[0])

    for sel in sels:
        # runs through sels appending _Ctrl to the name of sel
        # _Ctrl will replace existing suffix
        name = sel.rpartition("_")
        if not name[0]:
            name = f"{name[-1]}_Ctrl"
        else:
            name = f"{name[0]}_Ctrl"

        # queries location and orientation of each sel assigning values to variables name respectively
        location = cmds.xform(sel, q=True, translation=True, worldSpace=True)
        orientation = cmds.xform(sel, q=True, rotation=True, worldSpace=True)

        # creates curve at location with proper name
        curve = cmds.circle(n=name)
        # places pivot at center point then rotates curve with orientation values
        cmds.xform(curve, centerPivots=True)
        cmds.xform(curve, rotation=orientation)
        cmds.xform(curve, translation=location)

        # appends curve to a temp_lyst for use in color_picker()
        temp_lyst.append(curve)
        # appends curve to a parent_lyst for use in create_null_parent()
        parent_lyst.append(curve[0])

    # calls color_picker with input color
    color_picker(temp_lyst, color)
    # calls create_null_parent with parent_lyst
    create_null_parent(parent_lyst)


create_control(color="Yellow")
