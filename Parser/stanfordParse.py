
from nltk.parse import CoreNLPParser
import sys

parser = CoreNLPParser(url='http://localhost:9000')
parseSentence = str(sys.argv[1])
parsed = parser.raw_parse(parseSentence)
print(next(parsed))
