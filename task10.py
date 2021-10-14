
def common_words(word1,word2)
    word_1 = set (word1)
    word_2 = set (word2)
     
              common=list( word_1 & word_2)
                   if common ==0 :
                        print(-1)
                   return
          common_char =sorted (common)
              print (''.join(common_char))

common_words(word1,word2)
 