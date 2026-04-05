import sys
from database import init_db, get_all_jobs, add_job, update_job
from scraper import extract_finn_code, fetch_job_from_finn
from dialog import JobEditDialog
from models import Job
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QInputDialog,
    QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QDialog, QFormLayout, QLineEdit, QHBoxLayout, QAbstractItemView
)


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
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.edit_job_from_table)
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
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(row[1])))  # finn_code
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(row[2])))  # title
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(row[4])))  # company
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(row[5])))  # location
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(row[3])))  # description
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(row[7])))  # status

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
            add_job(updated_job)
            self.load_jobs()
        else:
            print("User cancelled")
    

    def edit_job_from_table(self, row, col):
        jobs = get_all_jobs()
        sel_row = jobs[row]

        job = Job(
            finn_code=sel_row[1],
            title=sel_row[2],
            description=sel_row[3],
            company=sel_row[4],
            location=sel_row[5],
            url=sel_row[6],
            status=sel_row[7],
            date_applied=sel_row[8] if len(sel_row) > 8 else None
        )

        job_id = sel_row[0]

        dialog = JobEditDialog(job)

        if dialog.exec():
            updated_job = dialog.get_updated_job()
            update_job(job_id, updated_job)

            self.load_jobs()


def main():
    init_db()

    app = QApplication(sys.argv)
    window = JobTracker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()