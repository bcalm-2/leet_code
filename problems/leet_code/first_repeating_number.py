def firstRepeated(arr):
        seen = {}
        min_index = []

        for i in range(len(arr)):
            if arr[i] in seen:
                min_index.append(seen[arr[i]])
            else:
                seen[arr[i]] = i

        if not min_index :
            return -1
        else:
            minm=min(min_index)
            return minm+1


print(firstRepeated([1,5,3,4,3,5,6])) 