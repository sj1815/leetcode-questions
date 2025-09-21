class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = collections.defaultdict(SortedList)
        self.rented = SortedList()
        self.movies = {}

        for shop, movie, price in entries:
            self.movies[(shop, movie)] = (price, False)
            self.unrented[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        res = []
        for _, shop in self.unrented[movie][:5]:
            res.append(shop)
        return res
        
    def rent(self, shop: int, movie: int) -> None:
        price, _ = self.movies[(shop, movie)]
        self.movies[(shop, movie)] = (price, True)
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))    

    def drop(self, shop: int, movie: int) -> None:
        price, _ = self.movies[(shop, movie)]
        self.movies[(shop, movie)] = (price, False)
        self.unrented[movie].add((price,shop))
        self.rented.remove((price, shop, movie))
        
    def report(self) -> List[List[int]]:
        res = []
        for _, shop, movie in self.rented[:5]:
            res.append((shop, movie))
        return res
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()