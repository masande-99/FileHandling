from tkinter import *


def make_file():

    root = Tk()
    root.title("text files")
    root.geometry("1000x500")
    root.configure(bg='blue')

    first_frame = Frame(root)
    first_frame.pack()
    first_frame.configure(bg="blue")

    second_frame = Frame(root)
    second_frame.pack()
    second_frame.configure(bg='blue')

    third_frame = Frame(root)
    third_frame.pack()

    fourth_frame = Frame(root)
    fourth_frame.pack()

    first_label = Label(first_frame, text="My weekend activities")
    first_label.grid(row=1, column=0)

    first_entry = Entry(second_frame)
    first_entry.grid(row=1, column=1, padx=100, pady=100, ipady=100, ipadx=200)

    def create_text():
        file = open("hey.txt", "w+")
        file.write(first_entry.get())
        file.close()

    crt_txt = Button(third_frame, text="Create file", command=create_text)
    crt_txt.grid(row=2, column=0)
    crt_txt.configure(bg="orange")

    def display_text():
        with open("/home/lifechoices/Documents/handle_files/hey.txt", "r") as file:
            data = file.read()
            first_entry.delete(0, END)  # Remove previous content
            first_entry.insert(END, data)

    my_txt = Button(third_frame, text="Display text", command=display_text)
    my_txt.grid(row=2, column=1)
    my_txt.configure(bg="lime")

    def clear_btn():
        first_entry.delete(0, END)

    clr_data = Button(third_frame, text="Clear", command=clear_btn)
    clr_data.grid(row=2, column=3)
    clr_data.configure(bg="navy")

    def exit_btn():
        root.destroy()

    ext = Button(third_frame, text="Exit", command=exit_btn)
    ext.grid(row=2, column=4)
    ext.configure(bg="red")

    def my_btn():

        file = open('hey.txt', 'a')
        for line in first_entry.get():
            file.write(line)

    my_data = Button(third_frame, text="Append data", command=my_btn)
    my_data.grid(row=2, column=2)
    my_data.configure(bg="yellow")

    root.mainloop()


make_file()
