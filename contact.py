# from flask import Flask, request, render_template

# # ...

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         # ... (previous form validation code)

#         if not errors:
#             # Form inputs are valid, you can process the form data (e.g., send an email or store it in a database)
            
#             # Construct the email message
#             subject = "New Contact Form Submission"
#             message = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

#             msg = MIMEMultipart()
#             msg['From'] = SENDER_EMAIL
#             msg['To'] = RECIPIENT_EMAIL
#             msg['Subject'] = subject
#             msg.attach(MIMEText(message, 'plain'))

#             # Connect to the SMTP server and send the email
#             try:
#                 with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#                     server.starttls()
#                     server.login(SMTP_USERNAME, SMTP_PASSWORD)
#                     server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

#                 return "Thank you for your submission! An email notification has been sent."
#             except Exception as e:
#                 return f"Error sending email: {str(e)}"
                
#     return render_template('contact.html', errors=errors)

# # ...
