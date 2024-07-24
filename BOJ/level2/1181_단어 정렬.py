count = int(input())
word = [input() for _ in range(count)]

word = set(word)
word = list(word)

word.sort()
word.sort(key=len)

for i in word: print(i)

# 조건
	# 1. 길이가 짧은 것부터(상위 조건)
	# 2. 길이가 같다면 알파벳 순으로(하위 조건)

# 하위조건과 상위조건이 있으면, 
# 하위 조건 정렬 후 상위 조건 정렬