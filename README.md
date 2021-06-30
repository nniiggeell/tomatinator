Milestone 2 Submission

Team Name: 

Tomatinator-3000

Proposed Level of Achievement: 

Apollo 11 

Motivation 
In this era where fake news is rampant, we want to create an app - TweeterBuddy, that helps users check their tweets for fake news. Moreover, social media cancel culture is brutal and we want to help users avoid it by giving them an idea of their tweet’s sentiment, check for grammatical errors and offensive language. The last thing we want is for our users to lose a million followers overnight! Furthermore, we want the Internet and the social media space to be more inclusive, friendly and warm. This app will encourage users to use kinder language on the micro-blogging website Twitter and in turn make the Internet a safer space.
Aim
We hope to create an application to enhance the utility of twitter by giving people an insight on how their tweet looks before posting it.
User Stories
1. 	As a journalist, I want to tell the correct information to the public.
2. 	As a ‘netizen’, I want to create a culture of acceptance and positivity online.
3. 	As a Twitter user, I want to ensure I don’t consume fake news or propaganda.
4. 	As an influencer, I want to ensure my tweets are not offensive to my followers.
Scope of Project
We are planning to make a mobile application which acts as an enhancement of the twitter app. Our application will have the basic UI which allows users to input a text and find out what the sentiment of the text is, and whether or not the text contains fake news. The “display history” button allows users to look at their previous inputs, see the distribution of words they use for each sentiment and type of news. The “display history” option will provide the user with multiple graphs, highlighting their most used hashtags, and a wordcloud with their most commonly used words for each sentiment and type of news. Currently, the app has a textbox where users can enter their text and get a fake news and sentiment analysis. The interface of the app and the history are under development.
 
Features and timeline
The application holds a database containing previous tweets and their analysis. It makes the user more aware and considerate about their tweets, making twitter a safer and reliable website as a whole.
Main Features:
A textbox for the user to input their text in
A display history feature to showcase the user’s last 5 positive, negative, neutral, real news and fake news tweets in a graphical form
 
Features to be completed by June (Milestone 1 & 2):
1. 	A textbox to write text
2. 	Sentiment analysis of the tweet
3. 	Fake news detection of the tweet
Proof of concepts: examples of our app
 

Things to note
We have yet to create a more sophisticated UI for the app. Currently the app is a very rudimentary version of itself. We plan on imitating Twitter’s UI and allowing the user to post tweets to twitter in real time from the app. The fake news model took longer than expected to be developed so UI could not be developed properly.
The sentiment analysis model has been completed and a telegram bot has been made. Check out @TomatinatorBot on telegram t.me/TomatinatorBot
Features to be completed by the end of July (Milestone 3):
·        Complete development of the UI, making the app more interactive and pleasing to look at
·        Integration of a real-time database, so all tweets made by the user can be stored
·        “Display History” feature, which will allow the user to analyse their tweeting habits
 
How the features will be implemented:
For the frontend, we use flutter. The complete twitter UI can be remade in flutter. We chose flutter as it is flexible and can develop an app for both Android and iOS simultaneously.
We also use python to create the models and the api for the models
For the creation of the models, we use TensorFlow and tweepy, as well as WordCloud python libraries
For the database of users’ tweets, we use Firebase as it is flexible, real-time and has fast in-place updates.
 
Tech Stack
·        Python
·        Flutter
·        Firebase (database to store users’ previous tweets)











Milestone 2 Project Log

S.No
Task
Date
Orbitee 1 (hours)
Orbitee 2 (hours)
Remarks
1
Liftoff
09-05-2021
7
7
Introductory zoom call, advisor meeting, poster and video
2
Team meeting and initial planning
10-05-2021
3
3
Discussed roles, project ideation and timeline
3
Meeting with advisor
12-05-2021
1
1
Met with advisor to discuss project strategy
4
Research and learn python
13-05-2021
3
3
Picked up the basics of the language online and practiced
5
Mission control
15-05-2021
2
2
Attended Git-Mission Control
6
Research and learn Machine Learning
20-05-2021
20
20
Learnt basic ML through online courses
7
Programming the model
21-05-2021
4
4
Programmed the model and tested optimized it
8
Programming the telegram bot
28-05-2021
3
3
Programmed the telegram bot to work with the model
9
Milestone1 wrap-up team meeting
29-05-2021
7
7
Discussed submission details, debugged the bot and polished the code
10
Milestone1 submission meeting
30-05-2021
1
1
Went through the project and uploaded everything to GitHub
11
Team meeting to review milestone 1 peer evaluation
6/2/2021
4
4
Going through reviews and analyzing areas to work on
12
Learning Deep learning
6/9/2021
5
5
Understanding DL for fake news model
13
Learning NLP
6/11/2021
3
3
Understanding NLP for the fake news model
14
Learning flutter
6/15/2021
4
4
learning flutter for app development
15
Making basic text app
6/16/2021
3
3
made the app that takes in an input text in flutter
16
Programming the fake news model
6/18/2021
4
4
researching and programming the fake news model
17
Connecting sentiment analysis model to flutter app
6/19/2021
4
4
made a rest api and connected the frontend with sentiment model
18
Programming the fake news model
6/20/2021
3
3
fixing bugs in the model, improving accuracy
19
learning firebase
6/21/2021
2
2
understood the basics
20
debugging the fake news model
6/22/2021
3
3
debugging and searching for alternative datasets
21
retraining the model with new dataset
6/23/2021
2
2
improving the accuracy of the model
22
uploading fake news model to heroku
6/24/2021
6
6
made an api and uploaded to heroku
23
Connecting fake news model to flutter app
6/25/2021
5
5
uploaded api to heroku and connected flutter frontend with the model
24
Milestone 2 readme, poster
6/27/2021
4
4
redid the readme file and worked on the api
25
Milestone 2 submission meeting
6/28/2021
5
5
finishing touches and wrapped-up milestone 2



Total hours each: 108 hours
