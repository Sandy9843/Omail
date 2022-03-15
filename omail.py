from tkinter import *
import tkinter
from tkinter.tix import COLUMN
from turtle import bgcolor, heading
from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#tkinter
def env():
    def enviar2():
        #omail enviar omail
        CLIENT_SECRET_FILE = "json/omail_claves.json"
        API_NAME = "gmail"
        API_VERSION = "v1"
        SCOPES = ["https://mail.google.com/"]
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        titulo1 = ""
        contenido1 = ""
        para1 = ""
        mimeMessage = MIMEMultipart()
        contenido1 = contenido.get()
        emailMsg = contenido1
        mimeMessage.attach(MIMEText(emailMsg, "plain"))
        para1 = para.get()
        mimeMessage["to"] = para1
        titulo1 = titulo.get()
        mimeMessage["subject"] = titulo1 #titulo
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId = "me", body = {"raw": raw_string}).execute()
        print(titulo1)
        print(contenido1)
        print(para1)
    #enviar
    ventana2 = tkinter.Tk()
    ventana2.title("mensaje nuevo")
    ventana2.geometry("510x450")
    ventana2.positionfrom()
    para =  tkinter.Entry(ventana2, font= "Helvetiica 18", width="39")
    para.place(x=0,y=18)
    titulo =  tkinter.Entry(ventana2, font= "Helvetiica 18", width="39")
    titulo.place(x=0,y=58)
    contenido =  tkinter.Entry(ventana2, width="63")
    contenido.place(x=0,y=90)
    enviar2 = tkinter.Button(ventana2, text= "Enviar", command= enviar2, bg="#1a73e8",  fg="white", width="10", height="2")
    enviar2.place(x=15,y=398)
    ventana2.mainloop()
#omail
ventana = Tk()
ventana.title("Omail")
ventana.state('zoomed')
ventana.geometry("510x450")
ventana.configure(bg="#007cff")
enviar = tkinter.Button(ventana, text= "Redactar", command= env, bg="white",  fg="black", width="20", height="2")
enviar.place(x=0,y=0)
ventana.mainloop()
#tkinter enviar omai