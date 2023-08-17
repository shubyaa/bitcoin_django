class Coin:
    def __init__(self, id, symbol, image, current_price, sparkline, last_updated):
        self.id = id
        self.symbol = symbol
        self.image = image
        self.current_price = current_price
        self.sparkline = sparkline
        self.last_updated = last_updated


class News:
    def __init__(self, title, media, link, summary):
        self.title = title
        self.media = media
        self.link = link
        self.summary = summary
