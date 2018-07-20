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


#Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

#Create a company, and three employees, and then assign the employees to the company.