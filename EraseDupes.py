
def remove_duplicates(seq):
    size = len(seq)
    edit = seq[:]
    for key,nval in enumerate(seq):
#        print "--------------------------\nSeq__Key =",key,"\n"
        for i in range(key+1,size):
#            print key, i, seq[key], seq[i]
            if seq[key] == seq[i]:
#                print "Removing",key
                edit.remove(seq[key])
                break

    return edit

print remove_duplicates([6,6,6,6])   
print remove_duplicates([7,1,2,1,2])