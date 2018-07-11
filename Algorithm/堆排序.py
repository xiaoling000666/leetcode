class Solution():
    def heap_sort(self, heap):
        root = (len(heap)-2)//2
        for i in range(root, -1, -1):
            left = 2 * i + 1
            if heap[left] > heap[i]:
                heap[left], heap[i] = heap[i],heap[left]
            right = left + 1
            if i == (len(heap)-2)//2 and (len(heap)) % 2 == 0:
                right = left
            if heap[right] > heap[i]:
                heap[right], heap[i] = heap[i], heap[right]
        return heap
    def main(self,heap):
        for i in range(len(heap)-2):
            heap[i:] = self.heap_sort(heap[i:])
            print(heap)


heap = [49,38,65,97,76,13,27,49]
s = Solution()
print(s.main(heap))