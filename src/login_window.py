from tkinter import *

"""
    Центрирует окно tkinter
"""
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def register():
 
    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window. 
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable
    
    register_screen = Toplevel() 
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    # Set text variables
    username = StringVar()
    password = StringVar()
 
    # Set label for user's instruction
    Label(register_screen, text="Введите данные для регистрации", bg="blue", font=("Calibri", 15)).pack()
    Label(register_screen, text="").pack()
    
    # Set username label
    username_lable = Label(register_screen, font=("Calibri", 15), text="Имя")
    username_lable.pack()
 
    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(register_screen, textvariable=username, font=("Calibri", 15))
    username_entry.pack()
   
    # Set password label
    password_lable = Label(register_screen, font=("Calibri", 15), text="Фамилия")
    password_lable.pack()
    
    # Set password entry
    password_entry = Entry(register_screen, font=("Calibri", 15))
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    
    # Set register button
    Button(register_screen, text="Регистрация", font=("Calibri", 15), width=10, height=1, bg="blue").pack()

    center(register_screen)

"""
    Создает и отображает окно входа в систему
"""
def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Вход в систему") # set the title of GUI window
 
    # create a Form label 
    Label(text="Вход в систему", width="300", height="2", font=("Calibri", 24)).pack() 
    Label(text="").pack() 
    
    # create Login Button 
    Button(text="Вход", height="2", font=("Calibri", 15), width="30").pack() 
    Label(text="").pack() 

    # create a register button
    Button(text="Регистрация", height="2", font=("Calibri", 15), width="30", command=register).pack()

    center(main_screen)

    # add command=register in button widget
    
    main_screen.mainloop() # start the GUI
    
main_account_screen() # call the main_account_screen() function