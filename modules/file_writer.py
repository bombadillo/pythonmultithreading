import threading
lock = threading.Lock()

class FileWriter:

    def write_string(self, string, file_name):
        with lock:
            f = open(file_name,'a')
            f.write(string)
            f.close()
