import time
import threading
class Threading:

    def cal_square(self,items):
        for n in items:
            time.sleep(0.2)
            print("square is:", n*n)

    def cal_cube(self,items):
        for n in items:
            time.sleep(0.2)
            print("cube is:",n*n*n)


if __name__ == '__main__':
    Items=[2,3,4,5,6]
    thr = Threading()
    t1= threading.Thread(target= thr.cal_square, args=(Items,))# here for target you just need to pass reference of the method not call the method
    t2=threading.Thread(target=thr.cal_cube, args=(Items,)) #comma after Items is to show it is Tuple, In Python trailing comma is required to indicate it is a Tuple

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")


