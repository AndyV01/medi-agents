from app.db.connection import SessionLocal
from app.db.repositories.inventory_repository import InventoryRepository


class StockAgent:
    """
    Agente encargado de consultar stock y precios.
    """

    def execute(self, message: str) -> str:

        db = SessionLocal()

        try:

            medication_name = (
                message.lower()
                .replace("precio del", "")
                .replace("precio de", "")
                .replace("tienen", "")
                .replace("¿", "")
                .replace("?", "")
                .strip()
            )

            print(
                f"MEDICAMENTO BUSCADO: {medication_name}"
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