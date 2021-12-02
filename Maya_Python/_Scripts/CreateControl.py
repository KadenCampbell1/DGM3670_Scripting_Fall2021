import maya.cmds as cmds
from CreateNullParent import create_null_parent
from ColorPicker import color_picker


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
