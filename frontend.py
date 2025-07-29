
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter.font import Font
from tkinter.filedialog import askopenfilename, asksaveasfilename
import NotyBackend
import pkg_resources
from symspellpy import SymSpell, Verbosity

root = Tk()

# ================================= Variables ================================= #
title_txt = StringVar()
title_txt.set("New Note")
ed = BooleanVar()
Id = IntVar()
ed.set(True)
bt = ttk.Button
search_entry = StringVar()
defaultFont = ("Hevletica", "10", "normal")
txtFont = Font(font=defaultFont)
tagId = IntVar()   #For text formating
tagId.set(1)

# ================================= App_Settings ================================= #

# root.geometry("700x470")  # 700x470 _ Base Geometry
NotyTitle = "Noty -- V1.3"
root.title(NotyTitle)
root.minsize(width=700, height=470)

color = StringVar(value=NotyBackend.view_2()[2])
root.configure(bg=color.get())
p1 = PhotoImage(file='Note.png')
root.iconphoto(True, p1)


# ================================= Frames ================================= #
f1 = Frame(root, width=50, height=470, bg=color.get())
f1.pack(side=LEFT, fill=Y)
f2 = Frame(root, width=700, height=50, bg=color.get())
f2.pack(fill=BOTH, pady=7)
f3 = Frame(root, width=700, height=50, bg=color.get())
f3.pack(fill=BOTH, pady=7)
f4 = Frame(root, width=700, height=330, bg=color.get())
f4.pack(fill=BOTH, expand=1)
f5 = Frame(root, width=700, height=30, bg=color.get())
f5.pack(side=TOP, fill=BOTH)

# ================================= Normal Function  ================================= #

def save_note():
    if ed.get():
        got_title = title_txt.get()
        got_main_txt = txt_box.get(0.0, END)
        unvalidTitles = []
        for i in NotyBackend.view():
            unvalidTitles.append(i[1])
        if (got_main_txt != "\n") and ((got_title != "") and got_title not in unvalidTitles):
            NotyBackend.insert(got_title, got_main_txt)

        elif got_title == "" or got_main_txt == "\n":
            tkinter.messagebox.showerror("ERROR!", "Cant save blank note or blank title!!")
        else: tkinter.messagebox.showerror("Erro!r", "There is a note with the same title!!")

    else:
        NotyBackend.update(Id.get(), txt_box.get(0.0, END))
        e1.config(state="normal")
        ed.set(True)
        tkinter.messagebox.showinfo("Good to now!!", "Internal save was successful!!")
        clear_all()


def clear_all():
    txt_box.delete(0.0, END)
    title_txt.set("")


def add_new_note():
    warningMessage = tkinter.messagebox.askyesno("Warnning!",
                                    "Are you sure you want to add a new note? your current note won't be saved!")
    if warningMessage:
        ed.set(True)
        clear_all()
        title_txt.set("New Added Note")
        root.title(NotyTitle)


def ctrl_s(event=None):
    save_note()


def open_from():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], )
    if not filepath:
        return
    txt_box.delete(1.0, END)
    try:
        with open(filepath, mode="rt") as input_file:
            text = input_file.read()
            txt_box.insert(END, text)
    except UnicodeDecodeError:
        with open(filepath, mode="rb") as input_file:
            text = input_file.read()
            txt_box.insert(END, text)
    except:
        tkinter.messagebox.showerror("Open Error!", "Couldn't Open The File!")
    root.title(f"NOTY - {filepath}")


def save_as():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_box.get(1.0, END)
        output_file.write(text)
    root.title(f"Noty - {filepath}")


def find():
    # remove tag 'found' from index 1 to END
    txt_box.tag_remove('found', '1.0', END)

    # returns to widget currently in focus
    theText = search_entry.get()

    if (theText):
        idx = '1.0'
        while 1:
            # searches for desried string from index 1
            idx = txt_box.search(theText, idx, nocase=1,
                                 stopindex=END)


            if not idx: break

            # last index sum of current index and
            # length of text
            lastidx = '% s+% dc' % (idx, len(theText))

            # overwrite 'Found' at idx
            txt_box.tag_add('found', idx, lastidx)
            idx = lastidx

            # mark located string as blue

        txt_box.tag_config('found', background='blue')

def font_options(use):
    '''Possible inputs of USE: bold, italic, size, restoreall'''
    selectedIdx = txt_box.tag_ranges(SEL)
    tagName = "fText" + "_" + str(tagId.get())
    selectedTxt = txt_box.tag_add(tagName, selectedIdx[0], selectedIdx[1])
    if use == "bold":
        txtFont.config(weight='bold')
        txt_box.tag_config(tagName, font=txtFont.actual())
        tagId.set(tagId.get() + 1)
        txtFont.config(family=defaultFont[0], size=defaultFont[1], weight=defaultFont[2])













    # if use == 0:
    #     def italic():
    #
    #         fb.set(fb.get() + " italic")
    #         txt_box.configure(font=fb.get())
    #
    #     italic()
    # elif use == 1:
    #     def bold():
    #         fb.set(fb.get() + " bold")
    #         txt_box.configure(font=fb.get())
    #     bold()
    # elif use == 2:
    #     a = fb.get().split(" ")
    #     b = a.pop(1)
    #     if op.get() == 1:
    #         c = a.insert(1, "10")
    #     elif op.get() == 2:
    #         c = a.insert(1, "15")
    #     elif op.get() == 3:
    #         c = a.insert(1, "20")
    #     elif op.get() == 4:
    #         c = a.insert(1, "25")
    #     elif op.get() == 5:
    #         c = a.insert(1, "30")
    #     d = " ".join(a)
    #     fb.set(d)
    #     txt_box.config(font=fb.get())
    # elif use == 3:
    #         fb.set("Helvetica 10")
    #         txt_box.configure(font=fb.get())


def txt_justify(po):
    try:
        tagname = str(txt_box.tag_ranges(SEL))
        txt_box.tag_add(tagname, SEL_FIRST + " linestart", SEL_LAST + " lineend")
        if po == "center":
            txt_box.tag_configure(tagname, justify=CENTER)
        if po == "right":
            txt_box.tag_configure(tagname, justify=RIGHT)
        if po == "left":
            txt_box.tag_configure(tagname, justify=LEFT)
    except: pass


def txt_corrector():
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    dictionary_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_dictionary_en_82_765.txt")
    bigram_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_bigramdictionary_en_243_342.txt")
    # term_index is the column of the term and count_index is the
    # column of the term frequency
    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
    sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

    # lookup suggestions for multi-word input strings (supports compound
    # splitting & merging)
    input_term = (txt_box.get(0.0, END))
    # max edit distance per lookup (per single word, not per whole input string)
    suggestions = sym_spell.lookup_compound(input_term, max_edit_distance=2)
    # display suggestion term, edit distance, and term frequency
    for suggestion in suggestions:
        txt_box.replace(0.0, END,  suggestion)

# ================================= Window Function  ================================= #

def setting():
    """
    This is the setting part wich The user can change some of the application's characterestics.
    """
    global se, tbbgColor
    se = Toplevel()

    se.attributes("-topmost", True)
    root.attributes("-disabled", True)

    se.configure(bg=color.get())
    se.resizable(height=False, width=False)
    se.geometry("400x500")
    se.title("Settings")
    #################### TextBox Background ####################
    colors = ["red", "pink", "gray", "white"]
    tbbgColor = NotyBackend.view_2()[1]
    tbbg_lbl = Label(se, text="TextBox Background : ", bg=color.get())
    tbbg_lbl.place(x=10, y=20)
    tbbg_combo = ttk.Combobox(se, values=colors)
    tbbg_combo.set("Select Color!")
    tbbg_combo.place(x=150, y=20)
    def set_tbbg_background():
        if tbbg_combo.current() != -1:
            tbbgColor = colors[tbbg_combo.current()]
            txt_box.configure(bg=tbbgColor)
            NotyBackend.replace(tbbgColor)
    tbbg_btn = bt(se, text="Apply", command=set_tbbg_background)
    tbbg_btn.place(x=310, y=20)

    #################### Background Color ####################
    bg_color_lbl = Label(se, text="Background Color : ", bg=color.get())
    bg_color_lbl.place(x=10, y =100)
    bg_color_combo = ttk.Combobox(se, values=colors)
    bg_color_combo.set("Select Background Color!")
    bg_color_combo.place(x=150, y=100)
    def set_background_color():
        if bg_color_combo.current() != -1:
            NotyBackend.replace(bg=colors[bg_color_combo.current()])
            tkinter.messagebox.showinfo("Settings", message="You Must Restart The App To Apply The Option!")
    bg_color_btn = bt(se, text="Apply", command=set_background_color)
    bg_color_btn.place(x=310, y=100)

    setting_lbl = Label(se, text="This is a beta mode for the settings of Noty Project so a lot of\noptions will be impelimented soon later.", bg=color.get())
    setting_lbl.place(x=30, y=380)
    se.bind("<Destroy>", lambda event=None: root.attributes("-disabled", False))

def note_select():
    nSWindow = Toplevel()

    nSWindow.attributes("-topmost", True)
    root.attributes("-disabled", True)

    nSWindow.title("Notes")
    nSWindow.geometry("400x400")
    nSWindow.configure(bg=color.get())
    nSWindow.resizable(width=False, height=False)
    search_l = Label(nSWindow, text="Search Note : ", bg=color.get())
    search_l.grid(row=0, column=0, pady=5)
    search_e = Entry(nSWindow, width=20)
    search_e.grid(row=0, column=1, padx=6, pady=5)

    li_box_1 = Listbox(nSWindow, width=40, height=22)
    li_box_1.grid(row=1, column=0, columnspan=60)
    nSWindow.bind("<Destroy>", lambda event=None: root.attributes("-disabled", False))

    def view_all():
        global saveid
        search_e.delete(0, END)
        li_box_1.delete(0, END)
        notes = NotyBackend.view()
        saveid = {}
        order = 1
        for note in notes:
            saveid[note[1]] = note[0]
            li_box_1.insert(END, (order,"--", note[1]))
            order += 1
        order = 1
    def get_row_by_index(event=None):
        if len(li_box_1.curselection()) > 0:
            index = li_box_1.curselection()[0]
            return index
    def get_row_by_id(event=None):
        if len(li_box_1.curselection()) > 0:
            index = li_box_1.curselection()[0]
            selected = saveid[li_box_1.get(index)[2]]
            return selected


    def delete_note():
        sel = get_row_by_id()
        NotyBackend.delete(sel)
        view_all()

    def edit():
        global Id
        note = NotyBackend.view()
        sel = get_row_by_index()
        title_txt.set(note[sel][1])
        e1.config(state="readonly")
        txt_box.delete(0.0, END)
        txt_box.insert(0.0, note[sel][2])
        ed.set(False)
        Id.set(note[sel][0])
        nSWindow.destroy()

    def search_note():
        global saveid
        li_box_1.delete(0, END)
        title = "%" + search_e.get() + "%"
        if len(NotyBackend.search(title)) > 0:
            se = NotyBackend.search(title)
            saveid = {}
            order = 1
            for note in se:
                saveid[note[1]] = note[0]
                print(saveid)
                li_box_1.insert(END, (order,"--", note[1]))
                order += 1
            order = 1

    search_b = bt(nSWindow, text="Go..", width=6, command=search_note)
    search_b.grid(row=0, column=2, pady=5)

    li_box_1.bind("<Button-1>", get_row_by_index)
    li_box_1.bind("<Button-1>", get_row_by_id)

    btn1 = bt(nSWindow, text="View All", width=15, command=view_all)
    btn1.place(x=270, y=50)
    btn2 = bt(nSWindow, text="Delete", width=15, command=delete_note)
    btn2.place(x=270, y=140)
    btn3 = bt(nSWindow, text="Load", width=15, command=edit)
    btn3.place(x=270, y=230)
    view_all()
    nSWindow.mainloop()


def about_us():
    au = Toplevel()

    au.attributes("-topmost", True)
    root.attributes("-disabled", True)

    au.title("About Us")
    au.resizable(width=False, height=False)
    au.geometry("300x300")
    au.configure(bg=color.get())
    canvas = Canvas(au, width=90, height=90, bd=10, bg="white")
    canvas.pack()
    img = PhotoImage(file='Note.png')
    canvas.create_image(7, 0, anchor=NW, image=img)
    au_la1 = Label(au,
                   text="Noty is a simple note editor that is provided by python.\n for more information about this project got to \'www.py\n-prog.blogfa.com\'.", bg=color.get())
    au_la1.pack(pady=10)
    au_la2 = Label(au, text="Provided by Mahan Mossavi\n\n©All rights reserved 2025", bg=color.get())
    au_la2.pack(pady=10)
    au.resizable(width=False, height=False)
    au.bind("<Destroy>", lambda event=None: root.attributes("-disabled", False))
    au.mainloop()

def font_select_win():
    fsw = Toplevel()

    fsw.attributes("-topmost", True)
    root.attributes("-disabled", True)

    fsw.geometry("500x500")
    fsw.bind("<Destroy>", lambda event=None: root.attributes("-disabled", False))
    fsw.mainloop()

# ================================= Lables  ================================= #
l1 = Label(f3, text="Note Title : ", bg=color.get(), font="Helvetica 11 bold")
l1.pack(side=LEFT, fill=X, expand=0)

# ================================= Entries ================================= #
helv10 = Font(family="Helvetica", size=10, weight="bold")
e1 = Entry(f3, width=30, textvariable=title_txt, font=helv10)
e1.pack(side=LEFT, fill=X, expand=0, padx=10)

e2 = Entry(f3, width=30, textvariable=search_entry)
e2.pack(side=RIGHT, fill=X, expand=0, padx=10)

# ================================= ScrollBars  ================================= #
scb1 = Scrollbar(f1)
scb1.pack(side=LEFT, fill=Y)


scb2 = Scrollbar(f5, orient=HORIZONTAL)
scb2.pack(side=BOTTOM, fill=X)
# ================================= Main Text Box  ================================= #
txt_box = Text(f4, background="white", width=95, height=22, wrap=WORD)
txt_box.pack(fill=BOTH, expand=1)
txt_box.bind("<Control-s>", ctrl_s)


txt_box.configure(yscrollcommand=scb1.set)
scb1.configure(command=txt_box.yview)

txt_box.configure(xscrollcommand=scb2.set)
scb2.configure(command=txt_box.xview)

txt_box.configure(bg=NotyBackend.view_2()[1])
# ================================= Main Menu  ================================= #
main_menu = Menu(root)

main_menu.add_command(label="Note Select", command=note_select)

main_menu.add_command(label="About Us", command=about_us)

txt_config_menu = Menu(main_menu, tearoff=0)

txt_config_menu.add_command(label="Font", command=font_select_win)

txt_config_menu.add_command(label="Bold", command=lambda : font_options("bold"))
txt_config_menu.add_command(label="Italic", command=lambda : font_options("italic"))

font_size_menu = Menu(txt_config_menu, tearoff=0)
op = IntVar()
fontsizeLabels = ["10", "15", "20", "25", "30"]

for i in range(5):
    font_size_menu.add_radiobutton(label=fontsizeLabels[i], value=i+1, variable=op, command=lambda : font_options("size"))

txt_config_menu.add_cascade(menu=font_size_menu, label="Font Size")
txt_config_menu.add_separator()
txt_config_menu.add_command(label="Restore All", command=lambda : font_options("restoreall"))
txt_config_menu.add_separator()
txt_config_menu.add_command(label="More(Coming soon)...", state="disabled")

main_menu.add_cascade(menu=txt_config_menu, label="Options")

main_menu.add_command(label="Settings", command=setting)


main_menu.add_command(label="Exit", command=root.destroy)


root.config(menu=main_menu)


# ================================= Buttons  ================================= #

btn_1 = bt(f2, text="Internal Save", width=12, command=save_note)
btn_1.pack(side=LEFT, fill=X, padx=10)

btn_2 = bt(f2, text="Clear All", width=12, command=clear_all)
btn_2.pack(side=LEFT, fill=X, padx=10)

btn_3 = bt(f3, text="Search...", width=12, command=find)
btn_3.pack(side=RIGHT, fill=X, padx=10)

btn_4 = bt(f2, text="Add New", width=12, command=add_new_note)
btn_4.pack(side=LEFT, fill=X, padx=10)


btn_5 = bt(f2, text="Open...", width=12, command=open_from)
btn_5.pack(side=LEFT, fill=X, padx=10)

btn_6 = bt(f2, text="Save As...", width=12, command=save_as)
btn_6.pack(side=LEFT, fill=X, padx=10)

btn_7 = bt(f2, text="Correct Text", width=12, command=txt_corrector)
btn_7.pack(side=LEFT, fill=X, padx=10)

# ================================= Justify_Buttons  ================================= #
center_btn = bt(f2, text="L", width=2, command=lambda: txt_justify("left"))
center_btn.pack(side=LEFT)
center_btn = bt(f2, text="C", width=2, command=lambda: txt_justify("center"))
center_btn.pack(side=LEFT)
center_btn = bt(f2, text="R", width=2, command=lambda: txt_justify("right"))
center_btn.pack(side=LEFT)




root.mainloop()
