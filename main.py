import smtplib
import random
import tkinter as tk
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageTk  # image handling
import re  # regular expressions

# Generate a random 6-digit OTP
otp = str(random.randint(100000, 999999))

# Email configuration
sender_email = '<Your Gmail Address>'  # Your Gmail email address
sender_password = '<Your Gmail password>'  # Your Gmail password
smtp_server = 'smtp.gmail.com'  # SMTP server for Gmail
smtp_port = 587  # SMTP port for Gmail

# Email template
email_template = """
<!DOCTYPE html>
<html>
<body>
    <div style="text-align: center;">
        <h1>OTP Verification</h1>
        <p>Your OTP code is: {otp}</p>
    </div>
</body>
</html>
"""

# Function to verify the validity of an email address using regular expressions
def is_valid_email(email):
    # Define a regular expression pattern for a valid email address
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Function to send OTP via email with template
def send_otp():
    user_email = email_entry.get()
    
    # Check the validity of the email address using regex
    if not is_valid_email(user_email):
        messagebox.showerror('Invalid Email', 'Please enter a valid email address.')
        return

    try:
        # Create an SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Create a MIME object
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = user_email
        message["Subject"] = 'OTP Verification'

        # Insert OTP into the email template
        email_body = email_template.format(otp=otp)

        # Attach the HTML email body
        message.attach(MIMEText(email_body, "html"))

        # Send the email
        server.sendmail(sender_email, user_email, message.as_string())

        # Move to the next step in the wizard
        goto_step(2)

    except Exception as e:
        messagebox.showerror('Error', f'Error sending OTP: {str(e)}')

# Function to verify OTP
def verify_otp():
    user_input_otp = otp_entry.get()
    if user_input_otp == otp:
        messagebox.showinfo('OTP Verified', 'OTP verification successful. You can proceed with registration/payment.')
        window.quit()

    else:
        messagebox.showerror('OTP Verification Failed', 'OTP verification failed. Please double-check the OTP and try again.')

# Function to toggle Dark/Light mode
dark_mode = False

# Function to toggle Dark/Light mode
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        # Apply dark mode styles
        window.configure(bg='black')
        frame.configure(bg='black')
        email_label.config(bg='black', fg='white')
        otp_label.config(bg='black', fg='white')
        send_otp_button.config(bg='#333', fg='white')
        verify_otp_button.config(bg='#333', fg='white')
        toggle_button.config(image=sun_icon, bg="white")  # Set the dark mode icon
    else:
        # Apply light mode styles
        window.configure(bg='#f0f0f0')
        frame.configure(bg='#f0f0f0')
        email_label.config(bg='#f0f0f0', fg='black')
        otp_label.config(bg='#f0f0f0', fg='black')
        send_otp_button.config(bg='#008CBA', fg='white')
        verify_otp_button.config(bg='#008CBA', fg='white')
        toggle_button.config(image=moon_icon, bg="#333")  # Set the light mode icon

# Function to navigate to a specific step in the wizard
def goto_step(step):
    frame.grid_forget()
    if step == 1:
        frame.grid(row=1, column=0)
        email_label.grid(row=0, column=0, pady=10)
        email_entry.grid(row=0, column=1, pady=5)
        send_otp_button.grid(row=1, column=0, columnspan=2, pady=10)
        toggle_button.grid(row=2, column=0, columnspan=2, pady=10)
    elif step == 2:
        frame.grid(row=1, column=0)
        otp_label.grid(row=0, column=0, pady=10)
        otp_entry.grid(row=0, column=1, pady=5)
        verify_otp_button.grid(row=1, column=0, columnspan=2, pady=10)
        toggle_button.grid(row=2, column=0, columnspan=2, pady=10)
        back_button.grid(row=3, column=0, columnspan=2, pady=10)



# Create a Tkinter window
# Create a Tkinter window
window = tk.Tk()
window.title('User Onboarding Wizard')

# Create icons for dark mode and light mode
sun_icon = Image.open("sun.png")  
moon_icon = Image.open("moon.png")  

sun_icon = ImageTk.PhotoImage(sun_icon)
moon_icon = ImageTk.PhotoImage(moon_icon)


# Initial step in the wizard
current_step = 1

def go_back_to_email_input():
    goto_step(1)

# Create a frame to hold the wizard content
frame = tk.Frame(window)
frame.grid(row=1, column=0)

# Create and pack email label and entry field for the first step
email_label = tk.Label(frame, text='Enter your email address:', bg='#f0f0f0', fg='black', font=('Arial', 12))
email_label.grid(row=0, column=0, pady=10)
email_entry = tk.Entry(frame, font=('Arial', 12))
email_entry.grid(row=0, column=1, pady=5)

# Create and pack send OTP button
send_otp_button = tk.Button(frame, text='Send OTP', command=send_otp, bg='#008CBA', fg='white', font=('Arial', 12))
send_otp_button.grid(row=1, column=0, columnspan=2, pady=10)
toggle_button = tk.Button(frame, image=sun_icon, command=toggle_dark_mode, bg='#333')
toggle_button.image = sun_icon  # Keep a reference to the image to avoid garbage collection
toggle_button.image_reference = sun_icon  # Keep a reference to the button itself to avoid garbage collection


# Create and pack OTP label and entry field for the second step
otp_label = tk.Label(frame, text='Enter the OTP sent to your email:', bg='#f0f0f0', fg='black', font=('Arial', 12))
otp_entry = tk.Entry(frame, font=('Arial', 12))
verify_otp_button = tk.Button(frame, text='Verify OTP', command=verify_otp, bg='#008CBA', fg='white', font=('Arial', 12))


# Create and pack the "Back" button in step 2
back_button = tk.Button(frame, text='Back', command=go_back_to_email_input, bg='#008CBA', fg='white', font=('Arial', 12))


# Start at the initial step
goto_step(current_step)

# Start the Tkinter main loop
window.mainloop()

