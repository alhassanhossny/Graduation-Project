# Priority Dictionary :
priorety = {"IT Fundamentals": 1, "Mathematics I": 2, "Physics I": 4, "Electronics": 3, "English Language I": 3,
            "Hand Drawing": 4,
            "History of Computing": 4, "Social Context of Computing": 4, "Programming Fundamentals": 1,
            "Mathematics II": 2,
            "Physics II": 4, "Digital Circuits": 4, " Interpersonal Communication": 4, "Human Rights": 4,
            "English Language II": 3,
            "Computer Law": 4, "Discrete Structures": 2, "Object-Oriented Programming": 1, "Project Management": 1,
            "Data Communications": 2,
            "Technical Writing": 4, "Foundations of Information Systems": 2, "Business Administration": 4,
            "Data Structures and Algorithms": 1,
            "Databases": 3, "Computer Architecture": 2, "Probability and Statistics": 4, "Computers and Ethics": 4,
            "Systems Analysis and Design": 4, "File Organization": 4, "Computer Networks": 2, "Image Processing": 3,
            "Software Engineering": 1, "Visual Programming": 3, "Computer Graphics": 3,
            "Algorithm Design and Analysis": 3,
            "Operating Systems": 3, "Automata and Language Theory": 4, "Advanced Computer Graphics": 4,
            "Artificial Intelligence": 3,
            "Software Development and Professional Practice": 1, "Field Training": 4, "Compiler Construction": 4,
            "Capstone Project I": 1,
            "Introduction to Computer Security": 4, "Web Programming": 4, "Computer Vision": 4,
            "Network Programming": 4, "Capstone Project II": 1,
            "Machine Learning": 4, "Cryptography": 4, "Parallel Computation": 4, "Computer Animation": 4,
            "Advanced Database": 4}

# Prerequisite Dictionary for every Course
prerequisite = {"IT Fundamentals": None, "Mathematics I": None, "Physics I": None, "Electronics": None,
                "English Language I": None, "Hand Drawing": None,
                "History of Computing": None, "Social Context of Computing": None,
                "Programming Fundamentals": "IT Fundamentals", "Mathematics II": "Mathematics I",
                "Physics II": None, "Digital Circuits": "Electronics", "Interpersonal Communication": None,
                "Human Rights": None, "English Language II": "English Language I",
                "Computer Law": None, "Discrete Structures": "Mathematics II",
                "Object-Oriented Programming": "Programming Fundamentals",
                "Project Management": "IT Fundamentals", "Data Communications": "IT Fundamentals",
                "Technical Writing": "English Language I", "Foundations of Information Systems": "IT Fundamentals",
                "Business Administration": None, "Data Structures and Algorithms": "Object-Oriented Programming",
                "Databases": "Foundations of Information Systems",
                "Computer Architecture": ["Programming Fundamentals", "Discrete Structures"],
                "Probability and Statistics": "Mathematics II", "Computers and Ethics": None,
                "Systems Analysis and Design": "IT Fundamentals", "File Organization": "Object-Oriented Programming",
                "Computer Networks": ["Computer Architecture", "Data Communications"],
                "Image Processing": "Data Structures and Algorithms",
                "Software Engineering": "Data Structures and Algorithms",
                "Visual Programming": "Data Structures and Algorithms",
                "Computer Graphics": ["Discrete Structures", "IT Fundamentals"],
                "Algorithm Design and Analysis": "Data Structures and Algorithms",
                "Operating Systems": "Computer Architecture",
                "Automata and Language Theory": ["Discrete Structures", "Programming Fundamentals"],
                "Advanced Computer Graphics": "Computer Graphics",
                "Artificial Intelligence": ["Discrete Structures", "IT Fundamentals"],
                "Software Development and Professional Practice": "Software Engineering",
                "Field Training": "Project Management",
                "Compiler Construction": ["Visual Programming", "Computer Architecture",
                                          "Data Structures and Algorithms"],
                "Capstone Project I": ["Project Management", "Software Development and Professional Practice"],
                "Introduction to Computer Security": ["Computer Networks", "Data Structures and Algorithms"],
                "Web Programming": ["Data Communications", "Programming Fundamentals"],
                "Computer Vision": ["Physics II", "Object-Oriented Programming"],
                "Network Programming": "Computer Networks",
                "Capstone Project II": "Capstone Project I",
                "Machine Learning": "Artificial Intelligence",
                "Cryptography": ["Computer Networks", "Data Structures and Algorithms"],
                "Parallel Computation": ["Operating Systems", "Algorithm Design and Analysis"],
                "Computer Animation": "Image Processing", "Advanced Database": "Database"}

# studied = ["Business Administration",
#            'Computer Architecture', 'Computer Law', 'Computers and Ethics', 'Data Structures and Algorithms',
#            'Databases', 'Digital Circuits', 'Discrete Structures', 'Electronics',
#            'English Language I', 'English Language II', 'File Organization',
#            'Foundations of Information Systems', 'Hand Drawing', 'History of Computing',
#            'Human Rights', 'IT Fundamentals', 'Interpersonal Communication', 'Mathematics I',
#            'Mathematics II', 'Object-Oriented Programming', 'Physics I', 'Physics II',
#            'Probability and Statistics', 'Programming Fundamentals', 'Project Management',
#            'Social Context of Computing', 'Systems Analysis and Design', 'Technical Writing']


def courses_check(studied, failed):
    can_registered = []
    for i in studied: # Not Studied Courses
        if i in prerequisite:
            del prerequisite[i]
    not_studied = list(prerequisite.keys())
    for i in prerequisite:  # Courses that can be Registered
        if prerequisite[i] in studied or prerequisite[i] is None or prerequisite[i] in failed:
            if i not in can_registered:
                can_registered.append(i)
        elif type(prerequisite[i]) == list:
            subprerequisite = prerequisite[i]
            flag = 1
            for s in subprerequisite:
                if s not in studied:
                    flag = 0
                    break
            if flag:
                if i not in can_registered:
                    can_registered.append(i)
    fp_courses = []
    sp_courses = []
    thp_courses = []
    fop_courses = []
    for i in can_registered: # Priority Check
        if priorety.get(i) == 1:
            fp_courses.append(i)
        elif priorety.get(i) == 2:
            sp_courses.append(i)
        elif priorety.get(i) == 3:
            thp_courses.append(i)
        else:
            fop_courses.append(i)
    allcources = [fp_courses, sp_courses, thp_courses, fop_courses]
    # print(allcources)
    return allcources
