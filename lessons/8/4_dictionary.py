from english_words import get_english_words_set
from hashlib import md5

hash_was = '5f4dcc3b5aa765d61d8327deb882cf99'

for word_now in get_english_words_set(('web2',)):
    if md5(word_now.encode()).hexdigest()==hash_was:
        print(word_now)
        break
