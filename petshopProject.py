from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb

ADMIN=1
GUEST=0
credentials={"admin":"admin123"}

def check_login(t1, t2):
    #check for credentials
    name=t1.get() #read the username from the entry
    pswd=t2.get() #read the password
    if name in credentials.keys():
        if credentials[name]==pswd:
            if name=="admin":
                main_menu(ADMIN)
            else:
                main_menu(GUEST)
        else:
            mb.showerror("Error","Incorrect Password!!!!")
    else:
        mb.showerror("Error","Incorrect Username!!!!")

#To destroy the previous frames
def fr_destroy():
    list = top.pack_slaves()
    for l in list:
        l.destroy()
    list = top.place_slaves()
    for l in list:
        l.destroy()
    list = top.grid_slaves()
    for l in list:
        l.destroy()

#display the login screen
def login():
    fr_destroy()
    
    frame=Frame(top, bg='LightCyan2', height=500, width=800)
    frame.pack()
    posx = 300
    posy = 40
    
    lbl=Label(frame, text="Login Details",bg="lightCyan2",fg="red2",width=15, font=(20))
    lbl.place(x=posx,y=posy)

    lbl1=Label(frame, text="Login",bg="lightCyan2",fg="blue",width=12)
    t1 = Entry(top)
    lbl1.place(x=posx-50,y=posy+150)
    t1.place(x=posx+50,y=posy+150)

    lbl2=Label(top, text="Password",bg="lightCyan2",fg="blue",width=12)
    t2 = Entry(top, show="*")
    lbl2.place(x=posx-50,y=posy+200)
    t2.place(x=posx+50,y=posy+200)
    
    button=Button(top, text="Submit",bg="SkyBlue1", command=lambda : check_login(t1,t2), width=20)
    button.place(x=posx,y=posy+300)
    
#To logout as ADMIN
def logout():
    main_menu(GUEST)
    
#Main Menu for performing the various operations
def main_menu(user):
    fr_destroy()
    frame=Frame(top, bg='LightCyan2', height=100, width=800)
    frame.pack(side=TOP)
    frame.pack_propagate(0)
    leftframe = Frame(top,bg='coral',width=600, height=400)
    leftframe.pack(side=LEFT)
    leftframe.pack_propagate(0)
    
    rightframe = Frame(top, bg='wheat1', width=200, height=400)
    rightframe.pack(side=RIGHT)
    rightframe.pack_propagate(0)    
   

    lbl=Label(frame, text="\n\nWELCOME TO THE PET SHOP",bg='LightCyan2', fg="blue",width=80, font=('Arial',16,'bold'))
    lbl.pack()
    #For guest user, only search option is enabled
    if user == GUEST:
        txt="GUEST"
        stat1=DISABLED
        stat2=NORMAL
    else:
        txt="ADMIN"
        stat1=NORMAL
        stat2=DISABLED
    lbl=Label(frame, text=txt,bg='LightCyan2', fg="blue2",width=10, font=('Arial',8,'bold'))
    lbl.place(x=650,y=10)
    bl1 = Button(frame, text="Login",bg="LightGreen",fg="red", width=7, command = login, state=stat2)
    bl1.place(x=640,y=30)
    bl2 = Button(frame, text="Logout",bg="LightGreen",fg="red", width=7, command = logout, state=stat1)
    bl2.place(x=710,y=30)

    image2 =Image.open(r"C:\Users\USER\Documents\classXII\petshop.jpg")
    image2.thumbnail((600,400))
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(leftframe, image=image1)
    background_label.image=image1
    background_label.pack()

    b1 = Button(rightframe, text="Add Pet", bg='yellow',fg="red", width=25, state =stat1,
                command=lambda :add_pet(user))
    b1.pack(padx=10, pady=10)
    b2 = Button(rightframe, text="Modify Pet", bg='yellow',fg="red", width=25, state=stat1, command=lambda:modify_pet(user))
    b2.pack(padx=10, pady=10)
    b3 = Button(rightframe, text="Delete Pet", bg='yellow',fg="red", width=25, state=stat1, 
                command=lambda:delete_pet(user))
    b3.pack(padx=10, pady=10)
    b4 = Button(rightframe, text="Search", bg='yellow',fg="red", width=25, command=lambda:search_pet(user))
    b4.pack(padx=10, pady=10)
    b5 = Button(rightframe, text="Exit", bg='yellow',fg="red", width=25, command=top.destroy)
    b5.pack(padx=10, pady=10)

#For inserting a record in the table
def insert_rec(entries, var):
    _id=int(entries[0].get())
    _type=entries[1].get()
    breed=entries[2].get()
    colour=entries[3].get()
    age=float(entries[4].get())
    height=float(entries[5].get())
    price=float(entries[6].get())
    gender=var.get()
    avail='Y'
    
    sql="insert into PET values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=_id,_type,breed,colour,age,height,price,gender,avail
    st = mycur.execute(sql,val)
    if st!=0:
        mb.showinfo("Status","Record has been successfully added")
    else:
        mb.showerror("Error","Record could not be added!!!!")
    mydb.commit()
    for e in entries:
        e.delete(0,'end')

#Displaying the screen for adding a pet
def add_pet(user):
    fr_destroy()
    frame=Frame(top, bg='LightCyan2', height=500, width=800)
    frame.pack()
    posx = 300
    posy = 40
    label_text=["ID (number)","Type","Breed","Colour","Age (years)","Height (cms)", "Price (Rs)"]
    labels=[]
    entries=[]
    
    lbl=Label(frame, text="ADD PET DETAILS",bg="lightCyan2",fg="red2",width=15, font=(16))
    lbl.place(x=posx+50,y=posy)
    posy+=50
    for l in label_text:
    
        lbl=Label(frame, text=l,bg="lightCyan2",fg="blue",width=12)
        t = Entry(frame, width=20)
        lbl.place(x=posx,y=posy)
        t.place(x=posx+100,y=posy)
        posy+=40
        labels.append(lbl)
        entries.append(t)
    var = StringVar()
    lbl=Label(frame, text="Gender",bg="lightCyan2",fg="blue",width=12)
    lbl.place(x=posx,y=posy)
    R1 = Radiobutton(frame, text="MALE", bg="lightCyan2",fg="blue", variable=var, value='M')
    R1.select()
    R1.place(x=posx+100, y=posy)
    R2 = Radiobutton(frame, text="FEMALE", bg="lightCyan2",fg="blue", variable=var, value='F')
    R2.place(x=posx+170, y=posy)
    R2.deselect()
    button=Button(frame, text="Submit",bg="SkyBlue1", command=lambda : insert_rec(entries,var), width=15)
    button.place(x=posx, y=posy+50)
    button=Button(frame, text="Back",bg="SkyBlue1", width=15, command=lambda:main_menu(user))
    button.place(x=posx+150, y=posy+50)

#Display the records
def display_recs(mycur,user):
    fr_destroy()
    frame=Frame(top, bg='LightCyan2', height=400, width=800)
    frame.pack()
    
    label_text=["ID","Type","Breed","Colour", "Age (years)","Height (cms)", "Price (Rs)","Gender", "Availability"]
    
    
    lbl=Label(frame, text="PET DETAILS",bg="lightCyan2",fg="red2",width=15, font=("bold",16))
    lbl.grid(row=0,column=4, pady=15)
    r=2
    c=0
    for l in label_text:
        lbl=Label(frame, text=l ,bg="lightCyan2",fg="blue",width=10)
        lbl.grid(row=r,column=c,pady=5)
        c+=1
    
    r+=1
    c=0
    for rec in mycur: 
        for word in rec:
            lbl=Label(frame, text=word,bg="lightCyan2",fg="black",width=10)
            lbl.grid(row=r,column=c,pady=5)
            c+=1
        r+=1
        c=0
    r+=1
    bframe=Frame(top, bg='LightCyan2', height=400, width=800)
    bframe.pack(side=BOTTOM)
    button=Button(bframe, text="Back",bg="SkyBlue1", width=15, command=lambda:main_menu(user))
    button.place(x=350, y=200)

#Search record
def search_rec(entries,user):
    _id=entries[0].get()
    
    if len(_id) != 0:
        _id=int(_id)
        sql="select * from PET where id = %s"
        val=_id
    else:
        _type=entries[1].get()
        if len(_type) != 0:
            sql="select * from PET where type LIKE %s"
            val="%"+_type+"%"
        else:
            _breed=entries[2].get()
            if len(_breed) != 0:
                sql="select * from PET where breed LIKE %s"
                val="%"+_breed+"%"
            else:
                _colour=entries[3].get()
                if len(_colour) != 0:
                    sql="select * from PET where colour LIKE %s"
                    val="%"+_colour+"%"
                else:
                    sql="select * from PET"
    
    st = mycur.execute(sql,val)
    if st!=0:
        display_recs(mycur,user)
    else:
        mb.showerror("Error","No record found!!!")

#Display frame to enter the search string
def search_pet(user):
    fr_destroy()
    frame=Frame(top, bg='LightCyan2', height=500, width=800)
    frame.pack()
    posx = 300
    posy = 40
    label_text=["ID (number)","Type","Breed","Colour"]
    labels=[]
    entries=[]
    
    lbl=Label(frame, text="SEARCH PET",bg="lightCyan2",fg="red2",width=15, font=(16))
    lbl.place(x=posx+50,y=posy)
    posy+=50
    for l in label_text:
    
        lbl=Label(frame, text=l,bg="lightCyan2",fg="blue",width=12)
        t = Entry(frame, width=20)
        lbl.place(x=posx,y=posy)
        t.place(x=posx+100,y=posy)
        posy+=40
        labels.append(lbl)
        entries.append(t)
    
    button=Button(frame, text="Search",bg="SkyBlue1", command=lambda : search_rec(entries,user), width=15)
    button.place(x=posx, y=posy+50)
    button=Button(frame, text="Back",bg="SkyBlue1", width=15, command=lambda:main_menu(user))
    button.place(x=posx+150, y=posy+50)

#Search Id in the tabl;e
def search_id(frame,entries, button):
    _id=entries[0].get()
    
    if len(_id) != 0:
        _id=int(_id)
        sql="select * from PET where id = %s"
        val=_id
    else:
        mb.showinfo("Status","Enter the id of the Pet to be modified/deleted")
        return
    
    st = mycur.execute(sql,val)
    if st==0:
        mb.showinfo("Status","The id does not exist!!!")
        return
    for rec in mycur:
        for i in range(1,len(entries)):
            entries[i]["state"]="normal"
            entries[i].delete(0,'end')
            entries[i].insert(0,rec[i])
    
    button["state"]="normal"
    
#Modify record in the table
def modify_rec(entries,button):
    _id=int(entries[0].get())
    _type=entries[1].get()
    breed=entries[2].get()
    colour=entries[3].get()
    age=float(entries[4].get())
    height=float(entries[5].get())
    price=float(entries[6].get())
    gender=entries[7].get()
    avail=entries[8].get()
    
    sql="update PET set type=%s,breed=%s,colour=%s,age=%s,height=%s,price=%s,gender=%s,avail=%s where id=%s"
    val=_type,breed,colour,age,height,price,gender,avail,_id
    st = mycur.execute(sql,val)
    if st!=0:
        mb.showinfo("Status","Record has been successfully modified")
        mydb.commit()
    else:
        mb.showinfo("Status","Record could not be modified!!!!")
    
    for e in entries:
        e.delete(0,'end')
    button["state"]="disabled"

#Display screen for modifying the pet details
def modify_pet(user):
    fr_destroy()
    frame=Frame(top, bg='LightCyan2', height=500, width=800)
    frame.pack()
    posx = 300
    posy = 20
    label_text=["Type","Breed","Colour","Age (years)","Height (cms)", "Price (Rs)", "Gender", "Availability"]
    labels=[]
    entries=[]
    
    lbl=Label(frame, text="MODIFY PET DETAILS",bg="lightCyan2",fg="red2",width=25, font=(16))
    lbl.place(x=posx,y=posy)
    posy+=50
    lbl=Label(frame, text="ID (number)",bg="lightCyan2",fg="blue",width=12)
    t = Entry(frame, width=20)
    lbl.place(x=posx,y=posy)
    t.place(x=posx+100,y=posy)
    labels.append(lbl)
    entries.append(t)
    posy+=40
    for l in label_text:
        lbl=Label(frame, text=l,bg="lightCyan2",fg="blue",width=12)
        t = Entry(frame, width=20,state="disabled")
        lbl.place(x=posx,y=posy)
        t.place(x=posx+100,y=posy)
        posy+=40
        labels.append(lbl)
        entries.append(t)
        
    button1=Button(frame, text="Search",bg="SkyBlue1", command=lambda : search_id(frame,entries,button2), width=15)
    button1.place(x=posx-150, y=posy)
    button2=Button(frame, text="Modify",bg="SkyBlue1", command=lambda : modify_rec(entries, button2), width=15)
    button2.place(x=posx, y=posy)
    button2["state"]="disabled"
    button3=Button(frame, text="Back",bg="SkyBlue1", width=15, command=lambda:main_menu(user))
    button3.place(x=posx+150, y=posy)

#Delete record from the table
def delete_rec(entries,button):
    
    confirm = mb.askyesno("Delete","Are you sure you want to delete this record?")
    if confirm:
        _id=int(entries[0].get())
    
        sql="delete from PET where id=%s"
        val=_id
        st = mycur.execute(sql,val)
        if st!=0:
            mb.showinfo("Status","Record has been successfully deleted")
            mydb.commit()
        else:
            mb.showerror("Status","Record could not be deleted!!!!")
    
    for e in entries:
        e.delete(0,'end')
    button["state"]="disabled"

#Display screen for deleting a record
def delete_pet(user):
    fr_destroy()
    frame=Frame(top, bg='LightCyan2', height=500, width=800)
    frame.pack()
    posx = 300
    posy = 20
    label_text=["Type","Breed","Colour","Age (years)","Height (cms)", "Price (Rs)", "Gender", "Availability"]
    labels=[]
    entries=[]
    
    lbl=Label(frame, text="DELETE PET",bg="lightCyan2",fg="red2",width=25, font=(16))
    lbl.place(x=posx,y=posy)
    posy+=50
    lbl=Label(frame, text="ID (number)",bg="lightCyan2",fg="blue",width=12)
    t = Entry(frame, width=20)
    lbl.place(x=posx,y=posy)
    t.place(x=posx+100,y=posy)
    labels.append(lbl)
    entries.append(t)
    posy+=40
    for l in label_text:
        lbl=Label(frame, text=l,bg="lightCyan2",fg="blue",width=12)
        t = Entry(frame, width=20,state="disabled")
        lbl.place(x=posx,y=posy)
        t.place(x=posx+100,y=posy)
        posy+=40
        labels.append(lbl)
        entries.append(t)
        
    button1=Button(frame, text="Search",bg="SkyBlue1", command=lambda : search_id(frame,entries,button2), width=15)
    button1.place(x=posx-150, y=posy)
    button2=Button(frame, text="Delete",bg="SkyBlue1", command=lambda : delete_rec(entries, button2), width=15)
    button2.place(x=posx, y=posy)
    button2["state"]="disabled"
    button3=Button(frame, text="Back",bg="SkyBlue1", width=15, command=lambda:main_menu(user))
    button3.place(x=posx+150, y=posy)


#main
top = Tk()

top.title("PET SHOP")
top.geometry("800x500")
top.resizable(0,0)
main_menu(GUEST)
top.mainloop()
