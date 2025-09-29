# objectCreatorUtil.py
from maya import cmds

def createObject(obj_type, name=None):
    """
    สร้างวัตถุใน Maya ตาม obj_type
    """
    obj = None
    if obj_type == "cube":
        obj = cmds.polyCube(name=name or "pCube#")[0]
    elif obj_type == "sphere":
        obj = cmds.polySphere(name=name or "pSphere#")[0]
    elif obj_type == "cone":
        obj = cmds.polyCone(name=name or "pCone#")[0]
    elif obj_type == "torus":
        obj = cmds.polyTorus(name=name or "pTorus#")[0]

    return obj
