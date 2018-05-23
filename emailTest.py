import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
fromaddr = "sinker78@gmail.com"
toaddr = "gkresse@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing"
 
body = "This is a test!\nThis is a test!\nThis is a test!"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "z@r18gma78")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
