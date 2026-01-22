class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        SUMM,I,V1,V2,LEFT,RIGHT = 0,1,2,3,4,5
        
        b = [[v+u,i,v,u,None,None] for (v,u),i in zip(pairwise(a),count())]
        if len(b)>1: b[0][RIGHT],b[-1][LEFT] = b[1],b[-2]
        for l,m,r in zip(b,b[1:],b[2:]):
            l[RIGHT],m[LEFT],m[RIGHT],r[LEFT] = m,l,r,m

        z,sl,res = sum(starmap(gt,pairwise(a))),SortedList(b),0
        while z:
            summ,_,v,u,l,r = sl.pop(0)
            z,res = z-(v>u),res+1
            if l:
                sl.remove(l)
                z = z-(l[V1]>l[V2])+(l[V1]>summ)
                l[V2],l[SUMM],l[RIGHT] = summ,l[V1]+summ,r
                sl.add(l)
            if r:
                sl.remove(r)
                z = z-(r[V1]>r[V2])+(summ>r[V2])
                r[V1],r[SUMM],r[LEFT] = summ,summ+r[V2],l
                sl.add(r)
            
        return res