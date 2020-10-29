"""
iContact

Add contact
Search contact

Author: @HomeOfCoding
"""
from tkinter import *
from tkinter import END
from string import capwords
import re

app = Tk()
# ___________________________
# Page Defaults

A12b = 'arial', 12, 'bold'
A12 = 'arial', 12
A10 = 'arial', 10
BG = '#fff'
FG = '#296296'

# ___________________________
# Functions

def search_data():

    textarea.config(fg=FG, state='normal')
    textarea.delete(1.0, END)

    # Getters
    get_search = capwords(search_input.get())

    filename = 'iContacts'

    with open(filename) as f_read:
        for line in f_read:
            if get_search in line:
                textarea.insert(END, line)
    

    search_entry.delete(0, END)
    search_entry.focus()


def submit_data(*args):

    textarea.delete(1.0, END)
    textarea.config(fg=FG)

    # Getters
    get_first = capwords(first_input.get())
    get_last = capwords(last_input.get())
    get_age = capwords(age_input.get())
    get_area = capwords(area_input.get())
    get_email = capwords(email_input.get())

    if get_first == '':
        textarea.config(fg='red', state='normal')
        textarea.insert(1.0, 'Please enter first name *required')
        first_entry.focus()
        first_entry.config(highlightcolor='red')
    elif get_last == '':
        textarea.config(fg='red', state='normal')
        textarea.insert(1.0, 'Please enter last name *required')
        last_entry.focus()
        last_entry.config(highlightcolor='red')
    elif get_age == '':
        textarea.config(fg='red', state='normal')
        textarea.insert(1.0, 'Please enter age *required')
        age_entry.focus()
        age_entry.config(highlightcolor='red')
    elif get_area == '':
        textarea.config(fg='red', state='normal')
        textarea.insert(1.0, 'Please enter location *required')
        area_entry.focus()
        area_entry.config(highlightcolor='red')
    elif get_email == '':
        textarea.config(fg='red', state='normal')
        textarea.insert(1.0, 'Please enter email *required')
        email_entry.focus()
        email_entry.config(highlightcolor='red')
    else:
        # Validate email input here..
        validate_email = get_email
        pattern = re.compile(r"^[a-zA-Z0-9]+([a-zA-Z0-9]+[\.-]"\
                             "[a-zA-Z0-9]+)?@([a-zA-Z0-9\d-])"\
                             "+\.([a-zA-Z]{2,15})(\.[a-zA-Z]{2,8})?$")
        matches = pattern.search(validate_email)

        # If Email Address is Valid
        if matches:
            textarea.config(fg=FG)
            try:
                # Write to File
                filename = 'iContacts'

                with open(filename, 'a') as f_append:
                    f_append.write('Name: ' + get_first + ' ' + get_last + '\n' + \
                                   get_first + '\'s Age: ' + get_age + '\n' + \
                                   get_first + '\'s Area: ' + get_area + '\n' + \
                                   get_first + '\'s Email: ' + get_email + \
                                   '\n\n---------------------\n\n')
                

                # Show Content on Screen
                textarea.config(fg=FG, state='normal')
                textarea.insert(1.0, 'Data saved successfully!\n\n' + \
                                'Name: ' + get_first + ' ' + get_last + '\n' + \
                                get_first + '\'s Age: ' + get_age + '\n' + \
                                get_first + '\'s Area: ' + get_area + '\n' + \
                                get_first + '\'s Email: ' + get_email)


                search_entry.delete(0, END)
                first_entry.delete(0, END)
                last_entry.delete(0, END)
                age_entry.delete(0, END)
                area_entry.delete(0, END)
                email_entry.delete(0, END)
                first_entry.focus()

            except:
                textarea.insert(1.0, 'Sorry!\nData not saved\nPlease try again')
                
        else:
            textarea.insert(1.0, 'Email is not valid')
            textarea.config(fg='red')
            email_entry.focus()


# ___________________________
# Getters

search_input = StringVar()
first_input = StringVar()
last_input = StringVar()
age_input = StringVar()
area_input = StringVar()
email_input = StringVar()

# ___________________________
# Page

# Main Frame (search)
main_frame = Frame(app, bg=BG)
main_frame.pack(ipady=20)

# Search Label
search_label = Label(main_frame, text='Search ', bg=BG, fg=FG, font=A12)
search_label.pack(side='left')

# Search Entry
search_entry = Entry(main_frame, bg=BG, fg=FG, font=A12, \
                     highlightcolor=FG, textvariable=search_input)
search_entry.pack(side='left', ipady=1)

# Search Button
search_btn = Button(main_frame, text='GO', bg=FG, fg=BG, font=A10, \
                    border=0, relief='flat', command=search_data)
search_btn.pack(side='left')

# ____________________________________________________________________
# Main Frame (separator)
main_frame = Frame(app, bg=FG)
main_frame.pack(fill='x', padx=40, ipady=1)
# ____________________________________________________________________

# ___________________________
# Main Frame (for: add contact label)
main_frame = Frame(app, bg=BG)
main_frame.pack(fill='x', padx=40, ipady=20)

# Add Contact Label
contact_label = Label(main_frame, text='Add Contact', bg=BG, fg=FG, font=A12b)
contact_label.pack(side='left')

# ___________________________
# Main Frame (first name)
main_frame = Frame(app, bg=BG)
main_frame.pack(ipady=2)

# First Name Label
first_label = Label(main_frame, text='First: ', bg=BG, fg=FG, font=A12)
first_label.pack(side='left', padx=(12, 0))

# First Name Entry
first_entry = Entry(main_frame, bg=BG, fg=FG, font=A12, \
                    highlightcolor=FG, textvariable=first_input)
first_entry.focus()
first_entry.pack(side='left', ipady=1)

# ___________________________
# Main Frame (last name)
main_frame = Frame(app, bg=BG)
main_frame.pack(ipady=2)

# Last Name Label
last_label = Label(main_frame, text='Last: ', bg=BG, fg=FG, font=A12)
last_label.pack(side='left', padx=(12, 0))

# Last Name Entry
last_entry = Entry(main_frame, bg=BG, fg=FG, font=A12, \
                    highlightcolor=FG, textvariable=last_input)
last_entry.pack(side='left', ipady=1)

# ___________________________
# Main Frame (age)
main_frame = Frame(app, bg=BG)
main_frame.pack(ipady=2)

# Age Label
age_label = Label(main_frame, text='Age: ', bg=BG, fg=FG, font=A12)
age_label.pack(side='left', padx=(12, 0))

# Age Entry
age_entry = Entry(main_frame, bg=BG, fg=FG, font=A12, \
                    highlightcolor=FG, textvariable=age_input)
age_entry.pack(side='left', padx=(1, 0), ipady=1)

# ___________________________
# Main Frame (area)
main_frame = Frame(app, bg=BG)
main_frame.pack(ipady=2)

# Area Label
age_label = Label(main_frame, text='Area: ', bg=BG, fg=FG, font=A12)
age_label.pack(side='left', padx=(8, 0))

# Area Entry (location)
area_entry = Entry(main_frame, bg=BG, fg=FG, font=A12, \
                    highlightcolor=FG, textvariable=area_input)
area_entry.pack(side='left', padx=(1, 0), ipady=1)

# ___________________________
# Main Frame (email)
main_frame = Frame(app, bg=BG)
main_frame.pack(ipady=2)

# Email Label
email_label = Label(main_frame, text='Email: ', bg=BG, fg=FG, font=A12)
email_label.pack(side='left')

# Email Entry
email_entry = Entry(main_frame, bg=BG, fg=FG, font=A12, \
                    highlightcolor=FG, textvariable=email_input)
email_entry.pack(side='left', padx=(3, 0), ipady=1)

# ___________________________
# Main Frame (textarea)
main_frame = Frame(app, bg=BG)
main_frame.pack(pady=(20, 0))

# Text Widget (textarea)
textarea = Text(main_frame, width=36, height=17, bg=BG, fg=FG, font=A12, \
                border=0, state='disabled')
textarea.pack(padx=(90, 0))

# Main Frame (submit button)
main_frame = Frame(app, bg=BG)
main_frame.pack(side='bottom', fill='x')

# Submit Button
sub_btn = Button(main_frame, text='Submit', bg=FG, fg=BG, font=A12, \
                    border=0, relief='flat', command=submit_data)
app.bind('<Return>', submit_data)
sub_btn.pack(fill='both', ipady=8)

# ___________________________
# Root Defaults

if __name__ == '__main__':

    app.title('iContact')
    app.geometry('550x660+0-32')
    app.resizable(False, False)
    app.config(bg=BG)
