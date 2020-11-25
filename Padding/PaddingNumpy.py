import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], [
    'barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

tokenizer = Tokenizer()
# fit_on_texts() 안에 코퍼스를 이별긍로하면 빈 도수를 기준으로 단어 집합을 생성
tokenizer.fit_on_texts(sentences)

encoded = tokenizer.texts_to_sequences(sentences)
print(encoded)

max_len = max(len(item) for item in encoded)
print(max_len)

for item in encoded:
    while len(item) < max_len:
        item.append(0)
padded_np = np.array(encoded)
print(padded_np)
