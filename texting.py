import classes
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

current_patient = ""

def send_message(patient):
    global current_patient
    current_patient = patient
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}. This is a message to confirm that you are enrolled by {} to recieve reminders to take {}.").format((patient.firstname +" "+ patient.lastname).upper(),classes.prescribed[patient.firstname + " " + patient.lastname], patient.drug.name.upper()))

def send(patient):
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}. This is a message to remind you to take {}. Please reply if you 'YES' if you have taken the drug. Included doctor message: {}").format((patient.firstname + " " +patient.lastname).upper(), patient.drug.name.upper(), patient.drug.message))

def second(patient):
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}. This is a second message to remind you to take {}. Please reply if you 'YES' if you have taken the drug or 'MISS' 10 minutes have passed since your first text reminder.").format((patient.firstname +" "+ patient.lastname).upper(), patient.drug.name.upper()))

def rate(patient):
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}.Can you please rate the effectiveness of {}, 1-3, where 3 is extremely effective and 1 is not working at all! ").format((patient.firstname + " " +patient.lastname).upper(), patient.drug.name.upper()))

if __name__ == "__main__":
    pass