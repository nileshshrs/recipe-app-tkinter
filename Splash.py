from tkinter import *
from customtkinter import *
import customtkinter
from PIL import ImageTk , Image
from form import loginPage
splashScreen=CTk()
splashScreen.title("splashscreen")
splashScreen.overrideredirect(True)
screenWidth= splashScreen.winfo_screenwidth()
screenHeight= splashScreen.winfo_screenheight()
splashScreenWidth=350
splashScreenHeight=400
splashScreenX=(screenWidth/2)-(splashScreenWidth/2)
splashscreenY=(screenHeight/2)-(splashScreenHeight/2)
def killWindow():
    splashScreen.destroy()
    loginPage()
splashScreen.geometry(f"{splashScreenWidth}x{splashScreenHeight}+{int(splashScreenX)}+{int(splashscreenY)}")
bgImage=customtkinter.CTkImage(light_image=Image.open("Assets/1.png"),size=(300, 300))
bgLabel=customtkinter.CTkLabel(splashScreen, text="", image=bgImage)
bgLabel.pack(fill=BOTH)
bgLabel.pack_propagate(False)
splashScreen.after(3000, killWindow)
splashScreen.mainloop()


