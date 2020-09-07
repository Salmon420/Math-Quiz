self.entry_label_1 = Label(text="numbers between", font="Arial 10",
                           bg="#F4F6FC", padx=10, pady=1)
self.entry_label_1.grid(row=1)

self.low_num_entry = Entry(self.entry_frame, width=2,
                           font="Arial 10 bold", bg="white")
self.low_num_entry.grid(row=1, column=1)

self.entry_label_2 = Label(self.entry_frame, text="and",
                           font="Arial 10", bg="#F4F6FC",
                           padx=10, pady=1)
self.entry_label_2.grid(row=1, column=2)

self.high_num_entry = Entry(self.entry_frame, width=2,
                            font="Arial 10 bold", bg="white")
self.high_num_entry.grid(row=1, column=3)

self.entry_label_2 = Label(self.entry_frame, text="Amount Of Questions",
                           font="Arial 10", bg="#F4F6FC",
                           padx=10, pady=1)
self.entry_label_2.grid(row=5, columnspan=5)

self.cho_num_entry = Entry(self.entry_frame, width=2,
                           font="Arial 10 bold", bg="white")
self.cho_num_entry.grid(row=6, column=2)

