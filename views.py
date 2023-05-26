from flask import render_template, Blueprint, request
from flask_cors import CORS
import json
from dataread import *

my_blueprint = Blueprint('my_blueprint', __name__)
CORS(my_blueprint)

department_id = 'COMP'  # Replace with the specific department ID
course_id = '200'  # Replace with the specific course ID


@my_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dropdown_value = request.form['dropdown']
        dropdown2_value = request.form['dropdown2']
        dropdown3_value = request.form['dropdown3']

        filtered_sections = course_data

        
        if dropdown_value != "all":
            filtered_sections = [x for x in filtered_sections if x[0] == dropdown_value]

        if dropdown2_value != "all":
            filtered_sections = [x for x in filtered_sections if x[3] == dropdown2_value]

        if dropdown3_value != "all":
            filtered_sections = [x for x in filtered_sections if x[8] == dropdown3_value]
        
        # Convert sections to JSON format
        sections_json = []
        for section in filtered_sections:
            sections_json.append({
                'department_id': section[0],
                'course_id': section[1],
                'section': section[2],
                'days': section[5],
                'start_time': section[6],
                'end_time': section[7],
                'instructor_name': section[8],
                'classroom': section[9],
                'alternate_classroom': section[10],
                'alternate_days': section[11],
                'alternate_start_time': section[12],
                'alternate_end_time': section[13],
            })

        return json.dumps(sections_json, indent=2)
    
    return render_template('New_index.html')


@my_blueprint.route('/departments', methods=['GET'])
def get_departments():
    departments.sort()
    departments_ = [{'label': department, 'value': department} for department in departments]
    return json.dumps(departments_)

@my_blueprint.route('/courses', methods=['GET'])
def get_courses():
    courses_ = [{'label': course[2], 'value': course[2]} for course in courses]
    return json.dumps(courses_)

@my_blueprint.route('/instructors', methods=['GET'])
def get_instructors():
    instructors = list(set([x[6] for x in sections]))
    instructors.sort()
    unique_instructors = [{'label': instructor, 'value': instructor} for instructor in instructors]
    return json.dumps(unique_instructors)

@my_blueprint.route('/submit', methods=['POST'])
def submit_courses():
    selected_courses = request.get_json()
    
    # Perform further processing with the selected courses
    # You can access the department, courseID, and instructor for each course
    
    # Example: Print the selected courses
    for course in selected_courses:
        department = course['department']
        course_id = course['courseID']
        instructor = course['instructor']
        print(f"Department: {department}, Course ID: {course_id}, Instructor: {instructor}")
    
    # Example: Return a response message
    return json.dumps("Courses submitted successfully")

'''@my_blueprint.route("/dataRetrieval", methods=['POST', 'GET'])
def dataRetrieval():   
    departments = [department.department_id for department in Department.query.all()]
    course_names = [course.course_name for course in Course.query.all()]
    instructor_names = [section.instructor_name for section in Section.query.all()]
    classrooms = [section.classroom for section in Section.query.all()]

    data = {
        "DEPT": departments,
        "COURSE_NAME": course_names,
        "INSTRUCTOR_NAME": list(set(instructor_names)),
        "CLASSROOM": list(set(classrooms))
    }

    json_data = json.dumps(data)
    return json_data'''
