class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer=[] #empty list
        hashmap1={}
        hashmap2={}
        for ch in p: # to first fix the length of window according to p
            if ch in hashmap1:
                hashmap1[ch]+=1
            else:
                hashmap1[ch]=1
        slow=0
        for fast in range(len(s)): # with first ietration
            ch=s[fast] # to check if it is present or not
            if ch in hashmap2:
                hashmap2[ch]+=1
            else:
                hashmap2[ch]=1 # to add in hashmap

            if fast-slow +1 >len(p): # for sliding the window , to check if the window length is greater than the fix size
                left=s[slow] # to remove the first element , first need to move it into temp variabe
                hashmap2[left]-=1 # then decrement the value to 0

                if hashmap2[left]==0: # now check if it is 0 , delete that key
                    del hashmap2[left]
                slow+=1 # pointer movies forward
            if hashmap1==hashmap2: # to checkthe frequencies
                answer.append(slow)
        return answer