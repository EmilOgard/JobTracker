from database import get_all_jobs, update_job
from models import Job
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QInputDialog,
    QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QDialog, QFormLayout, QLineEdit, QHBoxLayout, QAbstractItemView
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
    