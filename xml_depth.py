from xml.etree.ElementTree import XMLParser

class MaxDepth:
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):
        self.depth -= 1
    def data(self, data):
        pass
    def close(self):
        print( self.maxDepth - 1)

target = MaxDepth()
parser = XMLParser(target=target)

xml = '\n'.join([input() for _ in range(int(input()))])

parser.feed(xml)
parser.close()
