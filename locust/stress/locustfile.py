from locust import HttpUser, between, task
import random

class WebsiteUser(HttpUser):
    wait_time = between(5, 10)   

    @task
    def get_all(self):
        self.client.get("/api/")
        
    @task
    def get(self):
        npm = str(random.randint(1,9))
        self.client.get("/api/"+npm+"/")
