n = int(raw_input()) + 1

#f1 = lambda x : x[1:x[0]+1] + map(lambda y: 0 if y % x[x[0]] == 0 else y, x[x[0]+1:])
#f1 = lambda x : x[1:x[0]+1] + map(lambda y: 0 if y % x[x[0]] == 0 else y, x[x[0]+1:]) if x[x[0]] != 0 else x[1:]
#lambda x : x[1:x[0]+1] + map(lambda y: 0 if y % x[x[0]] == 0 else y, x[x[0]+1:]) if x[x[0]] != 0 else x[1:],

#f1 = lambda arr, x : arr[0:x+1] + map(lambda y: 0 if y % arr[x] == 0 else y, arr[x+1:])

eratosphen = lambda n : reduce(lambda arr, x : arr[0:x+1] + map(lambda y: 0 if y % arr[x] == 0 else y, arr[x+1:]) if arr[x] > 0 else arr, [range(2, n)] + range(n-2))
print eratosphen(n)
