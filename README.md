This is a POC that will check if the given resume is suitable for the given job description. 
Just insert the job description file path and give resume file path. Then it will extract the text and remove the unwanted spaces between them and then call the openai gpt-4-1106-preview
model and get back the result if the job is suitable for not. 
The implementation is done using langchain so, we just need to change the model name and api key, and it will start working. 

Here, is the result. 

Result for Different CVs, one for Software Engineer, and other for Robotics Engineer

![image](https://github.com/user-attachments/assets/b9782a2a-1cc7-4d41-9c0b-67c48a3e7ad4)


![image](https://github.com/user-attachments/assets/e8149097-4409-42a3-b2e1-ab4e51a4ca6a)

Run starter.py file using the following command :"python starter.py"



