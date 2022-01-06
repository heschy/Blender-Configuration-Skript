import bpy;

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
