
import json
data = {}
with open('tags/post-tags.txt') as json_file:
    data = json.load(json_file)


def similarity_jaccard(tag1,tag2):
     
    both_taged_count = 0
    either_one_taged = 0
    for key in data:
        temp = data[key]
        if tag1 in temp and tag2 in temp:
            both_taged_count+=1

        if tag1 in temp or tag2 in temp:
            either_one_taged+=1
     

    return ( both_taged_count/either_one_taged)
     


print ('regex','static')
print('Similarity: ',similarity_jaccard('regex','static')) 
print ('Distance: ',1 - similarity_jaccard('regex','static'),'\n')

print ('session','spring') 
print('Similarity: ',similarity_jaccard('session','spring')) 
print ('Distance: ',1 - similarity_jaccard('session','spring'), '\n')


print ('nullpointerexception','dependency-injection') 
print('Similarity: ',similarity_jaccard('nullpointerexception','dependency-injection')) 
print ('Distance: ',1 - similarity_jaccard('nullpointerexception','dependency-injection'))
