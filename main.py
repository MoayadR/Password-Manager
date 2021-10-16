from tkinter import *
from PIL import ImageTk,Image
import string
import secrets

root = Tk()

root.title("The Vault")
root.geometry("550x550")
root.config(bg="Black")

root.iconbitmap("Resources/icon.ico")

image1 = Image.open("Resources/Space.jpg")

test = ImageTk.PhotoImage(image1)

label1 = Label(image=test )
label1.image = test
label1.pack()


file =open("The Vault Note.txt" , "a")
file =open("The Vault Note.txt" , "r")
line_number =0
for line in file:
    line_number +=1
    data = line.split("./")
file.close()
    


def Encrypt(text):

    Encrypted = ""
    steplower=7
    stepdigit =9
    stepupper =4
    stepspecial1=6
    stepspecial2 =5
    stepspecial3=3

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            Encrypted += chr((ord(char) + stepupper-65) % 26 + 65)
 
        elif (char.islower()):
            Encrypted += chr((ord(char) + steplower - 97) % 26 + 97)

        elif (char.isdigit()):
            Encrypted += chr((ord(char) + stepdigit -48) % 10 + 48)

        elif (ord(char) >=58 and ord(char) <=64 ):
            Encrypted += chr((ord(char) + stepspecial1 -58) % 7 + 58)

        elif (ord(char) >=33 and ord(char) <=46 ):
            Encrypted += chr((ord(char) + stepspecial2 -33) % 14 + 33)    

        elif (ord(char) >=91 and ord(char) <=96 ):
            Encrypted += chr((ord(char) + stepspecial1 -91) % 6 + 91)

        elif (ord(char) >=123 and ord(char) <=126 ):
            Encrypted += chr((ord(char) + stepspecial3 -123) % 4 + 123)          
 
    return Encrypted


def Decrypt(text):

    Decrypted = ""
    steplower=7
    stepdigit =9
    stepupper =4
    stepspecial1=6
    stepspecial2 =5
    stepspecial3=3

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            Decrypted += chr((ord(char) - stepupper-65 +26) % 26 + 65)
 
        elif (char.islower()):
            Decrypted += chr((ord(char) - steplower - 97 +26) % 26 + 97)

        elif (char.isdigit()):
            Decrypted += chr((ord(char) - stepdigit -48 +10) % 10 + 48)

        elif (ord(char) >=58 and ord(char) <=64 ):
            Decrypted += chr((ord(char) - stepspecial1 -58 +7) % 7 + 58)

        elif (ord(char) >=33 and ord(char) <=46 ):
            Decrypted += chr((ord(char) - stepspecial2 -33 +14) % 14 + 33)    

        elif (ord(char) >=91 and ord(char) <=96 ):
            Decrypted += chr((ord(char) - stepspecial1 -91 +6) % 6 + 91)

        elif (ord(char) >=123 and ord(char) <=126 ):
            Decrypted += chr((ord(char) - stepspecial3 -123 +4) % 4 + 123)          
 
    return Decrypted






def MakeMasterPasswordScreen(Encrypt , Decrypt):
    
    root.geometry("550x550")
    root.config(bg = "Black")
    
    label2 = Label(root, text = "Make Your Master Password")
    label2.config( anchor = CENTER)
    label2.pack()

    entry1 = Entry(root, show = '*')
    entry1.pack()
    entry1.focus()

    label3 = Label(root, text = "Re Enter Your Master Password")
    label3.config( anchor = CENTER)
    label3.pack()

    entry2 = Entry(root, show = '*')
    entry2.pack()


    def MakeMasterPassword():
        if entry1.get() != entry2.get():
            label2.config(text = "The Passwords Doesn't match")
            label2.pack()
            entry1.delete(0,"end")
            entry2.delete(0,"end")
        else:
            masterpassword = entry1.get()
            file = open("The Vault Note.txt" , "a")
            file.write(Encrypt(masterpassword) +'./')
            file.close()
            loginScreen(Encrypt, Decrypt)


    button = Button(root, text = "Make!" , command=lambda: MakeMasterPassword() )
    button.config(anchor= S)
    button.pack()


def loginScreen(Encrypt, Decrypt):
    root.geometry("600x600")

    masterkey_label= Label(root , text = "Enter The Master Password")
    masterkey_label.config(anchor = CENTER)
    masterkey_label.pack()
    masterkey_entery = Entry(root ,show = '*' )
    masterkey_entery.pack()
    masterkey_entery.focus()

    

    def LoginScreenValidation():
        
        file =open("The Vault Note.txt" , "r")
        for line in file:
            data = line.split("./")
        file.close()

        Password = Decrypt(data[0])
        if Password == masterkey_entery.get():
            TheVault(Encrypt, Decrypt)
            
        else:
            masterkey_label.config(text="Wrong Password! Nice Try ")
            masterkey_entery.delete(0,"end")
               


    button1= Button(root,text = "Enter!" , width = 10 , height = 5 ,command =lambda: LoginScreenValidation())
    button1.pack()


def TheVault(Encrypt, Decrypt):
    for widget in root.winfo_children():
        widget.destroy()

    root.config(bg="White")
    root.geometry("800x600")

    name=""
    username=""
    password=""

    label2 = Label(root,text="Welcome To Paradise .",font= 24)
    label2.pack(side=TOP , anchor=CENTER)

    file =open("The Vault Note.txt" , "r")
    for line in file:
        data = line.split("./")

    numberofpasswords = 0
    for password in data:
        numberofpasswords = numberofpasswords +1

    numberofpasswords = numberofpasswords -2
    file.close()

    def NewPassWindow(name,username,password,count ,line,DisplayList):
        window =Tk()
        window.title("Make A Password")
        window.geometry("250x250")
        window.iconbitmap("Resources/icon.ico")
        lblname = Label(window,anchor=CENTER, text= "Enter The Name of the Website or Game")
        lblname.pack()
        entry1= Entry(window)
        entry1.pack()

        lblusername = Label(window,anchor=CENTER, text= "Enter The Username/Email")
        lblusername.pack()
        entry2= Entry(window)
        entry2.pack()
        
        lblpassword = Label(window,anchor=CENTER, text= "Enter The Password")
        lblpassword.pack()
        entry3= Entry(window)
        entry3.pack()

        def MakePassword(name,username,password,count ,line,DisplayList):
            name = entry1.get()
            username = entry2.get()
            password = entry3.get()

            file =open("The Vault Note.txt" , "a")
            file.write(Encrypt(name) +'./'+Encrypt(username)+'./'+Encrypt(password)+'./')
            file.close()
            
            window.destroy()
            TheVault(Encrypt, Decrypt)

        btn= Button(window,text="Make!" ,command= lambda : MakePassword(name,username,password,count ,line,DisplayList) )
        btn.pack()

        def GenerateRandom():
            random_password = ""
            for x in range(15):
                random_password = random_password + ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation ) )
            entry3.delete(first=0,last=100)
            entry3.insert(0,random_password)

        btngenerator = Button(window,text = "Generate A Strong Password!" , command= lambda:GenerateRandom())
        btngenerator.pack(side=BOTTOM )
        



    scrol=Scrollbar(root)
    scrol.pack(fill=Y , side=RIGHT)
    

    count=1
    DisplayList=Listbox(root , height= 30)
    DisplayList.pack(fill=BOTH )
    line=0
    countpassword =count+2
    for i in range(0,int (numberofpasswords/3)):
        DisplayList.insert(line,"Name Of Website/Game: "+Decrypt(data[count]) +"        " +"The Username/Email: " + Decrypt(data[count+1]) +"        " + "The Password: " +Decrypt(data[count+2]) + "        " + "The Password NO: " + str(countpassword)) 
        count = count+3
        countpassword = countpassword +3
        line = line+1

    

    
    def AboutMe():
        window =Toplevel()
        window.geometry("400x100")
        window.title("About Me")
        window.iconbitmap("Resources/icon.ico")
        Me = Label(window , text="Made by MoayadRida " , font=16)
        Me.pack(anchor=NW)
        Me = Label(window , text="For Contanct :" ,font = 12)
        Me.pack(anchor=NW)
        Me = Label(window , text="E-mail : moayad.r.abdalraouf@gmail.com" ,font = 12)
        Me.pack(anchor=NW)
       



    def DeleteLine():
        window =Tk()
        window.title("Delete A Password Line")
        window.geometry("250x200")
        window.iconbitmap("Resources/icon.ico")
        lblname = Label(window,anchor=CENTER, text= "Enter The NO Of Password")
        lblname.pack()
        entry1= Entry(window)
        entry1.pack()

        def Deletefun():
            index = int(entry1.get())
            if index !=0:
                data.pop(index)
                data.pop(index-1)
                data.pop(index-2)

                file =open("The Vault Note.txt" , "w")
                file.close()


                file =open("The Vault Note.txt" , "a")

                numberofpasswords = 0
                for password in data:
                    numberofpasswords = numberofpasswords +1

                numberofpasswords = numberofpasswords -2

                count =0
                for i in range(0,int (numberofpasswords+1)):
                    file.write(data[count] +'./')
                    count = count +1  


                file.close()
                TheVault(Encrypt,Decrypt) 
                    
                    

                

            else:
                lblname.config(text="Cannot Delete Password NO 0 As It Is The MasterPassword")


        button = Button(window ,text="Delete!" ,bg="Red" ,width=10 ,command=lambda:Deletefun())
        button.pack(anchor=CENTER)




        



    btn = Button(root, anchor=S , text= "Make A New Password" , command= lambda : NewPassWindow(name,username,password ,count ,line,DisplayList ))
    btn.pack(side=TOP , anchor=CENTER)

    btndeletepass = Button(root,bg="Red", anchor=S , text= "Delete A Line" , command= lambda:DeleteLine() )
    btndeletepass.pack(side=TOP , anchor=CENTER)

    scrol.config(command=DisplayList.yview())

    btn = Button(root, text= "About Me" , command= lambda:AboutMe())
    btn.pack(anchor=CENTER)

    





if line_number !=0 :
    loginScreen(Encrypt, Decrypt)
else:
    MakeMasterPasswordScreen(Encrypt, Decrypt)

    
    

root.mainloop()