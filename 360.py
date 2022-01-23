import bpy;

bl_info = {
    "name": "Blender Configuration Script - 360° Extra",
    "description": "This addon improves your ability to render 360° Videos in Blender.",
    "author": "Henry Schynol",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > Toolbar > Ansicht > Configurate 360° Scene",
    "warning": "This AddOn is still under development!", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/heschy/Stargate-Generator/wiki",
    "support": "TESTING",
    "category": "Nodes",
}

class RENDERTHRESIXTYDEGREESCENE_OT_mainop(bpy.types.Operator):
  bl_label = 'Update Settings'
  bl_idname = 'renderthreesixtydegreescene.mainop'
  
  def execute(self, context):
    camname = '360°_camera';
    size    = [4000,2000];

    bpy.context.scene.render.engine                     = 'CYCLES';
    bpy.data.objects[camname].data.type                 = 'PANO';
    bpy.data.objects[camname].data.cycles.panorama_type = 'EQUIRECTANGULAR';
    bpy.context.scene.render.resolution_x               = size[0];
    bpy.context.scene.render.resolution_y               = size[1];

    return {'FINISHED']
            
class RENDERTHRESIXTYDEGREESCENE_PT_mainpanel(bpy.types.Panel):
  bl_label= """Creates a Panel in the Object properties window"""
  bl_label = "Configurate 360° Scene"
  bl_idname = "renderthreesixtydegreescene.mainpanel"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = "VIEW"

  def draw(self, context):
    layout = self.layout
    layout.operator("renderthreesixtydegreescene.mainop")
    return {'FINISHED'}
      


classes = [RENDERTHRESIXTYDEGREESCENE_OT_mainop, RENDERTHRESIXTYDEGREESCENE_PT_mainpanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()
