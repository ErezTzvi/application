import os
from pathlib import Path
from flask import Flask,request
import json

students_path = Path("../wis-advanced-python-2021-2022/students/") # path to directory with json files for students
student_list = sorted([student for student in os.listdir(students_path) if student.endswith(".json")]) # Collect all json files of students and sort by name

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/") # default route. returns a list of students in an html format. Clicking on a students opens the info.
def main_page():
    return(html_list_of_students(student_list))




def html_list_of_students(json_files):
    """
    Parameters
    ----------
    json_files : TYPE list
        list of all students to be presented, json files in dir "students"

    Returns
    -------
    clickble html list of students in list
    """
    html = """
    <h1> Students in the Course:</h1>
    <ul>
    {}
    </ul>
    """.format("".join(["<li><a href=/student/"+student+">"+student.rstrip(".json")+"</a></li>" for student in json_files]))
    return(html)
