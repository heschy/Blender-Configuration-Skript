import bpy;

rendertime_reducing = 200;
#Init
BlenderRenderCycles                            = bpy.data.scenes['Scene'].cycles;
BlenderRenderEevee                             = bpy.data.scenes['Scene'].eevee;
BlenderRenderConfig                            = bpy.data.scenes['Scene'].render;
bpy.data.scenes['Scene'].use_nodes             = True;

#General Render Settings
BlenderRenderConfig.engine                     = 'CYCLES';
BlenderRenderConfig.tile_x                     = 128;
BlenderRenderConfig.use_lock_interface         = True;
BlenderRenderConfig.tile_y                     = 128;
BlenderRenderConfig.use_save_buffers           = True;
BlenderRenderConfig.use_persistent_data        = True;
BlenderRenderConfig.film_transparent           = True;
BlenderRenderConfig.fps                        = 25;

#Cycles Settings
BlenderRenderCycles.samples                    = 200;
BlenderRenderCycles.aa_samples                 = 200;
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

#Eevee Settings
BlenderRenderEevee.use_bloom                   = True;
BlenderRenderEevee.use_ssr                     = True;
BlenderRenderEevee.taa_render_samples          = 500;
BlenderRenderEevee.taa_samples                 = 0;
