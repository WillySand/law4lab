from locust import HttpUser, between, task
import random

creation = 140
deletion = 0

creation2 = 10000000140
deletion2 = 1000000000

creation3 = 2000000140
deletion3 = 2000000000

creation4 = 3000000140
deletion4 = 3000000000

creation5 = 4000000140
deletion5 = 4000000000


class WebsiteUser(HttpUser):
    wait_time = between(5, 10)   
    
    #def on_start(self):
        #self.client.get("/api/")
        
    
    @task
    def make_new(self):
        global creation
        creation+=1
        npm = str(creation)
        self.client.post("/api/", json={"nama":"nama"+npm, "alamat":"alamat"+npm, "npm":npm})
    
    @task
    def make_new2(self):
        global creation2
        creation2+=1
        npm = str(creation2)
        self.client.post("/api/", json={"nama":"nama"+npm, "alamat":"alamat"+npm, "npm":npm})
    
    @task
    def make_new3(self):
        global creation3
        creation3+=1
        npm = str(creation3)
        self.client.post("/api/", json={"nama":"nama"+npm, "alamat":"alamat"+npm, "npm":npm})
        
    @task
    def make_new4(self):
        global creation4
        creation4+=1
        npm = str(creation4)
        self.client.post("/api/", json={"nama":"nama"+npm, "alamat":"alamat"+npm, "npm":npm})
    
    @task
    def make_new5(self):
        global creation5
        creation5+=1
        npm = str(creation5)
        self.client.post("/api/", json={"nama":"nama"+npm, "alamat":"alamat"+npm, "npm":npm})

    @task
    def get_all(self):
        self.client.get("/api/")
        
    @task
    def get(self):
        global creation
        global deletion
        npm = str(int((creation+deletion)//2))
        self.client.get("/api/"+npm+"/")
    
    @task
    def get2(self):
        global creation2
        global deletion2
        npm = str(int((creation2+deletion2)//2))
        self.client.get("/api/"+npm+"/")
        
    @task
    def get3(self):
        global creation3
        global deletion3
        npm = str(int((creation3+deletion3)//2))
        self.client.get("/api/"+npm+"/")
    
    @task
    def get4(self):
        global creation4
        global deletion4
        npm = str(int((creation4+deletion4)//2))
        self.client.get("/api/"+npm+"/")
    
    @task
    def get5(self):
        global creation5
        global deletion5
        npm = str(int((creation5+deletion5)//2))
        self.client.get("/api/"+npm+"/")
    
    
    @task
    def update(self):
        global creation
        global deletion
        npm = str(int((creation+deletion)//2))
        self.client.put("/api/"+npm+"/", json={"nama":"nama"+str(int(npm)+1), "alamat":"alamat"+str(int(npm)+1)})
        
    @task
    def update2(self):
        global creation2
        global deletion2
        npm = str(int((creation2+deletion2)//2))
        self.client.put("/api/"+npm+"/", json={"nama":"nama"+str(int(npm)+1), "alamat":"alamat"+str(int(npm)+1)})
        
    @task
    def update3(self):
        global creation3
        global deletion3
        npm = str(int((creation3+deletion3)//2))
        self.client.put("/api/"+npm+"/", json={"nama":"nama"+str(int(npm)+1), "alamat":"alamat"+str(int(npm)+1)})
        
    @task
    def update4(self):
        global creation4
        global deletion4
        npm = str(int((creation4+deletion4)//2))
        self.client.put("/api/"+npm+"/", json={"nama":"nama"+str(int(npm)+1), "alamat":"alamat"+str(int(npm)+1)})
    
    @task
    def update5(self):
        global creation5
        global deletion5
        npm = str(int((creation5+deletion5)//2))
        self.client.put("/api/"+npm+"/", json={"nama":"nama"+str(int(npm)+1), "alamat":"alamat"+str(int(npm)+1)})
        
    @task
    def delete(self):
        global deletion
        deletion+=1
        npm = str(deletion)
        self.client.delete("/api/"+npm)
    @task
    def delet2(self):
        global deletion2
        deletion2+=1
        npm = str(deletion2)
        self.client.delete("/api/"+npm)
    @task
    def delete3(self):
        global deletion3
        deletion3+=1
        npm = str(deletion3)
        self.client.delete("/api/"+npm)
    @task
    def delete4(self):
        global deletion4
        deletion4+=1
        npm = str(deletion4)
        self.client.delete("/api/"+npm)
    @task
    def delete(self):
        global deletion5
        deletion5+=1
        npm = str(deletion5)
        self.client.delete("/api/"+npm)
