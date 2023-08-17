# Import library
import tkinter as tk
import subprocess
 
# Create window Tkinter
window = tk.Tk()
 
# Name our Tkinter application title
window.title(" Simple Windows App ")
 
# Define window size in Tkinter python
window.geometry("700x500")
 
# Create a label widget in Tkinter
label = tk.Label(window, text="Nhận diện khuôn mặt",
font=('Calibri 15 bold'))
label.pack(pady=20)
 
# Function to open file dataSet.py
def open_file_dataSet():
    file_path = "dataSet.py"
    subprocess.Popen(["python", file_path], shell=True)
     
# Function to open file trainingImg.py
def open_file_trainingImg():
    file_path = "trainingImg.py"
    subprocess.Popen(["python", file_path], shell=True)

# Function to open file RecognitionData.py
def open_file_RecognitionData():
    file_path = "RecognitionData.py"
    subprocess.Popen(["python", file_path], shell=True)
     
# Create 1st button to open file dataSet.py
btn1 = tk.Button(window, text="Nhập thông tin", command=open_file_dataSet)
btn1.pack(pady=20)
 
# Create 2nd button to open file trainingImg.py
btn2 = tk.Button(window, text="Training", command=open_file_trainingImg)
btn2.pack(pady=40)

# Create 3rd button to open file RecognitionData.py
btn2 = tk.Button(window, text="Nhận diện", command=open_file_RecognitionData)
btn2.pack(pady=40)

# Run main loop
window.mainloop()