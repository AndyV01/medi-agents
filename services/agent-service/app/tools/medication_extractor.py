from app.core.llm import llm


EXTRACT_MEDICATION_PROMPT = """
Extrae únicamente el nombre del medicamento mencionado.

Reglas:
- Responde solo con el nombre del medicamento.
- No agregues explicaciones.
- No agregues puntuación.
- Si no encuentras un medicamento responde: NONE

Mensaje:
{message}
"""


class MedicationExtractor:
    """
    Extrae el nombre de un medicamento desde un mensaje.
    """

    def extract(self, message: str) -> str | None:

        prompt = EXTRACT_MEDICATION_PROMPT.format(
            message=message
        )

        response = llm.invoke(prompt)

        medication_name = (
            response.content
            .strip()
            .replace(".", "")
        )

        if medication_name.upper() == "NONE":
            return None

        return medication_name