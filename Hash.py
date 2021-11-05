class myHash:

    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(10)]

    def hashing_f(self, key):
        hash_key = hash(key) % self.size
        return hash_key

    def set(self, key, value):
        hash_key = self.hashing_f(key)
        key_exists = False
        bucket = self.hashmap[hash_key]
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
        hash_key = self.hashing_f(key)
        bucket = self.hashmap[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return KeyError("%s not found" % key)

    def __str__(self):
        return str(self.hashmap)




myHash = myHash()
myHash.set(10, "Paris")
myHash.set(20, "New York")
myHash.set("another_city", "Tokyo")
myHash.set("my_city", "Neuilly")
print(myHash.get("my_city"))
