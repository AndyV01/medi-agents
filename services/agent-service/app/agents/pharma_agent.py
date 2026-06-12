class PharmaAgent:
    """
    Agente encargado de responder consultas farmacológicas.
    """

    def execute(self, message: str) -> str:

        return (
            "No se encontraron interacciones "
            "relevantes para la consulta."
        )