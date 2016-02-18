from modules.file_writer import FileWriter

class NumberIterator:

    def iterate(self):
        i = 0
        while i < 100:
            message = "integer {0}\n".format(i)
            FileWriter().write_string(message, 'test.txt')
            i += 1
