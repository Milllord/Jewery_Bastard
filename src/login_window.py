from tkinter import *
from turtle import color

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

def main_account_screen():
    
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
    Button(text="Регистрация", height="2", font=("Calibri", 15), width="30").pack()

    center(main_screen)
    
    main_screen.mainloop() # start the GUI
    
main_account_screen() # call the main_account_screen() function