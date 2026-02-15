class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        for row in image:
            row.reverse()

        for i in range(rows):
            for j in range(cols):
                if image[i][j]:
                    image[i][j] = 0
                    continue
                image[i][j] = 1

        return image