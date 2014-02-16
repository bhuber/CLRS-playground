#!/usr/bin/python

"""Mergesort implementation"""


def insertionsort(l, start=0, end=None, key=None):
    end = end or len(l)
    for i in xrange(start + 1, end):
        j = i - 1
        li = key(l[i]) if key else l[i]
        while j >= start and ((key and li < key(l[j])) or li < l[j]):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = li
    return l


def _merge(l, start, mid, end, key):
    key = key or (lambda x: x)
    left = list(l[start:mid])
    right = list(l[mid:end])
    li = 0
    ri = 0
    len_l = mid - start
    len_r = end - mid
    for k in xrange(start, end):
        if li >= len_l:
            l[k] = right[ri]
            ri += 1
        elif ri >= len_r:
            l[k] = left[li]
            li += 1
        else:
            if ((key and key(left[li]) >= key(right[ri])) or
                    left[li] >= right[ri]):
                l[k] = right[ri]
                ri += 1
            else:
                l[k] = left[li]
                li += 1
    return l


def mergesort(l, start=0, end=None, key=None):
    end = end or len(l)
    if end - start + 1 < 12:
        return insertionsort(l, start, end, key)
    mid = (start + end) / 2

    mergesort(l, start, mid, key)
    mergesort(l, mid, end, key)
    return _merge(l, start, mid, end, key)
