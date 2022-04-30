# we have to schedule time accordingly with the help of Task Schedular

import time
from plyer import notification

if __name__ == "__main__":
    while True:
       notification.notify(
          title="Please Drink Water Now...",
          message="As it refreshes our mind please drink water ",
          app_icon = "E:\python lab\icon.ico",
          timeout=10
    )
    time.sleep(60*60)
    
