from app.db.connection import SessionLocal
from app.db.repositories.inventory_repository import InventoryRepository
from app.tools.medication_extractor import MedicationExtractor


class StockAgent:
    """
    Agente encargado de consultar stock y precios.
    """

    def execute(
        self,
        message: str,
        history: list | None = None
    ) -> str:

        db = SessionLocal()

        try:

            extractor = MedicationExtractor()

            medication_name = extractor.extract(
                message
            )

            print(
                f"MEDICAMENTO EXTRAÍDO: {medication_name}"
            )

            # Si no encuentra medicamento en el mensaje actual,
            # intenta recuperarlo desde el historial.
            if not medication_name and history:

                for turn in reversed(history):

                    extracted = extractor.extract(
                        turn["message"]
                    )

                    if extracted:

                        medication_name = extracted

                        print(
                            f"MEDICAMENTO RECUPERADO DEL HISTORIAL: {medication_name}"
                        )

                        break

            if not medication_name:

                return (
                    "No pude identificar un medicamento "
                    "en tu consulta."
                )

            repository = InventoryRepository()

            medication = repository.get_by_name(
                db=db,
                medication_name=medication_name
            )

            if not medication:

                return (
                    "No encontré ese medicamento "
                    "en el inventario."
                )

            return (
                f"{medication.name} disponible. "
                f"Stock: {medication.stock} unidades. "
                f"Precio: ${medication.price}"
            )

        finally:

            db.close()