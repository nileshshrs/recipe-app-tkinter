from tkinter import *
from customtkinter import *
import customtkinter
from PIL import Image
import sqlite3
from main import mainScreen

textcolor = "whitesmoke"

try:
    cnxt = sqlite3.connect("data/userdata.db")
except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")
c = cnxt.cursor()
c.execute("CREATE TABLE IF NOT EXISTS userdata (USERNAME TEXT PRIMARY KEY NOT NULL UNIQUE, FIRSTNAME TEXT NOT NULL, LASTNAME TEXT NOT NULL, EMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL)")


def loginPage():
    global bgImage

    window = CTk()
    customtkinter.set_appearance_mode("dark")
    appWidth = 350
    appHeight = 500
    screenHeight = window.winfo_screenheight()
    screenWidth = window.winfo_screenwidth()
    centerX = (screenWidth/2)-(appWidth/2)
    centerY = (screenHeight/2)-(appHeight/2)
    window.geometry(f"{appWidth}x{appHeight}+{int(centerX)}+{int(centerY)}")
    window.resizable(False, False)
    window.title("login")

    def navigate():
        window.destroy()
        registerPage()

    def getUserData():
        global credentials
        username = usernameEntry.get().lower()
        password = passwordEntry.get()

        try:
            c.execute("select * from userdata where USERNAME='" +
                      username+"' and PASSWORD='"+password+"'")
            userdata = c.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing the database query: {e}")

        if userdata != []:
            for user in userdata:
                if username and password in user:
                    def fetchUser():
                        global credentials
                        window.destroy()
                        credentials = user[0]
                        mainScreen()
                    fetchUser()
        else:
            try:
                raise Exception("Username or password incorrect")
            except Exception as e:
                print(f"Error: {e}")
                errorLabel.configure(text=str(e), bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
                    
    frame1 = customtkinter.CTkFrame(
        window, height=appHeight, width=appWidth, bg_color="black")

    frame1.pack(fill="both")

    frame1.pack_propagate(False)

    loginLabel = customtkinter.CTkLabel(master=frame1, text="Sign In !", font=(
        "helvatica", 20, "bold"), text_color=textcolor)

    loginLabel.place(x=26, y=20)

    bgImage = customtkinter.CTkImage(
        light_image=Image.open("Assets/4.png"), size=(175, 141))

    imgWidget = customtkinter.CTkLabel(master=frame1, image=bgImage, text="")
    imgWidget.pack(pady=55, fill="both")

    errorLabel = customtkinter.CTkLabel(
        master=frame1, text="", width=300, height=25)
    errorLabel.place(y=200, x=25)

    usernameEntry = customtkinter.CTkEntry(
        master=frame1, placeholder_text="username", width=300, height=35,)
    usernameEntry.place(y=250, x=25)

    passwordEntry = customtkinter.CTkEntry(
        master=frame1, placeholder_text="password", width=300, height=35)
    passwordEntry.place(y=300, x=25)

    passwordEntry.configure(show="*")
    loginbtn = customtkinter.CTkButton(
        master=frame1, text="Login", width=300, height=30, command=getUserData)

    loginbtn.place(y=350, x=25)


    
    

    registerBtn = customtkinter.CTkButton(
        master=frame1, text="forgot password?", command=forgotPassword, width=140, height=25, hover=False, font=("", 12, "underline"), anchor=W, fg_color="#2B2B2B")
    registerBtn.place(x=25, y=390)

    rndmLabel=customtkinter.CTkLabel(master=frame1, height=2, width=340,fg_color="#2B2B2B", text="or")
    rndmLabel.place(y=415, x=5)

    forgotpasswordBtn = customtkinter.CTkButton(
        master=frame1, text="create account ?", height=30, command=navigate, width=300)
    forgotpasswordBtn.place(x=25, y=445)
    window.mainloop()


def registerPage():

    global registerImg

    window = CTk()
    customtkinter.set_appearance_mode("dark")
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
        loginPage()

    def getUserData():
        firstname = registerFirstName.get().lower()
        lastname = registerLastName.get().lower()
        username = registerusername.get().lower()
        email = registeremail.get().lower()
        password = registerpassword.get()
        confirmpassword = registerconfirmpassword.get()

        c.execute("select * from userdata where USERNAME='"+username+"'")

        dataResult = c.fetchall()
        userData = [
            (firstname),
            (lastname),
            (username),
            (email),
            (password),
        ]

        if dataResult == []:
            if firstname == "" or lastname == "" or username == "empty" or password == "" or email == "" or confirmpassword == "":
                errorLabel.configure(
                    text="please enter all the form fields", bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif len(firstname) <= 3 or len(lastname) <= 3 or len(username) <= 3:
                errorLabel.configure(text="username, firstname and lastname must be more than 3 letters",
                                     bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif "." and "@" not in email:
                errorLabel.configure(
                    text="invalid email address", bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif len(password) <= 5:
                errorLabel.configure(text="password must me longer than 5 character",
                                     bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif password != confirmpassword:
                errorLabel.configure(
                    text="password does not match", bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            else:
                c.execute(
                    "insert into userdata (FIRSTNAME, LASTNAME, USERNAME, EMAIL, PASSWORD) values(?,?,?,?,?)", (userData))
                cnxt.commit()
                errorLabel.configure(
                    text="registration successful", bg_color="lightgreen", text_color="darkgreen")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
        else:
            errorLabel.configure(text="username has already been taken, please select a new username",
                                 bg_color="lightpink", text_color="firebrick")
            errorLabel.after(5000, lambda: errorLabel.configure(
                text="", bg_color="#2B2B2B"))

        registerFirstName.delete(0, END)
        registerLastName.delete(0, END)
        registerusername.delete(0, END)
        registeremail.delete(0, END)
        registerpassword.delete(0, END)
        registerconfirmpassword.delete(0, END)

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
        master=formFrame, text="Sign up", width=417, height=30, command=getUserData)
    registerBtn.place(x=57, y=390)

    loginLabel = customtkinter.CTkLabel(
        master=formFrame, text="Already  have  an  account  ?", font=("helvatica", 16, "bold"))
    loginLabel.place(x=57, y=440)

    registerBtn = customtkinter.CTkButton(
        master=formFrame, text="login", width=200, command=navigate)
    registerBtn.place(x=270, y=440)

    window.mainloop()


def forgotPassword():
    window = customtkinter.CTkToplevel()
    customtkinter.set_appearance_mode("dark")
    appWidth = 490
    appHeight = 300
    screenHeight = window.winfo_screenheight()
    screenWidth = window.winfo_screenwidth()
    centerX = (screenWidth/2)-(appWidth/2)
    centerY = (screenHeight/2)-(appHeight/2)
    window.geometry(f"{appWidth}x{appHeight}+{int(centerX)}+{int(centerY)}")
    window.resizable(False, False)
    window.title("forgot password ?")

    mainFrame = customtkinter.CTkFrame(
        master=window, height=appHeight, width=appWidth)
    mainFrame.pack()
    mainFrame.pack_propagate(False)
    mainFrame.propagate(False)

    forgotPasswordTitle = customtkinter.CTkLabel(
        master=mainFrame, text="Forgot Password", font=("", 20, "bold"))
    forgotPasswordTitle.pack(pady=20)

    forgotPasswordDescription = customtkinter.CTkLabel(
        master=mainFrame, text="Lost your password? Please enter your username. You will\n be redirected to a new page to create a new password.", justify="center")
    forgotPasswordDescription.pack(pady=(0, 20))

    errorLabel = customtkinter.CTkLabel(
        master=mainFrame, text="", height=18, fg_color="#2C2B2C", width=300, text_color="#2C2B2C")
    errorLabel.pack(pady=(0,10))

    forgotPasswordEntry = customtkinter.CTkEntry(
        master=mainFrame, placeholder_text="username", width=300)
    forgotPasswordEntry.pack(pady=(0, 20))

    # function

    def getUsername():
        global forgot_username
        forgot_username = forgotPasswordEntry.get().lower()
        try:
            c.execute("select * from userdata where username='" +
                      forgot_username+"'")
            data = c.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing the database query: {e}")

        if data == []:
            errorLabel.configure(text="username not found", fg_color="lightpink", text_color="firebrick")
            errorLabel.after(5000, lambda: errorLabel.configure(text="", fg_color="#2B2B2B"))
            forgotPasswordEntry.delete(0, END)
        elif forgot_username == "":
            errorLabel.configure(text="username cannot be empty")
            errorLabel.after(5000, lambda: errorLabel.configure(text="", fg_color="#2B2B2B"))   
        else:
            for widgets in mainFrame.winfo_children():
                widgets.destroy()
            resetpasswordForm()

    def resetpasswordForm():
        forgotPasswordTitle = customtkinter.CTkLabel(
            master=mainFrame, text="Forgot Password", font=("", 20, "bold"))
        forgotPasswordTitle.pack(pady=20)

        forgotPasswordDescription = customtkinter.CTkLabel(
            master=mainFrame, text="Lost your password? Please enter your username. You will\n be redirected to a new page to create a new password.", justify="center")
        forgotPasswordDescription.pack(pady=(0, 20))

        errorLabel = customtkinter.CTkLabel(
            master=mainFrame, text="", height=18, fg_color="#2C2B2C", width=300, text_color="#2C2B2C")
        errorLabel.pack(pady=(0,10))

        forgotPasswordEntry = customtkinter.CTkEntry(
            master=mainFrame, placeholder_text="password", width=300)
        forgotPasswordEntry.pack(pady=(0, 20))
        forgotPasswordEntry.configure(show="*")

        forgotconfirmPasswordEntry = customtkinter.CTkEntry(
            master=mainFrame, placeholder_text="confirm-password", width=300)
        forgotconfirmPasswordEntry.pack(pady=(0, 20))
        forgotconfirmPasswordEntry.configure(show="*")

        ##inner function
        def submit():
            password=forgotPasswordEntry.get()
            confirmpassword=forgotconfirmPasswordEntry.get()

            if password=="" or confirmpassword=="":
                errorLabel.configure(text="password cannot be empty", text_color="firebrick", fg_color="pink")
                errorLabel.after(5000, lambda: errorLabel.configure(text="", fg_color="#2B2B2B"))
            else:
                if password!=confirmpassword:
                    errorLabel.configure(text="password does not match", text_color="firebrick", fg_color="pink")
                    errorLabel.after(5000, lambda: errorLabel.configure(text="", fg_color="#2B2B2B"))
                else:
                    c.execute("update userdata set PASSWORD=:newPassword WHERE USERNAME=:id", {
                    'newPassword': password, 'id': forgot_username})
                    cnxt.commit()
                    forgotPasswordEntry.delete(0, END)
                    forgotconfirmPasswordEntry.delete(0, END)
                    errorLabel.configure(text="password has been reset", text_color="darkgreen", fg_color="lightgreen")
                    errorLabel.after(5000, lambda: errorLabel.configure(text="", fg_color="#2B2B2B"))
                    window.after(3000, window.destroy)


        resetBtn = customtkinter.CTkButton(
        master=mainFrame, text="submit", height=25, command=submit, width=300)
        resetBtn.pack(pady=(0, 20))

    nextBtn = customtkinter.CTkButton(
        master=mainFrame, text="next", height=25, command=getUsername)
    nextBtn.pack(pady=(0, 20))
