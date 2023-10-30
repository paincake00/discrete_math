class File_manager:

    def file_read(self, file_name):
        try: 
            with open('files\\' + file_name) as file:
                return file.read()
        except FileNotFoundError:
            print("That file was not found :(")

    def file_write(self, file_name, text, mode):
        with open('files\\' + file_name, mode) as file:
            file.write(text)