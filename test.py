from data_structures.clist import CList
from data_structures.queue import Queue

# def test_clist():
#     clist = CList()
#     clist.add(10)
#     clist.add(20)
#     clist.add(30)
#     clist.add(40)
#     clist.add(50)
#     clist.add(60)
#     print("Initial list:")
#     clist.display()

#     clist.remove(20)
#     print("Modified list:")
#     clist.display()

#     clist.remove(60)
#     clist.add(65)
#     print("Modified list:")
#     clist.display()
# test_clist()



def test_queue():
    q = Queue()

    # 큐에 값 추가
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue size:", len(q))  # 출력: Queue size: 3
    print("Front element (peek):", q.peek())  # 출력: Front element (peek): 10

    # 큐에서 값 제거
    print("Queue_Dequeued:", q.dequeue())  # 출력: Dequeued: 10
    print("Front element (peek):", q.peek())  # 출력: Front element (peek): 10
    print("Queue_Dequeued:", q.dequeue())  # 출력: Dequeued: 20
    print("Queue size after dequeue:", len(q))  # 출력: Queue size after dequeue: 1
    print("Front element (peek):", q.peek())  # 출력: Front element (peek): 10
    # 마지막 값 제거
    print("Queue_Dequeued:", q.dequeue())  # 출력: Dequeued: 30



if __name__ == "__main__":
    test_queue()
