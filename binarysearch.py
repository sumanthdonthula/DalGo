class binarySearch:

    def binarySearch(self,list,val):

        mid=(len(list)-1)//2

        if val==list[mid]:
            return True  
        
        elif len(list)==1 and list[mid]!=val:
            return False

        elif val<list[mid]:
            return self.binarySearch(list[:mid],val)

        elif val>list[mid]:
            return self.binarySearch(list[mid+1:],val)
        

bst=binarySearch()
print(bst.binarySearch([1,2,3,4,5,8],8))