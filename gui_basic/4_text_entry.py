from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480") #가로 * 새로
root.geometry("640x480+300+100") #가로 * 새로 + x좌표 + y좌표

txt = Text(root, width=30, height=5) #줄바꿈 가능
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) #줄바꿈 불가능
e.pack()
e.insert(0, "한 줄만 입력해요.")

def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) #라인.인덱스 문장의 첫(1)번째 라인에서 0번째 인덱스부터 가지고와라
    print(e.get())

    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0, END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()