from app.db.connection import SessionLocal
from app.db.repositories.inventory_repository import InventoryRepository
from app.services.conversation_context_resolver import (
    ConversationContextResolver
)

context_resolver = ConversationContextResolver()


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

            medication_name = context_resolver.resolve_medication(
                message=message,
                history=history
            )

            print(
                f"MEDICAMENTO RESUELTO: {medication_name}"
            )

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