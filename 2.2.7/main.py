import turtle as trtl
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded
def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("2.2.7")

ping_img = tk.PhotoImage(file="dclogo.gif").subsample(4, 4)
ns_img = tk.PhotoImage(file="etnieslogo.gif").subsample(4, 4)
trace_img = tk.PhotoImage(file="nikesblogo.gif").subsample(4, 4)
save_img = tk.PhotoImage(file="dvslogo.gif").subsample(4, 4) 
dig_img = tk.PhotoImage(file="vanzlogo.gif").subsample(4, 4) 

# set up buttons to run the do_command function
ping_btn = tk.Button(frame, text="Ping URL", image=ping_img, compound="left",command=lambda: do_command("ping -c 10"))
ping_btn.grid(row=0, column=0, padx=10)

ns_btn = tk.Button(frame, text="NS lookup URL", image=ns_img, compound="left", command=lambda: do_command("nslookup -c 10"))
ns_btn.grid(row=0, column=1, padx=10)

trace_btn = tk.Button(frame, text="Trace route URL", image=trace_img, compound="left",command=lambda: do_command("traceroute -c 10"))
trace_btn.grid(row=0, column=2, padx=10)

dig_btn = tk.Button(frame, text="dig URL", image=dig_img, compound="left",command=lambda: do_command("dig -c 10"))
dig_btn.grid(row=0, column=4, padx=10)

save_btn = tk.Button(frame, text="Save", image=save_img, compound="left", command=mSave)
save_btn.grid(row=0, column=3, padx=10)


# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=200, width=275)
command_textbox.pack()

root.mainloop()




#https://logoeps.com/wp-content/uploads/2013/08/dvs-shoe-vector-logo.png dvs logo
#https://upload.wikimedia.org/wikipedia/en/thumb/7/70/DCSHOECOUSA_Logo.svg/640px-DCSHOECOUSA_Logo.svg.png dc logo
#https://i.pinimg.com/originals/08/a1/f7/08a1f7e68c1804749579a1329078f6c4.jpg vanz logo
#https://upload.wikimedia.org/wikipedia/commons/5/5c/Nike_SB_logo.png nike sb logo
#https://i.pinimg.com/736x/64/0a/18/640a1803b7fe81d637b2ea91207f04c3.jpg etnies logo