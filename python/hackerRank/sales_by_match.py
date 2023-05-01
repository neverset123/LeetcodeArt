def sockMerchant(n, arr):
    colors={}
    num_matched=0
    for i in arr:
        if i in colors:
            num_matched+=1
            colors.pop(i)
        else: colors[i]=1
    return num_matched

def sockMerchant_v2(n, arr):
    bins=[]
    for item in set(arr):
        bins.append(arr.count(item))
    return sum([i//2 for i in bins])


if __name__ == "__main__":
    test_data=[1,2,1,2,1,3,2]
    print(sockMerchant_v2(len(test_data), test_data))
