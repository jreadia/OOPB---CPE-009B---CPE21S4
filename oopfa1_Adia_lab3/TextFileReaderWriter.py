class TextFileReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

# Example Usage to read a txt file
reader_writer = TextFileReaderWriter('example.txt')
reader_writer.read()
print(reader_writer.read())

# Example Usage to write to a txt file
reader_writer = TextFileReaderWriter('example.txt')
reader_writer.write('This is a new content')
print(reader_writer.read())