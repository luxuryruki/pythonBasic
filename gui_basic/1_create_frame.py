from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480") #가로 * 새로
root.geometry("640x480+300+100") #가로 * 새로 + x좌표 + y좌표
root.resizable(False,False) # 창의 너비 높이 변경 불가

root.mainloop()