from distutils.cmd import Command
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import *
from tkinter.ttk import Style

#import emailsender

root = Tk()
root.title("Email Spammer")
root.geometry("300x250")

#STYLE

style = Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = '#0492c2')

#LabelSection
label1 = Label(root , text="Sender's Email")
label2 = Label(root , text="Receiver's Email")
label3 = Label(root , text="Message")
label4 = Label(root , text="Hours")
label5 = Label(root , text="Number of Emails")

label1.grid(row=0 , column=0)
label2.grid(row=1 , column=0)
label3.grid(row=2 , column=0)
label4.grid(row=3 , column=0)
label5.grid(row=4 , column=0)


#textBoxSection

senderemail = Entry(root , width=25, borderwidth=5)
senderemail.grid(row=0, column=2, columnspan=3)
receiveremail = Entry(root , width=25, borderwidth=5)
receiveremail.grid(row=1, column=2, columnspan=3)
msg = Entry(root , width=25, borderwidth=5)
msg.grid(row=2, column=2, columnspan=3)
hrs = Entry(root , width=25, borderwidth=5)
hrs.grid(row=3, column=2, columnspan=3)
noe = Entry(root , width=25, borderwidth=5)
noe.grid(row=4, column=2, columnspan=3)

#variables to save info


time = hrs.get()



#function

def onClick() :
    count = 0
    while count < int(noe.get()) :
        email_sender = senderemail.get()
        email_password = 'cuqvibvupktbqrts'

        email_receiver = receiveremail.get()

        subject = "SPAM"
        body =   msg.get()

        em = EmailMessage()
        em['From'] = email_sender
        em['to'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com' , 465 , context = context) as smtp: 
        #smtp = simple mail transfer protocol which is used to connect web browser to mail server
        #    first parameter is server location ; second is port used(use 587 for gmail)   
            smtp.login(email_sender , email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
           
            count += 1

        


#button

btn = Button(root , text="SEND" ,  command= onClick )
btn.grid(row= 6 , column=3, padx=50 , pady=50)






root.mainloop()