# import threading
import time
from random import choice
import threading


class TypingTest:
    words = ["Education", "Demonstration", "Lexicographic", "Tournament", "Baseball", "Juvenile"]
    words += ["Monetary", "Diamond", "Iterables", "Objection", "Manipulation", "Telecommunication"]
    timer_stop = 0

    def __init__(self):
        print("Starting")
        time.sleep(2)
        self.w = 0

    # def start_timer(self):
        # print("Loading")
        # s = time.time()
        # print(s)
        # time.sleep(5)
        # print("Loaded")
        # end = time.time()
        # print(end)

        # for i in range(1, 11):
        #     time.sleep(1)

        # start = time.time()
        # time.sleep(10)
        # end = time.time()
        # print(int(end-start))

    def timer(self):
        self.timer_stop = 30
        for i in range(30):
            time.sleep(1)
            self.timer_stop -= 1

    def start_test(self):
        timer_thread = threading.Thread(target=self.timer)
        timer_thread.start()
        while self.timer_stop > 0:
            word = choice(self.words)
            print(f"{word}")
            user_input = input()
            if user_input.lower() == word.lower():
                print("Typed correct")
                self.w += 1
            else:
                print("incorrect")
                # break

        print("Time Up")
        print(f"You typed : {self.w} words in 30 seconds")
        decision = input("Wanna Continue ? Y for yes and N for no\n")
        while True:
            if decision == "n":
                break
            else:
                self.start_test()


TypingTest().start_test()


