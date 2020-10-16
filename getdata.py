import requests
import urllib
import json
import csv

base_url = 'http://www.rmto.ir/_layouts/15/inplview.aspx?List=%7B5D5CCD01-729D-4994-B175-9D0B536F9557%7D&View=%7B1B59108F-35D0-4156-AC7F-A34A7318327D%7D&ViewCount=14&IsXslView=TRUE&IsCSR=TRUE&ListViewPageUrl=http%3A%2F%2Fwww.rmto.ir%2Flists%2Flist31%2Fallitems.aspx'

f = open('data.csv', 'w', encoding = 'utf-8-sig')
o = csv.writer(f)

o.writerow(["ID", "PermMask", "FSObjType", "Title", "FileLeafRef", "Created_x0020_Date.ifnew", "FileRef", "File_x0020_Type",
    "File_x0020_Type.mapapp", "HTML_x0020_File_x0020_Type.File_x0020_Type.mapcon", "HTML_x0020_File_x0020_Type.File_x0020_Type.mapico",
    "ContentTypeId", "_x0634__x0645__x0627__x0631__x06", "_x06a9__x062f__x0020__x0634__x06", "_x0646__x0627__x0645__x0020__x06",
    "_x0627__x0633__x062a__x0627__x06", "_x0634__x0647__x0631__x0020__x06", "_x0634__x0646__x0627__x0633__x06",
    "_x0648__x0636__x0639__x06cc__x06", "_x0646__x0648__x0639__x0020__x06", "_x0646__x0627__x0645__x0020__x060",
    "_x0647__x0648__x06cc__x062a_", "_x0646__x0627__x0645__x0020__x061", "_x0646__x0648__x0639__x0020__x060",
    "_x0645__x0633__x0626__x0648__x06", "_x0645__x062c__x0648__x0632__x00", "_x062d__x0648__x0632__x0647__x00",
    "_x0632__x0645__x06cc__x0646__x06", "_x0646__x0648__x0639__x0020__x061", "_x062a__x0635__x0631__x0641__x00",
    "_x067e__x0627__x06cc__x0627__x06", "_x062a__x0627__x0631__x06cc__x06", "_x0634__x0645__x0627__x0631__x060",
    "_x0646__x0648__x0639__x0020__x062", "_x0622__x062f__x0631__x0633__x00", "_x0645__x062c__x0648__x0632__x000"
])
            
for i in range (1, 152):
    print("Downloading page: {}".format(i))
    page = 12302 + i*30
    first_row = 1 + i*30
    if i > 0:
        url = base_url + "&Paged=TRUE&p_ID={page}&PageFirstRow={first_row}".format(page = page , first_row = first_row)
    else:
        url = base_url
    
    r = requests.post(url)
    if r.status_code == 200:
        print("Downloaded, now saving")
        data = r.json()
        for row in data["Row"]:
            o.writerow([
                row.get("ID"),
                row.get("PermMask"),
                row.get("FSObjType"),
                row.get("Title"),
                row.get("FileLeafRef"),
                row.get("Created_x0020_Date.ifnew"),
                row.get("FileRef"),
                row.get("File_x0020_Type"),
                row.get("File_x0020_Type.mapapp"),
                row.get("HTML_x0020_File_x0020_Type.File_x0020_Type.mapcon"),
                row.get("HTML_x0020_File_x0020_Type.File_x0020_Type.mapico"),
                row.get("ContentTypeId"),
                row.get("_x0634__x0645__x0627__x0631__x06"),
                row.get("_x06a9__x062f__x0020__x0634__x06"),
                row.get("_x0646__x0627__x0645__x0020__x06"),
                row.get("_x0627__x0633__x062a__x0627__x06"),
                row.get("_x0634__x0647__x0631__x0020__x06"),
                row.get("_x0634__x0646__x0627__x0633__x06"),
                row.get("_x0648__x0636__x0639__x06cc__x06"),
                row.get("_x0646__x0648__x0639__x0020__x06"),
                row.get("_x0646__x0627__x0645__x0020__x060"),
                row.get("_x0647__x0648__x06cc__x062a_"),
                row.get("_x0646__x0627__x0645__x0020__x061"),
                row.get("_x0646__x0648__x0639__x0020__x060"),
                row.get("_x0645__x0633__x0626__x0648__x06"),
                row.get("_x0645__x062c__x0648__x0632__x00"),
                row.get("_x062d__x0648__x0632__x0647__x00"),
                row.get("_x0632__x0645__x06cc__x0646__x06"),
                row.get("_x0646__x0648__x0639__x0020__x061"),
                row.get("_x062a__x0635__x0631__x0641__x00"),
                row.get("_x067e__x0627__x06cc__x0627__x06"),
                row.get("_x062a__x0627__x0631__x06cc__x06"),
                row.get("_x0634__x0645__x0627__x0631__x060"),
                row.get("_x0646__x0648__x0639__x0020__x062"),
                row.get("_x0622__x062f__x0631__x0633__x00"),
                row.get("_x0645__x062c__x0648__x0632__x000"),
            ])


    else:
        print("Finished downloading or error occured")
        print(r.status_code)
        print(r.text)
        break
f.close()