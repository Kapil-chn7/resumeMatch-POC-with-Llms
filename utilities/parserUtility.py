import os
import re
import PyPDF2
from utilities.ai import executor
def start():
    job_description= input("Please provide the job description file path")
    with open(job_description, 'r', encoding='utf-8') as file:
        content = file.read()
    job_description=content
    path =input("Please enter the path of the resume file:")
    if os.path.exists(path) or len(job_description)!=0 :
        print("converting resume to text")
        #converting resume to text
        text = convert_to_text(path)
        job_description = filter_text(job_description)
        print(text)
        data={
           "text":text, "job_description":job_description
        }
        result= executor(data)
        print("Here is the requested Result ", result)
        return 
        
    else:
        print("File not found or job description is empty")

def convert_to_text(path):
    print("converting resume to text")
    text=""
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    text=filter_text(text)
    return text

def filter_text(text):
    clean_text = re.sub(r' {2,}', ' ', text)
    clean_text.strip
    return clean_text






