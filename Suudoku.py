import tkinter
from tkinter import *
import copy
import tkinter.simpledialog as sd
from tkinter import ttk


def changePage(page):
    page.tkraise()


def sample1():
    global ban, ans
    ans = copy.deepcopy(ban)
    ShowGamen()


def ShowGamen():
    global ban, ans
    for i in range(10):
        if i % 3 == 0:
            canvas.create_line(w, h + i * Nagasa, w + 9 * Nagasa, h + i * Nagasa, fill='black', width=2.0)
            canvas.create_line(w + i * Nagasa, h, w + i * Nagasa, h + 9 * Nagasa, fill='black', width=2.0)
        else:
            canvas.create_line(w, h + i * Nagasa, w + 9 * Nagasa, h + i * Nagasa, fill='black')
            canvas.create_line(w + i * Nagasa, h, w + i * Nagasa, h + 9 * Nagasa, fill='black')

    for i in range(9):
        for j in range(9):
            if ban[j][i] > 0:
                canvas.create_text(w + (i + 0.5) * Nagasa, h + (j + 0.5) * Nagasa, text=str(ban[j][i]), font=Font1,
                                   fill=Color1)
            elif ans[j][i] > 0:
                canvas.create_rectangle(w + i * Nagasa + 1.5, h + j * Nagasa + 1.5, w + i * Nagasa + 43.5,
                                        h + j * Nagasa + 43.5, fill='floral white', outline='floral white')
                canvas.create_text(w + (i + 0.5) * Nagasa, h + (j + 0.5) * Nagasa, text=str(ans[j][i]), font=Font1,
                                   fill=Color2)


def buttonPress(e):
    global ban, ans
    x = e.x
    y = e.y
    i = int((x - w) / Nagasa)
    j = int((y - h) / Nagasa)
    if i >= 0 and i < 9 and j >= 0 and j < 9:
        if ban[j][i] == 0:
            canvas.create_rectangle(w + i * Nagasa + 1.5, h + j * Nagasa + 1.5, w + i * Nagasa + 43.5,
                                    h + j * Nagasa + 43.5, fill='peach puff', outline='peach puff')
            suuji = '1〜9の数字を入力'
            result = sd.askinteger('数値入力', suuji)
            ans[j][i] = int(result)
            ShowGamen()


def btn_click():
    if ans != kaitou:
        tkinter.messagebox.showinfo('不正解', '答えが間違えています！頑張りましょう！')
    else:
        tkinter.messagebox.showinfo('正解', 'よくできました！おめでとうございます！')


ban = []
ans = []
Font1 = 'Courier 24'
Font2 = 'courier 12'
Color1 = 'black'
Color2 = 'red'
board_size = 500
Bunkatu = 9
Nagasa = w = h = board_size / (Bunkatu + 2)

root = Tk()
root.title('楽しい数独')
root.geometry("500x550")
style = ttk.Style()
style.configure('.', font=('', 20))

# 1x1表示にする
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# 画面作成
frame_title = ttk.Frame(root)
frame_login = ttk.Frame(root)
frame_easy = ttk.Frame(root)
frame_normal = ttk.Frame(root)
frame_hard = ttk.Frame(root)

# 画面表示
# タイトル画面
frame_title.grid(row=0, column=0, sticky=(N, W, S, E))
label_title = ttk.Label(frame_title, text='楽しい数独')
label_title.place(x=180, y=190, )
startButton = ttk.Button(frame_title, text="Start", command=lambda: changePage(frame_login))
startButton.place(x=180, y=245)

# ログイン表示
frame_login.grid(row=0, column=0, sticky=(N, W, S, E))

label_easy = ttk.Label(frame_login, text='初級コース')
label_easy.place(x=180, y=200, )
easyButton = ttk.Button(frame_login, text="Start", command=lambda: changePage(frame_easy))
easyButton.place(x=180, y=250)

# 初級表示
frame_easy.grid(row=0, column=0, sticky=(N, W, S, E))

kaitou = [
    [6, 1, 9, 7, 3, 2, 5, 4, 8],
    [8, 5, 3, 9, 4, 1, 6, 2, 7],
    [4, 2, 7, 6, 5, 8, 1, 9, 3],
    [5, 7, 1, 2, 9, 4, 3, 8, 6],
    [2, 3, 8, 5, 7, 6, 4, 1, 9],
    [9, 6, 4, 1, 8, 3, 7, 5, 2],
    [3, 9, 5, 4, 2, 7, 8, 6, 1],
    [1, 8, 2, 3, 6, 5, 9, 7, 4],
    [7, 4, 6, 8, 1, 9, 2, 3, 5]
]

ban = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 7],
    [4, 0, 0, 6, 0, 8, 0, 0, 0],
    [0, 7, 1, 0, 0, 0, 3, 0, 0],
    [2, 3, 8, 5, 0, 6, 4, 1, 9],
    [9, 6, 4, 1, 0, 0, 7, 5, 0],
    [3, 9, 5, 0, 2, 7, 8, 0, 0],
    [1, 8, 2, 0, 6, 0, 9, 7, 4],
    [0, 4, 6, 8, 1, 9, 2, 0, 5]
]

canvas = tkinter.Canvas(frame_easy, width=board_size, height=board_size + 50)
canvas.create_rectangle(0, 0, board_size, board_size + 50, fill='floral white', outline='floral white')
sample1()
canvas.pack()
canvas.bind('<ButtonPress>', buttonPress)
goalButton = ttk.Button(frame_easy, text="Finish!", command=btn_click)
goalButton.place(x=360, y=480)

frame_title.tkraise()
root.mainloop()
