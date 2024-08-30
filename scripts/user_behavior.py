from locust import HttpUser, task, TaskSet, constant_pacing

class UserBehavior(TaskSet):
    """
    поведение пользователя при НТ

    методы:
        perform_login: вход пользователя
        perform_add_booking: добавляение бронирования
        perform_checkout: завершаение оформление заказа
    """

    @task(1)
    def perform_login(self) -> None:
        """
        вход пользователя
        """
        self.client.get("/login/testuser")

    @task(5)
    def perform_add_booking(self) -> None:
        """
        запрос на добавление бронирования
        """
        self.client.post("/booking/add", json={"service_name": "massage"})

    @task(4)
    def perform_checkout(self) -> None:
        """
       запрос на завершение заказа
        """
        self.client.post("/checkout", json={"order_id": 1234})

class PerfomanceUser(HttpUser):
    """
    пользователь для выполнения НТ

    атрибуты:
        tasks (list): список задач, которые пользователь выполняет
        wait_time (constant_pacing): время ожидания между выполнением задач
        host (str): URL-адрес хоста для тестирования
    """
    tasks = [UserBehavior]
    wait_time = constant_pacing(5)
    host = "http://localhost:8000"
