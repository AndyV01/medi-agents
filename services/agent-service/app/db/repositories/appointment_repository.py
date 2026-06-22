from sqlalchemy.orm import Session

from app.db.models.appointment import Appointment


class AppointmentRepository:

    def create(
        self,
        db: Session,
        patient_id: int,
        date: str
    ) -> Appointment:

        appointment = Appointment(
            patient_id=patient_id,
            date=date
        )

        db.add(appointment)
        db.commit()
        db.refresh(appointment)

        return appointment

    def get_by_patient(
        self,
        db: Session,
        patient_id: int
    ) -> Appointment | None:

        return (
            db.query(Appointment)
            .filter(
                Appointment.patient_id == patient_id,
                Appointment.status == "scheduled"
            )
            .order_by(
                Appointment.date.asc()
            )
            .first()
        )
    
    def get_next_by_patient(
        self,
        db: Session,
        patient_id: int
    ) -> Appointment | None:

        return (
            db.query(Appointment)
            .filter(
                Appointment.patient_id == patient_id,
                Appointment.status == "scheduled"
            )
            .order_by(
                Appointment.date.asc()
            )
            .first()
    )