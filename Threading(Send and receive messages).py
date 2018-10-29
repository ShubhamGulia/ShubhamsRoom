# This is how messenger are build

# thread doesnot wait for the other process to finish after starting it goes to next process

import threading
class ShubhamRoom(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x=ShubhamRoom(name="Hey SHubham\n")
y=ShubhamRoom(name="Hey Gulia\n")
x.start()
y.start()

