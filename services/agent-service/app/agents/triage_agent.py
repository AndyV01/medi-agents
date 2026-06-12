from app.core.llm import llm
from app.prompts.triage import TRIAGE_PROMPT


class TriageAgent:

    def classify(self, message: str) -> str:

        text = message.lower()

        # Reglas rápidas

        stock_keywords = [
            "precio",
            "cuesta",
            "valor",
            "stock",
            "disponible",
            "tienen",
            "venden",
            "comprar"
        ]

        if any(word in text for word in stock_keywords):
            return "stock"

        prompt = TRIAGE_PROMPT.format(
            message=message
        )

        response = llm.invoke(prompt)

        intent = response.content.strip().lower()

        print(f"RESPUESTA LLM: {intent}")

        if "stock" in intent:
            return "stock"

        if "pharma" in intent:
            return "pharma"

        if "appointment" in intent:
            return "appointment"

        return "handoff"