import smtplib
from email.header import Header
from email.mime.text import MIMEText


class NewsEmail:
    def __init__(self,user:str , pwd, send, receiver_list, content, subject = '', ) -> None:
        self.user = user    
        self.pwd = pwd      
        self.send = send
        self.receiver_list = receiver_list
        self.content = content
        self.subject = 'DALIY NEWS  -- your personal news collector!'
        self.type = user[user.find('@') + 1: user.find('.')]

    def send_email(self):
        msg = MIMEText(self.content, 'html', 'utf-8')
        msg['Subject'] = Header(self.subject, 'utf-8')
        try:
            smt = smtplib.SMTP(f'smtp.{self.type}.com')
            smt.helo()
            smt.ehlo()
            smt.login(self.user, self.pwd)
            for receiver in self.receiver_list:
                smt.sendmail(self.send, receiver, msg.as_string())
            smt.quit()
 
        except Exception as e:
            print(e)


 
