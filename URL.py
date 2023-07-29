#Task-3 URL Shortener

from tkinter import *
import pyshorteners

root=Tk()
root.title("shweta pal - URL Shortener")
root.iconbitmap(r"C:\Users\Shweta\Downloads\image.ico")
root.geometry("500x500")
root.configure(bg="lightblue")

#function to shorten the link

def shortenlink():
    longURL=my_entry.get()

    #shorten URL
    shortURL=pyshorteners.Shortener().tinyurl.short(longURL)

    #output it to the screen
    short_link_label.insert(END,shortURL)

#creating the GUI

label_1=Label(root,text="Enter Link to Shorten",font=("Helvetica",20),bg="lightblue")
label_1.pack(pady=30)

my_entry=Entry(root,font=("Helvetica",20))
my_entry.pack(pady=10)

my_button=Button(root,text="Shorten Link",font=("Helvetica",20),command=shortenlink,bg='lightgrey')
my_button.pack(pady=50)

label_2=Label(root,text="Shortened Link",font=("Helvetica",20),bg="lightblue")
label_2.pack(pady=10)

short_link_label=Entry(root,font=("Helvetica",20),bd=0,bg="lightblue",justify=CENTER,width=30)
short_link_label.pack(pady=30)

root.mainloop()

