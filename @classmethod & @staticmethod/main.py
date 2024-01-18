class Store:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    @classmethod
    def franchise(cls, store):
        # Returns a new object of class Store with the given name
        return cls(store.name + ' - Franchise')
    
    @staticmethod
    def storeDetails(store):
        return f"Name of the store is {store.name}."
    

store = Store("Amazon")
print(store)

storeF = store.franchise(store)
print(storeF)

print(store.storeDetails(storeF))