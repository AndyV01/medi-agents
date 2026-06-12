from sqlalchemy.orm import Session

from app.db.models.patient import Patient


class PatientRepository:
    """
    Repositorio para operaciones sobre pacientes.
    """

    def create(
        self,
        db: Session,
        name: str,
        phone: str
    ) -> Patient:

        patient = Patient(
            name=name,
            phone=phone
        )

        db.add(patient)
        db.commit()
        db.refresh(patient)

        return patient

    def get_by_id(
        self,
        db: Session,
        patient_id: int
    ) -> Patient | None:

        return (
            db.query(Patient)
            .filter(
                Patient.id == patient_id
            )
            .first()
        )

    def get_by_phone(
        self,
        db: Session,
        phone: str
    ) -> Patient | None:

        return (
            db.query(Patient)
            .filter(
                Patient.phone == phone
            )
            .first()
        )