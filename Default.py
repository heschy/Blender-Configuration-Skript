import bpy;

bl_info = {
    "name": "Heschy Render Settings",
    "description": "Improve your Render Settings, with one click.",
    "author": "Henry Schynol",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > Toolbar > View > Heschy Render Settings",
    "warning": "This Addon cannot be used in Blender 3.0 or higher!", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/heschy/Blender-Configuration-Skript/wiki",
    "support": "COMMUNITY",
    "category": "Render",
}

class HESCHY_CONFIG_SCRIPT_OT_mainop(bpy.types.Operator):
    """Quick Configuration Tool"""
    bl_label = "Configurate"
    bl_idname = "heschyconfig_nonodes.mainop"
    
    def execute(self, context):
        BlenderRenderCycles                            = bpy.context.scene.cycles;
        BlenderRenderEevee                             = bpy.context.scene.eevee;
        BlenderRenderConfig                            = bpy.context.scene.render;
        bpy.context.scene.use_nodes                    = True;

        BlenderRenderConfig.engine                     = 'CYCLES';
        BlenderRenderConfig.tile_x                     = 128;
        BlenderRenderConfig.use_lock_interface         = True;
        BlenderRenderConfig.tile_y                     = 128;
        BlenderRenderConfig.use_save_buffers           = True;
        BlenderRenderConfig.use_persistent_data        = True;
        BlenderRenderConfig.film_transparent           = True;
        BlenderRenderConfig.fps                        = 25;

        BlenderRenderCycles.samples                    = 50;
        BlenderRenderCycles.aa_samples                 = 50;
        BlenderRenderCycles.device                     = 'GPU';
        BlenderRenderCycles.use_denoising              = True;
        BlenderRenderCycles.use_preview_denoising      = True;
        BlenderRenderCycles.preview_samples            = 0;
        BlenderRenderCycles.preview_aa_samples         = 0;
        BlenderRenderCycles.shading_system             = True;
        BlenderRenderCycles.tile_order                 = 'CENTER'
        BlenderRenderCycles.debug_use_spatial_splits   = True;
        BlenderRenderCycles.caustics_reflective        = True;
        BlenderRenderCycles.caustics_refractive        = True;
        BlenderRenderCycles.denoiser                   = 'OPENIMAGEDENOISE'
        BlenderRenderCycles.preview_denoiser           = 'OPENIMAGEDENOISE'
        BlenderRenderCycles.use_preview_denoising      = False;
        BlenderRenderCycles.feature_set                = 'SUPPORTED';
        BlenderRenderCycles.use_adaptive_sampling      = True;
        BlenderRenderCycles.adaptive_threshold         = 0.0;
        BlenderRenderCycles.adaptive_min_samples       = 0;

        BlenderRenderEevee.use_bloom                   = True;
        BlenderRenderEevee.use_ssr                     = True;
        BlenderRenderEevee.taa_render_samples          = 500;
        BlenderRenderEevee.taa_samples                 = 0;
        
        return {'FINISHED'}
    
class HESCHY_CONFIG_SCRIPT_PT_mainpanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Heschy Render Settings"
    bl_idname = "heschyconfig_nonodes_mainpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "View"

    def draw(self, context):
        layout = self.layout

        layout.operator("heschyconfig_nonodes.mainop")


classes = [HESCHY_CONFIG_SCRIPT_OT_mainop, HESCHY_CONFIG_SCRIPT_PT_mainpanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == '__main__':
    register()
