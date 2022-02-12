# dvmn_bitly

# CLI bitly url shorterer

Run the app on a command line. Then just insert a link with https://. If there is a bitlink - you'll get a click counter. If not - will get a new bitly link. As an option you can run the app with argument -l. Example:
```
python main.py -l https://github.com
```
So you will see a new bitlink for the 
```
https://github.com
```

### How to install

Firstly you have to get a bearer token from (https://bit.ly). More info you find here: [get bitly token](https://dev.bitly.com/)

When you have a token it should be put on ```.env``` file in working directory like this:
```BITOKEN = 'Bearer 3f84de3b0f4f04117372d8b69691f2cfd584b356'```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).