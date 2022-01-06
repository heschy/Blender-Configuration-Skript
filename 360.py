from bpy import *;

camname = '360°_camera';
size    = [4000,2000];

context.scene.render.engine                     = 'CYCLES';
data.objects[camname].data.type                 = 'PANO';
data.objects[camname].data.cycles.panorama_type = 'EQUIRECTANGULAR';
context.scene.render.resolution_x               = size[0];
context.scene.render.resolution_y               = size[1];
