# """Control Creation creates a circle at a location and orientation based upon selection.
#
# Function receives a string "Red" or int and changes the circle's color to indicated color.
# importing a copy of CreateNullParent from 'C:\Users\Xmen9\Documents\maya\scripts'
#
# Functions:
# color_picker(sels, color) -- Overrides the color of selected shape nodes
# create_null_parent(sels) -- creates a null object with selected object(s) orientation, location, and name
# create_control(color) -- Creates circle control with selected object(s) orientation, location, and name
# """

import maya.cmds as cmds
# from CreateNullParent import create_null_parent


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


def create_null_parent(sels=None):
    """creates a null object with selected object(s) orientation, location, and name

    Null object created at each selected objects position and orientation.
    Null object will then be renamed with appended suffix _Grp. If there is no
    selection a default name ending in _Grp will be used.

    arguments:
    sels -- type list
    """

    if not sels:
        # sets sels to selection
        # allows create_null_parent() to run independently
        sels = cmds.ls(sl=True)

    name = None
    location = None
    temp_lyst = []

    if not sels:
        # with no selection a null object will be created at the origin named Root_Grp
        name = "Root_Grp"
        null_object = cmds.group(empty=True, name=name)
        temp_lyst.append(null_object)

    for sel in sels:
        # runs through sels appending _Grp to the name of sel
        name = f"{sel}_Grp"

        # queries location and orientation of each sel assigning values to variables name respectively
        location = cmds.xform(sel, q=True, translation=True, worldSpace=True)
        orientation = cmds.xform(sel, q=True, rotation=True, worldSpace=True)

        # creates null object with proper name
        null_object = cmds.group(empty=True, name=name)
        # rotates and transforms null object with orientation and location values
        cmds.xform(null_object, centerPivots=True)
        cmds.xform(null_object, rotation=orientation)
        cmds.xform(null_object, translation=location)

        # places sel in child relation to null object
        cmds.parent(sel, null_object)


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


def create_window():
    window = cmds.window(title="Control Creation", widthHeight=(500, 500))
    m_column = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=500, parent=window)
    cmds.text(label='', font="boldLabelFont", align='center', parent=m_column)
    cmds.text(label='Color Picker', font="boldLabelFont", align='center', parent=m_column)
    color_column = cmds.rowColumnLayout(numberOfRows=4, parent=m_column)
    cmds.button(label='None', command=lambda x: color_picker(0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(1), backgroundColor=(0,0,0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(2), backgroundColor=(0,0,0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(3), backgroundColor=(0,0,0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(4), backgroundColor=(0,0,0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(5), backgroundColor=(0,0,0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(6), backgroundColor=(0,0,0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(7), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(8), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(9), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(10), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(11), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(12), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(13), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(14), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(15), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(16), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(17), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(18), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(19), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(20), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(21), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(22), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(23), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(24), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(25), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(26), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(27), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(28), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(29), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(30), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.button(label='Black', command=lambda x: color_picker(31), backgroundColor=(0, 0, 0), parent=color_column)
    cmds.showWindow(window)


create_window()
