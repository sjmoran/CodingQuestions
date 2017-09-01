n = 312
n_list = [int(a) for a in list(str(n))]
L = len(n_list)

swapped = False
ind_a = L
for i in range(0, L - 1):
    if n_list[L - i - 1] < n_list[L - i - 2]:
        pivot = n_list[L - i - 2]
        pivot_ind = L - i - 2
        max_min_n = -1
        max_min_n_ind = -1
        for j in range(pivot_ind, L):
            if ((n_list[j] < pivot) and (n_list[j] > max_min_n)):
                max_min_n = n_list[j]
                max_min_n_ind = j
        swapped = True
        break

if swapped:
    n_list[max_min_n_ind] = pivot
    n_list[pivot_ind] = max_min_n

    n_list_sort = sorted(n_list[pivot_ind + 1:L], reverse=True)
    n_list[pivot_ind + 1:L] = n_list_sort

n_o = int(''.join(map(str, n_list)))
print "input: " + str(n)
print "next smallest number: " + str(n_o)
