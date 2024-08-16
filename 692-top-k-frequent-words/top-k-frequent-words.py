class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # my={}
        # for i in words:
        #     if i in my:
        #         my[i] +=1
        #     else:
        #         my[i]=1

        # sorted_dict = dict(sorted(my.items(), key=lambda item: item[1], reverse=True))
        # ans=[]
        # for j in sorted_dict.keys():
        #     if len(ans)!= k:
        #         ans.append(j)
        #     else:
        #         return ans
        # return ans 
        word_count = Counter(words)
        
        # Sort the words first by frequency (descending), then by lexicographical order
        sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], word))
        
        # Return the top k words
        return sorted_words[:k]

            
            



