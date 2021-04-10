def sequential_sort(target, reverse):
    input_list = target.copy()
    if reverse is True:
        for i in range(len(input_list)-1):
            for j in range(i+1,len(input_list)):
                if input_list[i]<input_list[j]:
                    input_list[i], input_list[j]=input_list[j],input_list[i]
    else:
        for i in range(len(input_list)-1):
            for j in range(i+1,len(input_list)):
                if input_list[i]>input_list[j]:
                    input_list[i], input_list[j]=input_list[j],input_list[i]

    return input_list


def insertion_sort(target, reverse):
    input_list = target.copy()
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


def quick_sort(input_list, reverse, front, rear):
    if reverse is False:
        if front>=rear:
            return
        pivot = front
        left = pivot+1
        right = rear
        while left<=right:
            ## Pivot보다 큰 수를 찾을때 까지.
            while left<=rear and input_list[left]<=input_list[pivot]:
                left+=1
            ## Pivot보다 작은 수를 찾을때 까지.
            while right>front and input_list[right]>=input_list[pivot]:
                right-=1
            if left>right:
                input_list[right], input_list[pivot] = input_list[pivot], input_list[right]
            else:
                input_list[left], input_list[right] = input_list[right], input_list[left]
        quick_sort(input_list,reverse=False,front=front, rear=right-1)
        quick_sort(input_list, reverse=False,front=right+1, rear=rear)
        return input_list
    else:
        if front>rear:
            return
        pivot = front
        left = pivot+1
        right = rear
        while left<=right:
            ## Pivot보다 작은 수를 찾을때 까지.
            while left<=rear and input_list[left]>=input_list[pivot]:
                left+=1
            ## Pivot보다  수를 찾을때 까지.
            while right>front and input_list[right]<=input_list[pivot]:
                right-=1
            if left>right:
                input_list[right], input_list[pivot] = input_list[pivot], input_list[right]
            else:
                input_list[left], input_list[right] = input_list[right], input_list[left]
        quick_sort(input_list,reverse=True,front=front, rear=right-1)
        quick_sort(input_list, reverse=True,front=right+1, rear=rear)
        return input_list


## Divide
def merge_sort(input_list):
    if len(input_list)<=1:
        return input_list
    mid = len(input_list)//2
    leftSide = input_list[:mid]
    rightSide = input_list[mid:]
    leftSide = merge_sort(leftSide)
    rightSide = merge_sort(rightSide)
    return merge(leftSide, rightSide)

## Conquer
def merge(l, r):
    result = []
    while len(l)>0 or len(r)>0:
        if len(l)>0 and len(r)>0:
            if l[0]<=r[0]:
                result.append(l[0])
                l = l[1:]
            else:
                result.append(r[0])
                r = r[1:]
        elif len(l)>0:
            result.append(l[0])
            l=l[1:]
        elif len(r)>0:
            result.append(r[0])
            r=r[1:]
    return result




def counting_sort(input_list, reverse):
    answer = list()
    count_list = [0]*(max(input_list)+1)
    if reverse is False:
        for i in range(len(input_list)):
            count_list[input_list[i]]+=1
        for i in range(len(count_list)):
            for j in range(count_list[i]):
                answer.append(i)
    else:
        for i in range(len(input_list)):
            count_list[input_list[i]]+=1
        for i in range(len(count_list)-1,0,-1):
            for j in range(count_list[i]):
                answer.append(i)
    return answer


def heap_sort(input_list):
    answer=[]

    return answer
