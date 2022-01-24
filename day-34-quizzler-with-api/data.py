import requests

CATEGORY_DICT = {
    "computer": 18
}
API_URL = f"https://opentdb.com/api.php"


class Data():
    def __init__(self, number_of_question=10, category="computer", difficulty="easy"):
        self.parameters = {
            "amount": number_of_question,
            "category": CATEGORY_DICT[category],
            "difficulty": difficulty,
            "type": "boolean"
        }
        self.url = f"https://opentdb.com/api.php"
        self.question_data = self.get_question_data()

    def get_question_data(self):
        response = requests.get(url=API_URL, params=self.parameters)
        response.raise_for_status()
        return response.json()["results"]
