class Solution:
    def romanToInt(self, s: str) -> int:
        map=dict()
        map['I']=1
        map['V']=5
        map['X']=10
        map['L']=50
        map['C']=100
        map['D']=500
        map['M']=1000
        sum=0
        i=0
        while i < len(s) :
            if(s[i]=='I'):
                if (i<len(s)-1 and s[i+1]=='V'):
                    sum+=4
                    i+=2
                elif(i<len(s)-1 and s[i+1]=='X'):
                    sum+=9
                    i+=2
                else:
                    sum+=1
                    i+=1
            elif(s[i]=='X'):
                if(i<len(s)-1 and s[i+1]=='L'):
                    sum+=40
                    i+=2
                elif(i<len(s)-1 and s[i+1]=='C'):
                    sum+=90
                    i+=2
                else:
                    sum+=10
                    i+=1
            elif(s[i]=='C'):
                if(i<len(s)-1 and s[i+1]=='D'):
                    sum+=400
                    i+=2
                elif(i<len(s)-1 and s[i+1]=='M'):
                    sum+=900
                    i+=2
                else:
                    sum+=100
                    i+=1
            else:
                sum+=map[s[i]]
                i+=1
        return sum