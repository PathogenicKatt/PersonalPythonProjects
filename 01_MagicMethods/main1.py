# Context Manager
from main import LocalUniversity

class UniversityDataManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.file_handle = None
        self.universities = []
    
    def __enter__(self):
        print(f"Opening file: {self.data_file}")
        self.file_handle = open(self.data_file, 'r')
        for line in self.file_handle:
            if line.strip():  # Skip empty lines
                name, province, numb_of_grad, year = line.strip().split(',')
                self.universities.append(LocalUniversity(name, province, int(numb_of_grad), int(year)))
        return self
    def find_by_province(self, province):
        return [uni for uni in self.universities if province in uni]
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_handle: # Close the file if it was opened
            self.file_handle.close()
            print(f"Closed file: {self.data_file}")
        return False  # Do not suppress exceptions

with UniversityDataManager('./01_MagicMethods/universities.csv') as udm:
    gauteng_unis = udm.find_by_province('Gauteng')
    for uni in gauteng_unis:
        print(uni)

    