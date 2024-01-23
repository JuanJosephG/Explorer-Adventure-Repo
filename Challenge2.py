class hash_table :
    def _init_ (self, size):
        self.size = size
        self.hash_table = {} #dictionary
    
    def hash_function(self, key):
        return hash(key) % self.size  #determines index of data
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if index not in self.hash_table: #bucket is empty,create a new dict for key
            self.hash_table[index] = {key: value}
        else:
            self.hash_table[index][key] = value
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.hash_table.get(index, {})
        return bucket.get(key,None)
    
name_hash_table = hash_table()

name_hash_table.insert("Rob", 1)
name_hash_table.insert("Joey", 5)
name_hash_table.insert("Jacob", 7)
name_hash_table.insert("random", 8)

print(name_hash_table.get("Robert"))
print(name_hash_table.get("Joey"))
print(name_hash_table.get("Jacob"))
print(name_hash_table.get("random"))