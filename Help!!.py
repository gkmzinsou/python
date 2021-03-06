
# List of references in article 1
cite_art1 = ["art2","art3","art4","art5"] 
cite_art2 = ["art3","art4","art5"]
cite_art3 = ["art4","art5"]
cite_art4 = ["art3","art5"]
cite_art5 = ["art1","art2"]

# key = articleID 
# value = list of articles that cite the article in key 
cites = {"art1":cite_art1,"art2":cite_art2,"art3":cite_art3,"art4":cite_art4,"art5":cite_art5}


def populatesCitedBy(dictArticleToCitationList):
    new = {}       # empty dictionary that I want to populate with this function         
    res = []
    for articleID in dictArticleToCitationList.keys():         
        for key, value in dictArticleToCitationList.items():
            if articleID in value :
                res.append(key)
    return res

print(populatesCitedBy(cites))

#Results : ['art5', 'art1', 'art5', 'art1', 'art2', 'art4', 'art1', 'art2', 'art3', 'art1', 'art2', 'art3', 'art4']

#What I want :
new = {"art1":["art5"],
       "art2":["art1","art5"],
       "art3":["art1","art2","art4"],
       "art4":["art1","art2","art3"],
       "art5":["art1", "art2", "art3", "art4"]}