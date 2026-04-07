from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perim = 2 * (width + height) - 4
        self.pos = 0
        self.initial = True

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perim
        self.initial = False

    def _decode(self):
        pos, w, h = self.pos, self.w, self.h
        if self.initial:
            return 0, 0, 0          
        if pos == 0:
            return 0, 0, 3          
        if pos <= w - 1:            
            return pos, 0, 0
        if pos <= w + h - 2:        
            return w - 1, pos - w + 1, 1
        if pos <= 2*w + h - 3:      
            return w - 2 - (pos - (w + h - 1)), h - 1, 2
        return 0, h - 2 - (pos - (2*w + h - 2)), 3   

    def getPos(self) -> List[int]:
        x, y, _ = self._decode()
        return [x, y]

    def getDir(self) -> str:
        _, _, d = self._decode()
        return ("East", "North", "West", "South")[d]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()