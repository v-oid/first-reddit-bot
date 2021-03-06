import praw
import config
import time
import os

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "void_stalkr's first test bot v0.0")
	print ("Logged in!")

	return r


def run_bot(r, comments_replied_to):
	print ("Obtaining 25 comments...")

	for comment in r.subreddit('test').comments(limit = 25):
		if "dog" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print ("String with \"dog\" found in comment " + comment.id)
			comment.reply("I also love doggos! [Here](https://i.imgur.com/7HffT4j.gifv) is an image of one")
			print ("Replied to comment " + comment.id)

			comments_replied_to.append(comment.id)
			
			with open ("comments_replied_to.txt", "a") as replies:
				replies.write(comment.id + "\n")

	print ("Sleeping for 10 seconds")
	#Sleep for 10 seconds...
	time.sleep(10)

def fetch_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as replies:
			comments_replied_to = replies.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)
	return comments_replied_to

r = bot_login()
comments_replied_to = fetch_saved_comments()
print (comments_replied_to)

while True:
	run_bot(r, comments_replied_to)