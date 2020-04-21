bl_info = {
    "name": "catafest addon start",
    "author": "Catalin George Festila",
    "license": "GPL",
    "version": (1, 1, 1),
    "blender": (2, 82, 0),
    "location": "View3D > Add > Mesh",
    "description": "Procedurally generate 3D catafest_addon_start from a random seed.",
    "warning": "",
    "wiki_url": "https://github.com/catafest/catafest_blender_start/blob/master/README.md",
    "tracker_url": "https://github.com/catafest/catafest_blender_start/issues",
    "category": "Add Mesh"
}

if "bpy" in locals():
    # reload logic (magic)
    import importlib
    importlib.reload(catafest_addon_start)
else:
    from . import catafest_addon_start

import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty
from bpy.types import Operator

class Generate_catafest_mesh(Operator):
    """Procedurally generate a catafest 3D mesh from a random seed."""
    bl_idname = "mesh.generate_mesh"
    bl_label = "catafest_blender_start"
    bl_options = {'REGISTER', 'UNDO'}

    random_seed = StringProperty(default='', name='Seed')


    def execute(self, context):
        catafest_addon_start.generate_mesh(
            self.random_seed)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(Generate_catafest_mesh.bl_idname, text="catafest_blender_start", icon="INFO")

def register():
    #bpy.utils.register_module(__name__)
    bpy.utils.register_class(Generate_catafest_mesh)
    #bpy.types.INFO_MT_mesh_add.append(menu_func)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    #bpy.utils.unregister_module(__name__)
    bpy.utils.unregister_class(Generate_catafest_mesh)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()
