import tkinter as tk
import microfabrication_functions as mfc
import microfabrication_constant as mfc_const

def set_text(text, entrybox):
    entrybox.delete(1.0,tk.END)
    entrybox.insert(1.0,text)
    return

class window:
    def __init__(self, parent):
        self.parent = parent 
        self.f1 =tk.Frame(self.parent, background = "Grey")

        T = tk.Text(self.parent)#, height=2, width=30)
        T.pack()
        # T.insert(tk.END, "Just a text Widget\nin two lines\n")

        image_filelist = mfc.read_files(mfc_const.IMAGE_PATH)

        for x in image_filelist:
            T.insert(tk.END, x.original_filename + "    "+ str(x.slice_num) + "   "+ str(x.UV_voltage) + "    " + str(x.blue_voltage) + "  "+str(x.display_time)+ '\n')
        validate_button = tk.Button(text = "Validate")
        validate_button.pack()

            



        
        




root = tk.Tk()
# root.resizable(0,0)
mw =  window(root)
tk.mainloop()