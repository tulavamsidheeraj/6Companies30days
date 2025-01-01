class Solution:
    def checkOverlap(self, r: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearX=max(x1,min(x2,xCenter))
        nearY=max(y1,min(y2,yCenter))
        d1=nearX-xCenter
        d2=nearY-yCenter
        return d1**2 + d2**2<=r*r
