T = int(input())
word_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
library = {}

for i in range(len(word_list)):
          library[word_list[i]] = i

for tc in range(1, T+1):
        TC, length = input().split()
        length = int(length)

        array = list(input().split())

        new_array = []

        # 글자를 key로 저장된 value값을 딕셔너리에서 찾아서 새로운 리스트 만들기
        for i in range(length):
                new_array.append(library.get(array[i]))

        new_array.sort()
        bb = {v:k for k,v in library.items()}

        print(f'#{tc}')
        for i in range(len(new_array)):
                print(bb[new_array[i]], end=' ')
