import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please take a short break",
            message = "Its good to take a short break after 25 minutes for a hard work" ,
            app_icon = "reminder.ico",
            timeout = 10

        )
        time.sleep(10)


