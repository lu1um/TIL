from collections import Counter

a = ['a', 'a', 'b', 'c']

b = Counter(a).most_common()
print(b)