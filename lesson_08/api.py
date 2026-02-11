import requests


class YougileApi:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        """
        Создание проекта
        POST /api-v2/projects
        """
        data = {"title": title}
        response = requests.post(
            f"{self.base_url}/api-v2/projects",
            json=data,
            headers=self.headers
        )
        return response.json(), response.status_code

    def update_project(self, project_id, title):
        """
        Изменение проекта
        PUT /api-v2/projects/{id}
        """
        data = {"title": title}
        response = requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response.json(), response.status_code

    def get_project(self, project_id):
        """
        Получение проекта по ID
        GET /api-v2/projects/{id}
        """
        response = requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
        return response.json(), response.status_code
