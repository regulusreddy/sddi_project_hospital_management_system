from mongoengine import *

class Stakeholders(Document):
    meta = {'allow_inheritance': True}
    username = StringField(required=True, primary_key=True)
    email = EmailField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    gender = StringField(required=True)
    dob = StringField(required=True)
    phone_number = StringField(required=True)
    address = StringField(required=True)
    zipcode = StringField(required=True)
    state = StringField(required=True)

class Appointments(EmbeddedDocument):
    meta = {'allow_inheritance': True}
    date = StringField()
    time = StringField()

class Other_Charges(EmbeddedDocument):
    charge_Description = StringField(required=True)
    charge_Value = FloatField(required=True)
    doctor=BooleanField(default=False)

class Bill(Document):
    patient_Id = StringField(required=True,primary_key=True)
    doctor_Id = StringField(required=True)
    doctor_Fees = FloatField(required=True)
    Extra_Charges=ListField(EmbeddedDocumentField(Other_Charges))
    dateOfDischarge=StringField(default="")
    dateOfAdmission=StringField(required=True)
    paid=BooleanField(default=False)

class Bills(EmbeddedDocument):
    patient_Id = StringField(required=True,primary_key=True)
    doctor_Id = StringField(required=True)
    doctor_Fees = FloatField(required=True)
    Extra_Charges=ListField(EmbeddedDocumentField(Other_Charges))
    dateOfDischarge=StringField(default="")
    dateOfAdmission=StringField(required=True)
    total=FloatField()

class prev_rec(Document):
    patient_Id = StringField(required=True, primary_key=True)
    records=ListField(EmbeddedDocumentField(Bills))

class PatientPaymentHistory(EmbeddedDocument):
    date = StringField()
    state = StringField()
    cause = StringField()
    payment_due = FloatField(default=0.0)
    payment_amount_insurance = FloatField()
    payment_amount_patient = FloatField()

class PatientAppointments(Appointments):
    state = StringField()
    under_doctor = StringField()
    doctor_username = StringField()

class Patient(Stakeholders):
    insured = BooleanField(required=True)
    currently_admitted = BooleanField(default=False)
    payment_records = ListField(EmbeddedDocumentField(PatientPaymentHistory))
    patient_appointments = ListField(EmbeddedDocumentField(PatientAppointments))
    doctor_name = StringField(default=None)
    records = ListField(EmbeddedDocumentField(Bills),default=None)

class TypeOfUser(Document):
    username = StringField(required=True)
    user_status = StringField(required=True)

class Timings(EmbeddedDocument):
    day = StringField()
    time = StringField()

class DoctorAppointments(Appointments):
    patient = StringField()
    patient_username = StringField()

class TransferRequests(EmbeddedDocument):
    patient_id = StringField(required=True)
    patient_name = StringField()
    location = StringField()
    description = StringField()
    consent = BooleanField(default=False)

class Doctor(Stakeholders):
    speciality = StringField(required=True, max_length=25)
    status = BooleanField(required=True)
    consulting_fees = FloatField(default=50.0)
    office_hours = ListField(EmbeddedDocumentField(Timings))
    doctor_appointments = ListField(EmbeddedDocumentField(DoctorAppointments))
    patients_admitted = ListField(StringField())
    patients_discharged = ListField(StringField())
    transfer_request = ListField(EmbeddedDocumentField(TransferRequests))

class Receptionist(Stakeholders):
    salary = FloatField(default=3500.0)

class Beds(Document):
    room_type = StringField(required=True)
    location = StringField(required=True, default="NC")
    room_number = IntField(default=8)
    bed_number = IntField(default=8)
    patient_name = StringField(default=None)


class Test(Document):
    id = IntField(primary_key=True)
    email = EmailField()