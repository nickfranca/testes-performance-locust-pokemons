from locust import HttpUser, task

class Pokemon(HttpUser):  
    BASE_URL = "http://node-api:4444"
    @task
    def list(self):        
        self.client.get(f"{self.BASE_URL}/pokemon")