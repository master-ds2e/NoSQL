import json
import pymongo
import datetime
#%% Homework I

client = pymongo.MongoClient('localhost', 27017)
mydb = client["Chapter_II"]
collection = mydb["Homework_1"]

with open('../data/pubmed_last_100k.json', encoding="utf8") as json_file:
    data = json.load(json_file)

[paper.pop('_id') for paper in data]
collection.insert_many(data)


#1) Create an index, explain your choice of key.

collection.create_index([ ("pmid",1) ])

#2) How many paper have a single author ? Two authors ?

print("Number of paper with one author", collection.count_documents({"author":{"$size":1}}))
print("Number of paper with two authors", collection.count_documents({"author":{"$size":2}}))

#3) What's the last paper inserted in the db ?

docs = collection.find().sort([("_id",-1)]).limit(10)
print("The last paper inserted has pmid : ",next(docs)['pmid'])

#4) Find articles with null value meshwords.

print("Number of paper with one author", collection.count_documents({"meshwords":{'$eq':None}}))

#5) Choose a keyword you are interested in (machine learning, computer vision,...). Find the number of articles with the choosen keyword in their meshwords or abstract.
docs = collection.find({"$or":[ { "abstract":{"$exists":1,"$regex" : ".*Deep learning.*"}},
                                {"meshwords":{"$exists":1,"$elemMatch" : {"$regex" : ".*Deep learning.*"}}} ]})
next(docs)                   

#6) What's the number of articles that have atleast one affiliation AND keywords.
docs = collection.find({ "author": {
        '$exists': 1, 
        '$elemMatch': { "affiliation": {'$exists': 1 } } 
    }
})

#7) How many articles have a publishing date after 2019 ?.
date_string = "01/01/2019"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
timestamp = datetime.datetime.timestamp(date)

print("Number of paper with one author", collection.count_documents({'unix':{'$gt':timestamp}}))

#8) Find articles where there's atleast one affiliation from "China".
docs = collection.find({"authors":
                        {"$exists":1,"$elemMatch" : {"affiliation" : 
                                                     {"$exists": 1, "$elemMatch" :{"name": {'$exists': 1,"$regex" : ".*Portugal.*" }}}}
                                }
                        }
                       )
next(docs)
#9) Check for any duplicates.

#10) Remove every articles where abstract starts with an "R".

#11) Select papers where number of authors = number of affilation.

#%% Homework II


import requests
import re
from collections import defaultdict
from lxml import etree
import tqdm
import time

def xml_to_dict(tree, paths=None, nsmap=None, strip_ns=False):
    """Convert an XML tree to a dictionary.
    :param tree: etree Element
    :type tree: :class:`lxml.etree._Element`
    :param paths: An optional list of XPath expressions applied on the XML tree.
    :type paths: list[basestring]
    :param nsmap: An optional prefix-namespace mapping for conciser spec of paths.
    :type nsmap: dict
    :param strip_ns: Flag for whether to remove the namespaces from the tags.
    :type strip_ns: bool
    """
    paths = paths or ['.//']
    nsmap = nsmap or {}
    fields = defaultdict(list)
    for path in paths:
        elements = tree.findall(path, nsmap)
        for element in elements:
            tag = re.sub(
                r'\{.*\}', '', element.tag) if strip_ns else element.tag
            fields[tag].append(element.text)
    return dict(fields)

sets = ["cs","stat","q-fin"]
XMLParser = etree.XMLParser(remove_blank_text=True, recover=True, resolve_entities=False)


for set_ in tqdm.tqdm(sets):
    response = requests.get("http://export.arxiv.org/oai2?verb=ListIdentifiers&set={}&from=2010-01-01&metadataPrefix=oai_dc".format(set_))
    tree = etree.XML(response.content, parser=XMLParser)
    papers = xml_to_dict(tree=tree)
    ids = [id_.split(":")[-1] for id_ in papers["{http://www.openarchives.org/OAI/2.0/}identifier"]]
    arxiv_txt = open('../data/arxiv_Homework_2.txt', 'a')
    [arxiv_txt.write(id_ + "\n") for id_ in ids]
    arxiv_txt.close()
    if len(papers) == 7:
        time.sleep(20)
        continue
    token = papers["{http://www.openarchives.org/OAI/2.0/}resumptionToken"][0]
    time.sleep(20)
    done = False
    while done == False:
            response = requests.get("http://export.arxiv.org/oai2?verb=ListIdentifiers&resumptionToken={}".format(token))
            tree = etree.XML(response.content, parser=XMLParser)
            papers = xml_to_dict(tree=tree)
            ids = [id_.split(":")[-1] for id_ in papers["{http://www.openarchives.org/OAI/2.0/}identifier"]]
            if len(ids) != 10000:
                done = True
            arxiv_txt = open('../data/arxiv_Homework_2.txt', 'a')
            [arxiv_txt.write(id_ + "\n") for id_ in ids]
            arxiv_txt.close()
            if len(papers) == 7:
                done = True
            else:
                token = papers["{http://www.openarchives.org/OAI/2.0/}resumptionToken"][0]
            time.sleep(20)


import requests
import feedparser
import tqdm
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client["Chapter_II"]
collection = mydb["Homework_2"]


with open("../data/arxiv_Homework_2.txt","r") as lines:
    ids = lines.read().split("\n")[0:-2]

results = {}
ids_query = []
iteration = 1

for id_ in tqdm.tqdm(ids):
    if iteration % 100 != 0:
        iteration += 1
        ids_query.append(id_)
    else:
        ids_query = ",".join(ids_query)
        response = requests.get('http://export.arxiv.org/api/query?id_list={}&max_results=100'.format(ids_query))
        feed = feedparser.parse(response.content)
        list_of_insertion = []
        for entry in feed.entries:
            list_of_insertion.append(dict(entry))
        collection.insert_many(list_of_insertion)
        ids_query = []
        iteration = 1
        time.sleep(1/3)

#1) Create an index, explain your choice of key.

#2) How many paper have a single author ? Two authors ?

#3) What's the last paper inserted in the db ?

#4) Find the number of articles with "technology" in their keyword or abstract.

#5) Find articles with missing keywords.

#6) What's the number of articles that have an affiliation AND keywords.

#7) How many articles have a publishing date after 2019 ?.

#8) Find articles where there's atleast one affiliation from "China".

#9) Check for any duplicates.

#10) Remove every articles where abstract starts with an "R".

#11) Select papers where number of authors = number of affilation.
