from tkinter import *
import tkinter as tk
import pymongo
from tkinter import messagebox

client = pymongo.MongoClient('localhost:27017')
db = client['library_management']
collection = db['library']


def search_book():
    search = search1.get()
    
    result = collection.find_one({"book_name": search})

    if result:
        author = result.get('author', 'Sorry, Author Information is Not Available')
        publish_year = result.get('publication_year', 'Sorry, Publish Year is Not Found')

        messagebox.showinfo("SUCCESS", f"The Book '{search}' is Found:\nAuthor of Book: {author}\nPublish Year Of Book:{publish_year}")

    else:
        messagebox.showerror("Sorry", f"Sorry, The Book '{search}' is Not Presented in Library..!!")



def login():
    username = admin_username.get()
    password = admin_password.get()
    if username == 'mohit' and password == 'mohit':
        show_admin_dashboard()
    else:
        messagebox.showerror('Sorry..!!', 'Invalid Login Credential')


def search_book_by_author_name():
    author = author1.get()

    if author:
        result = collection.find_one({'author': author})

        if result:
            book_name = result.get('book_name', 'Sorry, Book Information is Not Found')
            book_author = result.get('author', 'Sorry, Author Information is Not Available')
            publish_year = result.get('publication_year', 'Sorry, Publish Year is Not Found')

            messagebox.showinfo('FOUND', f"Book Found\nBook Name → '{book_name}'\nWritten By → '{book_author}'\nPublish Year → {publish_year}")

        else:
            messagebox.showerror('Sorry..!!', f'No Book Found of Author: {author}')
    else:
        messagebox.showerror('Sorry..!!', f"Please Provide Author Details")

def search_book_by_publish_year():
    publish_year = publish_year1.get()

    if publish_year:
        result = collection.find_one({'publication_year': publish_year})
        
        if result:
            book = result.get('book_name', 'Sorry..!! Book is Not Found')
            author = result.get('author', 'Sorry..!! Author is Not Found')
            publication_year = result.get('publication_year', 'Sorry..!! Publish Year is Not Found')

            messagebox.showinfo('SUCCESS', f'Book is Found:\nBook Name → {book}\nAuthor Name → {author}\nPublication Year → {publication_year}')


        else:
            messagebox.showerror('Sorry..!!', 'Not Book Found of This Author')

    else:
        messagebox.showerror('Sorry..!!', 'Please Provide Publish Year..!!')
    




def show_admin_dashboard():
    
    def post_book():

            book_name = write_book_name.get()
            author = write_author_name.get()
            publish_year = write_publish_year.get()
            isbm_number = write_isbm_number.get()

            if book_name and author and publish_year and isbm_number:    
                book_data = {
                    "book_name": book_name,
                    "author": author,
                    "publication_year": publish_year,
                    "ISBM": isbm_number,
                }

                collection.insert_one(book_data)
                messagebox.showinfo("SUCCESS", f"The Book {book_name}, of {author}, on {publish_year}, of {isbm_number} is successfully Uploaded")

            else:
                messagebox.showerror('Sorry..!!', 'Book Details are Not Completely Filled')

    def logout():
        root.deiconify()
        admin_dashboard.destroy()


    root.withdraw()
    admin_dashboard = tk.Toplevel(root)
    admin_dashboard.geometry('850x400')
    admin_dashboard.minsize(400, 650)
    admin_dashboard.config(bg='grey')
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.iconbitmap('library.ico')


    header = Label(admin_dashboard, text="Hello Welcome To Admin Dashboard", bg='black', fg='white', font=("Proxima Nova", 25, 'bold'), height=1)
    header.pack(side=TOP, fill=X)

    book_upload = Frame(admin_dashboard, bg='grey')
    book_upload.pack(anchor=NW, padx=30)

    blank_space = Label(book_upload, text="", bg='grey')
    blank_space.grid(row=0, column=0)

    
    book_title = Label(book_upload, text="Enter The Book Name: ", bg='grey', font=('arial',10))
    book_title.grid(row=1, column=0)

    write_book_name = Entry(book_upload)
    write_book_name.grid(row=1, column=1)


    blank_space = Label(book_upload, text="", bg='grey')
    blank_space.grid(row=2, column=0)


    author_name = Label(book_upload, text="Enter The Book Author: ", bg='grey', font=('arial',10))
    author_name.grid(row=3, column=0)

    write_author_name = Entry(book_upload)
    write_author_name.grid(row=3, column=1)


    blank_space = Label(book_upload, text="", bg='grey')
    blank_space.grid(row=4, column=0)


    publish_year = Label(book_upload, text="Enter The Book Publish Year: ", bg='grey', font=('arial',10))
    publish_year.grid(row=5, column=0)

    write_publish_year = Entry(book_upload)
    write_publish_year.grid(row=5, column=1)


    blank_space = Label(book_upload, text="", bg='grey')
    blank_space.grid(row=6, column=0)


    isbm_number = Label(book_upload, text="Enter The Book ISBM: ", bg='grey', font=('arial',10))
    isbm_number.grid(row=7, column=0)

    write_isbm_number = Entry(book_upload)
    write_isbm_number.grid(row=7, column=1)


    blank_space = Label(book_upload, text="", bg='grey')
    blank_space.grid(row=8, column=0)

    submit = Button(book_upload, command=post_book, text="Submit")
    submit.grid(row=9, column=1)

    logout_frame = Frame(admin_dashboard)
    logout_frame.pack(side=BOTTOM, anchor=SW)

    logout_button = Button(logout_frame, command=logout, text="Logout", bg='black', fg='white', font=("Proxima Nova", 10, 'bold'), height=1)
    logout_button.grid(row=0, column=0)




root=Tk()
root.geometry('850x400')
root.minsize(400, 650)
root.title('Library Management System')
root.config(background='grey')
root.iconbitmap('library.ico')

header = Label(root, text="Library Management System by Mohit Kumhar", bg='black', fg='white', font=("Proxima Nova", 25, 'bold'), height=1)
header.pack(side=TOP, fill=X)



blank_space = Label(root, text="", bg='grey')
blank_space.pack()
blank_space = Label(root, text="", bg='grey')
blank_space.pack()
blank_space = Label(root, text="", bg='grey')
blank_space.pack()


# Search The Books By Book Number 

search_book_student = Frame(root, bg='grey')
search_book_student.pack()

title1 = Label(search_book_student, text="Search for a Book Name → ", bg='grey', font=('arial',17))
title1.grid(row=0, column=0)

search1 = Entry(search_book_student, width=30, font=20)
search1.grid(row=0, column=1)


search_button = Button(search_book_student, command=search_book, text='Search', height=1, width=10, fg='black', bg='white', activebackground='black', activeforeground='white', highlightcolor='red', relief=RIDGE, underline=True, background='#A9A9A9', font=('arial', 10, 'bold'))
search_button.grid(row=0, column=3, padx=30)


blank_space = Label(search_book_student, text="", bg='grey')
blank_space.grid(row=1, column=0)


# Search Books By Author Name

title1 = Label(search_book_student, text="Search Books By Author Name → ", bg='grey', font=('arial',17))
title1.grid(row=3, column=0)

author1 = Entry(search_book_student, width=30, font=20)
author1.grid(row=3, column=1)


search_button = Button(search_book_student, command=search_book_by_author_name, text='Search', height=1, width=10, fg='black', bg='white', activebackground='black', activeforeground='white', highlightcolor='red', relief=RIDGE, underline=True, background='#A9A9A9', font=('arial', 10, 'bold'))
search_button.grid(row=3, column=3)


blank_space = Label(search_book_student, text="", bg='grey')
blank_space.grid(row=4, column=0)


# Search Book By Publish Year

title1 = Label(search_book_student, text="Search Book By Publish Year → ", bg='grey', font=('arial',17))
title1.grid(row=5, column=0)

publish_year1 = Entry(search_book_student, width=30, font=20)
publish_year1.grid(row=5, column=1)


search_button = Button(search_book_student, command=search_book_by_publish_year, text='Search', height=1, width=10, fg='black', bg='white', activebackground='black', activeforeground='white', highlightcolor='red', relief=RIDGE, underline=True, background='#A9A9A9', font=('arial', 10, 'bold'))
search_button.grid(row=5, column=3)
admin_login_button = Button(root, command=login, text='Login', height=1, width=10, fg='black', bg='white', activebackground='black', activeforeground='white', highlightcolor='red', relief=RIDGE, underline=True, background='#A9A9A9', font=('arial', 10, 'bold'))
admin_login_button.pack(anchor=SW, side=BOTTOM, padx=200)


login_frame = Frame(root, bg='grey')
login_frame.pack(anchor=SW, side=BOTTOM)



admin_login = Label(root, text="Admin can Login from Here: ",bg='grey', font=(40))
admin_login.pack(anchor=SW, side=BOTTOM)


enter_username = Label(login_frame, text="Enter Username: ",bg='grey', font=(40))
enter_username.grid(row=1, column=0, padx=20)


admin_username = Entry(login_frame, textvariable='Enter Username: ')
admin_username.grid(row=1, column=1, padx=20)


enter_password = Label(login_frame, text="Enter PassWord: ", bg='grey', font=(40))
enter_password.grid(row=2, column=0)


admin_password = Entry(login_frame, textvariable='Enter Password: ', show="*")
admin_password.grid(row=2, column=1)


blank_space = Label(login_frame, text="", bg='grey')
blank_space.grid(row=3, column=0)


root.mainloop()