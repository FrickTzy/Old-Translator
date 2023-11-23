from tkinter import *
from tkinter import ttk
from Translate import Translate
from Errors import SameLanguageError
import Music

switch = ""
scale_on = False

convert_lang = {
    "Auto": "",
    "English": "Eng",
    "Filipino": "Fil",
    "Japanese": "Jap"
}
# heh

convert_lang_to = {
    "English": Translate.jap,
    "Filipino": Translate.fil,
    "Japanese": Translate.jap
}


class Language:
    @staticmethod
    def change_lang(event):
        lang.set(drop_down.get())
        translate_result()

    @staticmethod
    def change_lang_result(event):
        lang_result.set(drop_down_for_result.get())
        translate_result()


def translate_result(event=None):
    lang_arg = convert_lang.get(lang.get(), "")
    word = input_word.get()
    lang_resultz = lang_result.get()
    lang_func = convert_lang_to.get(lang_resultz)
    if word != "":
        try:
            translated_result = lang_func(word, lang_arg)
        except SameLanguageError:
            translated_result = "Same Language! Please Try Again"
        except:
            translated_result = "Unknown Word!"
        result.config(text=translated_result, fg="black")
    else:
        result.config(text="Translating", fg="#757575")


def change_song_name(var: bool = False):
    global switch
    if var:
        song_name.set(Music.set_song_title())
    else:
        if Music.switch != switch:
            song_name.set(Music.set_song_title())
            switch = Music.switch
    window.after(1, change_song_name)


def change_logo():
    if Music.play:
        pause_button.config(image=pause_image)
    else:
        pause_button.config(image=play_image)


def change_vol():
    Music.change_volume(volume_scale.get())
    window.after(1, change_vol)


def show_scale(event=None):
    global scale_on
    if scale_on:
        volume_scale.place_forget()
        scale_on = False
        window.unbind("<Up>")
        window.unbind("<Down>")
    else:
        volume_scale.place(x=890, y=10)
        scale_on = True
        window.bind("<Up>", lambda eventz: volume_scale.set(volume_scale.get() + 0.1))
        window.bind("<Down>", lambda eventz: volume_scale.set(volume_scale.get() - 0.1))
        change_vol()


window = Tk()
Logo = PhotoImage(file="Images\\Ringo-chan_png.png")

window.title("Ringo Translator")
window.geometry("1000x600")
window.config(bg="#6f5ee0")
window.iconphoto(True, Logo)

top_frame = Frame(window, bg="#2b0342", width=1000, height=90)
music_frame = Frame(top_frame, width=400, height=100, bg="#2b0342")

lang_options = ["Auto", "Japanese", "English", "Filipino"]

lang = StringVar()
lang.set("Auto")

song_name = StringVar()
song_name.set(Music.set_song_title())

lang_result = StringVar()
lang_result.set("Japanese")

logo_image = PhotoImage(file="Images\\TranslatorLogo.png")
pause_image = PhotoImage(file="Images\\PauseButton.png")
play_image = PhotoImage(file="Images\\PlayButton.png")
next_image = PhotoImage(file="Images\\NextButton.png")
previous_image = PhotoImage(file="Images\\PreviousButtonz.png")
volume_image = PhotoImage(file="Images\\Volume.png")

logo_label = Label(top_frame, image=logo_image, bg="#2b0342")

style = ttk.Style()
style.theme_use("clam")
style.configure('TCombobox',
                background="white",
                fieldbackground="white",

                foreground="black",
                darkcolor="black",
                selectbackground="black",
                lightcolor="black",
                )

drop_down = ttk.Combobox(window,
                         values=lang_options)

drop_down.current(0)
drop_down.bind("<<ComboboxSelected>>", Language.change_lang)

lang_options.pop(0)

drop_down_for_result = ttk.Combobox(window,
                                    values=lang_options)

drop_down_for_result.current(0)
drop_down_for_result.bind("<<ComboboxSelected>>", Language.change_lang_result)

pause_button = Button(music_frame,
                      image=pause_image,
                      command=lambda: [Music.play_music(),
                                       change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342", )

next_button = Button(music_frame,
                     image=next_image,
                     command=lambda: [Music.change_music(window, True),
                                      change_song_name(True), change_logo()],
                     bg="#2b0342",
                     bd=0,
                     activebackground="#2b0342",
                     )

previous_button = Button(music_frame,
                         image=previous_image,
                         command=lambda: [Music.change_music(window, False),
                                          change_song_name(True), change_logo()],
                         bg="#2b0342",
                         bd=0,
                         activebackground="#2b0342",
                         )

volume_scale = Scale(window,
                     from_=1,
                     to=0,
                     length=70,
                     resolution=0.1,
                     fg="white",
                     background="#2b0342",
                     troughcolor="white",
                     bd=0,
                     highlightthickness=0,
                     sliderrelief='flat',
                     sliderlength=12
                     )

volume_scale.set(0.8)

volume_button = Button(music_frame,
                       image=volume_image,
                       command=show_scale,
                       bg="#2b0342",
                       bd=0,
                       activebackground="#2b0342", )

increase_volume = Button(music_frame, text="Increase Volume", command=lambda: Music.change_volume(True))
decrease_volume = Button(music_frame, text="Decrease Volume", command=lambda: Music.change_volume(False))

song_title = Label(music_frame, textvariable=song_name, bg="#2b0342", fg="white", font=("Ariel", 15), width=14,
                   anchor="n")

input_word = Entry(window,
                   bg="white",
                   font=("Calibri", 50),
                   width=27,
                   borderwidth=3,
                   relief="solid",
                   )
input_word.bind("<Return>", translate_result)

button = Button(window,
                text="Translate",
                command=translate_result,
                borderwidth=3,
                font=("Ariel", 8),
                relief="solid",
                fg="black",
                bg="white",
                activeforeground="#757575",
                width=35, height=5)

result = Label(window,
               width=96,
               height=5,
               borderwidth=3,
               relief="solid",
               text="Translating",
               fg="#757575",
               )

logo_label.place(x=-20, y=-53)
music_frame.place(x=680, y=16)
next_button.place(x=99, y=18)
previous_button.place(x=20, y=18)
song_title.place(x=0, y=-3)
pause_button.place(x=61, y=18)
volume_button.place(x=250, y=-13)

input_word.place(x=40, y=140)
button.place(x=744, y=290)
result.place(x=40, y=290)
drop_down.place(x=40, y=250)
drop_down_for_result.place(x=40, y=400)
top_frame.place(x=0, y=0)

Music.music(window)
change_song_name()

window.mainloop()
