from sqlalchemy.orm import Session

from app.db.models.medication import Medication


class InventoryRepository:

    def get_by_name(
        self,
        db: Session,
        medication_name: str
    ):

        return (
            db.query(Medication)
            .filter(
                Medication.name.ilike(f"%{medication_name}%")
            )
            .first()
        )