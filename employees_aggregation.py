#Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.
class Employee:
    """ This represents an employee """

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

class Company:
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []


if __name__ == '__main__':
    #Create Company
    NSS = Company("Nashville Software School", "April 1, 2013")

    #Create Employees
    Steve = Employee("Steve Brownlee", "Lead Instructor", "July 24, 2018")
    Joe = Employee("Joe Shepherd", "Instructor", "July 24, 2018")
    Kimmie = Employee("Kimmie Bird", "Junior Instructor", "July 24, 2018")

    #Add employees into the aggregate instance variable of the bank
    NSS.employees.append(Steve)
    NSS.employees.append(Joe)
    NSS.employees.append(Kimmie)

    #Loop through employees list and print each employee
    for employee in NSS.employees:
        print(employee.name, employee.title, employee.start_date)