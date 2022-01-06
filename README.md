# Blender-Configuration-Script
Blender Configuration Script is a collection of Python-scrypts  you can use to get the settings you want just with 5 clicks. 

## How To Use
1. Start Blender.      
2. Open the `Text Editor`-Panel.      
3. Click on `OPEN`.       
4. Select the Script you want to use.      
5. Click on the `Play`-Button to execute the Script.

## Scripts

### 360.py
#### Content
```python
from bpy import *;

camname = '360°_camera';
size    = [4000,2000];

context.scene.render.engine                     = 'CYCLES';
data.objects[camname].data.type                 = 'PANO';
data.objects[camname].data.cycles.panorama_type = 'EQUIRECTANGULAR';
context.scene.render.resolution_x               = size[0];
context.scene.render.resolution_y               = size[1];
```
#### Test

This script is tested with:

- Blender 3.0 `beta`
- Blender 2.93.5
- Blender 2.92.0

This script works with:

[X] Blender 3.0 `beta`
[X] Blender 2.93.5
[X] Blender 2.92.0

#### Usage

You can run ``360.py` if you want to render a 360° scene.

##### Important:
You have to rename the camera before executing the script.
The new name has to be: `360°_camera`. After executing the Script, you can change the cameras name, if you want.