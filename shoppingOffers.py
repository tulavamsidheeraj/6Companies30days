def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if not special:
            return sum([price[i] * needs[i] for i in range(len(needs))])


        instance = special[-1]
        n = len(needs)
        max_size = float('inf')
        ans = float('inf')

        if sum([price[i] * instance[i] for i in range(len(instance) - 1)]) < instance[-1]:
            max_size = 0 

        for i in range(n):
            if instance[i] > 0:
                max_size = min(max_size, needs[i] // instance[i])

        for k in range(max_size + 1): 
            new_needs = [needs[i] - instance[i] * k for i in range(n)]
            ans = min(ans, k * instance[n] + self.shoppingOffers(price, special[:-1], new_needs))
        
        return ans 
