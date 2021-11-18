# Control Creation creates a circle at a location and orientation based upon selection.
#
# Function receives a string "Red" or int and changes the circle's color to indicated color.
# importing a copy of CreateNullParent from 'C:\Users\Xmen9\Documents\maya\scripts'
#
# Functions:
# color_picker(sels, color) -- Overrides the color of selected shape nodes
# create_null_parent(sels) -- creates a null object with selected object(s) orientation, location, and name
# create_control(color) -- Creates circle control with selected object(s) orientation, location, and name


import maya.cmds as cmds


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
