import os
from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'daniromero1410@gmail.com'
email_contrasena = 'mmll dfca ojkz zavu'

email_receptor = 'laurafernandamm22@gmail.com'

asunto = 'Revisa el correo'
cuerpo = """
Te mande un correo, esta es una version de prueba desde un script de python 
"""



em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)


contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context = contexto) as smtp:
    smtp.login(email_emisor,email_contrasena)
    smtp.sendmail(email_emisor,email_receptor,em.as_string())
