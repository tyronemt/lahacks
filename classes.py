
global patients, doctors, prescribed
patients = []
doctors = []
prescribed = {}
ID_COUNT = 0

drugs_txt = open("drugs.txt",'r')
drugs = [(line.lower()).rstrip("\n") for line in drugs_txt.readlines()]

class Doctor:
    def __init__(self, name, username, password, phone):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone

class Patient:
    def __init__(self, name, birthday, phone):
        name_split = name.split(" ")
        self.firstname = name_split[0].lower()
        self.lastname = name_split[1].lower()
        self.birthday = birthday
        self.phone = phone
        self.ID = ID_COUNT
        self.taken = False
        self.drug = Drug('None', 'None',0)
        self.doctor = "NONE"

    def assign_drug(self, drug):
        self.drug = drug
        
    def assign_doctor(self, doctor):
        self.doctor = doctor

class Drug:
    def __init__(self, name, message, usage):
        self.name = name
        if len(message) > 0:
            self.message = message
        else:
            self.message = "NONE"
        self.counter = 0
        self.usage = usage
        self.strict_dosage = False
    
    def change_strict(self):
        self.strict_dosage = True

def add(patient_name, patient_birthday, patient_phone):
    global ID_COUNT
    new_patient = Patient(patient_name, patient_birthday, patient_phone)
    patients.append(new_patient)
    ID_COUNT += 1
    

def patient_exist(name, birthday):
    current_patient = "NA"
    patient_name_split = name.split(" ")
    for i in patients:
        if (i.firstname == patient_name_split[0].lower() and i.lastname == patient_name_split[1].lower() and i.birthday == birthday):
            return i
    if current_patient == "NA":
        return False

def prescribe(current_doctor, patient, drug, message, dosage):
    not_exist = True
    current_drug = "NA"
    while (not_exist):
        for i in drugs:
            if (i == drug.lower()):
                not_exist = False
                current_drug = i
        if (not_exist):
            return False
    usage = dosage

    drug_object = Drug(current_drug,message,usage)

    patient.assign_drug(drug_object)
    if type(current_doctor) == Doctor:
        prescribed[patient.firstname + " " + patient.lastname] = current_doctor.name
        patient.assign_doctor(current_doctor.name)
    else:
        prescribed[patient.firstname + " " + patient.lastname] = "SELF"
    return True

def doctor_login(username,password):
    for i in doctors:
        if i.username == username and i.password == password:
            return i
    return False


if __name__ == '__main__':
    pass


