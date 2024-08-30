from locust import LoadTestShape
import time

class StagesShape(LoadTestShape):
    """
    настройка этапов нагрузки в Locust

    атрибуты:
        stages (list): список этапов нагрузки с параметрами.
    """
    
    def_counter: int = int(time.time())

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 1},
        {"duration": 120, "users": 20, "spawn_rate": 2},
        {"duration": 180, "users": 40, "spawn_rate": 5},
        {"duration": 240, "users": 70, "spawn_rate": 10},
        {"duration": 300, "users": 100, "spawn_rate": 10}
    ]

    def tick(self):
        """
        метод определения текущего этапа нагрузки в зависимости от прошедшего времени.

        Returns:
            tuple: Возвращает количество пользователей и скорость их запуска.
        """
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
