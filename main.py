from flask import Flask, url_for, render_template, request, redirect
import classes
import pillSMS as ps
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse




app = Flask(__name__)


@app.route('/')
def base():
    return render_template('home.html')

@app.route('/map')
def map():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('home.html')

@app.route('/request')
def request():
    return render_template('home.html')

@app.route('/donate')
def donate():
    return render_template('home.html')


# @app.route("/sms", methods=['GET', 'POST'])
# def incoming_sms():
#     global t
#     patient = current_patient
#     """Send a dynamic reply to an incoming text message"""
#     # Get the message the user sent our Twilio number
#     body = request.values.get('Body', None)
#     phone = request.values.get('From',None)
#     for p in classes.prescribed.keys():
#         for i in classes.patients:
#             if p.split(" ")[0] == i.firstname and p.split(" ")[1] == i.lastname and phone == i.phone:
#                 patient = i

#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Determine the right reply for this message
#     if body.lower() == 'yes':
#         resp.message("Thank you for telling us! We will notify you when your next dose is.")
#         patient.drug.counter = 0
#         patient.taken = True
#         t = 0
#     elif body.lower() == 'miss':
#         if (type(patient) == classes.Patient and patient.drug.strict_dosage):
#             resp.message("{} has a strict dosage so please try not to miss your next dosage.".format(patient.drug.name.upper()))
#         elif(type(patient) == classes.Patient):
#             resp.message("Because {} does not have a strict dosage please take the missed dosage and try not to miss your next scheduled dosage.".format(patient.drug.name.upper()))
#         else:
#             resp.message("You are not subscribed to any drugs")
#         patient.taken = True
#         patient.drug.counter = 0
#         t = 0
#     elif body.lower() == "3":
#         pass
#     elif body.lower() == "2":
#         pass
#     elif body.lower() == "1":
#         pass
#     else:
#         resp.message("Invalid response")

#     return str(resp)

                

                
                


   
if __name__ == "__main__":
    
    app.run(debug=True)