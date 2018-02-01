python = ['a','b','c','d','e','f','g','h'] #defining list of students in python class
webapp = ['a','c','f','h','j','k','i','t']  #defining list of students in webapp class
def students(python,webapp):            #function for finding the list of common and uncommon Students
    common = set(python)&set(webapp)    #applying AND operator to find the commons
    uncommon = set(python)^set(webapp)  #applying OR operator to find the uncommons
    print("Students enrolled in both classes are:",common)
    print("Students enrolled in only one class are:",uncommon)
students(python,webapp)