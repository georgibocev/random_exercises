# Task: Implement a FileReader class that takes a file path and provides methods to read the file line by line or all at once.
# Example Input: reader = FileReader(“file.txt”); reader.read_line()
# Example Output: “First line of file.”

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_whole_file(self):
        with open(self.file_path, 'r') as file:
            return file.read().strip()

    def read_line(self):
        with open(self.file_path, 'r') as file:
            return file.readline().strip()

exampleReader = FileReader("../HW_03/file.txt")

print("First line is:", exampleReader.read_line())
print("Whole file is:", exampleReader.read_whole_file())
