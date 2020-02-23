from get_video import *
def test_tweet2video():
    assert tweet2video('blakelively','blakelively')
    assert tweet2video('EXO','EXO')
    assert tweet2video('sehun','sehun')
    assert tweet2video('baekhyun','baekhyun')
    assert tweet2video('evanlin','evanlin')
    assert tweet2video('chanyeol','chanyeol')
