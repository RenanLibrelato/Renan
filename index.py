#Importar as Bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar nossa Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

#Carregando Imagens
#logo = PhotoImage(file="icons/logo.png")


#Widget
LeftFrame = Frame(jan, width=200, height=300, bg="DARKCYAN", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="BLACK", relief="raise")
RightFrame.pack(side=RIGHT)

#LogoLabel = Label(LeftFrame, image=logo, bg="PURPLE")
#LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="BLACK", fg="WHITE")
UserLabel.place(x=5, y =159)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=155, y=170)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="BLACK", fg="WHITE")
PassLabel.place(x=5, y=209)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=155, y=220)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
        SELECT * FROM Users
        WHERE (User = ? and Password = ?)
        """, (User, Pass))
    print("Selecionou")
    VerifyLogin= DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo")
    except: 
        messagebox.showinfo(title="Login Info", message="Acesso Negado, Verifique se esta cadastrado no sitema")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=10, command=Login)
LoginButton.place(x=280, y=260)

def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo Widgets de Trabalho
    NomeLabel= Label(RightFrame, text= "Name:", font=("Century Gothic", 20), bg="BLACK", fg="white")
    NomeLabel.place(x=5, y=109)

    NomeEntry = Entry(RightFrame, width=30)
    NomeEntry.place(x=155, y=120)

    EmailLabel= Label(RightFrame, text= "Email:", font=("Century Gothic", 20), bg="BLACK", fg="white")
    EmailLabel.place(x=5, y=60)

    EmailEntry = Entry(RightFrame, width=30)
    EmailEntry.place(x=155, y=70)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preencha todos os campos")
        else:
            DataBaser.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
                """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada com Sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=15, command=RegisterToDataBase)
    Register.place(x=130, y=260)

    def BackToLogin():
        #Removendo Widget de Cadastro
    
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        #Trazendo de volta os Widget de Login
        LoginButton.place(x=280, y=260)
        RegisterButton.place(x=165, y=260)
        
    Back = ttk.Button(RightFrame, text="Back", width=10, command=BackToLogin)
    Back.place(x=280, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=10, command=Register)
RegisterButton.place(x=165, y=260)


jan.mainloop()