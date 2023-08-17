#import library
import cv2
import numpy as np
import sqlite3
import os
import tkinter as tk
from tkinter import messagebox

#function to insert or update user
def insertOrUpdate(id, name):
  
  conn = sqlite3.connect('data.db')

  query = "SELECT * FROM people WHERE ID="+ str(id)
  cuscor = conn.execute(query)

  isRecordExist=0

  for row in cuscor:
    isRecordExist=1
    
  if(isRecordExist==0):
    query = "INSERT INTO people(ID, Name) VALUES("+str(id)+", '"+str(name)+"')"
  else:
    query = "UPDATE people SET Name=' "+str(name)+" ' WHERE ID="+str(id)
  conn.execute(query)
  conn.commit()
  conn.close()

  #load cv
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

  # open camera 
  cap = cv2.VideoCapture(0)

  sampleNum=0

  # capture user and save to folder dataSet
  while(True):
    
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in faces:
      cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

      if not os.path.exists('dataSet'):
        os.makedirs('dataSet')

      sampleNum +=1

      cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y: y+h, x: x+w])

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    
    if sampleNum > 50:
      break;
    
  cap.release()
  cv2.destroyAllWindows()
    
# Create window Tkinter
root = tk.Tk()

# Name our Tkinter application title
root.title("Nhập thông tin")

# Define window size in Tkinter python
root.geometry("700x500")


def submit():
    Id = entry1.get()
    Name = entry2.get()
    insertOrUpdate(Id, Name)
    messagebox.showinfo("Thông báo", "Thành công.")
    # root.after(2000, root.destroy())

def cancel():
    root.destroy()

# Create label widget in Tkinter
label1 = tk.Label(root, text="Nhập Id:")
label1.pack()

label2 = tk.Label(root, text="Nhập Name:")
label2.pack()

# Create input widget in Tkinter
entry1 = tk.Entry(root, bg="lightgray", fg="blue", font=("Helvetica", 16))
entry1.pack()

entry2 = tk.Entry(root, bg="lightgray", fg="blue", font=("Helvetica", 16))
entry2.pack()

# Create button widget in Tkinter
submit_button = tk.Button(root, text="OK", command=submit)
submit_button.pack()

submit_button = tk.Button(root, text="CANCEL", command=cancel)
submit_button.pack()

# Chạy vòng lặp sự kiện
root.mainloop()