from app.db.connection import SessionLocal
from app.db.repositories.patient_repository import PatientRepository
from app.db.repositories.appointment_repository import AppointmentRepository


class AppointmentAgent:

    def execute(
        self,
        patient_id: int,
        message: str
    ) -> str:

        message_lower = message.lower()

        if any(
            keyword in message_lower
            for keyword in [
                "todos",
                "todas",
                "listar",
                "mostrar"
            ]
        ):
            return self._get_all_appointments(
                patient_id
            )

        return self._get_next_appointment(
            patient_id
        )

    def _get_next_appointment(
        self,
        patient_id: int
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
                f"{appointment.date}"
            )

        finally:

            db.close()

    def _get_all_appointments(
        self,
        patient_id: int
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