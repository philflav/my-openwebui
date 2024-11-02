from datetime import datetime
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        pass

    class UserValves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()

    def get_current_date(self) -> str:
        """
        Get the current date.
        :return: The current date as a string.
        """
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {current_date}"