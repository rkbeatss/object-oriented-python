class Employee:

    def __init__(self):
        self.__name = "Hubert"
        self.__age = 20

    def get_employee_info(self) -> str:
        return f"{self.__name} is currently {self.__age} years old!"

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_name(self, name: str) -> None:
        # Specific validation logic to setting a person's name only if it's not all uppercase
        # Encapsulation ensures that all the state control is concealed within the class
        if not name.isupper():
            self.__name = name

    def set_age(self, age: int) -> None:
        self.__age = age


if __name__ == "__main__":
    employee = Employee()
    print(employee.get_employee_info()) # Print 'Hubert is currently 20 years old!'
    employee.set_name("Rupsi")
    employee.set_age(23)
    print(employee.get_employee_info()) # Print 'Rupsi is currently 23 years old!'
    employee.set_name("HUBERT") # Our validation should stop this from being set 
    print(employee.get_name()) # still prints Rupsi
    employee.__name = "HUBERT" # this operation should also not work, no direct modification access allowed from outside the class
    print(employee.get_name()) # still Rupsi =]

