import json
import re

# import time
import datetime

# import calendar
json_file = open("data.json", "r")
data = json.load(json_file)
json_file.close()


def if_exist(email):
    global data
    for i in range(len(data)):
        if data[i]["Email"] == email:
            return (i, True)

    return (-1, False)


def new_subscription(email, username, sub_days, price):
    global data
    date_now = datetime.datetime.now()
    user_index, flag = if_exist(email)
    if flag:
        data[user_index]["Days"] += sub_days
        date = re.split(r"[/: ]", data[user_index]["Ends at"])
        new_date = datetime.datetime(
            int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4])
        )
        new_date += datetime.timedelta(days=sub_days)
        data[user_index]["Ends at"] = new_date.strftime("%Y/%m/%d %H:%M")
        data[user_index]["Payments"].append((date_now.strftime("%Y/%m/%d"), price))
    else:
        date_expiration = date_now + datetime.timedelta(days=sub_days)
        new_user = {
            "Email": email,
            "UserName": username,
            "Days": sub_days,
            "Started": date_now.strftime("%Y/%m/%d %H:%M"),
            "Ends at": date_expiration.strftime("%Y/%m/%d %H:%M"),
            "Payments": [(date_now.strftime("%Y/%m/%d"), price)],
        }
        data.append(new_user)


def delete_subscription(email):
    global data
    user_index, flag = if_exist(email)
    if flag:
        data.pop(user_index)
    else:
        print("User not exist!!")


def check_expire():
    global data
    soon = []
    for i in range(len(data)):
        # date_start = re.split(r"[/: ]", data[i]["Started"])
        # s_ = datetime.datetime(
        #     int(date_start[0]), int(date_start[1]), int(date_start[2]), int(date_start[3]), int(date_start[4])
        # )
        date_end = re.split(r"[/: ]", data[i]["Ends at"])
        e_ = datetime.datetime(
            int(date_end[0]),
            int(date_end[1]),
            int(date_end[2]),
            int(date_end[3]),
            int(date_end[4]),
        )

        n = str(e_ - datetime.datetime.now())
        remaining = int(re.split(r"[/:, ]", n)[0])
        if remaining < 3:
            soon.append(data[i])

    return soon


# date_now = datetime.date.today()
# # days_in_current_month = calendar.monthrange(date_now.year, date_now.month)[1]
# # days_left_current_month = days_in_current_month - date_now.day

# subs = 60


# print(json.dumps(x, indent=2))
def write_json(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    # new_subscription("test@someting.com", "user1", 5,190)
    s = check_expire()
    print(s)
    # # delete_subscription("test@someting.com")
    # write_json(data)
