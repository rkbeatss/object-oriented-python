from abc import ABC, abstractmethod


class Report(ABC):
    ''' 

    An API that defines common properties and behaviour of reports
    Can be composed of concrete and abstract methods 
    
    '''

    def get_report_type(self) -> str:
        return f"Report type: {self.name}"

    @abstractmethod
    def generate_report(self, year):
        raise NotImplementedError()


class ExpenseReport(Report):
    name = 'Expense Report'
    db = {2019: 50, 2020: 60, 2021: 80}

    def generate_report(self, year) -> str:
        res = f"---------- EXPENSE REPORT FOR {year} ---------- "
        res += f"\n           Expenses: ${self.__get_expenses(year)}"
        return res

    # Private bc when users invoke generate_report(), they just want the report and don't care about implementation details, therefore the details should be hidden
    def __get_expenses(self, year):
        return self.db.get(year) * 365


class AuditReport(Report):
    name = 'Audit Report'
    db = {2019: {'opinion': 'bad financial situation', 'auditor_name': 'Rupsi Kaushik'}, 2020: {'opinion': 'better financial situation',
                                                                                                'auditor_name': 'Abha Sharma'}, 2021: {'opinion': 'getting better good job', 'auditor_name': 'Zena Mankal'}}

    def generate_report(self, year) -> str:
        if year not in self.db:
            raise ValueError("No records for that year")
        res = f"---------- AUDIT REPORT FOR {year} ---------- "
        res += f"\n           Auditor Name: {self.__get_auditor_name(year)}"
        res += f"\n           Auditor Opinion: {self.__get_auditor_opinion(year)}"
        return res

    # Private method bc when users invoke generate_report(), they just want the report and don't care about further implementation details
    def __get_auditor_name(self, year):
        return self.db.get(year)['auditor_name']

    def __get_auditor_opinion(self, year):
        return self.db.get(year)['opinion']


if __name__ == "__main__":
    expense_report = ExpenseReport()
    audit_report = AuditReport()
    print(expense_report.generate_report(2020)) # Expense report for 2020
    print(expense_report.get_report_type()) # Expense Report
    print(audit_report.generate_report(2020)) # Audit report for 2021
    print(audit_report.get_report_type()) # Audit Report
    # These methods are not available to the users to reduce complexity ==> abstraction
    print(expense_report.__get_expenses(2020)) # Throws an AttributeError exception!
