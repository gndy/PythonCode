from Bio.Blast import NCBIXML

'''
blast xml results merger script.
It merges all overlapped HSPs in to one big HSP
'''
def mergeTuples(l):    
    tmp = []
    for i in l:
        tmp.extend(list(i))
    tmp.sort()
    return (tmp[0],tmp[3])

def isOverlap(t1,t2):
    tmp = [t1,t2]
    tmp.sort()
    if tmp[1][0]<=tmp[0][1]:
        return True
        
    elif tmp[1][0]-tmp[0][1]<19:
        return True
    else:
        return False
    
def cmpToList(mTuple,mList):
    for i in range(len(mList)):
        if isOverlap(mTuple,mList[i]):
            return i
    return None
    

blast_results = NCBIXML.parse(open("/home/wenlei/LUO/ZF/blast/bac_results.xml","r"))

for result in blast_results:
    for alignment in result.alignments:
        print alignment.hit_def
        mList = []
        for hsp in alignment.hsps:
            mTuple = (hsp.query_start,hsp.query_end)
            mList.append(mTuple)
        mList.sort()
        print mList
        tmp_list = [mList[0]]
        
        for i in mList:
            mark = cmpToList(i,tmp_list)
            if mark != None:
                tmp_list[mark] = mergeTuples([i,tmp_list[mark]])
            else:
                tmp_list.append(i)
        print tmp_list
            
                



                
            

                    
            



    
                
                

