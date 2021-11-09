#######
# IMPORT PACKAGES
#######

import praw
import pandas as pd


# Acessing the reddiwt api


reddit = praw.Reddit(client_id='SCCAe_MW2AQRpRyBnD9Vkw', #my client id
                     client_secret='YUCw18b32GVwqvMaWGljIG2EIZYuIw',  #your client secret
                     user_agent='PRAW_test', #user agent name
                     username = '',     # your reddit username
                     password = '')     # your reddit password

# reddit = praw.Reddit(client_id='IxcfGusFJcBM05qIHFj7_g',
#                      client_secret='0iou0P1Iv-Uncf0qKjR2ZQCWBkrH7w',
#                      user_agent='PRAW_test')

sub = ['Askreddit']  # make a list of subreddits you want to scrape the data from
print(reddit)

 

for s in sub:
    subreddit = reddit.subreddit(s)   # Choosing the subreddit


########################################
#   CREATING DICTIONARY TO STORE THE DATA WHICH WILL BE CONVERTED TO A DATAFRAME
########################################

#   NOTE: ALL THE POST DATA AND COMMENT DATA WILL BE SAVED IN TWO DIFFERENT
#   DATASETS AND LATER CAN BE MAPPED USING IDS OF POSTS/COMMENTS AS WE WILL 
#   BE CAPTURING ALL IDS THAT COME IN OUR WAY

# SCRAPING CAN BE DONE VIA VARIOUS STRATEGIES {HOT,TOP,etc} we will go with keyword strategy i.e using search a keyword
    query = ['antivax']

    for item in query:
        post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : []
        }
        comments_dict = {
            "comment_id" : [],
            "comment_parent_id" : [],
            "comment_body" : [],
            "comment_link_id" : []
        }
        for submission in subreddit.search(query,sort = "top",limit = 100):
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.score)
            post_dict["id"].append(submission.id)
            post_dict["url"].append(submission.url)
            post_dict["comms_num"].append(submission.num_comments)
            post_dict["created"].append(submission.created)
            post_dict["body"].append(submission.selftext)
            
            ##### Acessing comments on the post
            submission.comments.replace_more(limit = 100)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)
        
        post_comments = pd.DataFrame(comments_dict)

        post_comments.to_csv(s+"_comments_"+ item +"subreddit.csv")
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(s+"_"+ item +"subreddit.csv")