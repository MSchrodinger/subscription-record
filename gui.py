from tkinter import *


class Table:
    def __init__(self, window, list_columns, list_table):
        rows = len(list_table)
        columns = len(list_columns)
        for k in range(columns):
            self.e = Entry(window, width=20, fg="blue", font=("Arial", 16, "bold"))
            self.e.grid(row=0, column=k)
            self.e.insert(END, list_columns[k])

        for i in range(rows):
            for j in range(columns):

                self.e = Entry(window, width=20, fg="blue", font=("Arial", 16, "bold"))
                self.e.grid(row=i + 1, column=j)
                self.e.insert(END, list_table[i][list_columns[j]])


def donothing(root):
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


class Menubar:
    # menulist = [("File",["save","open"]), ("About",["save","open"])]

    def __init__(self, window, list_commands):
        self.menu_bar = Menu(window)
        for i in range(len(list_commands)):
            self.menu_ = Menu(self.menu_bar, tearoff=0)
            for j in range(len(list_commands[i][1])):
                self.menu_.add_command(
                    label=list_commands[i][1][j], command=lambda: print(j)
                )
            self.menu_bar.add_cascade(label=list_commands[i][0], menu=self.menu_)
        window.config(menu=self.menu_bar)

    def menu_comands(self, str_, window):
        if str_ == "Exit":
            window.quit()
        else:
            donothing(window)


if __name__ == "__main__":

    # Scroll_bar = Scrollbar(top)
    lst = [
        {
            "Email": "test@someting.com",
            "UserName": "user1",
            "Days": 10,
            "Started": "2020/05/17 16:07",
            "Ends at": "2020/05/21 16:07",
        }
    ]
    lst2 = ["Email", "UserName", "Days", "Started", "Ends at"]
    menulist = [("File", ["save", "open", "Exit"]), ("About", ["About"])]

    top = Tk()
    menu_bar = Menubar(top, menulist)

    # menubar = Menu(top)
    # filemenu = Menu(menubar, tearoff=0)
    # filemenu.add_command(label="New", command=donothing(top))
    # filemenu.add_command(label="Open", command=donothing(top))
    # filemenu.add_command(label="Save", command=donothing(top))
    # filemenu.add_command(label="Save as...", command=donothing(top))
    # filemenu.add_command(label="Close", command=donothing(top))

    # filemenu.add_separator()

    # filemenu.add_command(label="Exit", command=top.quit)
    # menubar.add_cascade(label="File", menu=filemenu)
    # top.config(menu=menubar)

    # top_frame = Frame(top)
    # top_frame.pack()

    # mid_frame = Frame(top)
    # mid_frame.pack(side=BOTTOM)

    # x = Menubar(top, menulist)
    # t = Table(mid_frame, lst2, lst)

    top.mainloop()
