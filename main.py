import tkinter as tk
from tkcalendar import Calendar
import random as r
from tkinter import ttk
import csv
import os
from config import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTER_DIR = os.path.join(BASE_DIR, "movie posters")


#mysql
import mysql.connector
mycon=mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,database=DB_NAME)
cursor=mycon.cursor()

#theme
fontst="SF Pro Light"
hsz=25
fsz=13
alt_fsz=10

win_bg="#9682de"
widget_altbg="#EDD2FF"
entry_bg="#FFFFFF"
button_bg="#4A90E2"


#setup of window one 
window=tk.Tk()
window.title("Movies")
window.geometry("1100x700")
window.config(background=win_bg)

#var setup
images={}
global book_details
book_details=[]
Admin_name='admin'
Admin_pass='123456'
images["QRcode2"] = tk.PhotoImage(file=os.path.join(BASE_DIR, "qrcode.png")).subsample(4, 4)
images["bg"] = tk.PhotoImage(file=os.path.join(BASE_DIR, "Background main.png")).subsample(2, 3)
images["QRcode"] = tk.PhotoImage(file=os.path.join(BASE_DIR, "main_qrcode.png"))

#clear the window to display new page, function
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


#2nd page (signup tab) -------------------
def signup_tab():
    def homlogbutf():
        clear_window()
        login_tab()

    def signup_but():
        user=user_entry.get()
        psw=psw_entry.get()

        if user!='' and psw!='' and len(psw)>5 and len(user)>2:
            sq=f"select * from user where username='{user}';"
            cursor.execute(sq)
            data=cursor.fetchall()
            if len(data)==0:
                sq1='''select * from user;'''
                cursor.execute(sq1)
                data=cursor.fetchall()
                i=len(data)
                sq2=f"insert into user values({i},'{user}','{psw}'); "
                cursor.execute(sq2)
                mycon.commit()

                clear_window()
                homepage()
            else:
                labinfo.config(text='Username already taken.')

        elif user=='' or psw=='':
            labinfo.config(text='Username or Password cannot be blank.')
        elif len(psw)<5:
            labinfo.config(text='Password too short. Please use at least 6 characters.')
        elif len(user)<2:
            labinfo.config(text='Username too short. Please use at least 3 charecters.')


    lab1=tk.Label(text='Enter username:',font=(fontst,fsz),background=win_bg).pack()
    user_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
    user_entry.pack()

    lab2=tk.Label(text='Enter password:',font=(fontst,fsz),background=win_bg).pack()
    psw_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
    psw_entry.pack()

    labinfo=tk.Label(text='',font=(fontst,fsz),background=win_bg,fg="#ff084a")
    labinfo.pack()

    signup_button=tk.Button(text='Sign Up',font=(fontst,fsz),background=button_bg,command=signup_but).pack(pady=(0,5))
    signlogbut=tk.Button(text='Already have an account?',font=(fontst,fsz),background=button_bg,command=homlogbutf).pack()

#1st page (login tab) -------------------
def login_tab():
    clear_window()
    def homsignbutf():
        clear_window()
        signup_tab()


    def login_but():
        window.geometry("1100x700")
        user_=user_entry_.get()
        psw_=psw_entry_.get()

        sq1=f"select * from user where binary password='{psw_}' and username='{user_}';"
        cursor.execute(sq1)
        data=cursor.fetchall()
        if len(data)==1:
            if data[0][1]==Admin_name and data[0][2]==Admin_pass:
                clear_window()
                Admin_tab()
            else:
                book_details.append(user_)
                clear_window()
                homepage()

        else:
            infolab_.config(text="Invalid username or password")

        



    lab0=tk.Label(text='Welcome Back!',font=(fontst,hsz),background=win_bg).pack(pady=(0, 15))


    lab1_=tk.Label(text='Enter Username:',font=(fontst,fsz),background=win_bg).pack()
    user_entry_=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
    user_entry_.pack()

    lab1_=tk.Label(text='Enter Password:',font=(fontst,fsz),background=win_bg).pack()
    psw_entry_=tk.Entry(window,show='*',font=(fontst,alt_fsz),background=entry_bg)
    psw_entry_.pack()

    infolab_=tk.Label(text='',font=(fontst,fsz),fg='#ff084a',background=win_bg)
    infolab_.pack()

    login_button=tk.Button(text='Login',font=(fontst,fsz),command=login_but,background=button_bg).pack(pady=(0, 5))
    logsignbut=tk.Button(text='Dont have an account?',font=(fontst,fsz),command=homsignbutf,background=button_bg).pack()
    bg_lab=tk.Label(image=images['bg']).pack(pady=7)



#1A page (admin tab)-------------------------
def Admin_tab():
    clear_window()
    

    sq="select * from user"
    cursor.execute(sq)
    data=cursor.fetchall()

    root=tk.Toplevel(window)              # new Tkinter window
    root.title("User Table")
    window.geometry("500x500")
    tree = ttk.Treeview(root)

    columns = [desc[0] for desc in cursor.description]
    tree["columns"] = columns
    tree["show"] = "headings"       # hide default first empty column

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100) 

    for row in data:
        tree.insert("", "end", values=row)            #Insert rows

    tree.pack(expand=True, fill="both")

    def clear_window2():
        for widget in window.winfo_children():
            if widget!=root:
                widget.destroy()
            
    def exit_buttonf():
        clear_window2()
        root.destroy()
        Admin_tab()
            
    def add_but():            #when add button pressed
        clear_window2()
        lab2_=tk.Label(text='Enter Username:',font=(fontst,fsz),background=win_bg).pack()
        name_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
        name_entry.pack()

        lab3_=tk.Label(text='Enter Password:',font=(fontst,fsz),background=win_bg).pack()
        password_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
        password_entry.pack()

        lab4_=tk.Label(text='',font=(fontst,fsz),fg="red",background=win_bg)
        lab4_.pack()
        

        def insert():
            name=name_entry.get()
            password=password_entry.get()

            sq1='''select * from user;'''
            cursor.execute(sq1)
            data=cursor.fetchall()
            try:
                lab4_.config(text='Done!')
                i=len(data)
                sq2=f"insert into user values({i},'{name}','{password}'); "        #To add a new record
                cursor.execute(sq2)
            except:
                lab4_.config(text='Error: Invalid Username')
            mycon.commit()

        insert_button=tk.Button(text='Add',font=(fontst,fsz),command=insert,background=button_bg).pack(pady=(0, 5))
        exit_button=tk.Button(text='←',font=(fontst,fsz),background=button_bg,command=exit_buttonf).pack(pady=(0, 5))


    def delete_but():
        clear_window2()        #when delete button pressed
        lab1_=tk.Label(text='Enter Serial No. to delete:',font=(fontst,fsz),background=win_bg).pack()
        sno_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
        sno_entry.pack()

        lab4_=tk.Label(text='',font=(fontst,fsz),fg="red",background=win_bg)
        lab4_.pack()

        def delete():
            sno=sno_entry.get()

            sq1='''select * from user;'''
            cursor.execute(sq1)
            data=cursor.fetchall()
            i=len(data)

            sq2=f"select * from user where sno={sno};"
            cursor.execute(sq2)
            data2=cursor.fetchall()
            if len(data2)==1:
                lab4_.config(text='Done!')
                sq3=f"delete from user where sno={sno};"
                cursor.execute(sq3)
                mycon.commit()
            else:
                lab4_.config(text='Error: Invalid Serial number')
        delete_button=tk.Button(text='Delete',font=(fontst,fsz),command=delete,background=button_bg).pack(pady=(0, 5))
        exit_button=tk.Button(text='←',font=(fontst,fsz),background=button_bg,command=exit_buttonf).pack(pady=(0, 5))

    
    def  modify_but(): 
        clear_window2()       #when modify buttono pressed
        lab1_=tk.Label(text='Enter Serial No. to modify:',font=(fontst,fsz),background=win_bg).pack()
        sno_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
        sno_entry.pack()

        lab2_=tk.Label(text='Enter new Username:',font=(fontst,fsz),background=win_bg).pack()
        name_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
        name_entry.pack()

        lab3_=tk.Label(text='Enter new Password:',font=(fontst,fsz),background=win_bg).pack()
        password_entry=tk.Entry(window,font=(fontst,alt_fsz),background=entry_bg)
        password_entry.pack()

        lab4_=tk.Label(text='',font=(fontst,fsz),background=win_bg)
        lab4_.pack()

        def modify():
            sno=sno_entry.get()
            name=name_entry.get()
            password=password_entry.get()

            sq2=f"select * from user where sno={sno};"
            cursor.execute(sq2)
            data2=cursor.fetchall()
            if len(data2)==1:
                lab4_.config(text='Done!')
                sq1 = f"update user set username = '{name}', password = '{password}' where sno = {sno};"
                cursor.execute(sq1)
                mycon.commit()
            else:
                lab4_.config(text='Error: Invalid Serial number')

        
        modify_button=tk.Button(text='Modify',font=(fontst,fsz),command=modify,background=button_bg).pack(pady=(0, 5))
        exit_button=tk.Button(text='←',font=(fontst,fsz),background=button_bg,command=exit_buttonf).pack(pady=(0, 5))

    window.geometry("1000x1000")
    lab0=tk.Label(window,text='Welcome Admin!',font=(fontst,hsz),background=win_bg).pack(pady=(0, 15))
    lab1=tk.Label(window,text='Manage Users',font=(fontst,hsz),background=win_bg).pack(pady=(0, 15))
    add_button=tk.Button(window,text='Add users',font=(fontst,fsz),command=add_but,background=button_bg).pack(pady=(0, 5))
    Delete_button=tk.Button(window,text='Delete users',font=(fontst,fsz),command=delete_but,background=button_bg).pack(pady=(0, 5))
    Modify_button=tk.Button(window,text='Modify existing users',font=(fontst,fsz),command=modify_but,background=button_bg).pack(pady=(0, 5))
    leave_button=tk.Button(window,text='EXIT',font=(fontst,fsz),command=login_tab,background=button_bg).pack(pady=(0, 5))

    

#3rd page (movie tab) -------------------
def homepage():
    window.geometry("1000x700")
    def poster_click(m):
        global movie_var
        movie_var=m
        movie_window()

    def movie_window():
        window.geometry("700x520")
        container.destroy()
        container_.destroy()
        search_label.destroy()

        sq=f"select * from movies where mname='{movie_var}';"
        cursor.execute(sq)
        data=cursor.fetchone()

        container2=tk.Frame()
        container2.pack()
        container2.config(bg=win_bg)

        img=tk.Label(container2,image=images[movie_var]).pack()
        name=tk.Label(container2,text=f"Movie Name: {data[1]}",font=(fontst,fsz),background=win_bg).pack(anchor='w')
        rating=tk.Label(container2,text=f"Rating: {data[2]}",font=(fontst,fsz),background=win_bg).pack(anchor='w')
        duration=tk.Label(container2,text=f"Duration: {data[3]}",font=(fontst,fsz),background=win_bg).pack(pady=(0,5),anchor='w')
        desc_lab=tk.Label(container2,text='Description:',font=(fontst,fsz),background=win_bg).pack(anchor='w')

        desc=tk.Text(wrap=tk.WORD, height=6, width=75,font=(fontst,fsz),background=widget_altbg)
        desc.insert(tk.END, data[4])
        desc.pack(pady=(0,5))
        desc.config(state='disabled')

        def exit_buttonf():
            clear_window()
            window.config("1100x700")
            homepage()

        container3=tk.Frame()
        container3.pack()
        container3.config(bg=win_bg)
        exit_button=tk.Button(container3,text='←',font=(fontst,fsz),background=button_bg,command=exit_buttonf).grid(row=0,column=1)
        book_button=tk.Button(container3,text='BOOK NOW',font=(fontst,fsz),background=button_bg,command=lambda: (book_details.append(movie_var),selection_window())).grid(row=0,column=0,padx=(0,5))


    def search_function():
        search=search_box.get()
        sq=f"select * from movies where mname like '{search}%';"
        cursor.execute(sq)
        data=cursor.fetchall()
        if len(data)!=0:
            global movie_var
            movie_var=data[0][1]
            movie_window()
        else:
            search_label.config(text='Invalid Movie Name')

    container_=tk.Frame(window)
    container_.pack()
    container_.config(bg=win_bg)

    search_box=tk.Entry(container_,text='search movie name',font=(fontst,fsz),background=entry_bg)
    search_box.grid(row=0,column=0)
    search_button=tk.Button(container_,text='⌕',font=(fontst,alt_fsz),background=button_bg,command=search_function)
    search_button.grid(row=0,column=1,padx=(0,5))
    search_label=tk.Label(text='',font=(fontst,fsz),background=win_bg,fg="#ff084a")
    search_label.pack()

    container=tk.Frame(window)
    container.pack()
    container.config(background=win_bg)

    posters = {
    "Avengers Endgame": "endgame_poster.png",
    "Inception": "inception_poster.png",
    "Jurassic Park": "jurassicpark_poster.png",
    "Dune: Part Two": "Dune2_poster.png",
    "Interstellar": "Interstellar_poster.png",
    "Mission: Impossible-The Final Reckoning": "MI8_poster.png",
    "Oppenheimer": "Oppenheimer_poster.png",
    "Skyfall": "Skyfall_poster.png",
    "The Batman": "TheBatman_poster.png",
    "Now You See Me 2": "nowyouseeme2_poster.png"
    }

    for movie, filename in posters.items():
        path = os.path.join(POSTER_DIR, filename)
        images[movie] = tk.PhotoImage(file=path).subsample(4, 4)



    endgame_button = tk.Button(container, image=images["Avengers Endgame"], text='Avengers Endgame',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="Avengers Endgame":poster_click(m))
    inception_button = tk.Button(container, image=images["Inception"], text='Inception',font=(fontst,fsz),background=button_bg, compound='top',command=lambda m="Inception":poster_click(m))
    jurassicpark_button = tk.Button(container, image=images["Jurassic Park"], text='Jurassic Park',font=(fontst,fsz),background=button_bg, compound='top',command=lambda m="Jurassic Park":poster_click(m))
    nowyouseeme2_button=tk.Button(container, image=images["Now You See Me 2"], text='Now You See Me 2',font=(fontst,fsz),background=button_bg, compound='top',command=lambda m="Now You See Me 2":poster_click(m))
    Dune2_button = tk.Button(container, image=images["Dune: Part Two"], text='Dune 2',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="Dune: Part Two":poster_click(m))
    Interstellar_button = tk.Button(container, image=images["Interstellar"], text='Interstellar',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="Interstellar":poster_click(m))
    MissionImpossible_button = tk.Button(container, image=images["Mission: Impossible-The Final Reckoning"], text='Mission Impossible 8',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="Mission: Impossible-The Final Reckoning":poster_click(m))
    Oppenheimer_button = tk.Button(container, image=images["Oppenheimer"], text='Oppenheimer',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="Oppenheimer":poster_click(m))
    Skyfall_button = tk.Button(container, image=images["Skyfall"], text='Skyfall',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="Skyfall":poster_click(m))
    TheBatman_button = tk.Button(container, image=images["The Batman"], text='The Batman',font=(fontst,fsz),background=button_bg,compound='top',command=lambda m="The Batman":poster_click(m))




    endgame_button.grid(row=0, column=0, padx=10, pady=10)
    inception_button.grid(row=0, column=1, padx=10, pady=10)
    jurassicpark_button.grid(row=0, column=2, padx=10, pady=10)
    nowyouseeme2_button.grid(row=0, column=3, padx=10, pady=10)
    Interstellar_button.grid(row=0, column=4, padx=10, pady=10)
    Dune2_button.grid(row=1, column=0, padx=10, pady=10)
    MissionImpossible_button.grid(row=1, column=1, padx=10, pady=10)
    Oppenheimer_button.grid(row=1, column=2, padx=10, pady=10)
    Skyfall_button.grid(row=1, column=3, padx=10, pady=10)
    TheBatman_button.grid(row=1, column=4, padx=10, pady=10)


#4th page (date,time,theatre selection) -------------------
def selection_window():
    clear_window()
    
    valcal_lab=tk.Label(text='Select Date:',font=(fontst,fsz),background=win_bg)
    valcal_lab.pack()

    calendar=Calendar(window,selectmode='day',date_pattern='yyyy-mm-dd')
    calendar.pack()

    def cal_butf():
        global thedate
        thedate=calendar.get_date()

        sq1=f"insert into date_manager values('{thedate}');"
        sq2='''select * from date_manager where mdate between curdate() and curdate() + interval 10 day;'''
        sq3='''delete from date_manager;'''

        cursor.execute(sq1)
        cursor.execute(sq2)
        data=cursor.fetchall()
        if len(data)==1:
            valcal_lab.config(text=f"selected date: {thedate}")
            cursor.execute(sq3)
            book_details.append(thedate)
            cal_but.destroy()
            time_select_window()
        else:
            valcal_lab.config(text='Invalid date: No movie Slots Available')
            cursor.execute(sq3)

    cal_but=tk.Button(text='confirm date',command=cal_butf,font=(fontst,fsz),background=button_bg)
    cal_but.pack()


    def time_select_window():
        time_lab=tk.Label(text='Select time:',font=(fontst,fsz),background=win_bg)
        time_lab.pack(pady=(5,0))

        container3=tk.Frame()
        container3.config(bg=win_bg)
        container3.pack(padx=10,pady=10)

        def gtime_butf():
            book_details.append(time)
            gtime_but.destroy()
            theatre_select_window()

        def timef(t,w):
            global time
            time=t
            time_lab.config(text=f"Selected Time: {w}")

        sq='''select convert(time(now()),char) from time_manager;'''
        sq2='''select convert(date(now()),char) from time_manager;'''
        cursor.execute(sq)
        data=cursor.fetchone()
        cursor.execute(sq2)
        data2=cursor.fetchone()

        if thedate[-1:-3:-1]==data2[0][-1:-3:-1] and thedate[0:4]==data2[0][0:4]:
            if int(data[0][0:2])<10:
                time_but1=tk.Button(container3, text='10 AM',font=(fontst,fsz),background=widget_altbg,command=lambda t='10:00',w='10 AM':timef(t,w)).grid(row=0,column=0)
            if int(data[0][0:2])<14:
                time_but2=tk.Button(container3,text=' 2 PM',font=(fontst,fsz),background=widget_altbg,command=lambda t='14:00',w='2 PM':timef(t,w)).grid(row=0,column=1)
            if int(data[0][0:2])<18:
                time_but3=tk.Button(container3,text=' 6 PM',font=(fontst,fsz),background=widget_altbg,command=lambda t='18:00',w='6 PM':timef(t,w)).grid(row=1,column=0)
            if int(data[0][0:2])<22:
                time_but4=tk.Button(container3,text='10 PM',font=(fontst,fsz),background=widget_altbg,command=lambda t='22:00',w='10 PM':timef(t,w)).grid(row=1,column=1)
        else:
            time_but1=tk.Button(container3, text='10 AM',font=(fontst,fsz),background=widget_altbg,command=lambda t='10:00',w='10 AM':timef(t,w)).grid(row=0,column=0)
            time_but2=tk.Button(container3,text=' 2 PM',font=(fontst,fsz),background=widget_altbg,command=lambda t='14:00',w='2 PM':timef(t,w)).grid(row=0,column=1)
            time_but3=tk.Button(container3,text=' 6 PM',font=(fontst,fsz),background=widget_altbg,command=lambda t='18:00',w='6 PM':timef(t,w)).grid(row=1,column=0)
            time_but4=tk.Button(container3,text='10 PM',font=(fontst,fsz),background=widget_altbg,command=lambda t='22:00',w='10 PM':timef(t,w)).grid(row=1,column=1)

        gtime_but=tk.Button(text='confirm time',font=(fontst,fsz),background=button_bg,command=gtime_butf)
        gtime_but.pack()

    def theatre_select_window():
        theatre_lab=tk.Label(text='Select a Theatre:',font=(fontst,fsz),background=win_bg)

        container2=tk.Frame()
        container2.config(bg=win_bg)
        container2.pack(padx=10,pady=10)

        def theatre_buttonf(th):
            clear_window()
            calendar.destroy()
            container2.destroy()
            book_details.append(th)
            seat_selection()

        tbut1=tk.Button(container2,text='Cinepolis',font=(fontst,fsz),background=widget_altbg,command=lambda th='Cinepolis':theatre_buttonf(th)).grid(row=0,column=0,padx=5,pady=5)
        tbut2=tk.Button(container2,text='   PVR   ',font=(fontst,fsz),background=widget_altbg,command=lambda th='PVR':theatre_buttonf(th)).grid(row=0,column=1,padx=5,pady=5)
        tbut3=tk.Button(container2,text='  Inox   ',font=(fontst,fsz),background=widget_altbg,command=lambda th='Inox':theatre_buttonf(th)).grid(row=1,column=0,padx=5,pady=5)
        tbut4=tk.Button(container2,text='MultiPlex',font=(fontst,fsz),background=widget_altbg,command=lambda th='MultiPlex':theatre_buttonf(th)).grid(row=1,column=1,padx=5,pady=5)


#5th page (no. of seats,seats selection)
def seat_selection():

    def seat_selector():

        seat_details=[]

        def butf(r,c,but):

            am=ord("A")
            if len(seat_details)<int(book_details[5]):
                seat_details.append(chr(am+r)+f"{c}")
                but.configure(state='disabled',background=widget_altbg)

            if len(seat_details)==int(book_details[5]):
                container4.destroy()
                screen_lab.destroy()

                seatno_display=tk.Label(text=f"Selected Seats: {str(seat_details)[1:len(str(seat_details))-1]}",font=(fontst,fsz),bg=widget_altbg)
                seatno_display.pack()

                def conf_seatsf():
                    book_details.append(seat_details)
                    clear_window()
                    cursor = mycon.cursor(dictionary=True)
                    seats=','.join(book_details[6])
                    sq=f"insert into ticket_manager values('{book_details[0]}','{book_details[1]}','{book_details[2]}','{book_details[3]}','{book_details[4]}','{seats}');"
                    cursor.execute(sq)
                    mycon.commit()
                    payment_page()

                def clear_seatsf():
                    conf_seats.destroy()
                    clear_seats.destroy()
                    container5.destroy()
                    seatno_display.destroy()
                    seat_selector()

                container5=tk.Frame()
                container5.pack()
                container5.config(bg=win_bg)
                conf_seats=tk.Button(container5,text='Confirm Seats',font=(fontst,fsz),background=button_bg,command=conf_seatsf)
                clear_seats=tk.Button(container5,text='Reselect',font=(fontst,fsz),background=button_bg,command=clear_seatsf)
                conf_seats.grid(row=0,column=0,padx=3,pady=5)
                clear_seats.grid(row=0,column=1,padx=3,pady=5)

        container4=tk.Frame()
        container4.config(bg=win_bg)
        container4.pack(pady=(0,10))
        screen_lab=tk.Label(text='---------SCREEN----------',font=(fontst,fsz),bg="gray")
        screen_lab.pack()

        for r in range(6):
            for c in range(10):
                am=ord('A')
                but=tk.Button(container4,text=f"{chr(am+r)}{c}",font=(fontst,fsz),background=button_bg)
                but.config(command=lambda r=r,c=c,but=but: butf(r,c,but))
                but.grid(row=r,column=c,padx=2,pady=2)

                randseat=chr(am+r)+str(c)
                sq=f"select seats from ticket_manager where mname='{book_details[1]}' and mdate='{book_details[2]}' and time='{book_details[3]}' and tname='{book_details[4]}';"
                cursor.execute(sq)
                data=cursor.fetchall()

                if len(data)>=1:
                    for seats in data:
                        if randseat in seats[0].split(','):
                            but.config(state='disabled',background='#ff084a')

    def seatno_butf():
        seatno=seatno_entry.get()
        try:
            if int(seatno)>0 and int(seatno)<=10:
                seat_lab2.config(text=f"select {seatno} seats-",font=(fontst,fsz),fg="#000000")
                book_details.append(seatno)
                seatno_button.destroy()
                seat_selector()
            else:
                seat_lab2.config(text="Select 1-10 seats",font=(fontst,fsz),fg="#ff084a")
        except ValueError:
            seat_lab2.config(text="Invalid Number of seats selected",font=(fontst,fsz),fg="#ff084a")

    seat_lab=tk.Label(text='Enter number of seats required:',font=(fontst,fsz),background=win_bg).pack()
    seatno_entry=tk.Entry(font=(fontst,alt_fsz),background=entry_bg)
    seatno_entry.pack()
    seatno_button=tk.Button(text='Confirm',font=(fontst,fsz),background=button_bg,command=seatno_butf)
    seatno_button.pack()
    seat_lab2=tk.Label(text='',background=win_bg)
    seat_lab2.pack()



#6th page (displays ticket)
def ticket_page():
    window.geometry("450x630")
    def e_butf():
        clear_window()
        book_details.clear()
        login_tab()

    cursor = mycon.cursor(dictionary=True)
    sq2=f'''select * from ticket_manager where username='{book_details[0]}' and time='{book_details[3]}' and mdate='{book_details[2]}' and mname='{book_details[1]}' and seats='{','.join(book_details[6])}';'''
    cursor.execute(sq2)
    dat1=cursor.fetchall()

    #mail
    f = open(os.path.join(BASE_DIR, "tempmail.txt"), "r")
    data=f.read()
    subwindow=tk.Toplevel(window)
    subwindow.geometry("600x600")
    subwindow.config(bg=win_bg)
    subwindow.title("GMAIL")
    lab=tk.Label(subwindow,text=data.format( mname=dat1[0]['mname'],username=dat1[0]['username'],tname=dat1[0]['tname'],mdate=dat1[0]['mdate'],time=dat1[0]['time'],seats=dat1[0]['seats']),font=(fontst,fsz),background=win_bg,wraplength=400,anchor="w").pack()
    f.close()

    #ticket page
    name=dat1[0]['mname']
    time=dat1[0]['time']
    date=dat1[0]['mdate']
    seats=dat1[0]['seats']
    tname=dat1[0]['tname']
    bookid=r.randint(10000,99999)

    lab0=tk.Label(text='Your Ticket Is Confirmed!',font=(fontst,hsz),background=win_bg).pack()

    cont1=tk.Frame(bg=win_bg)
    cont1.pack()
    cont_1=tk.Frame(cont1,bg=widget_altbg)
    cont_1.grid(row=0,column=0)
    cont_2=tk.Frame(cont1,bg=widget_altbg)
    cont_2.grid(row=0,column=1,padx=(5,0))
    
    lab1=tk.Label(cont_1,image=images[name]).pack()
    Lab2=tk.Label(cont_2,text=f'Movie name:{name}',font=(fontst,fsz),background=widget_altbg).pack(anchor='w')
    Lab3=tk.Label(cont_2,text=f'Date:{date}',font=(fontst,fsz),background=widget_altbg).pack(anchor='w')
    Lab4=tk.Label(cont_2,text=f'Show Time:{time}',font=(fontst,fsz),background=widget_altbg).pack(anchor='w')
    Lab5=tk.Label(cont_2,text=f'Theatre:{tname}',font=(fontst,fsz),background=widget_altbg).pack(anchor='w')
    Lab6=tk.Label(cont_2,text=f'Seats:{seats}',font=(fontst,fsz),background=widget_altbg).pack(anchor='w')
    lab7=tk.Label(text=f'Booking ID:{bookid}',font=(fontst,fsz),background=win_bg).pack()
    lab8=tk.Label(image=images['QRcode2']).pack()
    e_button=tk.Button(text='  Exit  ',font=(fontst,hsz),background=button_bg,command=e_butf).pack(pady=(5,0))
        



def payment_page():
    
    def cardp():
      
        def confirm_cardnum():
            global cn
            cnum=cardnum_entry.get()
            if len(cnum)==16 and cnum.isdigit():
                cardnumber_lab.config(text='')
                cn=cnum
                cardnum_but.destroy()
            else:
                cardnumber_lab.config(text='Invalid Card Number',fg="#ff084a")
                cn=False
            return cn  
        def confrim_cvv():
            global cvn
            cvnum=cvv_entry_.get()
            if len(cvnum)==3 and cvnum.isdigit():
                cvv_lab.config(text='')
                cvn=cvnum
                cvv_but.destroy()
            else:
                cvv_lab.config(text='Invalid CVV',fg="#ff084a")
                cvn=False
            return cvn
        def confrim_date():  
            global en   
            edate=expiry_entry_.get()
            if len(edate)==5:
                em=int(edate[0:2])
                ey=int(edate[3:5])
                sq2='''select convert(date(now()),char) from time_manager;'''
                cursor.execute(sq2)
                data=cursor.fetchone()
                eyr=int(data[0][2:4])
                emr=int(data[0][5:7])
                if ey==eyr and em>emr and em<=12:
                    expiry_lab.config(text='')
                    en=edate
                    expiry_but.destroy()
                elif em<=12 and ey>eyr and ey!=eyr:
                    expiry_lab.config(text='')
                    en=edate
                    expiry_but.destroy()
                else:
                    expiry_lab.config(text='Invalid Expiry Date',fg="#ff084a")
                    en=False
            else :
                expiry_lab.config(text='Invalid Format',fg="#ff084a")
                en=False
            return en
        def confrim_name():    
            global nn
            nname=cardname_entry_.get()
            check_name=nname.split()

            if len(check_name)==0:
                cardname_lab.config(text='Invalid Name',fg="#ff084a")
                nn=False
            else:
                checker=0
                for i in check_name:
                    if not i.isalpha():
                        cardname_lab.config(text='Invalid Name',fg="#ff084a")
                        nn=False
                        break
                    else:
                        checker+=1
                if checker==len(check_name):
                    cardname_lab.config(text='')
                    nn=nname
                    cardname_but.destroy()



            '''if nname.isalpha() and len(nname)>0:
                cardname_lab.config(text='')
                nn=nname
                cardname_but.destroy()
            else:
                cardname_lab.config(text='Invalid Name',fg="#ff084a")
                nn=False'''
            return nn
        
        def save_card():
             print([nn,cvn,en,cn])
             if nn!=False and cvn!=False and en!=False and cn!=False:
                f=open('payment.csv','a',newline='')
                csvw=csv.writer(f)
                csvw.writerow([nn,cvn,en,cn])
                f.close()
                save_button.destroy()
                newlab.config(text='Card saved for quick checkout!')
             else:
                newlab.config(text='Invalid Details Error Saving Card',fg="red")
        def load_card():
            f=open('payment.csv','r',newline='')
            csvr=csv.reader(f)
            for i in csvr:
                global nn, cvn, en, cn
                if i!=[]:
                    nn=i[0]
                    cvn=i[1]
                    en=i[2]
                    cn=i[3]
                    cardname_but.destroy()
                    cardnum_but.destroy()
                    cvv_but.destroy()
                    expiry_but.destroy()
                    save_button.destroy()
                    load_button.destroy()
                    cardnum_entry.destroy()
                    expiry_entry_.destroy()
                    cvv_entry_.destroy()
                    cardname_entry_.destroy()
                    newlab.config(text='Card Loaded')
                    cardnumber_lab.config(text=cn,bg=button_bg)
                    cvv_lab.config(text='**'+cvn[-1],bg=button_bg)
                    expiry_lab.config(text=en,bg=button_bg)
                    cardname_lab.config(text=nn,bg=button_bg)

            f.close()
        
                 

        def confirm_all():
            def otp_page():
                otp_=r.randrange(1,10000)
                if len(str(otp_))<4:
                    while True:
                        otp='0'+str(otp_)
                        if len(otp)==4:
                            break
                else:
                    otp=str(otp_) 
                subwindow1=tk.Toplevel(window)
                subwindow1.geometry("300x250")
                subwindow1.config(bg=win_bg)
                otpinfo_lab=tk.Label(subwindow1,text="otp sent to 98xxx xxxxx",font=(fontst,fsz),background=win_bg).pack()
                opt_lab=tk.Label(subwindow1,text=otp,font=(fontst,fsz),background=widget_altbg).pack()
                return otp
            def otp_conf():
                def check_otp(a):
                    if otp_entry.get()==a:
                        clear_window()
                        rand_lab=tk.Label(text="Pyment Successsful",font=(fontst,fsz),background=win_bg).pack()
                        rand_but=tk.Button(text="Finish",font=(fontst,fsz),background=button_bg,command=lambda:(clear_window(),ticket_page())).pack()
                    else:
                        otpentry_lab.config(text="Invalid OTP",fg="#ff084a")
                otpentry_lab=tk.Label(text="Enter the otp:",font=(fontst,fsz),background=win_bg)
                otpentry_lab.pack()
                otp_entry=tk.Entry(font=(fontst,alt_fsz),background=entry_bg)
                otp_entry.pack()
                a=''
                a=otp_page()
                otpentry_but=tk.Button(text="Confrim OTP",font=(fontst,fsz),background=button_bg,command=lambda a=a:check_otp(a)).pack()
            
            if nn!=False and cvn!=False and en!=False and cn!=False:
                clear_window()
                otp_conf()


        newlab=tk.Label(text='Secure Checkout:',font=(fontst,fsz),background=win_bg)
        newlab.pack(pady=40)
        container1 = tk.Frame(window)
        container1.config(bg=win_bg)
        container1.pack()

        cardnumber=tk.Label(container1,text='Card number:',font=(fontst,fsz),background=win_bg)
        cardnumber.grid(row=0,column=0 ,padx=5, pady=10) 
        cardnum_entry=tk.Entry(container1,font=(fontst,alt_fsz),background=entry_bg)
        cardnum_entry.grid(row=0,column=1,padx=5, pady=10)
        cardnum_but=tk.Button(container1,text='Confirm',font=(fontst,fsz),background=button_bg,command=confirm_cardnum)
        cardnum_but.grid(row=0,column=2,padx=5, pady=10)
        cardnumber_lab=tk.Label(container1,text='',font=(fontst,fsz),background=win_bg)
        cardnumber_lab.grid(row=1,column=0)

        cvv=tk.Label(container1,text='CVV:',font=(fontst,fsz),background=win_bg)
        cvv.grid(row=2,column=0,padx=5, pady=10)
        cvv_entry_=tk.Entry(container1,show='*',font=(fontst,alt_fsz),background=entry_bg)
        cvv_entry_.grid(row=2,column=1,padx=5, pady=10)
        cvv_but=tk.Button(container1,text='Confirm',font=(fontst,fsz),background=button_bg,command=confrim_cvv)
        cvv_but.grid(row=2,column=2,padx=5, pady=10)
        cvv_lab=tk.Label(container1,text='',font=(fontst,fsz),background=win_bg)
        cvv_lab.grid(row=3,column=0)

        expiry=tk.Label(container1,text='Card expiry date (mm/yy):',font=(fontst,fsz),background=win_bg)
        expiry.grid(row=4,column=0,padx=5, pady=10)
        expiry_entry_=tk.Entry(container1,font=(fontst,alt_fsz),background=entry_bg)
        expiry_entry_.grid(row=4,column=1,padx=5, pady=10)
        expiry_but=tk.Button(container1,text='Confirm',font=(fontst,fsz),background=button_bg,command=confrim_date)
        expiry_but.grid(row=4,column=2,padx=5, pady=10)
        expiry_lab=tk.Label(container1,text='',font=(fontst,fsz),background=win_bg)
        expiry_lab.grid(row=5,column=0)

        cardname=tk.Label(container1,text='Name on card:',font=(fontst,fsz),background=win_bg)
        cardname.grid(row=6,column=0,padx=5, pady=10)
        cardname_entry_=tk.Entry(container1,font=(fontst,alt_fsz),background=entry_bg)
        cardname_entry_.grid(row=6,column=1,padx=5, pady=10)
        cardname_but=tk.Button(container1,text='Confirm',font=(fontst,fsz),background=button_bg,command=confrim_name)
        cardname_but.grid(row=6,column=2,padx=5, pady=10)
        cardname_lab=tk.Label(container1,text='',font=(fontst,fsz),background=win_bg)
        cardname_lab.grid(row=7,column=0)

        confrim_all=tk.Button(text='Confirm All',command=confirm_all,font=(fontst,fsz),background=button_bg).pack()
        save_button=tk.Button(text='Save Card',command=save_card,font=(fontst,fsz),background=button_bg)
        save_button.pack()
        load_button=tk.Button(text='Load Saved Card',command=load_card,font=(fontst,fsz),background=button_bg)
        load_button.pack()

    def upi(t):
        def pay():
            lab.destroy()
            lab1.destroy()
            lab2.config(text="Payment Successful!")
            but=tk.Button(text='Finish',font=(fontst,fsz),bg=button_bg,command=lambda:(clear_window(),ticket_page())).pack()


        
        lab=tk.Label(image=images["QRcode"],bg=win_bg)
        lab.pack(pady=(0,5))
        lab1=tk.Label(text=f"To Pay: ₹{t}",font=(fontst,fsz),bg=entry_bg)
        lab1.pack()
        lab2=tk.Label(text='',font=(fontst,hsz),bg=win_bg)
        lab2.pack(pady=(0,10))

        subwindow=tk.Toplevel(window)
        subwindow.title("gpay")
        subwindow.geometry('200x150')
        subwindow.config(bg=win_bg)
        images["gpay"] = tk.PhotoImage(file=os.path.join(BASE_DIR, "Google_Pay_Logo.svg.png")).subsample(20, 20)
        pay_but = tk.Button(subwindow,image=images["gpay"], font = (fontst,fsz),command=pay,bg=widget_altbg ).pack()


    container1 = tk.Frame()
    container1.pack()
    container1.config(bg=entry_bg)
    container2=tk.Frame()
    container2.pack(pady=(10,0))
    container2.config(bg=win_bg)

    seatprice = 270
    nofse = len(book_details[6])
    tax =  (seatprice*nofse*30)/100
    total = (seatprice*nofse*130)/100
    lab=tk.Label(container1,text = "Payment Summary",font=(fontst,hsz),bg=entry_bg).pack(pady=(0,10))
    lab1 = tk.Label(container1,text = f"Number of seats: {nofse}",font=(fontst,fsz),bg=entry_bg).pack(anchor='w')
    lab3 = tk.Label(container1,text = f"Tax: ₹{tax}",font=(fontst,fsz),bg=entry_bg).pack(anchor='w')
    lab4 = tk.Label(container1,text = f"Total price: ₹{total}",font=(fontst,fsz),bg=entry_bg).pack(anchor='w')
    lab5 = tk.Button(container2,text = f"CREDIT/DEBIT CARD", font=(fontst,fsz),bg=button_bg,command=lambda:(clear_window(),cardp())).pack()
    lab6 = tk.Button(container2,text = f"       UPI       ", font=(fontst,fsz),bg=button_bg,command=lambda:(clear_window(),upi(total))).pack()









login_tab()

window.mainloop()