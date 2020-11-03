from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import threading




class Whatsapp():
    def __init__(self,root):
        self.root=root
        self.root.title("Whatsapp Messager")
        self.root.geometry("500x350")
        self.root.iconbitmap("logo337.ico")
        self.root.resizable(0,0)


        number=StringVar()
        hour=IntVar()
        minutes=IntVar()
        message=StringVar()



        def on_enter1(e):
            but_send['background']="black"
            but_send['foreground']="cyan"
  
        def on_leave1(e):
            but_send['background']="SystemButtonFace"
            but_send['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        def send():
            try:
                import pywhatkit as kit
                if number.get()!="":
                    if hour.get()!="Select Hours":
                        if minutes.get()!="Select Minutes":
                            if txt.get("1.0","end")!="":
                                kit.sendwhatmsg("+91{}".format(number.get()),txt.get('1.0',"end"),hour.get(),minutes.get())
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Hours")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter number")
            except:
                tkinter.messagebox.showerror("Error","Network Error")

        
        def thread_mess():

            t=threading.Thread(target=send)
            t.start()





        def clear():
            number.set("")
            hour.set("Select Hours")
            minutes.set("Select Minutes")
            txt.delete("1.0","end")




#=======================frame================================#
        mainframe=Frame(self.root,width=500,height=350,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=290,relief="ridge",bd=3,bg="#7964dd")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=53,relief="ridge",bd=3,bg="#534053")
        secondframe.place(x=0,y=290)

#===========================firstframe=========================================#
        lab_number=Label(firstframe,text="Enter Number",font=('times new roman',12),bg="#7964dd",fg="white")
        lab_number.place(x=20,y=20)

        ent_number=Entry(firstframe,width=30,font=('times new roman',12),relief="ridge",bd=3,textvariable=number)
        ent_number.place(x=150,y=20)


        lab_time=Label(firstframe,text="Select Time",font=('times new roman',12),bg="#7964dd",fg="white")
        lab_time.place(x=20,y=90)


        hours_list=list(range(1,25))
        hours_list_combo=Combobox(firstframe,values=hours_list,font=('arial',10),width=13,state="readonly",textvariable=hour)
        hours_list_combo.set("Select Hours")
        hours_list_combo.place(x=150,y=90)


        minutes_list=list(range(0,61))
        minutes_list_combo=Combobox(firstframe,values=minutes_list,font=('arial',10),width=13,state="readonly",textvariable=minutes)
        minutes_list_combo.set("Select Minutes")
        minutes_list_combo.place(x=280,y=90)


        lab_message=Label(firstframe,text="Message",font=('times new roman',12),bg="#7964dd",fg="white")
        lab_message.place(x=200,y=140)

        txt=Text(firstframe,width=40,height=5,font=('times new roman',12),relief="ridge",bd=3)
        txt.place(x=80,y=170)

        

#========================secondframe===========================================#

        but_send=Button(secondframe,width=13,text="Send",font=('times new roman',12),cursor="hand2",command=thread_mess)
        but_send.place(x=60,y=8)
        but_send.bind("<Enter>",on_enter1)
        but_send.bind("<Leave>",on_leave1)

        but_clear=Button(secondframe,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=290,y=8)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)




if __name__ == "__main__":
    root=Tk()
    app=Whatsapp(root)
    root.mainloop()