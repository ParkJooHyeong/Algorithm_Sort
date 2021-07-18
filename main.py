import sorting as fsort

input_list=[4,9,10,5,1,2,8,3,7,6]


print("순차정렬\t:",fsort.sequential_sort(input_list, reverse=False))
print("삽입정렬\t:",fsort.insertion_sort(input_list, reverse=False))
print("퀵정렬\t:", fsort.quick_sort(input_list.copy(),reverse=False, front=0, rear=len(input_list)-1))
print("계수정렬\t:", fsort.counting_sort(input_list.copy(), reverse=True))
print("병합정렬\t:", fsort.merge_sort(input_list.copy()))