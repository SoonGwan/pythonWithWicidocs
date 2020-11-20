from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"

stop_words = stop_words.split(' ')
word_tokens = word_tokenize(example)

result = []
# for w in word_tokens:
#     if w not in stop_words:
#         result.append(w)

result = [word for word in word_tokens if not word in stop_words]

print(word_tokens)
print(result)
