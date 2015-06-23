import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from radio_button_class import *
from wheat_class import *
from potato_class import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulated crop"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

        self.stacked_layout = QStackedLayout() # holds various layouts needed by the window
        self.stacekd_layout.addWidget(seld.select_crop_widget)

        #set the central widget to display layout

        self.central_widget = QWidget
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        
    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()

        self.create_view_crop_layout()
    def create_select_crop_layout(self):
        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat","Potato"))
        self.instantiate_buttons = QPushButton("Create Crop")
        
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_buttons)
        
        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        
        
        #connections
        self.instantiate_buttons.clicked.connect(self.instantiate_crop)

    def create_new_crop_layout(self,crop_type):
        #this is the second layout of the window - view the crop growth etc
        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Manually Grow")
        self.automatic_grow_button = QPushButton("Manually Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widgets to the status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #add line edit widgets to the status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        #add widgets/layouts to the grow layout
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        #create a wigdet to display the grow layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        
        
    
            

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()
