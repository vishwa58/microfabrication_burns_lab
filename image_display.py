
import microfabrication_functions as mfc
import microfabrication_constant as mconst
import time as time
import sys
import os as os
import  sdl2.ext 
import sdl2.sdlimage
#os.environ["PYSDL2_DLL_PATH"] = "/Users/vishwanathan/Desktop/UM-2/undergrad_research/PySDL2-0.9.5"
RESOURCES = sdl2.ext.Resources(__file__, mconst.IMAGE_PATH)
image_list = mfc
image_filelist = mfc.read_files(mconst.IMAGE_PATH)
sdl2.ext.init()
window = sdl2.ext.Window("Hello World!", size=(1000, 1000))
window.show()
#sdl2.SDL_SetWindowFullscreen(window, 1, flags = sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)


factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)


spritelist =[]

for filename in image_filelist  :
    sprite = factory.from_image(RESOURCES.get_path(filename.original_filename))
    spritelist.append(sprite)

spriterenderer = factory.create_sprite_render_system(window)
print("yoh")
processor = sdl2.ext.TestEventProcessor()
print("yeh")
processor.run(window)
sdl2.ext.get_events()
start = time.time()
print("yuh")
for sprite in spritelist:
    spriterenderer.render(sprite)
    sdl2.timer.SDL_Delay(50)

    
end = time.time()
print(end-start)


sdl2.ext.quit()










