class Employee:
    def __init__(self, first_name, last_name, job_title, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.start_date = start_date

class Company:
    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = list()

BCRC = Company("Battery Recharger Charging Corp", "123 Road St.", "Battery recharger charging")
BRCI = Company("Battery Charger Recharging Inc", "321 Street Rd.", "Battery charger recharging")

Fred = Employee("Fred", "Fredricks", "Battery Charger Recharging Specialist", "sometime")
Ted = Employee("Ted", "Tedricks", "Battery Recharger Charging Expert", "soon")
Ned = Employee("Ned", "Nedricks", "Battery Recharging Optimizationalist", "sometime soon")
Red = Employee("Red", "Redricks", "Battery Charger Technician", "whenever")
Hank = Employee("Hank", "Hankricks", "Rapper/Producer", "whenver he feels like it")

BCRC.employees.append(Ned)
BCRC.employees.append(Red)

BRCI.employees.append(Fred)
BRCI.employees.append(Ted)
BRCI.employees.append(Hank)

print(f'{BCRC.name} is in the {BCRC.industry} industry and has the following dinguses working for them:')
for employee in BCRC.employees:
    print(f'{employee.first_name} {employee.last_name} the {employee.job_title}. He will start {employee.start_date}.')

print()

print(f'{BRCI.name} is in the {BRCI.industry} industry and has the following dinguses working for them:')
for employee in BRCI.employees:
    print(f'{employee.first_name} {employee.last_name} the {employee.job_title}. He will start {employee.start_date}.')
