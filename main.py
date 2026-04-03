import sys
from database import init_db, get_all_jobs, add_job
from scraper import extract_finn_code, fetch_job_from_finn
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QInputDialog,
    QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QDialog, QFormLayout, QLineEdit, QHBoxLayout
)

class JobEditDialog(QDialog):
    def __init__(self, job):
        super().__init__()

        self.setWindowTitle("Edit Job")
        self.job = job
        layout = QFormLayout()

        self.title_input = QLineEdit(job.title or "")
        self.company_input = QLineEdit(job.company or "")
        self.location_input = QLineEdit(job.location or "")
        self.description_input = QLineEdit(job.description or "")
        self.status_input = QLineEdit(job.status or "")

        layout.addRow("Title:", self.title_input)
        layout.addRow("Company:", self.company_input)
        layout.addRow("Location:", self.location_input)
        layout.addRow("Description:", self.description_input)
        layout.addRow("Status:", self.status_input)

        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")

        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)

        layout.addRow(button_layout)
        self.setLayout(layout)

    def get_updated_job(self):
        self.job.title = self.title_input.text()
        self.job.company = self.company_input.text()
        self.job.location = self.location_input.text()
        self.job.description = self.description_input.text()
        self.job.status = self.status_input.text()

        return self.job

class JobTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Job Tracker")
        self.resize(800, 500)

        layout = QVBoxLayout()

        self.add_button = QPushButton("Add Job")
        self.add_button.clicked.connect(self.add_job_dialog)
        layout.addWidget(self.add_button)

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_jobs()

    def load_jobs(self):
        jobs = get_all_jobs()

        self.table.setRowCount(len(jobs))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "FinnCode", "Position", "Company", "Location", "Description", "Status"
        ])

        for row_idx, row in enumerate(jobs):
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))


    def add_job_dialog(self):
        text, ok = QInputDialog.getText(self, "Add Job", "Enter FinnCode")

        if not ok or not text:
            return
    
        code = extract_finn_code(text)

        if not code:
            print("Invalid code")
            return
        
        job = fetch_job_from_finn(code)

        dialog = JobEditDialog(job)

        if dialog.exec():
            updated_job = dialog.get_updated_job()
            add_job(job)
            self.load_jobs()
        else:
            print("User cancelled")


def main():
    init_db()

    app = QApplication(sys.argv)
    window = JobTracker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()