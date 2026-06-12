from app.db.connection import SessionLocal
from app.db.models.medication import Medication


def seed():

    db = SessionLocal()

    medications = [
        Medication(
            name="Ibuprofeno",
            stock=120,
            price=250
        ),
        Medication(
            name="Paracetamol",
            stock=80,
            price=180
        ),
        Medication(
            name="Amoxicilina",
            stock=45,
            price=520
        )
    ]

    for medication in medications:

        exists = (
            db.query(Medication)
            .filter(
                Medication.name == medication.name
            )
            .first()
        )

        if not exists:
            db.add(medication)

    db.commit()
    db.close()


if __name__ == "__main__":
    seed()