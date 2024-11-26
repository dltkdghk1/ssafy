from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    # on_start : 가상 유저 생성 시 자동으로 호출되는 메서드
    def on_start(self):
        print('test start')

    @task
    def normal_sort(self):
        self.client.get("test/normal_sort/")

    @task
    def priority_queue(self):
        self.client.get("test/priority_queue/")

    @task
    def bubble_sort(self):
        self.client.get("test/bubble_sort/")


