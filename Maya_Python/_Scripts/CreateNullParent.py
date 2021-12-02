# """Create Null Parent creates a Null at a location and orientation based upon selection and parents selection to Null.
#
# Function receives a selection list.
#
# Functions:
# create_null_parent(sels) -- creates a null object with selected object(s) orientation, location, and name
# """

import maya.cmds as cmds


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

create_null_parent()