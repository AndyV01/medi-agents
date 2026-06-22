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

            appointments = (
                appointment_repository.get_by_patient(
                    db=db,
                    patient_id=patient_id
                )
            )

            if not appointments:

                return (
                    "No tienes turnos registrados."
                )

            response = "Tus turnos:\n"

            for appointment in appointments:

                response += (
                    f"- {appointment.date} "
                    f"({appointment.status})\n"
                )

            return response

        finally:

            db.close()