def successfulPairs(self, spells, potions, success):
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]