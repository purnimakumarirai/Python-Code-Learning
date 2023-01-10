#creating class
class User:
       def __int__(self, email,name,password, current_job):

         self.email = email
         self.name = name
         self.password = password
         self.current_job = current_job

       def change_password(self, new_password):
              self.password = new_password
       def change_job_title(self,new_job_title):
              self.current_job = new_job_title
       def get_user_info(self):
              print(f"User {self.name} current works as a {self.current_job}. you can contact them at {self.email}")

#creating object
app_user1 = User( )
app_user1.get_user_info()
