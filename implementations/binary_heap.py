from math import floor


class BinaryHeap:
    def __init__(self, ) -> None:
        self.a = []

    def get_min(self):
        return self.a[0]

    def insert(self, x) -> None:
        self.a.append(x)
        i = len(self.a)-1
        par_i = floor((i-1)/2)
        # sift up
        while i > 0 and self.a[i] < self.a[par_i]:
            self.a[i], self.a[par_i] = self.a[par_i], self.a[i]
            i = par_i
            par_i = floor((i-1)/2)

    def remove_min(self):
        self.a[0] = self.a[-1]
        self.a = self.a[:-1] 
        i = 0
        l_i = 2*i + 1 # idx of left child
        # sift down
        n = len(self.a)
        while l_i < len(self.a):
            j = l_i # left child exists
            if j+1 < n and self.a[j+1] < self.a[j]:
                j = j + 1 # right child exists and smaller then left child
            if self.a[i] <= self.a[j]:
                break
            else:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j
                l_i = 2*i + 1

    # TODO: move code from insert and remove_min to sift_*.
    def sift_up(self):
        pass

    def sift_down(self):
        pass

    @staticmethod
    def get_parent(idx: int)-> int:
        return floor((idx-1)/2)



if __name__ == "__main__":
    heap = BinaryHeap()
    ##
    l = [3,2,1,5,11,4]
    for e in l:
        print(e)
        heap.insert(e)
    
    print(l)
    for i in range(len(l)):
        print(heap.get_min(), end=" ")
        heap.remove_min()
