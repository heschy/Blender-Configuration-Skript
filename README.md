# Blender-Configuration-Script
Blender Configuration Script is a collection of Python-scrypts  you can use to get the settings you want just with 5 clicks. 

## How To Use
1. Start Blender.      
2. In the Top-left Menubar click edit
3. In edit click Preferences
4. Select Addons
5. Click install
6. Choose the Addon you want to install. (360.py is used to set up 360° Scenes and default.py is used to improve your render Quality)
7. Down left select the thre rows and click on Save Preferences
8. Close the Preferences Window and start blending you scene



### Compatibility

The Scripts work for the Blender 2.8 and 2.9 Series. The Blender 3.0 Series uses a different API and is incompatible with the addons.

##### Important:
You have to rename the camera before executing the 360.py script.
The new name has to be: `360°_camera`. After executing the Script, you can change the cameras name, if you want.
But when the Script is being executed, the Camera you want to render the 360° Images/Videos with needs to have this name. If the Camera doesn't have this Name, the addon is unable to find your camera. This ISsue will be improved soon. But first I am creating [another cool Addon for Blender](https://github.com/heschy/Stargate-Generator)!
