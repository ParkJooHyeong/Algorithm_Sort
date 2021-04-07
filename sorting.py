def sequential_sort(input_list, reverse):

    if reverse is True:
        for i in range(len(input_list)-1):
            for j in range(i+1,len(input_list)):
                if input_list[i]<input_list[j]:
                    input_list[i], input_list[j]=input_list[j],input_list[i];
    else:
        for i in range(len(input_list)-1):
            for j in range(i+1,len(input_list)):
                if input_list[i]>input_list[j]:
                    input_list[i], input_list[j]=input_list[j],input_list[i];

    return input_list


def insertion_sort(input_list, reverse):
    if reverse is True:
        for i in range(1, len(input_list)):
            for j in range(i,0,-1):
                if input_list[j]>input_list[j-1]:
                    input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
                else:
                    break
    else:
        for i in range(1, len(input_list)):
            for j in range(i,0,-1):
                if input_list[j]<input_list[j-1]:
                    input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
                else:
                    break

    return input_list


def quick_sort(input_list):
    answer=[]

    return answer


def binary_sort(input_list):
    answer=[]

    return answer


def counting_sort(input_list):
    answer=[]

    return answer


def heap_sort(input_list):
    answer=[]

    return answer
