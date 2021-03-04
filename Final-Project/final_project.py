# Import Library
import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass

# Membaca daftar email lalu dibuat menjadi list
read_email = open("daftaremail.txt", "r")
daftar_email = (read_email.read().splitlines())
#print (daftar_email)

# Membaca nama yang tertera sebelum @ pada nama email
nama_email = []
for email in daftar_email:
    nama = email.split("@")
    nama_email.append(nama[0])
# print(nama_email)

# User configuration
sender_email = "wheremybrainp@gmail.com"
sender_name = "Python-Dean"

# Input Password email pengirim
password = getpass(prompt='Masukkan Password: ')

# Data penerima dalam bentuk list
receiver_emails = daftar_email
receiver_names = nama_email


# Email body
email_html = open('email.html')
email_body = email_html.read()

# nama file yang ingin dikirim
filename = "namecard.jpg"

# Proses pengiriman email
for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
    print("Mengirim email...")
    # Pengaturan informasi pengirim
    msg = MIMEMultipart()
    msg['To'] = formataddr((receiver_name, receiver_email))
    msg['From'] = formataddr((sender_name, sender_email))
    msg['Subject'] = 'Hello, ' + receiver_name + '. This is my AIM Basic Python Final Project'

    msg.attach(MIMEText(email_body, 'html'))

# Encode Gambar ke Base 64
    try:
        # Open file in binary mode
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        msg.attach(part)
    except Exception as e:
        print(f'Oh no! We didn\'t found the attachment!\n{e}')

    try:
        # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Encrypts the email
        context = ssl.create_default_context()
        server.starttls(context=context)
        # We log in into our Google account
        server.login(sender_email, password)
        # Sending email from sender, to receiver with the email body
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email terkirim!')
    except Exception as e:
        print(f'Oh no! Something bad happened!\n {e}')
    finally:
        print('Menutup server...')
        server.quit()
print("Program Telah Selesai! Terima Kasih")
