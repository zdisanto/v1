


# documents-- just simple text strings in this case

doc1 = "Would you like green eggs and ham?"

doc2 = "I do not like them, Sam-I-Am."

doc3 = "I do not like green eggs and ham."

doc4 = "Would you like them here or there?"

doc5 = "I would not like them here or there."

doc6 = "I would not like them anywhere."


# compiling into collection-- just put then in a list []

collection = [doc1, doc2, doc3, doc4, doc5, doc6]


# a function for cleaning up text, here just removing punctuation

def clean_text(doc):
    
    res = doc
    
    # remove common punctuation
    res = res.replace( ',' , '' )
    res = res.replace( '.' , '' )
    res = res.replace( '?' , '' )
    res = res.replace( '!' , '' )
    res = res.replace( '(' , '' )
    res = res.replace( ')' , '' )
    res = res.replace( '\n' , '' )
    res = res.replace( '\"' , '' )
    res = res.replace( '\'' , '' )
    res = res.replace( ';' , '' )
    res = res.replace( ':' , '' )
    #doc = doc.replace( '-' , '' )
    
    return(res)



# a function for normalizing text, forcing it all to lower-case
    
def normalize_text(doc):
    
    res = doc
    
    #force lowercase
    res = res.lower()
    
    return(res)




# a function for tokenizing text, splitting it up by spaces

def tokenize_text(doc):
    
    res = doc
    
    # split into words by on spaces
    res = res.split( " " )
    
    return(res)


# a function to wrap up the other three text-processes together

def process_collection(coll):
    res_coll = []
    
    for doc in coll:
        
        res_doc = doc
        
        res_doc = clean_text(res_doc)
        res_doc = normalize_text(res_doc)
        res_doc = tokenize_text(res_doc)
        
        res_coll.append(res_doc)
    
    return(res_coll)
        


tokenized_collection = process_collection(collection)


### Indexing!

# a function to build the term-document occurrences
#  we'll use each document's index in the collection list as its doc_ID

def term_doc_occur(tkn_col):
    
    res = []
    
    #loop using integers as the IDs
    for i in range(0, len(tkn_col)):
        
        #for each term
        for term in tkn_col[i]:
            
            #record that term and its ID
            occ = (term, i)
            res.append(occ)
    
    return(res)


occurrences = term_doc_occur(tokenized_collection)
        


# sorting the occurrences

# in this case, we're lucky! the default behavior of sorted()
#  automatically sorts the first term alphabetically,
#  and because the terms were recorded in order

sort_occ = sorted(occurrences)




# merging

# function to merge within documents -- ignoring duplicates

def merge_within(sorted_occurrences):
    
    res = []
    
    #keep track of the last occurrence to compare for duplicates
    prev_occ = None
    
    #looking at each occurrence in the list
    for occ in sorted_occurrences:
        
        # if it's not the same as the previous one, save it
        if occ != prev_occ:
            res.append(occ)
            
        #then update the previous occurrence tracker
        prev_occ = occ
    
    return(res)



sort_unique_occ = merge_within(sort_occ)


# merge between documents to create the postings

def merge_between(unique_occurrences):

    res = []
    
    #track the current term (nothing for now)
    curr_term = None
    
    #and setup an empty postings list
    postings = []
    
    for occ in unique_occurrences:
        
        # if we hit a new term
        if occ[0] != curr_term:
            
            # assuming we don't have an empty list, save it
            if curr_term != None:
                res.append((curr_term, postings))
            
            # and start the postings for a new term
            curr_term = occ[0]
            postings = [occ[1]]
        
        #otherwise, add to the postings
        else:
            postings.append(occ[1])
    
    # add the final postings
    res.append((curr_term, postings))
    
    return(res)
    
        
inverted_index = merge_between(sort_unique_occ)


# define a query

query = "would you??"


# do some text processing

def tokenize_query(query):
    
    #use the text-processing functions from before (inside processed first)
    return(tokenize_text(normalize_text(clean_text(query))))



processed_query = tokenize_query(query)



# retrieve the postings



# a function to retrieve postings from the index
  ## this is actually a really inefficient search structure
  ## later we'll talk about:
  ## - Hash tables
  ## - Search trees

def get_postings(term, inv_index):
    
    res = []
    
    #a pointer to use to walk through the index list
    i = 0
    
    #loop, while we have no result, and we haven't left the index
    while res == [] and i < len(inv_index):
        
        #found the term, grab its postings
        if inv_index[i][0] == term:
            res = inv_index[i][1]
            
        #otherwise, keep looking
        else:
            i += 1
    
    return(res)


  

def get_query_postings(procd_query, inv_index):
    
    res = []
    
    #grab the postings for each term
    for term in procd_query:
        res.append(get_postings(term, inv_index))
        
    return(res)

query_postings = get_query_postings(processed_query, inverted_index)



def sort_postings_by_length(qpostings):
    
    #sort using the function len(), sorts by the length each postings list
    return(sorted(qpostings, key=len))
    
sorted_postings = sort_postings_by_length(query_postings)



# evaluate query


# defining the intersection function

def intersection(postings1, postings2):
    
    res = []

    # pointers into our postings lists
    p1 = 0
    p2 = 0
    
    #as long as neither pointer has fallen off the end of the list
    while (p1 < len(postings1)) and (p2 < len(postings2)):
        
        #if we have a match, save it and advance both pointers
        if postings1[p1] == postings2[p2]:
            res.append(postings1[p1])
            p1 += 1
            p2 += 1
        
        #otherwise, advance the smaller pointer
        else:
            if postings1[p1] < postings2[p2]:
                p1 += 1
            else:
                p2 += 1
    
    return(res)




# function to intersect all of our postings

def intersect_all_postings(query_postings):
    
    #store the intermittent results (starting with the first postings list)
    result = query_postings[0]      
    
    #split the rest of the terms off (using the slice operator)
    remaining = query_postings[1:]  
    
    #loop while we have terms left, and the intermittent result isn't depleted
    while remaining != [] and result != []:
        
        #intersect the intermittent results with the next term
        result = intersection(result, remaining[0]) 
        
        #split the rest of the terms
        remaining = remaining[1:] #slice off the first term
    
    return(result)
        



query_document_IDs = intersect_all_postings(sorted_postings)



# could do some sorting on this list of documents! But we won't for now. 



# print the documents out from the collection

def print_results(query, ids, collection):
    
    #if we found nothing, print a null result
    if ids == []:
        print("No results found for \"%s\"." % (query))
    
    #otherwise, print the list
    else:

        print("Results for: \"%s\"" % (query))
        
        #print each line prettily (result number, docID, and the document's text)
        for i in range(0,len(ids)):
            print("%3d.\t(Doc%3d)\t%s" % (i+1, ids[i], collection[ids[i]]))

print_results(query, query_document_IDs, collection)



################################################


# a function to cleanly wrap up the index-building functions above

def index_collection(collection):
    tokens = process_collection(collection)
    occ = term_doc_occur(tokens)
    sort_occ = sorted(occ)
    sort_unique_occ = merge_within(sort_occ)
    inverted_index = merge_between(sort_unique_occ)
    return(inverted_index)



# a function to cleanly wrap up the query-processing functiongs above

def process_query(query, index, collection):
    procd = tokenize_query(query)
    posts = get_query_postings(procd, index)
    posts_sorted = sort_postings_by_length(posts)
    ids = intersect_all_postings(posts_sorted)
    print_results(query, ids, collection)
    return(ids)


#################################################



# other examples!

sonnets_collection = [
"FROM fairest creatures we desire increase,",
"That thereby beauty's rose might never die,",
"But as the riper should by time decease,",
"His tender heir might bear his memory:",
"But thou, contracted to thine own bright eyes,",
"Feed'st thy light'st flame with self-substantial fuel,",
"Making a famine where abundance lies,",
"Thyself thy foe, to thy sweet self too cruel.",
"Thou that art now the world's fresh ornament",
"And only herald to the gaudy spring,",
"Within thine own bud buriest thy content",
"And, tender churl, makest waste in niggarding.",
"Pity the world, or else this glutton be,",
"To eat the world's due, by the grave and thee.",

"When forty winters shall beseige thy brow,",
"And dig deep trenches in thy beauty's field,",
"Thy youth's proud livery, so gazed on now,",
"Will be a tatter'd weed, of small worth held:",
"Then being ask'd where all thy beauty lies,",
"Where all the treasure of thy lusty days,",
"To say, within thine own deep-sunken eyes,",
"Were an all-eating shame and thriftless praise.",
"How much more praise deserved thy beauty's use,",
"If thou couldst answer 'This fair child of mine",
"Shall sum my count and make my old excuse,'",
"Proving his beauty by succession thine!",
"This were to be new made when thou art old,",
"And see thy blood warm when thou feel'st it cold.",

"Look in thy glass, and tell the face thou viewest",
"Now is the time that face should form another;",
"Whose fresh repair if now thou not renewest,",
"Thou dost beguile the world, unbless some mother.",
"For where is she so fair whose unear'd womb",
"Disdains the tillage of thy husbandry?",
"Or who is he so fond will be the tomb",
"Of his self-love, to stop posterity?",
"Thou art thy mother's glass, and she in thee",
"Calls back the lovely April of her prime:",
"So thou through windows of thine age shall see",
"Despite of wrinkles this thy golden time.",
"But if thou live, remember'd not to be,",
"Die single, and thine image dies with thee.",

"Unthrifty loveliness, why dost thou spend",
"Upon thyself thy beauty's legacy?",
"Nature's bequest gives nothing but doth lend,",
"And being frank she lends to those are free.",
"Then, beauteous niggard, why dost thou abuse",
"The bounteous largess given thee to give?",
"Profitless usurer, why dost thou use",
"So great a sum of sums, yet canst not live?",
"For having traffic with thyself alone,",
"Thou of thyself thy sweet self dost deceive.",
"Then how, when nature calls thee to be gone,",
"What acceptable audit canst thou leave?",
"Thy unused beauty must be tomb'd with thee,",
"Which, used, lives th' executor to be."
]


sonnets_index = index_collection(sonnets_collection)

process_query("thy?", sonnets_index, sonnets_collection)
process_query("DIE?", sonnets_index, sonnets_collection)
process_query("of thyself", sonnets_index, sonnets_collection)
process_query("self-love?", sonnets_index, sonnets_collection)




# Note on hash tables
#  hash tables make handling the inverted index VERY simple!
#  uses text as "keys"
#  vut doesn't have search at all to access the contents
#    - runs in more or less constant time



### Notes:
# 
# ultimately, you'll probably want to use Objects
# 
# working without objects can be fairly brittle
#  - if something about the way you're processing documents changes
#  - or you want to change any of your structures
#  - or add new or interesting meta-data
#
# You might have to rework EVERYthing
# 
# Objects make it easier to change data and processes as you go
#  without having to rebuild from scratch.


