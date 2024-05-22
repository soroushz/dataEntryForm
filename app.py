import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook
import os
import datetime

# Step 10: Initialize the workbook if it does not exist
if not os.path.exists('data.xlsx'):
    wb = Workbook()
    ws = wb.active
    ws.append(["First Name", "Last Name", "Age", "Comment", "Gender"])
    wb.save('data.xlsx')

# Step 9: Function to submit the form data
def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = selected_date_label.cget("text")
    comment = text_comment.get("1.0", tk.END).strip()
    gender = gender_var.get()

    if not first_name or not last_name or not age or not comment or not gender:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    # Write data to an Excel sheet
    workbook = openpyxl.load_workbook('data.xlsx')
    sheet = workbook.active
    sheet.append([first_name, last_name, age, comment, gender])
    workbook.save('data.xlsx')

    messagebox.showinfo("Success", "Data submitted successfully!")
    clear_form()

# Step 11: Function to clear the form
def clear_form():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    cal.selection_clear()
    cal.set_date(today)
    text_comment.delete("1.0", tk.END)
    gender_var.set("")
    selected_date_label.config(text="")

# Step 12: Function to exit the application
def exit_app():
    root.destroy()

# Function to toggle calendar visibility
def toggle_calendar():
    if cal.winfo_ismapped():
        cal.grid_remove()
    else:
        cal.grid()

# Step 3: Function to load and resize logo images
def load_logo(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Step 1: Initialize the main window and the Frame
root = ThemedTk(theme="arc")
root.title("Data Entry Application")
root.geometry("600x700")
root.resizable(True, True)

# Center frame in the main window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create the Frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")


# Configure grid layout to be responsive
for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)


# Step 2: Define styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))
style.configure("TText", font=("Helvetica", 10))

# Step 3: Load and resize logos
logo_size = (30, 30)
logo_first_name = load_logo("images/name.png", logo_size)
logo_last_name = load_logo("images/name_family.png", logo_size)
logo_age = load_logo("images/date.png", logo_size)
logo_comment = load_logo("images/comment.png", logo_size)
logo_gender = load_logo("images/gender-equality.png", logo_size)

# Step 4: Creating widgets

# First name
lbl_first_name = ttk.Label(frame, text="First Name:")
lbl_first_name.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)

entry_first_name = ttk.Entry(frame)
entry_first_name.grid(row=0, column=1, sticky="ew", pady=5)

logo_lbl_first_name = ttk.Label(frame, image=logo_first_name)
logo_lbl_first_name.grid(row=0, column=2, padx=(10, 0), pady=5)

# Last name
lbl_last_name = ttk.Label(frame, text="Last Name:")
lbl_last_name.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)

entry_last_name = ttk.Entry(frame)
entry_last_name.grid(row=1, column=1, sticky="ew", pady=5)

logo_lbl_last_name = ttk.Label(frame, image=logo_last_name)
logo_lbl_last_name.grid(row=1, column=2, padx=(10, 0), pady=5)

# Age
lbl_age = ttk.Label(frame, text="Age:")
lbl_age.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)

# Step 5: Creating calender

selected_date_label = ttk.Label(frame, text="")
selected_date_label.grid(row=3, column=1, sticky="ew", pady=5)

# Today's date
today = datetime.date.today()

cal = Calendar(frame, selectmode='day', year=today.year, month=today.month, day=today.day)
cal.grid(row=3, column=1, sticky="ew", pady=5)
cal.grid_remove()  # Hide the calendar initially

def on_date_selected(event):
    selected_date = cal.get_date()
    selected_date_label.config(text=selected_date)
    cal.grid_remove()

cal.bind("<<CalendarSelected>>", on_date_selected)

logo_lbl_age = ttk.Label(frame, image=logo_age)
logo_lbl_age.grid(row=2, column=2, padx=(10, 0), pady=5)

# Toggle calendar button
btn_toggle_cal = ttk.Button(frame, text="Calendar", command=toggle_calendar)
btn_toggle_cal.grid(row=2, column=1, sticky="ew", pady=5)

# Step 6: Create a comment box
# Comment
lbl_comment = ttk.Label(frame, text="Comment:")
lbl_comment.grid(row=4, column=0, sticky="nw", padx=(0, 10), pady=5)

text_comment = tk.Text(frame, height=4, width=20)
text_comment.grid(row=4, column=1, sticky="ew", pady=5)

logo_lbl_comment = ttk.Label(frame, image=logo_comment)
logo_lbl_comment.grid(row=4, column=2, padx=(10, 0), pady=5)

# Step 7: Create radiobutton
# Gender
lbl_gender = ttk.Label(frame, text="Gender:")
lbl_gender.grid(row=5, column=0, sticky="w", padx=(0, 10), pady=5)

gender_var = tk.StringVar()
gender_frame = ttk.Frame(frame)
gender_frame.grid(row=5, column=1, sticky="w", pady=5)

gender_male = ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
gender_female = ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
gender_other = ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other")

gender_male.grid(row=0, column=0, padx=5)
gender_female.grid(row=0, column=1, padx=5)
gender_other.grid(row=0, column=2, padx=5)

logo_lbl_gender = ttk.Label(frame, image=logo_gender)
logo_lbl_gender.grid(row=5, column=2, padx=(10, 0), pady=5)

# Step 8: Create buttons
# Buttons
btn_submit = ttk.Button(frame, text="Submit", command=submit_form)
btn_clear = ttk.Button(frame, text="Clear", command=clear_form)
btn_exit = ttk.Button(frame, text="Exit", command=exit_app)

btn_submit.grid(row=6, column=0, padx=5, pady=10, sticky="ew")
btn_clear.grid(row=6, column=1, padx=5, pady=10, sticky="ew")
btn_exit.grid(row=6, column=2, padx=5, pady=10, sticky="ew")

# Run the application
root.mainloop()
