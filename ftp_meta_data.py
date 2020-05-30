"""
@author: brian.dsouza
"""
import datetime
import time
import ftputil
from dateutil import parser
import os
import csv
try:
    csv_file = open('ftp_meta_data.csv','w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Folder','File_Name','Size','Last_Modified'])
    
    with ftputil.FTPHost('ipaddress', 'username', 'password') as ftp_host:
        ist = pytz.timezone("Asia/Kolkata")
        print('Connected')
        foldersorfiles = ftp_host.listdir(ftp_host.curdir)
        print("List of folders or filenames "+foldersorfiles)
        check_dir = 'mention the location name here' 
        #check_dir ='/brian/folder/'
        folders = ftp_host.listdir(check_dir)
            for file in filesInsideFolder:
                print(file) 
                filePath = check_dir+'/'+file
                info = ftp_host.stat(filePath)
                                       
                csv_writer.writerow([folders,file,info.st_size])
    

    csv_file.close()
except Exception as e:
    print('Error in FTP:: ' + str(e))
        
