import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink water",
            message = "Keep Hydrated & Energetic. ",
            app_icon = "C:\Users\ADMIN\Downloads\icon.ico",
            timeout=5
        )
        time.sleep(5)








# from collections import Counter
# days=["Mon","Tue","Wed","Thu"]
# count=Counter(days)
# for x in range(1,5,2):
#     d=x%3
#     count.update([days[d]]*x)
# print(count)


