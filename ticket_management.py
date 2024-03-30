from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter
import sqlite3


root=Tk()
root.title("Rtms")
root.geometry("1550x800+0+0")

#=================================Database==========================================================
# Create a database and connect to one
conn=sqlite3.connect('railway.db')

# Create Cursor
c=conn.cursor()

#Create table
'''
c.execute("""CREATE TABLE railways12(
    Reservation_Quota text,
    Name text,
    sex text,
    Age integer,
    Phone_num integer,
    Train_num integer,
    Train_Name text,
    class text,
    berth text,
    Source text,
    Destination text,
    Date text,
    Time text,
    Food text,
    Amount integer
)
""")
'''


# ================================Functions==========================================================


def pick_date(event=""):
    global cal,top
    top=Toplevel()
    #date_window.grab_set()
    top.title("Choose the date")
    top.geometry("250x220+590+370")
    cal=Calendar(top,selectmode="day",date_pattern="dd/mm/y")
    cal.pack()
    submit_btn=Button(top,text="Submit",command=grab_date)
    submit_btn.pack()

def grab_date():
    global cal,top
    date_box.delete(0,END)
    date_box.insert(0,cal.get_date())
    top.destroy()

def trainsec():
    if (src_ch.get()=="Select anyone"):
        messagebox.showwarning("Error","Please select source ")
        return
    elif (des_ch.get()=="Select anyone"):
        messagebox.showwarning("Error","Please destination source ")
        return
    elif (src_ch.get()==des_ch.get()):
        messagebox.showwarning("Error","Please select different locations")
        return

    train_list=['Deccan Odyssey','The Golden Chariot','Maharajas Express','Duronto Express','Garib Rath','Tejas Express','Shatabdi Express',
            'Vande Bharat Express','Rajdhani Express','Yuva Express','Antyodaya Express','Kavi Guru Express','Humsafar Express',
            'Vivek Express','Mahamana Express','Rajya Rani Express','Uday Express','Suvidha Express','Gatimaan Express','Himsagar Express',
            'Jan Sadharan Express','Double Decker Express','Ajanta Express','Amritsar Mail']
    
    def select_train(event=""):
        k=0
        if(r==1):
            k=200
        # "EC","1AC","2AC","3AC","SL","2S"
        l=0;
        if(clicked3=="EC"):
            l=1700
        elif(clicked3=="1AC"):
            l=1500
        elif(clicked3=="2AC"):
            l=1200
        elif(clicked3=="3AC"):
            l=1000
        elif(clicked3=="SL"):
            l=500
        elif(clicked3=="2S"):
            l=300

        value=str(train_listbox.get(train_listbox.curselection()))
        x=value
        if(x=='Deccan Odyssey'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"A001")
            train_name_box.insert(0,'Deccan Odyssey')
            time_box.insert(0,'01:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='The Golden Chariot'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"B002")
            train_name_box.insert(0,'The Golden Chariot')
            time_box.insert(0,'02:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Maharajas Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"C003")
            train_name_box.insert(0,'Maharajas Express')
            time_box.insert(0,'03:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Duronto Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"D004")
            train_name_box.insert(0,'Duronto Express')
            time_box.insert(0,'04:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Garib Rath'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"E005")
            train_name_box.insert(0,'Garib Rath')
            time_box.insert(0,'05:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Tejas Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"F006")
            train_name_box.insert(0,'Tejas Express')
            time_box.insert(0,'06:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Shatabdi Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"G007")
            train_name_box.insert(0,'Shatabdi Express')
            time_box.insert(0,'07:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Vande Bharat Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"H008")
            train_name_box.insert(0,'Vande Bharat Express')
            time_box.insert(0,'08:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Rajdhani Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"I009")
            train_name_box.insert(0,'Rajdhani Express')
            time_box.insert(0,'09:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Yuva Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"J010")
            train_name_box.insert(0,'Yuva Express')
            time_box.insert(0,'10:00')  
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))  

        elif(x=='Antyodaya Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"K011")
            train_name_box.insert(0,'Antyodaya Express')
            time_box.insert(0,'11:00') 
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Kavi Guru Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"L012")
            train_name_box.insert(0,'Kavi Guru Express')
            time_box.insert(0,'12:00') 
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Humsafar Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"M013")
            train_name_box.insert(0,'Humsafar Express')
            time_box.insert(0,'13:00') 
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))   

        elif(x=='Vivek Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"N014")
            train_name_box.insert(0,'Vivek Express')
            time_box.insert(0,'14:00') 
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Mahamana Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"P015")
            train_name_box.insert(0,'Mahamana Express')
            time_box.insert(0,'15:00') 
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt)) 

        elif(x=='Rajya Rani Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"R016")
            train_name_box.insert(0,'Rajya Rani Express')
            time_box.insert(0,'16:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Uday Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"S017")
            train_name_box.insert(0,'Uday Express')
            time_box.insert(0,'17:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Suvidha Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"T018")
            train_name_box.insert(0,'Suvidha Express')
            time_box.insert(0,'18:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))    

        elif(x=='Gatimaan Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"U019")
            train_name_box.insert(0,'Gatimaan Express')
            time_box.insert(0,'19:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Himsagar Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"V020")
            train_name_box.insert(0,'Himsagar Express')
            time_box.insert(0,'20:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Jan Sadharan Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"W021")
            train_name_box.insert(0,'Jan Sadharan Express')
            time_box.insert(0,'21:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Double Decker Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"X022")
            train_name_box.insert(0,'Double Decker Express')
            time_box.insert(0,'22:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Ajanta Express'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"Y023")
            train_name_box.insert(0,'Ajanta Express')
            time_box.insert(0,'23:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))

        elif(x=='Amritsar Mail'):
            train_no_box.delete(0,END)
            train_name_box.delete(0,END)
            time_box.delete(0,END)
            Amount_box.delete(0,END)
            train_no_box.insert(0,"Z024")
            train_name_box.insert(0,'Amritsar Mail')
            time_box.insert(0,'00:00')
            amt=random.randint(2000,3500)+l+k
            Amount_box.insert(0,str(amt))
    
    train_listbox=Listbox(dataframeright,font=("arial",12,"bold"),width=20,height=16)
    train_listbox.bind("<<ListboxSelect>>",select_train)
    train_listbox.grid(row=0,column=0,padx=4)
    train_list_scroll.config(command=train_listbox.yview)

    l=random.choices(train_list,k=random.randint(1,7))
    for item in l:
        train_listbox.insert(END,item)
    


def add():
    # Create a database and connect to one
    conn=sqlite3.connect('railway.db')

    # Create Cursor
    c=conn.cursor()

    # Insert into table
    c.execute("INSERT INTO railways12 VALUES(:Reserve_Quota,:Name,:Sex,:Age,:Phone_num,:Train_num,:Train_name,:class,:berth,:source,:destination,:date,:time,:food,:Amount)",
              
              {
                  'Reserve_Quota':clicked1.get(),
                  'Name':name_box.get(),
                  'Sex':clicked2.get(),
                  'Age':age_box.get(),
                  'Phone_num':phone_box.get(),
                  'Train_num':train_no_box.get(),
                  'Train_name':train_name_box.get(),
                  'class':clicked3.get(),
                  'berth':clicked4.get(),
                  'source':src_ch.get(),
                  'destination':des_ch.get(),
                  'date':date_box.get(),
                  'time':time_box.get(),
                  'food':r.get(),
                  'Amount':Amount_box.get()
              }        
            )


    #Commit Changes
    conn.commit()

    # Close Connection
    conn.close

    messagebox.showinfo("Success","Member has been inserted successfully");
    # Clear the text boxes
    reset()
    return  
    
def show():
    for item in root.lib_table.get_children():
        root.lib_table.delete(item)

     # Create a database and connect to one
    conn=sqlite3.connect('railway.db')

    # Create Cursor
    c=conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM railways12")   # In sqllite3 ,it automatically made the primary key .oid- refers to primary key
    records=c.fetchall()  # fetch all records, fetchmany-fetch selected records, fetchone-fetch 1st record
    #print(records)

    #Loop through results
    print_rec=''

    for record in records:
        root.lib_table.insert("",END,values=record)


    #Commit Changes
    conn.commit()

    # Close Connection
    conn.close
    return

def get_cursor(event=""):
    textbox.delete("1.0","end")
    cursor_row=root.lib_table.focus()
    content=root.lib_table.item(cursor_row)
    row=content['values']
    textbox.insert(END,"Reservation Quota : "+row[0]+"\n")
    textbox.insert(END,"Name : "+row[1]+"\n")
    textbox.insert(END,"Sex : "+row[2]+"\n")
    textbox.insert(END,"Age : "+str(row[3])+"\n")
    textbox.insert(END,"Phone number : "+str(row[4])+"\n")
    textbox.insert(END,"Train number : "+row[5]+"\n")
    textbox.insert(END,"Train name : "+row[6]+"\n")
    textbox.insert(END,"Class : "+row[7]+"\n")
    textbox.insert(END,"Berth : "+row[8]+"\n")
    textbox.insert(END,"Source : "+row[9]+"\n")
    textbox.insert(END,"Destination : "+row[10]+"\n")
    textbox.insert(END,"Date : "+row[11]+"\n")
    textbox.insert(END,"Time : "+row[12]+"\n")
    textbox.insert(END,"Food : "+str(row[13])+"\n")
    textbox.insert(END,"Amount : "+str(row[14])+"\n")

    # Clear the text boxes
    clicked1.set("Select anyone")
    name_box.delete(0,END)
    clicked2.set("Select anyone")
    age_box.delete(0,END)
    phone_box.delete(0,END)
    train_no_box.delete(0,END)
    train_name_box.delete(0,END)
    clicked3.set("Select anyone")
    clicked4.set("Select anyone")
    src_ch.set("Select anyone")
    des_ch.set("Select anyone")
    date_box.delete(0,END)
    time_box.delete(0,END)
    Amount_box.delete(0,END)
    r.set(0)

    # put values
    clicked1.set(row[0])
    name_box.insert(0,row[1])
    clicked2.set(row[2])
    age_box.insert(0,row[3])
    phone_box.insert(0,row[4])
    train_no_box.insert(0,row[5])
    train_name_box.insert(0,row[6])
    clicked3.set(row[7])
    clicked4.set(row[8])
    src_ch.set(row[9])
    des_ch.set(row[10])
    date_box.insert(0,row[11])
    time_box.insert(0,row[12])
    r.set(row[13])
    Amount_box.insert(0,row[14])
    global zz
    zz=row[15]
    
def update():
    # Create a database and connect to one
    conn=sqlite3.connect('railway.db')

    # Create Cursor
    c=conn.cursor()

    # Insert into table
    c.execute("""UPDATE  railways12 SET
              Reservation_Quota=:Reserve_Quota,
              Name=:Name,
              sex=:Sex,
              Age=:Age,
              Phone_num=:Phone_num,
              Train_num=:Train_num,
              Train_Name=:Train_name,
              class=:class,
              berth=:berth,
              Source=:source,
              Destination=:destination,
              Date=:date,
              Time=:time,
              Food=:food,
              Amount=:Amount
              where oid=:oid
              """,
              {
                  'Reserve_Quota':clicked1.get(),
                  'Name':name_box.get(),
                  'Sex':clicked2.get(),
                  'Age':age_box.get(),
                  'Phone_num':phone_box.get(),
                  'Train_num':train_no_box.get(),
                  'Train_name':train_name_box.get(),
                  'class':clicked3.get(),
                  'berth':clicked4.get(),
                  'source':src_ch.get(),
                  'destination':des_ch.get(),
                  'date':date_box.get(),
                  'time':time_box.get(),
                  'food':r.get(),
                  'Amount':Amount_box.get(),
                  'oid':zz
              }        
            )


    #Commit Changes
    conn.commit()

    # Close Connection
    conn.close

    show() # to show the updated value

    messagebox.showinfo("Success","Member has been updated!")

    # Clear the text boxes
    clicked1.set("Select anyone")
    name_box.delete(0,END)
    clicked2.set("Select anyone")
    age_box.delete(0,END)
    phone_box.delete(0,END)
    train_no_box.delete(0,END)
    train_name_box.delete(0,END)
    clicked3.set("Select anyone")
    clicked4.set("Select anyone")
    src_ch.set("Select anyone")
    des_ch.set("Select anyone")
    date_box.delete(0,END)
    time_box.delete(0,END)
    Amount_box.delete(0,END)
    r.set(0)
    return  
       
def reset():
    train_list=['Deccan Odyssey','The Golden Chariot','Maharajas Express','Duronto Express','Garib Rath','Tejas Express','Shatabdi Express',
            'Vande Bharat Express','Rajdhani Express','Yuva Express','Antyodaya Express','Kavi Guru Express','Humsafar Express',
            'Vivek Express','Mahamana Express','Rajya Rani Express','Uday Express','Suvidha Express','Gatimaan Express','Himsagar Express',
            'Jan Sadharan Express','Double Decker Express','Ajanta Express','Amritsar Mail']

    train_listbox=Listbox(dataframeright,font=("arial",12,"bold"),width=20,height=16)
    #train_listbox.bind("<<ListboxSelect>>",select_train)
    train_listbox.grid(row=0,column=0,padx=4)
    train_list_scroll.config(command=train_listbox.yview)
    
    for item in train_list:
        train_listbox.insert(END,item)

    # Clear the text boxes
    clicked1.set("Select anyone")
    name_box.delete(0,END)
    clicked2.set("Select anyone")
    age_box.delete(0,END)
    phone_box.delete(0,END)
    train_no_box.delete(0,END)
    train_name_box.delete(0,END)
    clicked3.set("Select anyone")
    clicked4.set("Select anyone")
    src_ch.set("Select anyone")
    des_ch.set("Select anyone")
    date_box.delete(0,END)
    time_box.delete(0,END)
    Amount_box.delete(0,END)
    r.set(0)
    textbox.delete("1.0",END)
    return  

def delete():
    # Create a database and connect to one
    conn=sqlite3.connect('railway.db')

    # Create Cursor
    c=conn.cursor()

    # Delete into table
    c.execute("DELETE FROM railways12 WHERE oid="+str(zz))


    #Commit Changes
    conn.commit()

    # Close Connection
    conn.close

    reset()
    show()
    messagebox.showinfo("Success","Member has been deleted!")
    return

def exit():
    iExit=tkinter.messagebox.askyesno("Railway management system","Do you want to exit")
    if iExit>0:
        root.destroy()
        return
    else:
        return
#=======================================================================================================
lbltitle=Label(root,text="TICKET MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
lbltitle.pack(side=TOP,fill=X)

frame=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
frame.place(x=0,y=130,width=1530,height=400)

#====================data frame left ==============
dataframeleft=LabelFrame(frame,text="Customer Information",bg="powder blue",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
dataframeleft.place(x=0,y=5,width=900,height=350)


lblquota=Label(dataframeleft,text="Reservation Quota",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
lblquota.grid(row=0,column=0,sticky=W)

option1=["General","Ladies","Defence","Parliament house","Physically handicapped","Senior citizen","Foreign tourist","Railway employee"]
clicked1=StringVar()
clicked1.set("Select anyone")

Quota_menu=OptionMenu(dataframeleft,clicked1,*option1)
Quota_menu.config(bg="white",fg="black",font=("arial",10,"bold"),width=20)
Quota_menu.grid(row=0,column=1,padx=25)


name=Label(dataframeleft,text="Name",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
name.grid(row=1,column=0,sticky=W)

name_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
name_box.grid(row=1,column=1)


age=Label(dataframeleft,text="Age",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
age.grid(row=2,column=0,sticky=W)

age_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
age_box.grid(row=2,column=1)


sex=Label(dataframeleft,text="Sex",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
sex.grid(row=3,column=0,sticky=W)

option2=["Male","Female","Others"]
clicked2=StringVar()
clicked2.set("Select anyone")

sex_menu=OptionMenu(dataframeleft,clicked2,*option2)
sex_menu.config(bg="white",fg="black",font=("arial",10,"bold"),width=20)
sex_menu.grid(row=3,column=1)


Class=Label(dataframeleft,text="Class",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
Class.grid(row=4,column=0,sticky=W)

option3=["EC","1AC","2AC","3AC","SL","2S"] #EC-executive class,AC-Air conditioned,SL-Sleeper,2S-second class
global clicked3
clicked3=StringVar()
clicked3.set("Select anyone")

Class_menu=OptionMenu(dataframeleft,clicked3,*option3)
Class_menu.config(bg="white",fg="black",font=("arial",10,"bold"),width=20)
Class_menu.grid(row=4,column=1)


berth=Label(dataframeleft,text="Berth",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
berth.grid(row=5,column=0,sticky=W)

option4=["Upper berth","Middle berth","Lower berth","Side upper berth","Side lower berth"]
clicked4=StringVar()
clicked4.set("Select anyone")

berth_menu=OptionMenu(dataframeleft,clicked4,*option4)
berth_menu.config(bg="white",fg="black",font=("arial",10,"bold"),width=20)
berth_menu.grid(row=5,column=1)


phone=Label(dataframeleft,text="Phone No.",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
phone.grid(row=6,column=0,sticky=W)

phone_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
phone_box.grid(row=6,column=1)


food=Label(dataframeleft,text="Food",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
food.grid(row=7,column=0,sticky=W)
global r
r=StringVar()
r.set(None)
Radiobutton(dataframeleft,text="Yes",variable=r,value="Yes",bg="powder blue",font=("times new roman",12,"bold"),padx=20).grid(row=7,column=1,sticky=W)
Radiobutton(dataframeleft,text="No",variable=r,value="No",bg="powder blue",font=("times new roman",12,"bold"),padx=20).grid(row=7,column=1,sticky=E)


source=Label(dataframeleft,text="Source Station",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
source.grid(row=0,column=2,sticky=W)

capitals=["Agartala","Ahemdabad","Amaravati","Bengaluru","Bhopal","Bhubaneswar","Chennai","Chandigard","Dehradun","Delhi","Gangtok","Goa",
          "Gurugram","Hyderabad","Imphal","Jaipur","Kochi","Kolkata","Ladakh","Lucknow","Mumbai","Patna","Pune","Raipur","Ranchi",
          "Shillong","Shimla","Srinagar","Varanasi"]

global src_ch
src_ch=StringVar()
src_ch.set("Select anyone")

source_menu=OptionMenu(dataframeleft,src_ch,*capitals)
source_menu.config(bg="white",fg="black",font=("arial",10,"bold"),width=20)
source_menu.grid(row=0,column=3)


destination=Label(dataframeleft,text="Destination Station",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
destination.grid(row=1,column=2,sticky=W)

stations=["Agartala","Ahemdabad","Amaravati","Bengaluru","Bhopal","Bhubaneswar","Chennai","Chandigard","Dehradun","Delhi","Gangtok","Goa",
          "Gurugram","Hyderabad","Imphal","Jaipur","Kochi","Kolkata","Ladakh","Lucknow","Mumbai","Patna","Pune","Raipur","Ranchi",
          "Shillong","Shimla","Srinagar","Varanasi"]

if src_ch.get() != "Select anyone":
    stations.remove(src_ch.get())
    stations.current(0)

stops=stations

global des_ch
des_ch=StringVar()
des_ch.set("Select anyone")

des_menu=OptionMenu(dataframeleft,des_ch,*stops)
des_menu.config(bg="white",fg="black",font=("arial",10,"bold"),width=20)
des_menu.grid(row=1,column=3)


date=Label(dataframeleft,text="Date",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
date.grid(row=2,column=2,sticky=W)

date_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
date_box.grid(row=2,column=3)
date_box.bind("<ButtonRelease-1>",pick_date)


train_no=Label(dataframeleft,text="Train No.",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
train_no.grid(row=4,column=2,sticky=W)

train_no_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
train_no_box.grid(row=4,column=3)


train_name=Label(dataframeleft,text="Train Name",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
train_name.grid(row=5,column=2,sticky=W)

train_name_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
train_name_box.grid(row=5,column=3)


time=Label(dataframeleft,text="Arrival Time",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
time.grid(row=6,column=2,sticky=W)

time_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
time_box.grid(row=6,column=3)


Amount=Label(dataframeleft,text="Amount",bg="powder blue",font=("times new roman",15,"bold"),padx=50,pady=6)
Amount.grid(row=7,column=2,sticky=W)

Amount_box=Entry(dataframeleft,font=("arial",10,"bold"),width=25,justify=CENTER)
Amount_box.grid(row=7,column=3)

#=======================================Train Details===================================================
dataframeright=LabelFrame(frame,text="Train Details",bg="powder blue",bd=12,relief=RIDGE,font=("arial",12,"bold"))
dataframeright.place(x=910,y=5,width=540,height=350)

textbox=Text(dataframeright,font=("arial",12,"italic"),width=32,height=16,padx=2,pady=8)
textbox.grid(row=0,column=2)

train_list_scroll=Scrollbar(dataframeright)
train_list_scroll.grid(row=0,column=1,sticky="ns")

train_list=['Deccan Odyssey','The Golden Chariot','Maharajas Express','Duronto Express','Garib Rath','Tejas Express','Shatabdi Express',
            'Vande Bharat Express','Rajdhani Express','Yuva Express','Antyodaya Express','Kavi Guru Express','Humsafar Express',
            'Vivek Express','Mahamana Express','Rajya Rani Express','Uday Express','Suvidha Express','Gatimaan Express','Himsagar Express',
            'Jan Sadharan Express','Double Decker Express','Ajanta Express','Amritsar Mail']

train_listbox=Listbox(dataframeright,font=("arial",12,"bold"),width=20,height=16)
#train_listbox.bind("<<ListboxSelect>>",select_train)
train_listbox.grid(row=0,column=0,padx=4)
train_list_scroll.config(command=train_listbox.yview)

for item in train_list:
    train_listbox.insert(END,item)


#=================Buttons frame================
framebutton=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
framebutton.place(x=0,y=530,width=1530,height=70)

btnAdddata=Button(framebutton,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white",command=add)
btnAdddata.grid(row=0,column=0)

btnShowdata=Button(framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white",command=show)
btnShowdata.grid(row=0,column=1)

btnUpdate=Button(framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white",command=update)
btnUpdate.grid(row=0,column=2)

btnDelete=Button(framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white",command=delete)
btnDelete.grid(row=0,column=3)

btnReset=Button(framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white",command=reset)
btnReset.grid(row=0,column=4)

btnExit=Button(framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white",command=exit)
btnExit.grid(row=0,column=5)

check=Button(dataframeleft,text="Check Availability",bg="blue",fg="white",font=("arial",12,"bold"),width=25,padx=50,command=trainsec)
check.grid(row=3,column=2,columnspan=3)

#=================Database information frame================
framedetails=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
framedetails.place(x=0,y=600,width=1530,height=195)

tableframe=Frame(framedetails,bd=6,relief=RIDGE,padx=20,bg="powder blue")
tableframe.place(x=0,y=2,width=1460,height=165)

xscroll=ttk.Scrollbar(framedetails,orient=HORIZONTAL)
yscroll=ttk.Scrollbar(framedetails,orient=VERTICAL)

root.lib_table=ttk.Treeview(framedetails,column=("Reserve_Quota","Name","Sex","Age","Phone_num","Train_num",
                "Train_Name","class","berth","Source","Destination","Date","Time","Food","Amount"),
                xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

xscroll.pack(side=BOTTOM,fill=X)
yscroll.pack(side=RIGHT,fill=Y)

xscroll.config(command=root.lib_table.xview)
yscroll.config(command=root.lib_table.yview)


root.lib_table.heading("Reserve_Quota",text="Reservation Quota")
root.lib_table.heading("Name",text="Name")
root.lib_table.heading("Sex",text="Sex")
root.lib_table.heading("Age",text="Age")
root.lib_table.heading("Phone_num",text="Phone Number")
root.lib_table.heading("Train_num",text="Train Number")
root.lib_table.heading("Train_Name",text="Train Name")
root.lib_table.heading("class",text="Class")
root.lib_table.heading("berth",text="Berth")
root.lib_table.heading("Source",text="Source")
root.lib_table.heading("Destination",text="Destination")
root.lib_table.heading("Date",text="Date")
root.lib_table.heading("Time",text="Time")
root.lib_table.heading("Food",text="Food")
root.lib_table.heading("Amount",text="Amount")


root.lib_table["show"]="headings"
root.lib_table.pack(fill=BOTH,expand=1)


root.lib_table.column("Reserve_Quota",width=130)
root.lib_table.column("Name",width=130)
root.lib_table.column("Sex",width=100)
root.lib_table.column("Age",width=100)
root.lib_table.column("Phone_num",width=100)
root.lib_table.column("Train_num",width=100)
root.lib_table.column("Train_Name",width=120)
root.lib_table.column("class",width=100)
root.lib_table.column("berth",width=100)
root.lib_table.column("Source",width=100)
root.lib_table.column("Destination",width=100)
root.lib_table.column("Date",width=100)
root.lib_table.column("Time",width=100)
root.lib_table.column("Food",width=100)
root.lib_table.column("Amount",width=100)

root.lib_table.bind("<ButtonRelease-1>",get_cursor)
# root.lib_table.bind("<ButtonRelease-1>",update)

root.mainloop()