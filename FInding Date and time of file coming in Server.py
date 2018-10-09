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
print()
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
