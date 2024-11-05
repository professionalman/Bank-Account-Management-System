from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql



class Appli(object):
  def __init__(self, master):
     self.master=master

     def upd():
         acc_no= DoubleVar()
         acc_no = (e_acc_no.get())
         if (acc_no == "" ):
             MessageBox.showinfo("ID is required for delete", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="root", database="bank_data")
             cursor= con.cursor()
             cursor.execute("select amount from acct where acc_no='" + acc_no + "'")
             myresul = cursor.fetchall()
             for x in myresul:
                 print(x)
                 fb.insert(0,x)
             cursor.execute("commit")
             MessageBox.showinfo("Update Status", "Deposited Successfully")
             con.close()




     def dept():
         amtn= dp.get()
         acc_no= DoubleVar()
         acc_no = (e_acc_no.get())
         if (acc_no == "" ):
             MessageBox.showinfo("ID is required for delete", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="root", database="bank_data")
             cursor= con.cursor()
             cursor.execute("update acct set amount= amount + ('" + amtn + "') where acc_no='" + acc_no + "'")
             cursor.execute("commit")
             con.close()
             upd()

     
     def sub():
         acc_no= DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="root", database="bank_data")
             cursor= con.cursor()
             cursor.execute("select amount from acct where acc_no='" + acc_no + "'")
             myresult = cursor.fetchall()
             for x in myresult:
                 print(x)
                 lb.insert(0,x)
             cursor.execute("commit")
             con.close()
             

             


     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#fcad03")
     self.bottom.pack(fill=X)

     #top Frame design
     self.top_image=PhotoImage(file='icon/money.png')
     self.top_image_lable= Label(self.top, image=self.top_image, bg="white")
     self.top_image_lable.place(x=50, y=15)

     self.top_image2=PhotoImage(file='icon/money.png')
     self.top_image2_lable= Label(self.top, image=self.top_image, bg="white")
     self.top_image2_lable.place(x=580, y=15)

     self.heading= Label(self.top, text="Balance Deposit", font="arial 18 bold", bg="white")
     self.heading.place(x= 265, y=30)

     #bottom Frame Design

     #buttons and lables
     acc_no= DoubleVar()
     acc_no = Label(self.bottom, text="Account number ", font="arial 14 bold", bg="#fcad03")
     acc_no.place(x=40, y=55)

     detail = Label(self.bottom, text="Current Balance ", font="arial 14 bold", bg="#fcad03")
     detail.place(x=40, y=110)

     amt = Label(self.bottom, text="Amount ", font="arial 14 bold", bg="#fcad03")
     amt.place(x=40, y=165)

     upb = Label(self.bottom, text="Updated Balance ", font="arial 14 bold", bg="#fcad03")
     upb.place(x=40, y=220)

     #Enteries
     
     e_acc_no= Entry(self.bottom, width= "60", textvariable=acc_no)
     e_acc_no.place(x=320, y=55)

     lb= Entry(self.bottom, width="60" )
     lb.place(x=320 , y= 110)

     dp= Entry(self.bottom, width="60" )
     dp.place(x=320 , y= 165)

     fb= Entry(self.bottom, width="60" )
     fb.place(x=320 , y= 220)





     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="52", command=sub)
     self.submit.place(x=45 , y=270)

     self.dep= Button(self.bottom, text=" Deposit ", font="arial 15 bold", width="52", command=dept)
     self.dep.place(x=45 , y=330)

     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("700x500+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
