# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        #initialize
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def __str__(self):
        # YOUR CODE STARTS HERE
        #format
        return f'{self.cid}({self.credits}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        #checks if the courses are equal
        if isinstance(other, Course):
            return self.cid == other.cid
        else:
            return False

        
class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        #create an empty dictionary
        self.courseOfferings = {}
        pass

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        #checkt to see if the ID is in the dictionary or not
        if cid not in self.courseOfferings:
            #if it is not then add it
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return "Course added successfully"
        elif cid in self.courseOfferings:
            #if it is nothing changes just returns a message
            return "Course already added"

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        #if the id key exists in the dictionary, delete it to remove the course
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        return "Course not found"

    def _loadCatalog(self, file):
        with open(file, 'r') as f: 
            course_info = f.readlines()  # You might change .readlines() for .read() if it suits your implementation 
        # YOUR CODE STARTS HERE
        #split evey line of the file by commas
        for course_lines in course_info:
            info = course_lines.split(",")
            cid, cname, credits = info
            final = self.addCourse(cid.strip(), cname.strip(), int(credits.strip()))

class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        if self.courses == {}:
            return "No courses"
        #join the course keys with the join keyword
        return '; '.join(self.courses.keys())
    
    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        #check to see if the input is valid
        if isinstance(course, Course):
            #if the id key is not in the dictionary, add it
            if course.cid not in self.courses:
                self.courses[course.cid] = course
            else:
                return "Course already added"

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        #checks to see if the input is valid
        if isinstance(course, Course):
            #if the id exists, delete it
            if course.cid in self.courses:
                del self.courses[course.cid]
            else:
                return "No such course"

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        total = 0
        #for all the courses in self.courses, add all the credits together
        for course in self.courses.values():
            total += course.credits
        return total


    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        value = self.totalCredits >= 12
        return value
    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount
        self.loan_id = self.__getloanID

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Balance: ${self.amount}'

    __repr__ = __str__

    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        return random.randint(10000, 99999)

class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        if not isinstance(self.name, str):
            return None
        #formatting the string to the correct output
        return f'Person({self.name}, ***-**-{self.ssn[-4:]})'
        
    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        if not isinstance(self.ssn, int):
            return None
        return self.ssn
        
    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if self.ssn == other:
            return True
        return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name, ssn)
        self.supervisor = supervisor

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__

    @property
    def id(self):
        # YOUR CODE STARTS HERE
        s_initials = self.name.split(" ")
        initials = ""
        for name in s_initials:
            #creating the string format
            initials += name[0].lower()
        return f"905{initials}{self.ssn[-4:]}"

    @property
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self.getSupervisor = new_supervisor
            return "Completed!"
        return None

    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return "Completed!"
        return None

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return "Completed!"
        return None

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return "Completed!"
        return None

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        if isinstance(person, Person):
            student = Student(person.name, person.ssn, "Freshman")
            return student
        return None


class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.classCode = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Student({self.name}, {self.id}, {self.classCode})"

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        return StudentAccount(self)

    @property
    def id(self):
        # YOUR CODE STARTS HERE
        s_initials = self.name.split(" ")
        initials = ""
        for name in s_initials: 
            initials += name[0].lower()
        #returns the formatted id with the last four digits of social security
        return initials + self.ssn[-4:]

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        # register the semester and define class Code
        if self.active and not self.hold:
            next_semester_number = len(self.semesters) + 1
            if next_semester_number <= 2:
                self.classCode = "Freshman"
            elif next_semester_number <= 4:
                self.classCode = "Sophomore"
            elif next_semester_number <= 6:
                self.classCode = "Junior"
            else:
                self.classCode = "Senior"
            
            self.semesters[next_semester_number] = Semester()
        else:
            return "Unsuccessful operation"

    def enrollCourse(self, cid, catalog):
        #check elligibility
        if self.active and not self.hold:
            #max(semesters) is used to get the last semester object in the dictionary
            current_semester = self.semesters[max(self.semesters)]
            #check if the course exists in the catalog
            if cid in catalog.courseOfferings:
                course = catalog.courseOfferings.get(cid)
                #check if the student is already enrolled in the course
                if cid not in current_semester.courses:
                    cost = course.credits * self.account.CREDIT_PRICE
                    current_semester.addCourse(course)
                    self.account.chargeAccount(cost)
                    #if the student is not enrolled, add the course and charge the account
                    return "Course added successfully"
                else:
                    return "Course already enrolled" 
            else:
                return "Course not found"
        else:
            return "Unsuccessful operation"

    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        #check if the student is elligible
        if self.active and not self.hold and len(self.semesters) > 0:
            current_semester = self.semesters[max(self.semesters)]
            #check again if the course is in the catalog or not
            if cid in current_semester.courses:
                course = current_semester.courses[cid]
                refund = (course.credits * self.account.CREDIT_PRICE) / 2
                #make the payment and drop the course
                self.account.makePayment(refund)
                current_semester.dropCourse(course)
                return "Course dropped successfully"
            else:
                return "Course not found"
        else:
            return "Unsuccessful operation"

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        #first checks to see if the student is elligible
        if not self.active:
            return "Unsuccessful Operation"
        #then whether or not the student is full time
        elif not self.semesters[max(self.semesters)].isFullTime:
            return "Not full time"
        else:
            #gets a loan and pays the amount to the account
            loan = Loan(amount)
            self.account.loans[loan.loan_id] = loan
            self.account.makePayment(amount)

class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''

    CREDIT_PRICE = 1000
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        #check if the amount is greater
        if amount < 0.0:
            return "Payment amount cannot be negative"
        #subtract balance amount
        self.balance -= amount
        return self.balance

    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        if amount < 0.0:
            return "Charge amount cannot be negative"
        #add amount to balance
        self.balance += amount
        return self.balance

def run_tests():
    import doctest
    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    #doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()