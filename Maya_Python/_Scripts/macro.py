import maya.cmds as cmds

objs = []
temp = []
snow_obj = []
snowman = ""
geo = ""

# Hat
temp = cmds.polyCylinder(radius=0.8, height=0.25, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0],
                         roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 4.4, 0, objs[-1], relative=True)
cmds.polyExtrudeFacet(objs[-1] + ".f[40:59]", kft=True, ls=[.5, .5, 0])
cmds.polyExtrudeFacet(objs[-1] + ".f[40:59]", kft=True, ls=[1, 1, 1], translate=[0, 1, 0])

# Head
temp = cmds.polySphere(radius=0.8, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 3.75, 0, objs[-1], relative=True)

# Eyes
temp = cmds.polySphere(radius=0.1, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(0.25, 3.85, 0.75, objs[-1], relative=True)
temp = cmds.polySphere(radius=0.1, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(-0.25, 3.85, 0.75, objs[-1], relative=True)

# Nose
temp = cmds.polyCone(radius=0.25, height=0.75, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=0, axis=[0, 0, 1],
                     roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 3.75, 0.75, objs[-1], relative=True)

# Mouth
temp = cmds.polySphere(radius=0.05, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(0.4, 3.5, 0.75, objs[-1], relative=True)

temp = cmds.polySphere(radius=0.05, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(-0.4, 3.5, 0.75, objs[-1], relative=True)

temp = cmds.polySphere(radius=0.05, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(0.2, 3.4, 0.75, objs[-1], relative=True)

temp = cmds.polySphere(radius=0.05, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(-0.2, 3.4, 0.75, objs[-1], relative=True)

temp = cmds.polySphere(radius=0.05, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 3.35, 0.75, objs[-1], relative=True)

# Torso
temp = cmds.polySphere(radius=1.2, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 2, 0, objs[-1], relative=True)

# Buttons
temp = cmds.polyCylinder(radius=0.2, height=0.05, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 0, 1],
                         roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 2, 1.2, objs[-1], relative=True)
temp = cmds.polyCylinder(radius=0.2, height=0.05, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 0, 1],
                         roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 2.75, 0.95, objs[-1], relative=True)
cmds.rotate(-35, 0, 0, objs[-1], relative=True, objectSpace=True, forceOrderXYZ=True)

temp = cmds.polyCylinder(radius=0.2, height=0.05, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0, 0, 1],
                         roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])
cmds.move(0, 1.25, 0.95, objs[-1], relative=True)
cmds.rotate(-35, 0, 0, objs[-1], relative=True, objectSpace=True, forceOrderXYZ=True)

# Body
temp = cmds.polySphere(radius=1.5, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], createUVs=2,
                       constructionHistory=1)
objs.append(temp[0])

# Arms
temp = cmds.polyCylinder(radius=0.1, height=3.5, subdivisionsX=6, subdivisionsY=2, subdivisionsZ=1, axis=[0, 1, 0],
                         roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])
cmds.move(-2, 3.5, 0, objs[-1], relative=True)
cmds.rotate(0, 0, 45, objs[-1], relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.move(-0.25, -0.25, 0, objs[-1] + ".e[6:11]", relative=True)
cmds.polyExtrudeFacet(objs[-1] + ".f[18]", objs[-1] + ".f[20]", objs[-1] + ".f[22]", kft=False,
                      translate=[-0.75, 0.75, 0], ls=[.5, .5, 0])
cmds.move(0.25, 0, 0.25, objs[-1] + ".f[22]", relative=True)
cmds.move(-0.25, 0.25, 0.25, objs[-1] + ".f[20]", relative=True)
cmds.move(0.25, 0.25, -0.25, objs[-1] + ".f[18]", relative=True)

temp = cmds.polyCylinder(radius=0.1, height=3.5, subdivisionsX=6, subdivisionsY=2, subdivisionsZ=1, axis=[0, 1, 0],
                         roundCap=0, createUVs=3, constructionHistory=1)
objs.append(temp[0])

cmds.move(2, 3.5, 0, objs[-1], relative=True)
cmds.rotate(0, 0, -45, objs[-1], relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.move(0.25, -0.25, 0, objs[-1] + ".e[6:11]", relative=True)
cmds.polyExtrudeFacet(objs[-1] + ".f[18]", objs[-1] + ".f[20]", objs[-1] + ".f[22]", kft=False,
                      translate=[0.75, 0.75, 0], ls=[.5, .5, 0])
cmds.move(0.25, 0, 0.25, objs[-1] + ".f[22]", relative=True)
cmds.move(0.25, 0.25, 0.25, objs[-1] + ".f[20]", relative=True)
cmds.move(0.25, 0.25, -0.25, objs[-1] + ".f[18]", relative=True)

# Group, Combine  & Rename
snowObj = cmds.polyUnite(objs)
cmds.delete(constructionHistory=True)
snowman = cmds.rename(snowObj[0], "Snowman")
geo = cmds.group(empty=True, name="Geo")
cmds.parent(snowman, geo)
