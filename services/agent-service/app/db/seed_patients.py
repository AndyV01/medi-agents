from app.db.connection import SessionLocal
from app.db.models.patient import Patient


db = SessionLocal()

try:

    patient = Patient(
        name="Andy",
        phone="099123456"
    )

    db.add(patient)
    db.commit()

finally:

    db.close()