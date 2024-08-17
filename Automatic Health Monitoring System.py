class DiagnosisReport:
    def __init__(self, date, diagnosis, doctor_notes, follow_up):
        self.date = date
        self.diagnosis = diagnosis
        self.doctor_notes = doctor_notes
        self.follow_up = follow_up

    def __str__(self):
        return f"Date: {self.date}, Diagnosis: {self.diagnosis}, Doctor's Notes: {self.doctor_notes}, Follow-up: {self.follow_up}"


class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.reports = []

    def add_report(self, report):
        self.reports.append(report)

    def get_summary(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Total Visits: {len(self.reports)}"


class HealthMonitoringSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def add_diagnosis_report(self, patient_id, report):
        if patient_id in self.patients:
            self.patients[patient_id].add_report(report)
        else:
            print(f"Patient ID {patient_id} not found!")

    def get_patient_summary(self, patient_id):
        if patient_id in self.patients:
            return self.patients[patient_id].get_summary()
        else:
            return f"Patient ID {patient_id} not found!"

    def get_patient_reports(self, patient_id):
        if patient_id in self.patients:
            return '\n'.join([str(report) for report in self.patients[patient_id].reports])
        else:
            return f"Patient ID {patient_id} not found!"


def main():
    system = HealthMonitoringSystem()

    while True:
        print("\n--- Automatic Health Monitoring System ---")
        print("1. Add Patient")
        print("2. Add Diagnosis Report")
        print("3. View Patient Summary")
        print("4. View Patient Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")

            new_patient = Patient(patient_id=patient_id, name=name, age=age)
            system.add_patient(new_patient)
            print("Patient added successfully!")

        elif choice == "2":
            patient_id = input("Enter Patient ID: ")
            date = input("Enter Diagnosis Date (YYYY-MM-DD): ")
            diagnosis = input("Enter Diagnosis: ")
            doctor_notes = input("Enter Doctor's Notes: ")
            follow_up = input("Enter Follow-up Instructions: ")

            new_report = DiagnosisReport(date=date, diagnosis=diagnosis, doctor_notes=doctor_notes, follow_up=follow_up)
            system.add_diagnosis_report(patient_id=patient_id, report=new_report)
            print("Diagnosis report added successfully!")

        elif choice == "3":
            patient_id = input("Enter Patient ID: ")
            summary = system.get_patient_summary(patient_id=patient_id)
            print(summary)

        elif choice == "4":
            patient_id = input("Enter Patient ID: ")
            reports = system.get_patient_reports(patient_id=patient_id)
            print(reports)

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
