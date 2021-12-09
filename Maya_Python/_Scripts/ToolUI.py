import maya.cmds as cmds
import ColorPicker as cp
import CreateControl as cc
import CreateNullParent as cnp
import SequentialRenamer as sr


class ToolUI:
    def __init__(self):
        self.window = "rigging_tools_ui"
        self.m_column = "main_column"
        self.rename_textfield = ""

    def create_window(self):

        self.delete_window()

        # Main window creation with Column Layout
        self.window = cmds.window(self.window, title="Rigging Tools", widthHeight=(500, 500))
        self.m_column = cmds.columnLayout(self.m_column, columnAttach=('both', 5),
                                          rowSpacing=10, columnWidth=500, parent=self.window)

        self.create_control_ui()
        self.color_picker_ui()
        self.sequential_renamer_ui()

        self.show_window()

    def color_picker_ui(self):
        # Color Picker
        # Uses buttons to change the color of the object selected
        cmds.text(label='', font="boldLabelFont", align='center', parent=self.m_column)
        cmds.text(label='Color Picker', font="boldLabelFont", align='center', parent=self.m_column)
        color_column = cmds.gridLayout(numberOfColumns=8, numberOfRows=4, parent=self.m_column,
                                       backgroundColor=(0.5, 0.5, 0.5), cellWidthHeight=(61, 25),
                                       columnsResizable=False, autoGrow=False)

        cmds.button(label='None',
                    command=lambda *x: self.color_button_cmd(c=0),
                    parent=color_column)
        cmds.button(label='Black',
                    command=lambda *x: self.color_button_cmd(c=1),
                    backgroundColor=(0, 0, 0),
                    parent=color_column)
        cmds.button(label='Grey',
                    command=lambda *x: self.color_button_cmd(c=2),
                    backgroundColor=(0.25098, 0.25098, 0.25098),
                    parent=color_column)
        cmds.button(label='D_White',
                    command=lambda *x: self.color_button_cmd(c=3),
                    backgroundColor=(0.6, 0.6, 0.6),
                    parent=color_column)
        cmds.button(label='Red',
                    command=lambda *x: self.color_button_cmd(c=4),
                    backgroundColor=(0.60784, 0, 0.15686),
                    parent=color_column)
        cmds.button(label='D_Blue',
                    command=lambda *x: self.color_button_cmd(c=5),
                    backgroundColor=(0, 0.01569, 0.37647),
                    parent=color_column)
        cmds.button(label='L_Blue',
                    command=lambda *x: self.color_button_cmd(c=6),
                    backgroundColor=(0, 0, 1),
                    parent=color_column)
        cmds.button(label='D_Green',
                    command=lambda *x: self.color_button_cmd(c=7),
                    backgroundColor=(0, 0.27451, 0.09804),
                    parent=color_column)
        cmds.button(label='D_Purple',
                    command=lambda *x: self.color_button_cmd(c=8),
                    backgroundColor=(0.14902, 0, 0.26275),
                    parent=color_column)
        cmds.button(label='Pink',
                    command=lambda *x: self.color_button_cmd(c=9),
                    backgroundColor=(0.78431, 0, 0.78431),
                    parent=color_column)
        cmds.button(label='L_Brown',
                    command=lambda *x: self.color_button_cmd(c=10),
                    backgroundColor=(0.54118, 0.28235, 0.2),
                    parent=color_column)
        cmds.button(label='D_Brown',
                    command=lambda *x: self.color_button_cmd(c=11),
                    backgroundColor=(0.24706, 0.13725, 0.12157),
                    parent=color_column)
        cmds.button(label='D_Orange',
                    command=lambda *x: self.color_button_cmd(c=12),
                    backgroundColor=(0.6, 0.14902, 0),
                    parent=color_column)
        cmds.button(label='B_Red',
                    command=lambda *x: self.color_button_cmd(c=13),
                    backgroundColor=(1, 0, 0),
                    parent=color_column)
        cmds.button(label='B_Green',
                    command=lambda *x: self.color_button_cmd(c=14),
                    backgroundColor=(0, 1, 0),
                    parent=color_column)
        cmds.button(label='Blue',
                    command=lambda *x: self.color_button_cmd(c=15),
                    backgroundColor=(0, 0.25490, 0.6),
                    parent=color_column)
        cmds.button(label='White',
                    command=lambda *x: self.color_button_cmd(c=16),
                    backgroundColor=(1, 1, 1),
                    parent=color_column)
        cmds.button(label='Yellow',
                    command=lambda *x: self.color_button_cmd(c=17),
                    backgroundColor=(1, 1, 0),
                    parent=color_column)
        cmds.button(label='Sky Blue',
                    command=lambda *x: self.color_button_cmd(c=18),
                    backgroundColor=(0.39216, 0.86275, 1),
                    parent=color_column)
        cmds.button(label='B_Green',
                    command=lambda *x: self.color_button_cmd(c=19),
                    backgroundColor=(0.26275, 1, 0.63922),
                    parent=color_column)
        cmds.button(label='Peach',
                    command=lambda *x: self.color_button_cmd(c=20),
                    backgroundColor=(1, 0.6902, 0.6902),
                    parent=color_column)
        cmds.button(label='Tan',
                    command=lambda *x: self.color_button_cmd(c=21),
                    backgroundColor=(0.89412, 0.67451, 0.47451),
                    parent=color_column)
        cmds.button(label='L_Yellow',
                    command=lambda *x: self.color_button_cmd(c=22),
                    backgroundColor=(1, 1, 0.38824),
                    parent=color_column)
        cmds.button(label='Forest',
                    command=lambda *x: self.color_button_cmd(c=23),
                    backgroundColor=(0, 0.6, 0.32941),
                    parent=color_column)
        cmds.button(label='Brown',
                    command=lambda *x: self.color_button_cmd(c=24),
                    backgroundColor=(0.63137, 0.41569, 0.18824),
                    parent=color_column)
        cmds.button(label='M_Yellow',
                    command=lambda *x: self.color_button_cmd(c=25),
                    backgroundColor=(0.61961, 0.63137, 0.18824),
                    parent=color_column)
        cmds.button(label='M_Green',
                    command=lambda *x: self.color_button_cmd(c=26),
                    backgroundColor=(0.40784, 0.63137, 0.18824),
                    parent=color_column)
        cmds.button(label='M_Blue',
                    command=lambda *x: self.color_button_cmd(c=27),
                    backgroundColor=(0.18824, 0.63137, 0.36471),
                    parent=color_column)
        cmds.button(label='P_Sky Blue',
                    command=lambda *x: self.color_button_cmd(c=28),
                    backgroundColor=(0.18824, 0.63137, 0.63137),
                    parent=color_column)
        cmds.button(label='P_Blue',
                    command=lambda *x: self.color_button_cmd(c=29),
                    backgroundColor=(0.18824, 0.40392, 0.63137),
                    parent=color_column)
        cmds.button(label='Purple',
                    command=lambda *x: self.color_button_cmd(c=30),
                    backgroundColor=(0.43529, 0.18824, 0.63137),
                    parent=color_column)
        cmds.button(label='Magenta',
                    command=lambda *x: self.color_button_cmd(c=31),
                    backgroundColor=(0.63137, 0.18824, 0.41569),
                    parent=color_column)

    def create_control_ui(self):
        # Create Control and Null Parent
        # Uses buttons to create a control for each selected object
        cmds.text(label='', font="boldLabelFont", align='center', parent=self.m_column)
        cmds.text(label='Controls', font="boldLabelFont", align='center', parent=self.m_column)
        control_row = cmds.rowLayout(parent=self.m_column, backgroundColor=(0.5, 0.5, 0.5), numberOfColumns=3,
                                     columnWidth3=(165, 165, 165), columnAlign=(1, 'right'),
                                     columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])

        cmds.text(label='Control Creation', font="boldLabelFont", align='center', parent=control_row)
        cmds.button(label='Control', backgroundColor=(0, 0.7, 0), command=lambda *x: self.ctrl_builder_button_cmd(), parent=control_row)
        cmds.button(label='Null Parent', backgroundColor=(0, 0, 1), command=lambda *x: self.create_null_parent_cmd(), parent=control_row)


    def sequential_renamer_ui(self):
        # Sequential Renamer
        # Uses text field with button to rename each selected object
        renamer_column = cmds.columnLayout(self.m_column, backgroundColor=(0.5, 0.5, 0.5), columnAttach=('both', 0),
                                           columnWidth=490, parent=self.m_column)
        cmds.text(label='', font="boldLabelFont", align='center', parent=renamer_column)
        cmds.text(label='Renaming', font="boldLabelFont", align='center', parent=renamer_column)
        self.rename_textfield = cmds.textFieldButtonGrp(label='Name', placeholderText="Leg_##_Jnt", buttonLabel='Apply',
                                                        buttonCommand=lambda *x: self.sequential_renamer_cmd(),
                                                        parent=renamer_column)

    def color_button_cmd(self, c):
        import importlib
        importlib.reload(cp)
        cp.color_picker(color=c)

    def ctrl_builder_button_cmd(self):
        import importlib
        importlib.reload(cc)
        cc.create_control()

    def create_null_parent_cmd(self):
        import importlib
        importlib.reload(cnp)
        cnp.create_null_parent()

    def sequential_renamer_cmd(self):
        import importlib
        importlib.reload(sr)
        text_data = cmds.textFieldButtonGrp(self.rename_textfield, q=True, text=True)
        sr.rename(text_data)

    def show_window(self):
        if cmds.window(self.window, exists=True):
            cmds.showWindow(self.window)

    def delete_window(self):
        # deletes window if UI already exists
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)


my_UI = ToolUI()
my_UI.create_window()
