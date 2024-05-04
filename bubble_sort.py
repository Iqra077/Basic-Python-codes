def bubble(a):
    i = len(a) - 1
    while i > 0:
        if a[i] < a[i-1]:
            t = a[i]
            a[i] = a[i-1]
            a[i-1] = t
        i = i-1
def SortRec(a, n):
    if n <= 1:
        return 1
    SortRec(a, n-1)
    bubble(a)

def main():
    a=[4,2,8,1,9]
    v = SortRec(a,5)
    print(v)
main()
