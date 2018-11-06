# IS

The purpose of this program is natural processing of English into symbolic notation, followed by  the creation of an automated proof of the claim.

Before using:

```
$ pip3 install -U nltk

$ unzip stanford-corenlp-full-2018-02-27

$ cd stanford-corenlp-full-2018-02-27

$ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
-preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
-status_port 9000 -port 9000 -timeout 15000 &
```

