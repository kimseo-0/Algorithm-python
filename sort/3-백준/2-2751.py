import sys
input = sys.stdin.readline

def quick_sort(array) :
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  
  left_array = [x for x in tail if x <= pivot]
  right_array = [x for x in tail if x > pivot]
  
  return quick_sort(left_array) + [pivot] + quick_sort(right_array)
  
N = int(input())
num_list = []
for i in range(N):
  num_list.append(int(input())) 
  
num_list = quick_sort(num_list)
  
for i in range(N):
  print(num_list[i])
  
# quick sort > memory over
# library > solve
