import os
import re
import signal
import datetime
import time
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
from email.mime.base import MIMEBase

file_incoming_path = "/home/suriya/extractors/"
TotalFile = set(
    ["first.tar.gz", "second.tar.gz", "third.tar.gz", "fourth.tar.gz", "fifth.zip", "sixth.zip", "seventh.zip",
     "eight.zip", "ninth.zip", "ten.zip"])
# print TotalFile
ls = set(os.listdir(file_incoming_path))
# print ls
ReceivedFileList = list(TotalFile.intersection(ls))  # FG06.tar.gz,#CLG1_backlog.tar.gz
NotReceivedFileList = list(ls.union(TotalFile) - ls.intersection(TotalFile))
# print NotReceivedFileList
# print ReceivedFileList
FileDescriptionName = list()
process_date_found = list()
start_time_found = list()
start_utc_time_found = list()
file_size_found = list()
color = list()
TAR = '[\w\W\d\_\s]+.tar.gz'  # Regular Expression
ZIP = '[\w\W\d\_@\s]+.zip'  # Regular Expression
CompiledTar = re.compile(TAR)
CompiledZip = re.compile(ZIP)
# print CompiledTar
# print CompiledZip
Today10am = str(datetime.time(hour=10, minute=0, second=0, microsecond=0))
print
Today10am
for i in ReceivedFileList:
    if CompiledTar.match(i):
        FileDescriptionName.append(i[::-1].split('.', 1)[1].split('.', 1)[1][::-1])
        process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
        file_size_found.append(str(((os.path.getsize(file_incoming_path + i)))))
        TimeArrived = datetime.datetime.now().time().strftime('%H:%M %p')
        start_utc_time_found.append(datetime.datetime.utcnow().strftime("%H:%M %p"))
        if TimeArrived > Today10am:
            start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
            print
            "arrived delay"
            color.append("yellow")
        if TimeArrived <= Today10am:
            start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
            print
            "arrived on time"
            color.append("green")
    if CompiledZip.match(i):
        FileDescriptionName.append(i[::-1].split('.', 1)[1][::-1])
        process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
        file_size_found.append(str(((os.path.getsize(file_incoming_path + i)))))
        TimeArrived = datetime.datetime.now().time().strftime('%H:%M %p')
        start_utc_time_found.append(datetime.datetime.utcnow().strftime("%H:%M %p"))
        if TimeArrived > Today10am:
            print
            "arrived delay"
            start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
            color.append("yellow")
        if TimeArrived <= Today10am:
            start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
            print
            "arrived on time"
            color.append("green")
for i in NotReceivedFileList:
    if CompiledTar.match(i):
        FileDescriptionName.append(i[::-1].split('.', 1)[1].split('.', 1)[1][::-1])
        process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
        start_time_found.append("N/A")
        start_utc_time_found.append("N/A")
        file_size_found.append("not mentioned")
        color.append("red")
    if CompiledZip.match(i):
        FileDescriptionName.append(i[::-1].split('.', 1)[1][::-1])
        process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
        start_time_found.append("N/A")
        file_size_found.append("not mentioned")
        start_utc_time_found.append("N/A")
        color.append("red")

print
FileDescriptionName
print
color
print
process_date_found
print
start_time_found
print
start_utc_time_found
print
file_size_found

style = "background:"
style1 = "style="
fromaddr = "creativityshah@gmail.com"
toAddr = "aakashkumar667@gmail.com"
# toadr = ', '.join(str(e) for e in toAddr)
# print toadr
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toAddr
msg['Subject'] = "Daily record count Status"
part = MIMEBase('application', "octet-stream")
Encoders.encode_base64(part)
html = '<html> <head>  </head> <body> <h1>Statistics</h1> <table style="border-collapse: collapse;" border="1" width="1000" cellspacing="0" cellpadding="0"> <tr style="background: #4d20bc;"> <td colspan="2" rowspan="3" style="margin-left:15px"; class="decorate">Feeding&nbsp;System</td> <td rowspan="3" class="decorate" style="margin-left:15px";>File&nbsp;Size</td> <td rowspan="3" class="decorate" style="margin-left:15px";>File&nbsp;Dated</td><td rowspan="3" class="decorate" style="margin-left:15px";> Type </td> <td rowspan="3" class="decorate" style="margin-left:15px";> Critical/Non&nbsp;Critical </td><td colspan="4" width="256" class="decorate" style="margin-left:100px";>Cut-off&nbsp;Time</td><td rowspan="3" class="decorate" style="margin-left:5px";>Status</td> </tr> <tr style="background: #4d20bc;"> <td colspan="2" class="decorate" style="margin-left:45px"; >Standard </td><td colspan="2" class="decorate" style="margin-left:45px";> Actual </td> </tr> <tr style="background: #4d20bc;"> <td class="decorate" style="margin-left:20px";>IST </td><td class="decorate" style="margin-left:20px";>CET </td> <td class="decorate" style="margin-left:20px";>IST </td> <td class="decorate" style="margin-left:20px";>CET </td></tr>'
for i in xrange(0, len(FileDescriptionName)):
    html += '<tr><td style="background:pink";></td><td ' + "style=\"font-size:14px;\"" + '' + ">" + ''.join(
        FileDescriptionName[i:i + 1]) + '</td><td>' + '</td><td>'.join(
        file_size_found[i:i + 1]) + '</td><td>' + '</td><td>'.join(process_date_found[
                                                                   i:i + 1]) + '</td><td>Outbound</td><td>Non-crictal</td><td>10:00&nbsp;AM</td><td>5:30&nbsp;PM</td><td>' + '</td><td>'.join(
        start_time_found[i:i + 1]) + '</td><td>' + '</td><td>'.join(
        start_utc_time_found[i:i + 1]) + '</td><td ' + '' + style1 + '"' + style + '" "'.join(
        color[i:i + 1]) + ';">&nbsp;</td></tr>'
html += '</table><p>Status : <span style="color:green;"> GREEN </span> - File arrival on-time, <span style="color:yellow;"> YELLOW</span> - File arrival delayed, <span style="color:red;"> RED </span> - File not received in time and previous day file is used for load</p></body></html>'

part2 = MIMEText(html, 'html')
msg.attach(part2)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "12345@shah")
text = msg.as_string()
server.sendmail(fromaddr, toAddr, text)
print
"mail sent successfully"
server.quit()
# write to another file
