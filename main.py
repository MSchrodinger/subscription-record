import json
import re

# import time
import datetime

# import calendar


# json_file = open("data.json", "r")
# data = json.load(json_file)
# json_file.close()


class Subs_record:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        self.data = json.load(open(data_file_name, "r"))

    def if_exist(self, email):
        for i in range(len(self.data)):
            if self.data[i]["Email"] == email:
                return (i, True)

        return (-1, False)

    def new_subscription(self, email, username, sub_days, price):
        date_now = datetime.datetime.now()
        user_index, flag = self.if_exist(email)
        if flag:
            self.data[user_index]["Days"] += sub_days
            self.date = re.split(r"[/: ]", self.data[user_index]["Ends at"])
            new_date = datetime.datetime(
                int(self.date[0]),
                int(self.date[1]),
                int(self.date[2]),
                int(self.date[3]),
                int(self.date[4]),
            )
            new_date += datetime.timedelta(days=sub_days)
            self.data[user_index]["Ends at"] = new_date.strftime("%Y/%m/%d %H:%M")
            self.data[user_index]["Payments"].append(
                (date_now.strftime("%Y/%m/%d"), price)
            )
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
            self.data.append(new_user)

    def delete_subscription(self, email):
        user_index, flag = self.if_exist(email)
        if flag:
            self.data.pop(user_index)
        else:
            print("User not exist!!")

    def check_expire(self):
        self.soon = []
        for i in range(len(self.data)):
            # date_start = re.split(r"[/: ]", data[i]["Started"])
            # s_ = datetime.datetime(
            #     int(date_start[0]), int(date_start[1]), int(date_start[2]), int(date_start[3]), int(date_start[4])
            # )
            date_end = re.split(r"[/: ]", self.data[i]["Ends at"])
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
                self.soon.append(data[i])

        return self.soon

    def write_json(self):
        json.dump(self.data, open(self.data_file_name, "w"))


# date_now = datetime.date.today()
# # days_in_current_month = calendar.monthrange(date_now.year, date_now.month)[1]
# # days_left_current_month = days_in_current_month - date_now.day

# subs = 60


# print(json.dumps(x, indent=2))


if __name__ == "__main__":
    # new_subscription("test@someting.com", "user1", 5,190)
    s = Subs_record("data.json")
    s.new_subscription("test2@someting.com", "user2", 10, 100)
    s.write_json()
    print(json.dumps(s.data, indent=2))
    print()
    # # delete_subscription("test@someting.com")
    # write_json(data)
