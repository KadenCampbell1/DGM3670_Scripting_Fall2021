# """Sequential Renamer based upon selection order renames objects sequentially.
#
# Function receives a string "Name_##_Type" and replaces "#" with the same number of digits.
#
# Functions:
# rename(name) -- renames selected items to name in sequential order
# """

import maya.cmds as cmds


def rename(name):
    """renames selected items to name in sequential order"""
    # checks if name is str
    if not isinstance(name, str):
        raise ValueError(f"name must be type String. example: 'Name_##_NodeType'")

    name_lyst = name.split("_")

    # checks if name is has '#' signs
    char = 0
    while char < len(name_lyst):
        if name_lyst[char][0] == "#":
            break
        elif char >= len(name_lyst):
            raise SyntaxError(f"name must include '_#_'")
        char += 1

    # creates a dictionary with keys for the index locations of # and a value
    # of how many # signs were present.
    locations = {}
    char = 0
    while char < len(name_lyst):
        if name_lyst[char][0] == "#":
            digits = 0
            for i in name_lyst[char]:
                digits += 1
            locations[char] = digits
        char += 1

    # goes through sels and assigns name with sels index +1
    sels = cmds.ls(sl=True)
    for sel in range(len(sels)):
        for j in locations.keys():
            name_lyst[j] = f"{str(sel + 1).zfill(locations[j])}"

        name_seq = "_".join([str(item) for item in name_lyst])

        cmds.rename(sels[sel], name_seq)
