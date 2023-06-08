from json import *
from django.shortcuts import render
from pyrebase import pyrebase
from AAAS.code import *
from AAAS.courses import *

# -------------------^^ Confegrations for FireBase ^^------------------- #
config = {
    'apiKey': "AIzaSyBdAGklSfW5-AQmGJTpVsJJSfnzHjuvb00",
    'authDomain': "aaas-a442a.firebaseapp.com",
    'databaseURL': "https://aaas-a442a.firebaseio.com",
    'projectId': "aaas-a442a",
    'storageBucket': "aaas-a442a.appspot.com",
    'messagingSenderId': "163237067783"

}
# -------------------^^ Assigning Confogration to Varibles for FireBase  ^^------------------- #
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


# # -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def reglogin(request):
    return render(request, "Registrer_Login.html")  # {"e": email, "n": name}


# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def registrer_logIn(request):  # TODO: Edit To Authontication of Registrer Process
    email = request.POST.get('email')
    print(email)
    passw = request.POST.get("pass")

    try:
        # if email==
        user = authe.sign_in_with_email_and_password("yehia@fci.lu.edu.eg", passw)
    except:
        message = "invalid username or Pass+word or check your internet connection"
        return render(request, "Registrer_Login.html", {"msg": message})

    return render(request, "new_Registrer_Main.html")  # {"e": email, "n": name}


# -------------------^^ landing page View ^^------------------- #
def registrer_role(request):
    return render(request, "regestrer_updates.html")


# -------------------^^ landing page View ^^------------------- #
def reg_main(request):
    return render(request, "new_Registrer_Main.html")


# -------------------^^ Git Student Courses List View ^^------------------- #
def post_add(request):
    name = request.POST.get('uname')
    id = request.POST.get('userid')
    print(name)
    email = request.POST.get('uemail')
    print(email)
    passw = request.POST.get('upass')
    phone_number = request.POST.get('phone')
    address = request.POST.get('address')
    department = request.POST.get('depart')

    print(passw)
    # try:
    user = authe.create_user_with_email_and_password(email, passw)
    uid = user['localId']
    data = {"name": name, "user id": id, "Email": email, "status": "1", "password": passw, "phone number": phone_number,
            "address": address, 'department': department, }
    database.child("users").child(uid).child("details").set(data)
    return render(request, "new_Registrer_Main.html")


# -------------------^^ Login page View ^^------------------- #
def signIn(request):
    return render(request, "newlogin.html")


# -------------------^^ LogOut page View ^^------------------- #
def logoutforStudent(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request, "newlogin.html")


# -------------------^^ LogOut page View ^^------------------- #
def logoutforRegistrer(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request, "Registrer_Login.html")


# -------------------^^ Get User Details Function ^^------------------- #
def getUser(request):
    user = database.Post.get(id)
    all_users = database.child("users").shallow().get()
    print(all_users.val())

    session_id = user['idToken']
    request.session['uid'] = str(session_id)


# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def postsign_Student(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid username or Pass+word or check your internet connection"
        return render(request, "newlogin.html", {"msg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    idtoken = request.session['uid']
    url = request.POST.get('url')
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
    id = database.child('users').child(a).child('details').child('user id').get(idtoken).val()
    e_mail = database.child('users').child(a).child('details').child('Email').get(idtoken).val()
    department = database.child('users').child(a).child('details').child('department').get(idtoken).val()
    phone = database.child('users').child(a).child('details').child('phone number').get(idtoken).val()
    address = database.child('users').child(a).child('details').child('address').get(idtoken).val()
    return render(request, "new_main.html", {"n": name, "id": id, "mail": e_mail, "department": department,
                                             "phone": phone, "address": address})


# -------------------^^ Users Registration page View ^^------------------- #
def register_Details(request):
    return render(request, "registeration_info.html")


# -------------------^^ Users Registration page View ^^------------------- #
def report(request):
    return render(request, "report.html")


# -------------------^^ Users Registration page View ^^------------------- #
def contact_us(request):
    return render(request, "contact_us.html")


# -------------------^^ Users Registration page View ^^------------------- #
def profile(request):
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "profile.html", {"n": name, "id": id2,
                                            "mail": e_mail, "department": department, "phone": phone,
                                            "address": address})


# -------------------^^ Users Registration page View ^^------------------- #
def student_report(request):
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "stReport.html", {"n": name, "id": id2,
                                             "mail": e_mail, "department": department, "phone": phone,
                                             "address": address})


# ------------------------^^ Load Session Function ^^--------------- #
def load_Session(request):
    idtoken = request.session['uid']
    url = request.POST.get('url')
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
    id2 = database.child('users').child(a).child('details').child('user id').get(idtoken).val()
    e_mail = database.child('users').child(a).child('details').child('Email').get(idtoken).val()
    department = database.child('users').child(a).child('details').child('department').get(idtoken).val()
    phone = database.child('users').child(a).child('details').child('phone number').get(idtoken).val()
    address = database.child('users').child(a).child('details').child('address').get(idtoken).val()
    return name, id2, e_mail, department, phone, address


# -------------------^^ Main Student page View ^^------------------- #
def mainstu(request):
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "new_main.html", {"n": name, "id": id2,
                                             "mail": e_mail, "department": department, "phone": phone,
                                             "address": address})


# -------------------^^ (Old) Courses Registration page View ^^------------------- #
# def course_submit(request):
#     try:  # Session Start
#         idtoken = request.session['uid']
#         url = request.POST.get('url')
#         a = authe.get_account_info(idtoken)
#         a = a['users']
#         a = a[0]
#         a = a['localId']
#         # -------------------^^ Getting Data From Database ^^------------------- #
#         list_sub = database.child('users').child(a).child('studied_courses').get().val()
#         failed = database.child('users').child(a).child('failed_courses').get().val()
#         print(list_sub.keys())
#         print(failed)
#         if list_sub is not None:
#             keys = list(list_sub.keys())
#         else:
#             keys = []
#         if failed is not None:
#             keys2 = list(failed)
#         else:
#             keys2 = []
#         # data = json.loads(developerJsonString{})
#         # list_sub = database.child('users').child(a).child('registered_courses').(data, idtoken)
#         # print(list_sub)
#         allcourses = courses_check(keys, keys2)
#         semsGPA = dumps(1.9)
#         print(semsGPA)
#         dataJSON1 = dumps(allcourses)
#         # Get Dictionary data
#         dicsh = getCredithours()
#         # dumps Dictionary data
#         dataJSON = dumps(dicsh)
#         name, id2, e_mail, department, phone, address = load_Session(request)
#         return render(request, "about_stu.html",
#                       {"data": dataJSON1, "Dict": dataJSON, "ps": semsGPA, "n": name, "id": id2,
#                        "mail": e_mail, "department": department, "phone": phone,
#                        "address": address})
#     except:
#         return print("Exception Happened")


# -------------------^^ Course Registration page View ^^------------------- #
def course_registration(request):
    try:  # Session Start
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        usrid = a
        # print(usrid)
        # -------------------^^ Getting Data From Database ^^------------------- #
        list_sub = database.child('users').child(a).child('studied_courses').get().val()
        failed = database.child('users').child(a).child('failed_courses').get().val()
        # print(list_sub.keys())
        print(failed)
        if list_sub is not None:
            keys = list(list_sub.keys())
        else:
            keys = []
        if failed is not None:
            keys2 = list(failed)
        else:
            keys2 = []
    except:
        return print("Exception Happened")
    allcourses = courses_check(keys, keys2)
    semsGPA = dumps(1.9)
    # print(semsGPA)
    dataJSON1 = dumps(allcourses)
    # Get Dictionary data
    dicsh = getCredithours()
    # dumps Dictionary data
    dataJSON = dumps(dicsh)
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "courseRegister.html",
                  {"data": dataJSON1, "Dict": dataJSON, "ps": semsGPA, "n": name, "id": id2,
                   "mail": e_mail, "department": department, "phone": phone,
                   "address": address, "userid": usrid})


# -------------------^^ Contact US page View ^^------------------- #
def aboutst(request):
    courses_Description = getCoursesDescrition()  # Assign List Of Available Courses
    dataJSON1 = dumps(courses_Description)
    return render(request, "about_stu.html", {"Description": dataJSON1})


# -------------------^^ Contact US page View ^^------------------- #
def aboutus(request):
    return render(request, "aboutus.html")


# -------------------^^ Code Testin page View for features ^^------------------- #
def code_test(request):
    # create data dictionary
    dataDictionary = {
        'hello': 'World',
        'geeks': 'forgeeks',
        'ABC': 123,
        456: 'abc',
        14000605: 1,
        'list': ['geeks', 4, 'geeks'],
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    dicsh = getCredithours()
    # dump data
    dataJSON = dumps(dicsh)
    return render(request, 'anyGrade.html', {'data': dataJSON})


# ------------------------------------------- registrar functions-------------------------------
# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
# def postsign_registrer(request):
#     email = request.POST.get('email')
#     print(email)
#     passw = request.POST.get("pass")
#     if email == 'fahd@fci.lu.edu.eg':
#         authe.sign_in_with_email_and_password('fahd@fci.lu.edu.eg', passw)
#     else:
#         print("failed")
#
#     return render(request, "new_Registrer_Main.html")


def post_add(request):
    try:
        name2 = request.POST.get('uname')
        id = request.POST.get('userid')
        print(name2)
        email = request.POST.get('uemail')
        print(email)
        passw = request.POST.get('upass')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')
        department = request.POST.get('depart')
        print(passw)
        # try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid = user['localId']
        data = {"name": name2, "user id": id, "Email": email, "status": "1", "password": passw,
                "phone number": phone_number,
                "address": address, 'department': department, }
        database.child("users").child(uid).child("details").set(data)
    except:
        message = "Unable to create account try again"
        return render(request, "addUser.html", {"msg": message})
    return render(request, "new_Registrer_Main.html")


def newUser(request):
    return render(request, "addUser.html")
