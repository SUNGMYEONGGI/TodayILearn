def solution(array, n):
    array.append(n)
    array.sort()
    n_num = array.index(n)
    # return array
    if n == array[-1]:
        return array[n_num-1]
    elif n != array[-1]:
        if n-(array[n_num-1]) > (array[n_num+1])-n:
            return array[n_num+1]
        else:
            return array[n_num-1]