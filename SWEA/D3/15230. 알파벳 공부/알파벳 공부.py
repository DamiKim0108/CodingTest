alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

T = int(input())

for tc in range(1, T+1):
    words = list(input())

    counts= 0 

    for i in range(len(words)):
        if words[i] == alphabet[i]:
            counts +=1
        else:
            break
            
    print('#{} {}'.format(tc, counts))

