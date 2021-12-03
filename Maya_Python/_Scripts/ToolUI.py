import importlib
import maya.cmds as cmds
import ColorPicker as cp
import CreateControl as cc
importlib.reload(cp)
importlib.reload(cc)


class ToolUI:
    def __init__(self):
        self.window = "ControlCreationUI"
        self.m_column = "MainColumn"

    def create_window(self):

        self.delete_window()

        # Main window creation with Column Layout
        self.window = cmds.window(self.window, title="Control Creation", widthHeight=(500, 500))
        self.m_column = cmds.columnLayout(self.m_column, columnAttach=('both', 5),
                                          rowSpacing=10, columnWidth=500, parent=self.window)

        self.color_picker_ui()

        self.show_window()

    def color_picker_ui(self):
        # Color Picker
        # Uses buttons to change the color of the object selected
        cmds.text(label='', font="boldLabelFont", align='center', parent=self.m_column)
        cmds.text(label='Color Picker', font="boldLabelFont", align='center', parent=self.m_column)
        color_column = cmds.gridLayout(numberOfColumns=8, parent=self.m_column,
                                       backgroundColor=(0.5, 0.5, 0.5), cellWidthHeight=(55, 25),
                                       columnsResizable=True, autoGrow=True)

        cmds.button(label='None',
                    command=lambda x: cp.color_picker(color=0),
                    parent=color_column)
        cmds.button(label='D_Red',
                    command=lambda x: cp.color_picker(color=1),
                    backgroundColor=(0.5, 0, 0),
                    parent=color_column)
        cmds.button(label='Grey',
                    command=lambda x: cp.color_picker(color=2),
                    backgroundColor=(0.7, 0.7, 0.7),
                    parent=color_column)
        cmds.button(label='D_White',
                    command=lambda x: cp.color_picker(color=3),
                    backgroundColor=(0.9, 0.9, 0.9),
                    parent=color_column)
        cmds.button(label='Red',
                    command=lambda x: cp.color_picker(color=4),
                    backgroundColor=(0.7, 0, 0),
                    parent=color_column)
        cmds.button(label='D_Blue',
                    command=lambda x: cp.color_picker(color=5),
                    backgroundColor=(0, 0, 0.5),
                    parent=color_column)
        cmds.button(label='L_Blue',
                    command=lambda x: cp.color_picker(color=6),
                    backgroundColor=(0, 0, 1),
                    parent=color_column)
        cmds.button(label='D_Green',
                    command=lambda x: cp.color_picker(color=7),
                    backgroundColor=(0, 0.5, 0),
                    parent=color_column)
        cmds.button(label='D_Grey',
                    command=lambda x: cp.color_picker(color=8),
                    backgroundColor=(0.1, 0.1, 0.1),
                    parent=color_column)
        cmds.button(label='Pink',
                    command=lambda x: cp.color_picker(color=9),
                    backgroundColor=(1, 0.5, 0.9),
                    parent=color_column)
        cmds.button(label='Orange',
                    command=lambda x: cp.color_picker(color=10),
                    backgroundColor=(1, 0.7, 0.2),
                    parent=color_column)
        cmds.button(label='D_Grey',
                    command=lambda x: cp.color_picker(color=11),
                    backgroundColor=(0.4, 0.4, 0.4),
                    parent=color_column)
        cmds.button(label='D_Orange',
                    command=lambda x: cp.color_picker(color=12),
                    backgroundColor=(1, 0.5, 0),
                    parent=color_column)
        cmds.button(label='B_Red',
                    command=lambda x: cp.color_picker(color=13),
                    backgroundColor=(1, 0, 0),
                    parent=color_column)
        cmds.button(label='B_Green',
                    command=lambda x: cp.color_picker(color=14),
                    backgroundColor=(0, 1, 0),
                    parent=color_column)
        cmds.button(label='Blue',
                    command=lambda x: cp.color_picker(color=15),
                    backgroundColor=(0, 0, 0.7),
                    parent=color_column)
        cmds.button(label='White',
                    command=lambda x: cp.color_picker(color=16),
                    backgroundColor=(1, 1, 1),
                    parent=color_column)
        cmds.button(label='Yellow',
                    command=lambda x: cp.color_picker(color=17),
                    backgroundColor=(1, 0.8, 0.2),
                    parent=color_column)
        cmds.button(label='Sky Blue',
                    command=lambda x: cp.color_picker(color=18),
                    backgroundColor=(0.7, 0.7, 1),
                    parent=color_column)
        cmds.button(label='B_Green',
                    command=lambda x: cp.color_picker(color=19),
                    backgroundColor=(0.7, 1, 0.7),
                    parent=color_column)
        cmds.button(label='Peach',
                    command=lambda x: cp.color_picker(color=20),
                    backgroundColor=(1, 0.8, 1),
                    parent=color_column)
        cmds.button(label='Tan',
                    command=lambda x: cp.color_picker(color=21),
                    backgroundColor=(1, 0.9, 0.9),
                    parent=color_column)
        cmds.button(label='L_Yellow',
                    command=lambda x: cp.color_picker(color=22),
                    backgroundColor=(1, 0.9, 0.3),
                    parent=color_column)
        cmds.button(label='Forest',
                    command=lambda x: cp.color_picker(color=23),
                    backgroundColor=(0, 0.3, 0),
                    parent=color_column)
        cmds.button(label='Brown',
                    command=lambda x: cp.color_picker(color=24),
                    backgroundColor=(0.6, 0.4, 0),
                    parent=color_column)
        cmds.button(label='M_Yellow',
                    command=lambda x: cp.color_picker(color=25),
                    backgroundColor=(0.7, 0.6, 0.2),
                    parent=color_column)
        cmds.button(label='M_Green',
                    command=lambda x: cp.color_picker(color=26),
                    backgroundColor=(0.4, 0.4, 0),
                    parent=color_column)
        cmds.button(label='M_Blue',
                    command=lambda x: cp.color_picker(color=27),
                    backgroundColor=(0.2, 0.3, 0.5),
                    parent=color_column)
        cmds.button(label='P_Sky Blue',
                    command=lambda x: cp.color_picker(color=28),
                    backgroundColor=(0.8, 0.8, 1),
                    parent=color_column)
        cmds.button(label='P_Blue',
                    command=lambda x: cp.color_picker(color=29),
                    backgroundColor=(0.5, 0.5, 1),
                    parent=color_column)
        cmds.button(label='Purple',
                    command=lambda x: cp.color_picker(color=30),
                    backgroundColor=(0.7, 0.3, 0.7),
                    parent=color_column)
        cmds.button(label='Magenta',
                    command=lambda x: cp.color_picker(color=31),
                    backgroundColor=(0.4, 0, 0.4),
                    parent=color_column)

    def show_window(self):
        if cmds.window(self.window, exists=True):
            cmds.showWindow(self.window)

    def delete_window(self):
        # deletes window if UI already exists
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)
