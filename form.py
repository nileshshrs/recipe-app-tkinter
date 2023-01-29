from tkinter import *
from customtkinter import *
import tkinter
import customtkinter
from tkinter import ttk
from PIL import ImageTk, Image

textcolor = "whitesmoke"

def registerPage():
    window = CTk()
    registerImg = customtkinter.CTkImage(
        light_image=Image.open("Assets/5.png"), size=(250, 250))
    appWidth = 850
    appHeight = 500
    screenHeight = window.winfo_screenheight()
    screenWidth = window.winfo_screenwidth()
    centerX = (screenWidth/2)-(appWidth/2)
    centerY = (screenHeight/2)-(appHeight/2)
    window.geometry(f"{appWidth}x{appHeight}+{int(centerX)}+{int(centerY)}")
    window.resizable(False, False)
    window.title("register")
    def navigate():
        window.destroy()
        #loginPage()


    imageFrame = customtkinter.CTkFrame(
        master=window, height=appHeight, width=.35*appWidth,)
    imageFrame.place(x=0, y=0)
    imageFrame.propagate(False)
    imgWidget = customtkinter.CTkLabel(
        master=imageFrame, image=registerImg, height=appHeight, width=.35*appWidth, text="")
    imgWidget.pack(padx=20)
    formFrame = customtkinter.CTkFrame(
        master=window, height=appHeight, width=.65*appWidth)
    formFrame.place(x=296, y=0)
    formFrame.pack_propagate(False)
    formFrame.propagate(False)
    registerTitle = customtkinter.CTkLabel(master=formFrame, text="Sign up...!", font=(
        "helvatica", 25, "bold"), text_color=textcolor)
    registerTitle.place(x=50, y=25)
    errorLabel = customtkinter.CTkLabel(master=formFrame, text="", width=420)
    errorLabel.place(y=90, x=57)
    registerFirstName = customtkinter.CTkEntry(
        master=formFrame, width=205, placeholder_text="first name", height=30)
    registerFirstName.place(x=57, y=140)
    registerLastName = customtkinter.CTkEntry(
        master=formFrame, width=205, placeholder_text="last name", height=30)
    registerLastName.place(x=270, y=140)
    registerusername = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="username", height=30)
    registerusername.place(x=57, y=190)
    registeremail = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="email", height=30)
    registeremail.place(x=57, y=240)
    registerpassword = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="password", height=30)
    registerpassword.place(x=57, y=290)
    registerpassword.configure(show="*")
    registerconfirmpassword = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="confirm-password", height=30)
    registerconfirmpassword.place(x=57, y=340)
    registerconfirmpassword.configure(show="*")
    registerBtn = customtkinter.CTkButton(
        master=formFrame, text="Sign up", width=417, height=30, )#command=getUserData
    registerBtn.place(x=57, y=390)
    loginLabel = customtkinter.CTkLabel(
        master=formFrame, text="Dont  have  an  account  ?", font=("helvatica", 16, "bold"))
    loginLabel.place(x=57, y=440)
    registerBtn = customtkinter.CTkButton(
        master=formFrame, text="login", width=200, command=navigate)
    registerBtn.place(x=270, y=440)
    window.mainloop()