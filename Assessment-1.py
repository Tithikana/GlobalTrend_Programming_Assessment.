class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    def delete(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return root
    def get_max(self):
        return self.heap[0] if self.heap else None
    def _heapify_up(self,index):
        parent=(index-1)//2
        if index>0 and self.heap[index]> self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self._heapify_up(parent)
    def _heapify_down(self,index):
        largest=index
        left=2*index+1
        right=2*index+2
        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=index:
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self._heapify_down(largest)

heap=MaxHeap()
while(1):
    print("1.For Insert")
    print("2.For Delete")
    print("3.For Get Max Heap")
    print("0.For Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        x=int(input("Enter a value:"))
        heap.insert(x)
    elif ch==2:
        print("Delete value is:",heap.delete())
    elif ch==3:
        print("Max value is:",heap.get_max())
    elif ch==0:
        print("Exit From The Program")
        break
    else:
        print("Invalid choice.Please enter another choice")
        
        
