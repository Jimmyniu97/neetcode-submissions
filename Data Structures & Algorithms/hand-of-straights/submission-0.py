from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        for card in sorted(hand):
            while counter[card] > 0:
                for x in range(card, card+groupSize):
                    if counter[x] == 0:
                        return False
                    counter[x] -= 1

        return True 

