def longestsubstringwkdistinctchars(string,k):
        start_window=0
        dict={}
        maxl=float("-inf")
        for endwindow in range(0,len(s)):
            if s[endwindow] not in dict.keys():
                dict[s[endwindow]]=1
                
            else:
                dict[s[endwindow]]+=1
                
                
            while len(dict)>k:
                dict[s[start_window]]-=1
                if dict[s[start_window]]==0:
                    del dict[s[start_window]]
                start_window+=1
                
            maxl=max(maxl,endwindow-start_window+1)
        
        return maxl