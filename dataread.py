infile = open("coursedata.txt", "r")

course_data = infile.read().split("\n")
course_data = [x.split("!!") for x in course_data[:-1]]

infile.close()

# Taking care of table 1
departments = list(set([x[0] for x in course_data]))

# Getting to table 2
# DEPT, ID, NAME, CREDITS
courses = list(set((x[0], x[1], x[3], x[4])for x in course_data))
courses = sorted(courses, key=lambda x: (x[0], x[1]))

# Getting to table 3
# DEPT, ID, SECTION, DAYS, START, END, INSTRUCTOR, CLASSROOM, ALT CLASSROOM, ALT DAYS, ALT START, ALT END
sections = []
for x in course_data:
    result = x[5]
    start = x[6]
    end = x[7]

    if start == "None":
        start = None
    
    if end == "None":
        end = None

    filtered_data = [x[0], x[1], x[2], result, start, end, x[8], x[9], None, None, None, None]

    if x[10] != "None":
        alt_result = x[11]
        filtered_data[8], filtered_data[9], filtered_data[10], filtered_data[11] = x[10], alt_result, x[12], x[13]

    sections.append(tuple(filtered_data))