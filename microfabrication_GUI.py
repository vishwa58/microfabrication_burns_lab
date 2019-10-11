import tkinter as tk
import microfabrication_functions as mfc
import microfabrication_constant as mfc_const
import  time as time

image_filelist = mfc.read_files(mfc_const.IMAGE_PATH) #This list holds the names of all the images nd is sorted by slice num


def set_text(text, entrybox):
    entrybox.delete(1.0,tk.END)
    entrybox.insert(1.0,text)
    return


#This function takes in a list of images and a label and will place the image in the center of the screen for a proper amt of time

#This function will have to be fixed in the future to incorporate the new stuff
def cycle_images(image_list, tkinter_label):
    for filename in image_list:#loops throguh differnt files
        exposure = tk.PhotoImage(file = (mfc_const.IMAGE_PATH+filename.original_filename))
        tkinter_label.config(image = exposure)
        # central_image = tk.Label(self, text = "image goes here", image = exposure)
        tkinter_label.image =exposure
        t_end = (time.time())+(60.0/1000)
        print("prob an infitinte loop")
        x =3
        while((time.time())<=t_end):
            print(time.time())
            print(t_end)
            print('def an infinite loop')
            tkinter_label.place(relx=0.5, rely=0.5, anchor ='c')
            print("not and infinite loop?")




class window_controller(tk.Tk):
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frame_list[page_name]
        #self.update_idletasks()
        if (page_name == "driverwindow"):
            frame.tkraise()
            self.attributes("-fullscreen", True)
        else:
            frame.tkraise()
            self.attributes("-fullscreen", False)
            self.geometry('600x600')
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #n = tk.Label(container, text = "oogaboog")
        #n.pack()
        self.frame_list = {}
        for F in (open_window, driverwindow):
            page_name = F.__name__ #creates a variable equal to the class name
            frame = F(container, controller=self)
            self.frame_list[page_name] = (frame)
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("open_window")



        # change geometry of the window
        


class open_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        validate_button = tk.Button(self, text = "Validate", command = lambda: controller.show_frame("driverwindow"))
        validate_button.pack()
#         self.parent = parent 
#         self.f1 =tk.Frame(self.parent, background = "Grey")

        T = tk.Text(self)#, height=2, width=30)
        T.pack()
        # T.insert(tk.END, "Just a text Widget\nin two lines\n")
        label =tk.Label(self, text = "oogabooga")
        label.pack()
        #image_filelist = mfc.read_files(mfc_const.IMAGE_PATH)

        for x in image_filelist:
            T.insert(tk.END, x.original_filename + "    "+ str(x.slice_num) + "   "+ str(x.UV_voltage) + "    " + str(x.blue_voltage) + "  "+str(x.display_time)+ '\n')


class driverwindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'black')
        self.controller = controller

        invalidate_button = tk.Button(self, text = "Invalidate", command = lambda: controller.show_frame("open_window"))
        invalidate_button.pack()

        self.central_image = tk.Label(self, text = "image goes here")

        cycle_images(image_filelist, self.central_image)


        # tenthtop = tk.PhotoImage(file = "basket.png")

        # self.central_image.image =tenthtop
        # self.central_image.place(relx=0.5, rely=0.5, anchor ='c')



        # self.parent = parent 
        # self.f2 = tk.Frame(self.parent, background = "Grey")
        # t = tk.Label(text = "big chungus")
        # t.pack()
                   



        
        



# root = tk.Tk()
# root.resizable(0,0)
mw =  window_controller()
#tenthtop = tk.PhotoImage(file = "basket.png")
#mw.show_frame("open_window")
mw.mainloop()