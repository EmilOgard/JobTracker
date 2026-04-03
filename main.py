import sys
from database import init_db, get_all_jobs
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
)

class JobTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Job Tracker")
        self.resize(800, 500)

        layout = QVBoxLayout()

        self.add_button = QPushButton("Add Job")
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


def main():
    init_db()

    app = QApplication(sys.argv)
    window = JobTracker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()