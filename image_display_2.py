
import microfabrication_functions as mfc
import microfabrication_constant as mconst
import time as time
import sys
import os as os
import  sdl2.ext 
import sdl2.sdlimage
import ctypes
#os.environ["PYSDL2_DLL_PATH"] = "/Users/vishwanathan/Desktop/UM-2/undergrad_research/PySDL2-0.9.5"
from sdl2 import *






def driver_function():
    spritelist =[]
    
    if (sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)<0): #If SDL does not intialize properly the program will quit
        exit(0)


    # RESOURCES = sdl2.ext.Resources(__file__, mconst.IMAGE_PATH) 

    image_filelist = mfc.read_files(mconst.IMAGE_PATH)# function that can be found in microfabrication_GUI that store the information

    window = SDL_CreateWindow(b"Hello World", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, 1000, 1000, sdl2.SDL_WINDOW_SHOWN)
    #SDL function that creates a window. Most of the parameters in this function are fairly redundant since the window will be fullscreen. 
    #Look up pySDL documentation if you need to change the size

    sdl2.SDL_SetWindowFullscreen(window, 1, flags = sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP) #Sets the window to be fullscreen

    renderer = sdl2.SDL_CreateRenderer(window, -1,0) #creates the renderer which is how you display images on the screen
    #the first parameter describes which window contains the renderer. The second parameters is irrelevent unless you have a list of renderers
    #The third parameter is only used if you have extraneous flags that you want to use.



    #This is a loop takes the image list we created earlier and converts it into a series of textures(images). The images are then stored in a 
    #list that is called sprite list. This is done because creating a window and displaying it at the same time is very time consuming and would slow down
    #the programs
    for filename in image_filelist:
         image = sdl2.ext.load_image(mconst.IMAGE_PATH+filename.original_filename)
         image = SDL_CreateTextureFromSurface(renderer, image)
         spritelist.append(image)



    #The "while true" loop is at the center of the program. Since SDL is a UI software it uses something called an event loop which means it needs
    #an inifinite loop to constatnly have a UI displayed.
    while True:

        #The first line creates an object called an event. The next line polls for the event to see if the user has made any changes that the UI
        #needs to respond to. In our program the only event that needs to be watch for is for the user to quit
        event = SDL_Event() 
        SDL_PollEvent(ctypes.byref(event)) #This 


        count =0 #This variable will be used to determine how many images will be displayed. Once count is the same size as the image list the program will end
        timelist=[]
        firststart=time.time()

        while True: #This second "while true" loop is used to actually display the
            SDL_PollEvent(ctypes.byref(event)) 
            starter =time.time()
            if (count ==0):
                SDL_Delay(1000)
                starter =time.time()
                firststart=time.time()
            if (len(spritelist)==count):
                break

            sdl2.SDL_RenderCopy(renderer, spritelist[count], None, None)
            sdl2.SDL_RenderPresent(renderer)

            SDL_Delay(mconst.DISPLAY_TIME)
            ender=time.time()-starter
            timelist.append(ender)
            count+=1
        end = time.time()
        # print(end-start)

        # for timet in timelist:
        #     print(timet)
        # print(end-firststart)
        break


        if event.type == SDL_QUIT:
            running = False 
            break






if __name__ == "__main__": 
    sys.exit(driver_function())








