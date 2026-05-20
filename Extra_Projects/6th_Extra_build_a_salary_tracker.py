import json
import os

# ==========================================
# STEP 1: EMPLOYEE BLUEPRINT (DATA LAYER)
# ==========================================
class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
    _ot_rate_per_hour = 15.0
    _tax_rate = 0.05  # 5% Tax

    def __init__(self, emp_id, name, level, attendance_days=22, ot_hours=0):
        self.emp_id = emp_id
        self.name = name
        self.level = level
        self.attendance_days = attendance_days
        self.ot_hours = ot_hours

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        if not value or not isinstance(value, str):
            raise TypeError("Employee ID must be a non-empty string.")
        self._emp_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise TypeError("Name must be a non-empty string.")
        self._name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid level '{new_level}'. Supported: {list(Employee._base_salaries.keys())}")
        
        # Guard against lowering level (Demotion Check)
        if hasattr(self, '_level'):
            if Employee._base_salaries[new_level] < Employee._base_salaries[self._level]:
                raise ValueError("Demotion is not allowed through this system.")
        self._level = new_level

    # Net Salary Calculation Logic
    def calculate_salary(self):
        base = Employee._base_salaries[self.level]
        # Pro-rate salary based on standard 22 working days
        earned_base = (base / 22) * self.attendance_days
        ot_pay = self.ot_hours * Employee._ot_rate_per_hour
        gross_salary = earned_base + ot_pay
        tax = gross_salary * Employee._tax_rate
        return round(gross_salary - tax, 2)

    def to_dict(self):
        """Converts object data into dictionary format for JSON saving."""
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "level": self.level,
            "attendance_days": self.attendance_days,
            "ot_hours": self.ot_hours
        }

    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Level: {self.level} | Net Salary: ${self.calculate_salary()}"


# ==========================================
# STEP 2 & 3: COMPANY CLASS & DATA PERSISTENCE
# ==========================================
class Company:
    def __init__(self, filename="payroll.json"):
        self.employees = {}  # Using dictionary with emp_id as key for fast lookups
        self.filename = filename

    def add_employee(self, employee):
        if employee.emp_id in self.employees:
            print(f"Error: Employee ID {employee.emp_id} already exists!")
            return False
        self.employees[employee.emp_id] = employee
        print(f"Successfully added employee: {employee.name}")
        return True

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            removed = self.employees.pop(emp_id)
            print(f"Removed employee: {removed.name}")
            return True
        print("Error: Employee ID not found.")
        return False

    def get_total_monthly_payout(self):
        return sum(emp.calculate_salary() for emp in self.employees.values())

    def generate_payroll_report(self):
        if not self.employees:
            print("\n--- No employees registered in the system. ---")
            return
        print("\n" + "="*70)
        print(f"{'ID':<10} | {'NAME':<20} | {'LEVEL':<12} | {'NET SALARY':<10}")
        print("="*70)
        for emp in self.employees.values():
            print(f"{emp.emp_id:<10} | {emp.name:<20} | {emp.level:<12} | ${emp.calculate_salary():<10}")
        print("="*70)
        print(f"Total Company Budget Payout: ${self.get_total_monthly_payout():,}\n")

    # Save Data to JSON File
    def save_to_file(self):
        try:
            data_to_save = {emp_id: emp.to_dict() for emp_id, emp in self.employees.items()}
            with open(self.filename, 'w') as f:
                json.dump(data_to_save, f, indent=4)
            print("Data saved successfully to file.")
        except Exception as e:
            print(f"Failed to save data: {e}")

    # Load Data from JSON File
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return  # No file exists yet, start fresh
        try:
            with open(self.filename, 'r') as f:
                raw_data = json.load(f)
            for emp_id, data in raw_data.items():
                self.employees[emp_id] = Employee(
                    emp_id=data["emp_id"],
                    name=data["name"],
                    level=data["level"],
                    attendance_days=data["attendance_days"],
                    ot_hours=data["ot_hours"]
                )
            print(f"Successfully loaded {len(self.employees)} employees from database.")
        except Exception as e:
            print(f"Error loading database: {e}. Starting with an empty system.")


# ==========================================
# STEP 4: INTERACTIVE MENU LOOPS (UI LAYER)
# ==========================================
def main():
    company = Company()
    company.load_from_file()

    while True:
        print("\n=== 💼 REAL-WORLD PAYROLL & SALARY TRACKER ===")
        print("1. Add New Employee")
        print("2. View Payroll Report")
        print("3. Update Employee Level (Promotion)")
        print("4. Record Monthly Attendance & OT Hours")
        print("5. Remove Employee")
        print("6. Save & Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            print("\n--- Register New Employee ---")
            emp_id = input("Enter Employee ID (e.g., EMP01): ").strip()
            name = input("Enter Full Name: ").strip()
            level = input("Enter Level (trainee/junior/mid-level/senior): ").strip().lower()
            
            try:
                new_emp = Employee(emp_id, name, level)
                company.add_employee(new_emp)
            except (TypeError, ValueError) as err:
                print(f"Input Error: {err}")

        elif choice == "2":
            company.generate_payroll_report()

        elif choice == "3":
            print("\n--- Promote Employee ---")
            emp_id = input("Enter Employee ID: ").strip()
            if emp_id in company.employees:
                new_level = input("Enter New Level: ").strip().lower()
                try:
                    company.employees[emp_id].level = new_level
                    print(f"🚀 {company.employees[emp_id].name} has been successfully promoted to {new_level}!")
                except ValueError as err:
                    print(f"Promotion Failed: {err}")
            else:
                print("Employee ID not found.")

        elif choice == "4":
            print("\n--- Record Attendance & Overtime ---")
            emp_id = input("Enter Employee ID: ").strip()
            if emp_id in company.employees:
                try:
                    days = int(input("Enter Attendance Days (0-22): "))
                    ot = float(input("Enter Overtime Hours worked: "))
                    if not (0 <= days <= 22) or ot < 0:
                        raise ValueError("Invalid days or OT bounds.")
                    
                    company.employees[emp_id].attendance_days = days
                    company.employees[emp_id].ot_hours = ot
                    print(f"Stats updated for {company.employees[emp_id].name}.")
                except ValueError:
                    print("Error: Invalid numerical inputs provided.")
            else:
                print("Employee ID not found.")

        elif choice == "5":
            emp_id = input("Enter Employee ID to remove: ").strip()
            company.remove_employee(emp_id)

        elif choice == "6":
            company.save_to_file()
            print("System shutting down. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()