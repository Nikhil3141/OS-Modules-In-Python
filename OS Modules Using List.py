import os
import signal
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
file_incoming_path="/Users/nitinsingh/Desktop/untitled folder 4"#Puting Path of your Files
ls=set(os.listdir(file_incoming_path))
print(ls)
process_date_found=list()
TimeArrived=list()
start_utc_time_found=list()
file_size_found=list()
color=list()
for i in file_incoming_path:
    TimeArrived = datetime.datetime.now().time().strftime('%H:%M %p')
    start_utc_time_found.append(datetime.datetime.utcnow().strftime("%H:%M %p"))
    process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
    file_size_found.append(str(((os.path.getsize("/Users/nitinsingh/Desktop/untitled folder 4")))))#Puting Path of your Files
print (start_utc_time_found)
print(file_size_found)
print(process_date_found)
html = """\
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
    text-align: centre;
}
</style>
</head>
<body>

<h2>File Access Using List</h2>

<table style="width:100%">
  <caption> File Date and Time </caption>
  <tr>
    <th>File</th>
    <th>Date and Time</th>
  </tr>
  <tr>
    <td>` </td>
    <td> </td>
  </tr>
 """
for (j,k,l) in zip(start_utc_time_found,file_size_found,process_date_found):
    html = html + "<tr><td>" + j + "</td><td>" + k+ "</td><td>" + l + "</td></tr>"
html = html + """
</table>

</body>
</html>
"""

print(html)