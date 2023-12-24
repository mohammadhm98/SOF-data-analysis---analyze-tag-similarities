import operator
import json

def preproccess_extract_qid_and_tnames_only():
    posts_id = {}
    tags = {}

    p_id = open("tags/pid.txt", "a")
    t_id = open("tags/tid.txt", "a")
    post_counter = 0
    tag_counter = 0
    with open("tags/tags.txt") as infile:
        for line in infile:
            if (line.split()[0] not in posts_id):
               posts_id[line.split()[0]] = post_counter
               post_counter +=1

            if (line.split()[1] not in tags):
               tags[line.split()[1]] = tag_counter
               tag_counter +=1   

    p_id.write(json.dumps(posts_id))
    p_id.close() 

    t_id.write(json.dumps(tags))
    t_id.close() 



def preproccess_extract_post_tags():
    p_t = open("tags/post-tags.txt", "a")
    posts_tags = {} 
    with open("tags/tags.txt") as infile:
            for line in infile:
                
                pid = line.split()[0] 
                t = line.split()[1]
                if  pid in posts_tags.keys():
                    posts_tags[pid].append(t)
                else:
                    posts_tags[pid] = [t]    
    p_t.write(json.dumps(posts_tags))
    p_t.close() 



def get_top_five(addr):
    
    tag_similarity = {}
    tag1 = ''
    with open(addr) as infile:
            for line in infile:
                t1 = line.split()[0] 
                tag1 = t1
                t2 = line.split()[1]
                sim = line.split()[2]             
                tag_similarity[t2] = float(sim)

    tag_similarity_sorted_list = dict(sorted(tag_similarity.items(), key=operator.itemgetter(1),reverse=True))
    c = 0 
    print('recommended tags for {}'.format(tag1))
    for index, key in enumerate(tag_similarity_sorted_list):
        if  index > 0 and index <6:
            print(key, tag_similarity_sorted_list[key])



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
     

def find_similarity(tag):
    key_list = list(tag_names)

 
    tag_similarity2 = open("tags/{}-similarities.txt".format(tag), "a")
    for i in range(0,  (len(tag_names)-1)) :
            sim = similarity_jaccard(tag,key_list[i] )
            tag_similarity2.write("{}  {} {}\n".format(tag,key_list[i], sim))    
    
 
    tag_similarity2.close 



# preproccess_extract_qid_and_tnames_only()
# preproccess_extract_post_tags()

data = {}
with open('tags/post-tags.txt') as json_file:
    data = json.load(json_file)

tag_names = {}
with open('tags/tid.txt') as json_file:
    tag_names = json.load(json_file)
print ('loaded')


# find_similarity('intellij-idea')
# find_similarity('jax-rs')
# find_similarity('user-interface')

get_top_five("tags/user-interface-similarities.txt")
print ('\n')
get_top_five("tags/jax-rs-similarities.txt")
print ('\n')
get_top_five("tags/intellij-idea-similarities.txt")
