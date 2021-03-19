import os


def get_wishlist():
    '''Returns a list of securities based on some criterias scraped from many sources '''
    return ['Bitcoin', 'Ethereum', 'Cardano']


def get_analysis(security):
    '''return Sentiment, Technical and Fundamental analysis for a security on a scale of 1-10'''
    return {"data": {"sentiments": 6, "technical": 7, "fundamental": 5}}


def register_for_notifications(email, phoneNumber):
    '''registers an email and or phone number for notifications'''


if __name__ == '__main__':
    main()
