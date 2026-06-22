from app.db.connection import SessionLocal
from app.db.repositories.patient_repository import PatientRepository
from app.db.repositories.appointment_repository import AppointmentRepository


class AppointmentAgent:

    def execute(
        self,
        patient_id: int,
        message: str
    ) -> str:

        db = SessionLocal()

        try:

            patient_repository = PatientRepository()
            appointment_repository = AppointmentRepository()

            patient = patient_repository.get_by_id(
                db=db,
                patient_id=patient_id
            )

            if not patient:

                return (
                    "No encontré el paciente registrado."
                )

            appointment = (
                appointment_repository.get_next_by_patient(
                    db=db,
                    patient_id=patient_id
                )
            )

            if not appointment:

                return (
                    "No tienes turnos registrados."
                )

            return (
                f"Tu próximo turno es el "
                f"{appointment.date} "
            )

        finally:

            db.close()