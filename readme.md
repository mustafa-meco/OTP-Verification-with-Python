# OTP Verification Project

This OTP (One-Time Password) Verification project is a simple Python application that enables users to send and verify OTPs via email. It's designed to be a part of an onboarding or authentication process, ensuring that users have a valid email address and can receive and enter an OTP for verification.

## Features

1. **OTP Generation**: The project generates a random 6-digit OTP for each verification process.

2. **Email Verification**: Users are required to enter their email address, which is validated using regular expressions to ensure its validity.

3. **Email Sending**: The application sends the OTP to the provided email address using the Gmail SMTP server. It employs the `smtplib` library for sending emails.

4. **Dark and Light Mode**: The application offers a toggle between dark and light modes to suit user preferences.

5. **User-Friendly Interface**: The graphical user interface is created using the Tkinter library, making it easy to use.

## Prerequisites

Before running the project, ensure that you have the following prerequisites installed:

- Python (3.x recommended)
- The required Python libraries: `smtplib`, `random`, `tkinter`, `Pillow` (PIL), and `re`.

## Getting Started

1. **Generate an OTP**: When the application is launched, it generates a random 6-digit OTP.

2. **Email Configuration**: Configure the sender's email and SMTP server information in the code. This is typically your Gmail email address and app password for Gmail.

3. **Email Template**: You can customize the email template in the code. The OTP is inserted into an HTML email template.

4. **Send OTP**: Users enter their email address and click the "Send OTP" button to receive the OTP via email. The email address is validated before sending the OTP.

5. **OTP Verification**: After receiving the OTP in their email, users enter it in the application and click the "Verify OTP" button. If the OTP matches, a success message is displayed; otherwise, an error message is shown.

6. **Dark/Light Mode**: Users can switch between dark and light modes by clicking the sun/moon icon.

## Usage

1. Run the application by executing the Python script.

2. Enter a valid email address and click "Send OTP."

3. Retrieve the OTP from your email and enter it in the application.

4. Click "Verify OTP" to complete the verification process.

## Customization

You can further customize the project by:

- Modifying the email template to match your application's branding and messaging.
- Adjusting the dark and light mode styles to fit your user interface design.

## Acknowledgments

This project uses various Python libraries, including Tkinter for the user interface, smtplib for email sending, and regular expressions for email validation.

## License

Feel free to modify and use it for your own purposes.

## Author

Mustafa Ghoneim - [LinkedIn](https://www.linkedin.com/in/mustafa-gamal739/)

## Note

This project is designed for educational and demonstration purposes. Please be aware of potential security and privacy concerns when using email verification in production applications. Ensure that sensitive data, such as email credentials, is handled securely.
