## What is it?
BLender Configuration Script (aka `Heschy Render Config`/`Heschy Render Settings`) is an addon for Blender.     
It changes your Render settings, in order to get more realistic images. Of course it wont set your configurations to the optimum,    
but it it is still good.     

### Warning:
Blender changed a few things in the API when creating Blender 3.0      
This Addon wont work on Blender 3.0 or higher.     

## Wich settings are going to be reseted?

1. To get more realistic Images, you will render with Cycles
2. To stop interrupting Render procces, you wont be able to change anything while blender renders your scene.
3. Cycles will render Transparent Background
4. The Framerate is going to be 60 frames per second, to create higher-quality animations
5. You will render on your GPU
6. You will render 50 Frames + Denoising to reduce render time and increase Quality
7. You will use Adaptive sampling, to reduce render time
8. If you want to use Eevee, you will render Reflections ass well.
9. If you use Eevee, you will render Bloom as well.
