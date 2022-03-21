class Solution:
    im  = []
    def flo(self, image, sr, sc, color, newColor):
        # print("sr, sc: ", sr, sc)
        if sr < 0 or sc < 0 or sr > len(image)-1 or sc > len(image[0])-1 or self.im[sr][sc] == 1 or image[sr][sc] != color:
            return
        
        self.im[sr][sc] = 1
        image[sr][sc] = newColor
            
        self.flo(image, sr-1, sc, color, newColor)
        self.flo(image, sr, sc-1, color, newColor)
        self.flo(image, sr+1, sc, color, newColor)
        self.flo(image, sr, sc+1, color, newColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.im = []
        for i in range(len(image)):
            r = []
            for j in range(len(image[0])):
                r.append(0)
            self.im.append(r)
        # print("image: ", len(image), len(image[0]), "im: ", len(self.im), len(self.im[0]))
        self.flo(image, sr, sc, image[sr][sc], newColor)
        return image
#  input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
#  output: Output: [[2,2,2],[2,2,0],[2,0,1]]