from app.core.llm import llm
from app.prompts.triage import TRIAGE_PROMPT

class TriageAgent:
 """
 Agente responsable de clasificar la intención del paciente.
 """

 def classify(self, message: str) -> str:
    """
    Clasifica la intención del mensaje del paciente.
    """

    prompt = TRIAGE_PROMPT.format(
        message=message
    )

    response = llm.invoke(prompt)

    intent = response.content.strip().lower()

    intent = (
        intent
        .replace("la respuesta es:", "")
        .replace(".", "")
        .strip()
    )
    return intent