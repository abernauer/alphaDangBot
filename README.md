# alphaDangBot
A Prototype or proof-of-concept discord bot for Dan Gheesling's discord server. 


## Setting up a virtual environment and the api token to connect to or to run the bot on the server

1. prerequisites have python and pip installed
2. fork the repo and run git clone on the repo
3. setup a virtual environment
4. Run pip install on the requirements.txt
5. create a file named .env in your working directory
6. set the contents of the DISCORD_TOKEN equal to the token on the Bot page on the developer portal


make the virtual environment:
``` bash
python3 -m venv bot-env
```
activate the virtual environment with the following on Unix and Mac:
```
source bot-env/bin/activate
```
On Windows activate it with:
```
bot-env\Scripts\activate.bat
```

Run pip install on the requirements.txt:
```
python -m pip install -r requirements.txt
```

Create the file named .env in your working directory and substitute your-bot-taken with api token:
```bash
DISCORD_TOKEN=your-bot-token
```

Finally you can run the bot with:
```
python bot.py
```

## Implemented commands

* goals: the goals command returns the community goals of the 596
```
!goals
```
* bruh: returns the dangBRUH emote repeated ten times
```
!bruh
```
* schedule: returns the most recent schedule
```
!schedule
```

* choose: chooses between multiple choices
```
!choose DarkSouls HollowKnight
```
* danglishDict: returns one random entry from the danglish dictionary
```
!danglishDict
```
* awwwa: returns Appreciate Where We Are
```
!awwa
```