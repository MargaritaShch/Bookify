from locust import HttpUser, task, TaskSet, constant_pacing

class UserBehavior(TaskSet):

    @task(1) #вес задачи(вероятность выполнения)
    def perform_login(self):
        self.client.get("/login/testuser")

    @task(5)
    def perform_add_booking(self):
        #запрос к эндпоинту с json-данными
        self.client.post("/booking/add", json={"service_name": "massage"})

    @task(4)
    def perform_checkout(self):
        self.client.post("/checkout", json = {"order_id": 1234})

class PerfomanceUser(HttpUser):
    #поведение пользователя
    tasks = [UserBehavior]
    #пейсинг
    wait_time = constant_pacing(5)
    host = "http://localhost:8000"
