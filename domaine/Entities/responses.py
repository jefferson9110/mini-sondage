class Response:
    def __init__(self, user_id: int, survey_id: int, content: str, response_id: int = 0, created_at=None):
        self.id = response_id
        self.user_id = user_id
        self.survey_id = survey_id
        self.content = content  # 'OUI' ou 'NON'
        self.created_at = created_at