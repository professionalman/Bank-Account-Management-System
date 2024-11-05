from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql
import datetime


date = datetime.datetime.now().date()
date= str(date)

class Appli(object):
  def __init__(self, master):
     self.master=master
     def sub():
         acc_no= DoubleVar()
         amount= DoubleVar()
         phone_no= DoubleVar()
         acc_no = (e_acc_no.get())
         fname = (e_fname.get())
         lname = (e_lname.get())
         d_ob= (e_d_ob.get())
         s_c = (t.get())
         amount = (e_amount.get())
         address = (e_address.get())
         phone_no = (e_phone_no.get())
         m_f_t = (i.get())

         if (acc_no == "" or fname == "" or s_c == "" or amount =="" or address =="" or phone_no == "" or m_f_t ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="root", database="bank_data")
             cursor= con.cursor()
             cursor.execute("insert into acct values('" + acc_no + "','"+ fname +"','"+ lname +"','"+ d_ob +"', '"+ s_c +"','"+ amount +"' , '"+ address +"','" + phone_no + "', '"+ m_f_t +"')")
             cursor.execute("insert into users values('" + acc_no + "','"+ phone_no +"')")
             cursor.execute("commit")
             MessageBox.showinfo("Insert Status", "Inserted Successfully")
             e_fname.delete(0,'end')
             e_lname.delete(0,'end')
             e_amount.delete(0,'end')
             e_address.delete(0,'end')
             e_phone_no.delete(0,'end')
             e_d_ob.delete(0,'end')
             con.close()


     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#fcad03")
     self.bottom.pack(fill=X)

     #top Frame design
     self.top_image=PhotoImage(file='icon/money.png')
     self.top_image_lable= Label(self.top, image=self.top_image, bg="white")
     self.top_image_lable.place(x=100, y=15)

     self.top_image2=PhotoImage(file='icon/money.png')
     self.top_image2_lable= Label(self.top, image=self.top_image, bg="white")
     self.top_image2_lable.place(x=750, y=15)

     self.heading= Label(self.top, text="Create Account", font="arial 18 bold", bg="white")
     self.heading.place(x= 370, y=30)

     #bottom Frame Design

     #buttons and lables
     acc_no= DoubleVar()
     acc_no = Label(self.bottom, text="Account number ", font="arial 14 bold", bg="#fcad03")
     acc_no.place(x=40, y=55)

     fname = Label(self.bottom, text="First Name ", font="arial 14 bold", bg="#fcad03")
     fname.place(x=40, y=110)

     lname = Label(self.bottom, text="Last Name ", font="arial 14 bold", bg="#fcad03")
     lname.place(x=40, y=165)

     s_c = Label(self.bottom, text="Account Type ", font="arial 14 bold", bg="#fcad03")
     s_c.place(x=40, y=220)

     amount= DoubleVar()
     amount = Label(self.bottom, text="Initial Amount ", font="arial 14 bold", bg="#fcad03")
     amount.place(x=40, y=275)

     address = Label(self.bottom, text="Address ", font="arial 14 bold", bg="#fcad03")
     address.place(x=40, y=330)
     
     phone_no= DoubleVar()
     phone_no = Label(self.bottom, text="Phone Number ", font="arial 14 bold", bg="#fcad03")
     phone_no.place(x=40, y=385)

     m_f_t = Label(self.bottom, text="Sex ", font="arial 14 bold", bg="#fcad03")
     m_f_t.place(x=40, y=440)

     d_ob = Label(self.bottom, text="Date of Birth ", font="arial 14 bold", bg="#fcad03")
     d_ob.place(x=40, y=495)

     #Enteries
     
     e_acc_no= Entry(self.bottom, width= "60", textvariable=acc_no)
     e_acc_no.place(x=320, y=55)

     e_fname= Entry(self.bottom, width= "60")
     e_fname.place(x=320, y=110)

     e_lname= Entry(self.bottom, width= "60")
     e_lname.place(x=320, y=165)

     t= StringVar()
     Radiobutton(self.bottom, text="Savings Account",  value="S", bg="#fcad03", variable=t).place(x=320, y=220)
     Radiobutton(self.bottom, text="Current Account",  value="C", bg="#fcad03", variable=t).place(x=450, y=220)

     e_amount= Entry(self.bottom, width= "60")
     e_amount.place(x=320, y=275)

     e_address= Entry(self.bottom, width= "60")
     e_address.place(x=320, y=330)
     
     e_phone_no= Entry(self.bottom, width= "60")
     e_phone_no.place(x=320, y=385)

     i= StringVar()
     Radiobutton(self.bottom, text="Male",  value="M", bg="#fcad03", variable=i).place(x=320, y=440)
     Radiobutton(self.bottom, text="Female",  value="F", bg="#fcad03", variable=i).place(x=430, y=440)
     Radiobutton(self.bottom, text="Transgender",  value="T", bg="#fcad03", variable=i).place(x=540, y=440)

     e_d_ob= Entry(self.bottom, width= "60")
     e_d_ob.place(x=320, y=495)

     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="30", command=sub)
     self.submit.place(x=320 , y=550)
     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("900x700+200+0")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
