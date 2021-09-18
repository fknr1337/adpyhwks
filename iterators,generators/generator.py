from hashlib import md5


def hashing(path):
    with open(path) as file:
        for line in file.readlines():
            hashed_line = md5(line.encode()).hexdigest()
            yield hashed_line


gen = hashing('test.txt')

for hashed_data in gen:
    print(hashed_data)