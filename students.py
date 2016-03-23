students = [
	{
    'name': 'risper',
    'langs': ['Python', 'JavaScript', 'c++'],
    'age': 23
	},

     {
    'name': 'ten',
    'langs': ['Python', 'Java', 'PHP'],
    'age': 83
	},


	 {
    'name': 'dolly',
    'langs': ['HTML', 'JavaScript', 'angularjs'],
    'age': 59
	},
	{
    'name': 'chege',
    'langs': ['css', 'Ruby', 'PHP'],
    'age': 96
	}
]

def add_student(student):
	students.append(student)

def oldest_student():
	oldest_age = 18
	oldest_student = ""
	for student in students:
		age = student["age"]
		if age > oldest_age:
			oldest_age = age
			oldest_student = student["name"]
	return  oldest_age



def student_lang(lang):
	code = []
	for student in students:
		if lang in student["lang"]
			code.append(student)
	return code			



