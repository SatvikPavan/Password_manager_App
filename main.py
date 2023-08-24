# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_entry.insert(0,f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

def save():
    website=website_entry.get()
    email=Email_entry.get()
    password=password_entry.get()
    if len(website) == 0 or len(password)==0:
        pop_up=messagebox.showinfo(title="oops", message="please dont leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nemail:{email} \npassword:{password} \nIs it ok to save?")
        if is_ok:
            f=open("data.txt","a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    # f.open("data.txt","r")
canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

Email_label=Label(text="Email/Username:")
Email_label.grid(column=0,row=2)


password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)


Add_button=Button(text="Add",width=36,command=save)
Add_button.grid(column=1,row=4,columnspan=2)

website_entry=Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
website_entry.get()

Email_entry=Entry(width=40)
Email_entry.grid(column=1,row=2,columnspan=2)
Email_entry.insert(0, "satvik@gmail.com")
Email_entry.get()

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)
password_entry.get()



window.mainloop()
