import os,sys
import glob
import random
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#指定したフォルダの中に存在するファイルをランダムに開くソフト
#フォルダの指定
def folder_select():
    global folder
    global folder_path
    #ファイルパスの取得
    initdir = os.path.abspath(os.path.dirname(__file__))
    #親ディレクトリを指定
    folder = filedialog.askdirectory(initialdir = initdir)
    folder_path.set(folder)

#何の画像もしくは動画もしくはファイル全般を開くか選択
#forとか使えばもっとすっきりする気がする…
def searching_file():
    global files_i_want
    global element_count
    if checked1.get() == 1:
        if checked2.get() == 4:
            folder_a = folder + "/**"
            folder_b = folder_a + "/*.jpg"
            files_i_want_a = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.jpeg"
            files_i_want_b = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.png"
            files_i_want_c = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.gif"
            files_i_want_d = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.bmp"
            files_i_want_e = glob.glob(folder_b, recursive=True)
            files_i_want = files_i_want_a + files_i_want_b + files_i_want_c + files_i_want_d + files_i_want_e
            element_count = len(files_i_want)
        else:
            folder_b = folder + "/*.jpg"
            files_i_want_a = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.jpeg"
            files_i_want_b = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.png"
            files_i_want_c = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.gif"
            files_i_want_d = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.bmp"
            files_i_want_e = glob.glob(folder_b, recursive=True)
            files_i_want = files_i_want_a + files_i_want_b + files_i_want_c + files_i_want_d + files_i_want_e
            element_count = len(files_i_want)
    elif checked1.get() == 2:
        if checked2.get() == 4:
            folder_a = folder + "/**"
            folder_b = folder_a + "/*.avi"
            files_i_want_a = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.mp4"
            files_i_want_b = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.mpg"
            files_i_want_c = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.mpeg"
            files_i_want_d = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.mov"
            files_i_want_e = glob.glob(folder_b, recursive=True)
            folder_b = folder_a + "/*.wmv"
            files_i_want_f = glob.glob(folder_b, recursive=True)
            files_i_want = files_i_want_a + files_i_want_b + files_i_want_c + files_i_want_d + files_i_want_e + files_i_want_f
            element_count = len(files_i_want)
        else:
            folder_b = folder + "/*.avi"
            files_i_want_a = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.mp4"
            files_i_want_b = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.mpg"
            files_i_want_c = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.mpeg"
            files_i_want_d = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.mov"
            files_i_want_e = glob.glob(folder_b, recursive=True)
            folder_b = folder + "/*.wmv"
            files_i_want_f = glob.glob(folder_b, recursive=True)
            files_i_want = files_i_want_a + files_i_want_b + files_i_want_c + files_i_want_d + files_i_want_e + files_i_want_f
            element_count = len(files_i_want)
    elif checked1.get() == 3:
        if checked2.get() == 4:
            folder_a = folder + "/**"
            folder_b = folder_a + "/*"
            files_i_want = glob.glob(folder_b, recursive=True)
            element_count = len(files_i_want)
        else:
            folder_b = folder + "/*"
            files_i_want = glob.glob(folder_b, recursive=True)
            element_count = len(files_i_want)
    else:
        messagebox.showerror("Error", "エラーですよ。")

#選択されたデータを開く
def open_file():
    a_file_i_want = random.randint(0, element_count)
    openpen_file = files_i_want[a_file_i_want]
    subprocess.Popen([ openpen_file ], shell=True)

#以下tkinterによるGUI
#allのチェックボックスを選択したら画像もしくは動画のチェックボックスは選べない
def choose():
    if checked1.get() == 3:
        image_chk.configure(state = 'disable')
        movie_chk.configure(state = 'disable')
    else:
        image_chk.configure(state = 'enable')
        movie_chk.configure(state = 'enable')

#ソフトのタイトル、サイズ
root = Tk()
root.title("file-random")
root.geometry("500x200")
root.resizable(False, False)

#ウィジェット（枠、ボタン）の作成
frame1 = ttk.Frame(root, padding=10)
frame2 = ttk.Frame(root, padding=10)
frame3 = ttk.Frame(root, padding=15)
label1 = ttk.Label(frame1, text = "フォルダ選択", foreground = '#000000', background = '#FFCCFF')
label2 = ttk.Label(frame2, text = "ファイル種類選択", foreground = '#000000', background = '#FFCCFF')
folder_path = StringVar()
entry1 = ttk.Entry(frame1, textvariable = folder_path, width = 50)
button1 = ttk.Button(frame1, text="【フォルダ参照】", command = folder_select)
button2 = ttk.Button(frame3, text="ファイルを選ぶ", command = searching_file)
button3 = ttk.Button(frame3, text="ファイルを開く", command = open_file)

#チェックボックスの作成
#チェックボックスのグループ1
checked1 = IntVar()
checked1.set(0)
image_chk = ttk.Checkbutton(frame2, text = '.jpg,jpeg,png,gif,bmp', variable = checked1, onvalue = 1, command = choose)
movie_chk = ttk.Checkbutton(frame2, text = '.avi,mp4,mpg,mpeg,mov,wmv', variable = checked1, onvalue = 2, command = choose)
all_chk = ttk.Checkbutton(frame2, text = "all", variable = checked1, onvalue = 3, command = choose)
#チェックボックスのグループ2
checked2 = IntVar()
checked2.set(0)
subfolder = ttk.Checkbutton(frame3, text = 'サブフォルダを含める', variable = checked2, onvalue = 4)

#レイアウト
frame1.grid(padx = 10, pady = 15, sticky = W+E)
frame2.grid(padx = 10, sticky = W+E)
frame3.grid(padx = 90.5, pady = 5, sticky = W+E)
label1.pack(side = LEFT)
label2.pack(side = LEFT)
entry1.pack(side = LEFT)
image_chk.pack(side = LEFT)
movie_chk.pack(side = LEFT)
all_chk.pack(side = LEFT)
subfolder.grid(column=0, row=6)
button1.pack(side = LEFT)
button2.grid(column=2, row=6)
button3.grid(column=4, row=6)

#以上の機能を備えたソフトの起動
root.mainloop()
