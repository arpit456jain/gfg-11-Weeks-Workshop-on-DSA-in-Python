def create_hash_map_of_freq(arr):
    hash_map = {}
    for i in arr:
        if i in hash_map.keys():
            hash_map[i]+=1
        else:
            hash_map[i] = 1
    return hash_map

def maximum_sum(n,arr,k):
    # T.C is ver high error->TLE
    sum1=0
    maxfreq = 0
    maxfreqelement = 0
    while(k>0):
        hasmap = create_hash_map_of_freq(arr)
        print(hasmap)
        arr.sort()
        for i,j in hasmap.items():
            if j>=maxfreq:
                maxfreq=j
                maxfreqelement=i
        print("max freq is",maxfreq,maxfreqelement)

        arr[:] = arr[::-1]
        for i in arr:
            print(arr,i)
            if k<=0:
                break
            if i == maxfreqelement:
                sum1+=maxfreqelement
                k=k-1
            print(sum1,k)
        try:
            while(True):
                arr.remove(maxfreqelement)
        except:
            pass

    return sum1

if __name__ == "__main__":
    t=1
    for tc in range (t):
        N,K = map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        print(maximum_sum(N,A,K))
