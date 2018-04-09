## Test of chatbot

### Test case

- create a python virtualenv        source <virtualenv>bin/activate
- pip install Flask chatterbot urllib3

- run chatbot  as web serivce
   cd <chatbot_dir>
   python app.py

-test1
http://localhost:5000/chatbot/conversations?question=I need a App, how much it will cost？

-test2
http://localhost:5000/chatbot/conversations?question=需要一个订餐系统，大概多少钱？

### Open tasks

- configure port

- integrate with mainriversoft.com as chatbot

-