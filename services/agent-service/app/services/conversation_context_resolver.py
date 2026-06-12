from app.tools.medication_extractor import MedicationExtractor


class ConversationContextResolver:

    def __init__(self):
        self.extractor = MedicationExtractor()

    def resolve_medication(
        self,
        message: str,
        history: list | None = None
    ) -> str | None:

        medication = self.extractor.extract(
            message
        )

        if medication:
            return medication

        if not history:
            return None

        for turn in reversed(history):

            medication = self.extractor.extract(
                turn["message"]
            )

            if medication:
                return medication

        return None