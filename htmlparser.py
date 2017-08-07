from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        if attrs:
            print('\n'.join('-> {} > {}'.format(*el) for el in attrs))
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        if attrs:
            print('\n'.join('-> {} > {}'.format(*el) for el in attrs))


parser = MyHTMLParser()

N = int(input())
while N > 0:
    N = N - 1
    parser.feed(input())
