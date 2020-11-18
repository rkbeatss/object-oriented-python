class Employee:
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    # Each employee subclass may want a common method to get a summary of their info
    def get_employee_summary(self):
        return f"Employee #{self.id}: {self.lname}, {self.fname} \n Monthly Salary: ${self.calculate_monthly_salary()}"


class Programmer(Employee):
    def __init__(self, id, fname, lname, hourly_wage, weekly_hours):
        super().__init__(id, fname, lname)
        # Specific employees may have differing wages and weekly hours that they work
        self.wage = hourly_wage
        self.hours = weekly_hours

    def calculate_monthly_salary(self):
        return (self.wage * self.hours * 4)


if __name__ == "__main__":
    emp1 = Programmer(7, "Rupsi", "Kaushik", 30, 20)
    # Print Employee #7: Kaushik, Rupsi
    # Monthly Salary: $2400
    print(emp1.get_employee_summary())
