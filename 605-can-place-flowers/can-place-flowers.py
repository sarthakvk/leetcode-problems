class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        c = 0

        for i in range(len(flowerbed)):
            if (i == 0 or flowerbed[i-1] != 1) and (i == len(flowerbed)-1 or flowerbed[i+1] != 1):
                if flowerbed[i] != 1:
                    c += 1
                    flowerbed[i] = 1
        return c >= n