import operator
import json
data = {}
with open('tags/post-tags.txt') as json_file:
    data = json.load(json_file)

 

tag_names = {}
with open('tags/tid.txt') as json_file:
    tag_names = json.load(json_file)
print ('loaded')

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
     

def get_top_10():
    
    tag_similarity = {}
    counter = 0 
    with open("tags/sim.txt") as infile:
            for line in infile:
                
                t1 = line.split()[0] 
                t2 = line.split()[1]
                sim = line.split()[2]             
                tag_similarity[t2+ " "+t1] = float(sim)

    tag_similarity_sorted_list = dict(sorted(tag_similarity.items(), key=operator.itemgetter(1),reverse=True))
    c = 0 
    for i in (tag_similarity_sorted_list):
        if c ==10:
            break
        print (i, tag_similarity_sorted_list[i])
        c+=1

key_list = list(tag_names)
tag_similarity = open("tags/sim2.txt", "a")
print('writing in tags/sims2.txt')
print ('executing this code will take a while :))')
for i in range(0,  (len(tag_names)-1)) :
        for j in range(i + 1, len(tag_names)-1):
            sim = similarity_jaccard(key_list[i],key_list[j])
            tag_similarity.write("{}  {} {}\n".format(key_list[i],key_list[j],sim))
tag_similarity.close 


# t1,t2 = 'html','css'
# print(t1,t2,similarity_jaccard(t1,t2)) 

