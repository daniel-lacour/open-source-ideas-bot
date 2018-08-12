#Begin Imports
import re
import tweepy
from github import Github
#End Imports
#Begin Global Variables
g = Github("xxxxxxx")
repo = g.get_repo("open-source-ideas/open-source-ideas")
issues = g.get_repo("open-source-ideas/open-source-ideas").get_issues()
issues_number_list = []
issues_list = []
CONSUMER_KEY ="xxxxx"
CONSUMER_SECRET = "xxxxxxxxxx"   
ACCESS_KEY = "xxxxxxx"    
ACCESS_SECRET = "xxxxxxx"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#End Global Variables
for issue in issues:
    issues_number_list.append(issue.number)
    issues_list.append(issue)
issuelistdoc = open('issuelist.txt', 'w', encoding='utf-8')
for i in issues_list:
    issuelistdoc.write("%s\n" % i)
issuelistdoc.close()
#Takes list of issues and puts them in text file, as well as cleans them up.
inputfile = open("issuelist.txt", 'r', encoding='utf-8')
outputfile = open("issuelist-cleaned.txt","w", encoding='utf-8')
for line in inputfile:
    outputfile.write(re.sub(r'Issue\(title\=|, number=..\)|, number=.\)', '', line))

inputfile.close()
outputfile.close()
#cleaned issue list
finalinf = open('issuelist-cleaned.txt', 'r', encoding='utf-8')
finalin = finalinf.readlines()
finalinf.close()
#previous list
previousf = open('previousissueslist.txt', 'r', encoding='utf-8')
previous = previousf.readlines()
previousf.close()
found = False
for line in finalin:
    if line in previous:
        found = True
    else:
        previousf = open('previousissueslist.txt', 'a', encoding='utf-8')
        previousf.write(line)
        previousf.close()
        tbp = open("currentposts.txt", "a", encoding='utf-8')
        tbp.write(line)
        tbp.close()
tbp = open("currentposts.txt", "r", encoding='utf-8')
newissues = tbp.readlines()
for line in newissues:
    try:
        api.update_status(line)
        print("1")
    except tweepy.error.TweepError:
        print("Error posting: " + line)
        pass
tbp.close()
open('currentposts.txt', 'w').close()