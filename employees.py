#Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

#Practice Inheritance on Company / Employee "is-a" relationship
class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []


    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above
    def get_employees(self):
        """Returns employee of the company"""

        return self.employees

    def set_employee(self, employee):
        """Sets employee of the company
        Parameters: 
        employee: dictionary with 3 properties name,
        title, start_date
        """

        self.employees.append(employee)

#Create a company, and three employees, and then assign the employees to the company. (Using the above example)

if __name__ == '__main__':
    #Create a company
    NSS = Company("Nashville Software School", "April 1, 2013")

    #Create employees
    NSS.set_employee({'name':'Steve Brownlee', 'title':'Lead Instructor', 'start_Date':'July 24, 2018'})
    NSS.set_employee({'name': 'Joe Shepherd', 'title': 'Instructor', 'start_date': 'July 24, 2018'})
    NSS.set_employee({'name': 'Kimmie Bird', 'title': 'Junior Instructor', 'start_date': 'July 24, 2018'})

    print(NSS.company_name)
    print(NSS.date_founded)
    print(NSS.employees)

#Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

    #Comment:  See file employees_aggregation.py for answer
