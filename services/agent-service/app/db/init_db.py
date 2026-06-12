from app.db.connection import engine, Base

# Importar todos los modelos
from app.db.models.medication import Medication
from app.db.models.patient import Patient
from app.db.models.appointment import Appointment


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()