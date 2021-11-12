class MyHash:

    def __init__(self):
        self.size = 10
        self.hashMap = [[] for _ in range(10)]

    def hashing_f(self, key):
        hashKey = hash(key) % self.size
        return hashKey

    def set(self, key, value):
        hashKey = self.hashing_f(key)
        key_exists = False
        bucket = self.hashMap[hashKey]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def get(self, key):
        hashKey = self.hashing_f(key)
        bucket = self.hashMap[hashKey]
        for k, v in bucket:
            if k == key:
                return v
        return KeyError("%s not found" % key)

    def __str__(self):
        return str(self.hashMap)




myHash = MyHash()
myHash.set(10, "Paris")
myHash.set(20, "New York")
myHash.set("another_city", "Tokyo")
myHash.set("my_city", "Neuilly")
print(myHash.get("my_city"))
