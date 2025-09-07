def find_max_occurred_alphabet(string):
    arr=[0 for i in range(26)]
    for s in string:
        if not s.isalpha():
            continue
        arr[ord(s.lower())-ord('a')] += 1
    max_alpha_idx = arr.index(max(arr))
    return(chr(max_alpha_idx+97))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# 문자인지 확인: 문자.isalpha()
# 문자열 -> 아스키: ord('a')
# 아스키 -> 문자열: chr(97)