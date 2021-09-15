S = input()

tag = False
new_word = ""
save_word = ""

for w in S:
    if tag == False:
        if w == "<":
            new_word = new_word + "<"
            tag = True
        elif w == " ":
            new_word = new_word + " "
            save_word += new_word  # 공백에서 단어가 나뉘므로 save_word에 new_word 갱신
            new_word = "" # new_word 초기화
        else:
            new_word = w + new_word
    
    else: # elif tag == True
        if w == ">":
            new_word = new_word + ">" 
            tag = False
            save_word += new_word # ">"에서 tag가 구분되므로 save_word에 new_word 갱신
            new_word = "" # new_word 초기화
        else:
            new_word = new_word + w

# 단어의 끝이 ">", ""로 끝나지 않는 경우를 위해서 save_word에 new_word 한 번 더 갱신
save_word += new_word

print(save_word)
