# alphaDangBot
A Prototype or proof-of-concept discord bot for Dan Gheesling's discord server. 


## Setting up a virtual environment and the api token to connect to or to run the bot on the server

* prerequisites have python and pip installed
* setup a virtual environment
* install discord.py
* install dotenv

make the virtual environment:
``` bash
python3 -m venv bot-env
```
activate the virtual environment:
```
source bot-env/bin/activate
```
On Windows activate it with:
```
bot-env\Scripts\activate.bat
```

```bash
pip install -U discord.py

```
* create a file named .env in your working directory
* set the contents of the DISCORD_TOKEN equal to the token on the Bot page on the developer portal

```bash
DISCORD_TOKEN=your-bot-token
```

