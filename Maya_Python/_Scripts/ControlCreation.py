def color_picker(sels, color):
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
    pass


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
    pass
