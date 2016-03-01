def rename_key(mkeys, mkey, index):
    nkey = mkey+'_'+str(index)
    if nkey in mkeys:
        index += 1
        return rename_key(mkeys, mkey, index)
    else:
        return nkey
    
mlist = ['a','b','a_1']

print rename_key(mlist,'a',1)
