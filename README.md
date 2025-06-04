# AONPRD Crawler
As of now, this is just a simple script to scrape all the PF2 monster images from the [Archives of Nethys](https://2e.aonprd.com/) for use in your VTT of choice.

Note that, at present, the images are `.webp` so if your VTT can't handle that, you'll need to convert them.

You might find the images unsuitable for tokens since they lack borders. If so, I highly recommend the [Tokenizer](https://foundryvtt.com/packages/vtta-tokenizer/) FoundryVTT module, or else [RollAdvantage](https://rolladvantage.com/).

## Usage
`$ pip install -r requirements.txt`

`$ python3 aonprd_crawler.py`

Follow the prompts to give the script the required information.