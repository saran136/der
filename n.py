no_of_char=256
def max_distinct(str,n):
    count=[0]*no_of_char
    for i in range(n):
        count[ord(str[i])]+=1
    max_dist=0
    for i in range(no_of_char):
        if(count[i]!=0):
            max_dist+=1
    return max_dist

def small_substr(str):
    n=len(str)
    max_dist=max_distinct(str,n)
    mini=n
    for i in range(n):
        for j in range(n):
            sub_str=str[i:j]
            sub_str_length=len(sub_str)
            sub_dist_char=max_distinct(sub_str,sub_str_length)
            if(sub_str_length<mini and max_dist == sub_dist_char):
                mini=sub_str_length
    return mini

stri=input()
val=small_substr(stri)
print(val)
