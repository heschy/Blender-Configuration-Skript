# Blender-Configuration-Skript
is a simple Python Skript Setup the Blender Settings with 5 clicks.

## How To Use
1. Start Blender.      
2. Go to the `Scripting`-Area in The Blender Interface.      
3. Click on `OPEN`-Button in the Text-Editor.       
4. Select the Scrypt File.      
* Edit the File if you wnat to do this. 
5. Click on the `Play`-Button to execute the Script.

## What is this?
This is a Python Script, Blender uses Python to do anything.
With a simple Pyhton Script you can change the Settings of Blender with 2 Clicks: Open and Run.

This Python Scrypt is realy simple. Here are a few Lines you will change sometimes:

```
11 - BlenderRenderConfig.engine  = 'CYCLES';
13 - BlenderRenderConfig.use_lock_interface = True;
18 - BlenderRenderConfig.fps = 25;
```

In Line 10 I set the `Render Engine` property to  `'CYCLES'`. This is because I use Cycles everytime wehen I Render something.
Cycles is a `Physic Based Render-Engine`. You need Cycles for Transparent Materials Like Water, Glass, and a completly Transparent Material.
For realitic Reflactions you need Cycles too. Cycles is perfect for Movies and realitic Images. The Rendertime is not so fast but you can reduce Rendertime
if you reduce the samples ( Propertys for the Samples are here: 20, 21 25,26,40,41).

In Line 12 the Scrypt sets the `LockInterface`-Property because this reduces the Rendertime.

By default the FPS-Value is 24, my Script sets this Value to 25 because this is simpier to use then 24. You can edit this Property in Line 17.

## Reduce Render-Time

If you want to reduce your rendertime you can edit line 3:

```
rendertime_reducing = 200;
```

Replace the `200` with a `20`
