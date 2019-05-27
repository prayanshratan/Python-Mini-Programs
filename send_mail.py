import smtplib

fadd= 'prayanshratan2984@gmail.com'
tadd= 'no-reply@etretail.com'
msg= 'Mssg sent by Python!'
username= fadd
password= 'ratan2984'
server= smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fadd, tadd, msg)