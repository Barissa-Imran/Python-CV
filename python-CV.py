from docx import Document
from docx.shared import Inches
import pyttsx3 

def speak(text):
    pyttsx3.speak(text)

document = Document()

# profile picture
document.add_picture(
    'MEE 2.png', 
    width=Inches(2.0)
)

# name phone number and email details
speak('what is your name? ')
name = input('what is your name? ')
speak('Hello' + name +'How are you today? ')

speak('what is your phone number? ')
phone_number = input('what is your phone number? ')

speak('please provide an email address')
email = input('what is your email? ')

document.add_paragraph(
    name + ' | '+ phone_number + ' | ' + email
)
# about me
document.add_heading('About me')
speak('Tell me about yourself?')
document.add_paragraph(
    input('Tell me about yourself? ')
)

# work experience
document.add_heading('Work Experience')
p = document.add_paragraph()

speak('This is the work experience section')
speak('Please read the prompts on the screen and answer appropiately')
company = input('Enter Company ')
from_date = input('From date ')
to_date = input('To Date')

p.add_run(company + ' ').bold = True
p.add_run(from_date + '-' + to_date + '\n').italic

experience_details = input(
    'Describe your experience at' + company
)
p.add_run(experience_details)

document.save('cv.docx')
