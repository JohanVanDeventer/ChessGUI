import subprocess


# creates a new engine in a subprocess, with functions to send input and read output
# the engine must use uci
class Engine:
    def __init__(self, path_to_engine_exe):
        self.process = subprocess.Popen(path_to_engine_exe, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def send_input(self, input_txt, is_flush=True):
        self.process.stdin.write(input_txt.encode())
        if is_flush:
            self.process.stdin.flush()

    def receive_output(self):
        return self.process.stdout.readline().decode().strip()

    def close(self):
        self.send_input("quit\n")
        self.process.stdin.close()
        self.process.stdout.close()
        self.process.wait()
