import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Take a Break !",
            message="Go to Real World, this virtual world is NOT your reality",
            app_icon="I:\Coding\Python\hourglass.ico",
            timeout=10
        )
        time.sleep(60*60)
