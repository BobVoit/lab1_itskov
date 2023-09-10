class FileWrire:
    @classmethod
    def write_in_file(cls, file_name, text):
        f = open(file_name, 'w')
        f.write(text)
        f.close()