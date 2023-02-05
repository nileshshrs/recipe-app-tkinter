from tkinter import *
from customtkinter import *
import tkinter
import customtkinter
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3
import form
import random

cnxt = sqlite3.connect("data/userdata.db")
c = cnxt.cursor()

textcolor = "whitesmoke"
selectRecipe = ""


def mainScreen():

    win3 = CTk()
    users = form.credentials

    greetings = (f"Welcome, {users}...!")

    c.execute("CREATE TABLE IF NOT EXISTS recipedata (ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME TEXT NOT NULL, RECIPETITLE TEXT NOT NULL, RECIPEDETAILS TEXT NOT NULL, FOREIGN KEY (USERNAME) REFERENCES userdata(USERNAME))")
    win3.resizable(False, False)
    appWidth = 1100
    appHeight = 720

    screenWidth = win3.winfo_screenwidth()
    screenHeight = win3.winfo_screenheight()

    x = (screenWidth/2)-(appWidth/2)
    y = (screenHeight/2)-(appHeight/2)

    win3.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
    win3.title("Recipe application")

    c.execute("select RECIPETITLE from recipedata where USERNAME='"+users+"'")
    records = c.fetchall()

    # form frame
    formFrame = customtkinter.CTkFrame(
        master=win3, width=550, height=appHeight, corner_radius=0)
    formFrame.pack(side=LEFT)
    formFrame.pack_propagate(False)
    formFrame.propagate(False)

    # recipe list label
    recipelistLabel = customtkinter.CTkLabel(master=formFrame, text="Recipe List", font=(
        "helvatica", 15, "bold"), text_color=textcolor)
    recipelistLabel.pack(padx=25, pady=(15, 0), anchor=W)
    # listbox frame
    listboxFrame = customtkinter.CTkFrame(master=formFrame, corner_radius=0)
    listboxFrame.pack(padx=25, pady=10, anchor=W)

    # scrollbar
    recipeListScrollbar = ttk.Scrollbar(master=listboxFrame, orient=VERTICAL)
    # recipe list
    recipeList = Listbox(master=listboxFrame, width=45, bg="#333637",
                         height=6, fg=textcolor, yscrollcommand=recipeListScrollbar.set)
    recipeList.pack(padx=0, side=LEFT)
    # scrollbar config
    recipeListScrollbar.config(command=recipeList.yview)
    recipeListScrollbar.pack(side=RIGHT, fill=Y, )
    # title entry
    titleLabel = customtkinter.CTkLabel(
        master=formFrame, text="Recipe Title", font=("", 15, "bold"))
    titleLabel.pack(padx=25, pady=(5, 0), anchor=W)
    titleEntry = customtkinter.CTkEntry(master=formFrame, width=500, height=40,
                                        border_width=1, placeholder_text="enter recipe title...", corner_radius=5)
    titleEntry.pack(padx=25, pady=(0, 20))
    # recipedetail box
    recipeDetailLabel = customtkinter.CTkLabel(
        master=formFrame, text="Your recipe", font=("", 15, "bold"))
    recipeDetailLabel.pack(padx=25, pady=0, anchor=W)
    recipeDetailsbox = customtkinter.CTkTextbox(
        master=formFrame, width=500, corner_radius=5, border_width=1, height=300, wrap=WORD)
    recipeDetailsbox.pack(padx=25, pady=(0, 15))
    # formframe

    # recipe view frame
    recipeViewFrame = customtkinter.CTkFrame(
        master=win3, width=550, height=appHeight, corner_radius=0)
    recipeViewFrame.pack(side=RIGHT)
    recipeViewFrame.pack_propagate(False)
    recipeViewFrame.propagate(False)
    # greetings title
    greetingsLabel = customtkinter.CTkLabel(
        master=recipeViewFrame, text=greetings, font=("", 25, "bold"), text_color=textcolor)
    greetingsLabel.pack(anchor=W, pady=(10, 0))
    # search
    searchBox = customtkinter.CTkEntry(
        master=recipeViewFrame, placeholder_text="search recipe", width=270, height=25)
    searchBox.pack(anchor=W, pady=(20, 0))
    # view recipetitle
    viewRecipeTitle = customtkinter.CTkLabel(
        master=recipeViewFrame, text="T.O.F.U", font=("", 20, "bold"), text_color=textcolor,)
    viewRecipeTitle.pack(padx=10, anchor=W, pady=(20, 15))
    # recipebox
    text = "\n\n\n \t\t\tTons \n\n\n \t\t\t  of \n\n\n  \t\t\tFood \n\n\n \t\t\t  for \n\n\n \t\t\t   U\n\n\n\n\n\nA place where you can cook whatever you want eat."
    recipeBox = customtkinter.CTkTextbox(master=recipeViewFrame, font=(
        "", 17), text_color=textcolor, width=515, corner_radius=0, height=440, fg_color="#2C2B2C", wrap=WORD)  # 2C2B2C
    recipeBox.pack(anchor=W, padx=10, pady=(10, 20))
    recipeBox.insert(0.0, text)
    recipeBox.configure(state=DISABLED)
    # get a random recipe
    randomRecipeLabel = customtkinter.CTkLabel(
        master=recipeViewFrame, text="Not sure what you want to cook ...?", text_color=textcolor, font=("", 17, "italic"))
    randomRecipeLabel.pack(anchor=W, pady=(10, 5), padx=10)
    # logout
    logoutlabel = customtkinter.CTkLabel(
        master=recipeViewFrame, text="Done cooking or viewing your recipe ?", text_color=textcolor, font=("", 17, "italic"))
    logoutlabel.pack(anchor=W, pady=10, padx=10)



    createBtn = customtkinter.CTkButton(
        master=formFrame, width=500, text="create recipe", command=createMyRecipe)
    createBtn.place(x=25, y=620)

    updateBtn = customtkinter.CTkButton(
        master=formFrame, width=500, text="modify", command=updateMyRecipe)
    updateBtn.place(x=25, y=660)
    updateBtn.configure(state=DISABLED)

    updateRecipeBtn = CTkButton(
        master=formFrame, width=200, text="update recipe", height=25, command=fetchMyRecipe)
    updateRecipeBtn.place(x=325, y=58)

    deleteRecipeBtn = CTkButton(
        master=formFrame, width=200, text="delete recipe", height=25, command=delete)
    deleteRecipeBtn.place(x=325, y=96)

    selectRecipeBtn = CTkButton(
        master=formFrame, width=200, text="select recipe", height=25, command=getMyRecipe)
    selectRecipeBtn.place(x=325, y=135)

    randomBtn = CTkButton(master=recipeViewFrame,
                          text="random recipe", width=240, command=randomRecipe)
    randomBtn.place(y=628, x=283)

    logoutBtn = CTkButton(master=recipeViewFrame,
                          text="log out", width=220, command=logout)
    logoutBtn.place(y=670, x=303)

    searchBtn = CTkButton(master=recipeViewFrame,
                          text="search", width=125, height=25, command=search)
    searchBtn.place(y=60, x=278)

    clearBtn = CTkButton(master=recipeViewFrame, text="clear all",
                         width=125, height=25, command=clearall)
    clearBtn.place(y=60, x=408)
    win3.mainloop()
