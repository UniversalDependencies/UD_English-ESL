Treebank of Learner English (TLE)

===GENERAL===

Manual POS tag and dependency annotations for 5,124 English as a Second
Language (ESL) sentences. The sentences are drawn from the Cambridge Learner
Corpus First Certificate in English (FCE) dataset. The annotations follow the 
standard English UD guidelines, along with a set of supplementary guidelines 
for ESL. The treebank is split randomly to a training set of 4,124 sentences,
development set of 500 sentences and a test set of 500 sentences.
Further information is available on esltreebank.org

===STATISTICS===

Tree count:  5124
Word count:  97681
Token count: 97681
Dep. relations: 46 of which 7 language specific
POS tags: 17
Category=value feature pairs: 0

===DATA===

Due to FCE licensing restrictions, the annotations are released without 
the data. To merge the annotations with the corresponding FCE sentences, 
please follow these steps (require python).
1) Download the FCE dataset from http://ilexir.co.uk/applications/clc-fce-dataset/
to the current directory, thereby signing the FCE license agreement.
2) Unzip the downloaded file fce-released-dataset.zip. 
3) Run "python merge.py" to obtain annotation files with the FCE sentences.

===METADATA===

#ID=[document_id] [sent_id]: sentence identifier. 
doc_id is the path to the FCE document from which the sentence was obtained. 
sent_id is the sentence number (with respect to the automatic sentence tokenization).
#SENT=[sentence]: the error annotated xml version of the FCE sentence.
Available only in the merged version.

===CITATION===

You are encouraged to cite the following papers when using the treebank:

Yevgeni Berzak, Jessica Kenney, Carolyn Spadine, Jing Xian Wang, Lucia Lam, 
Keiko Sophie Mori, Sebastian Garza and Boris Katz (2016) "Universal Dependencies 
for Learner English", arXiv preprint.

Helen Yannakoudakis, Ted Briscoe and Ben Medlock (2011) "A New Dataset and 
Method for Automatically Grading ESOL Texts", In Proceedings of the 49th 
Annual Meeting of the Association for Computational Linguistics: Human 
Language Technologies (ACL), pages 180–189.

=== Machine-readable metadata ===

Documentation status: complete
Data source: manual
Data available since: UD v1.3
License: CC BY-SA 4.0
Genre: learner-essays
Contributors: Berzak, Yevgeni; Kenney, Jessica; Spadine, Carolyn; Wang, Jing Xian; Lam, Lucia; Mori, Keiko Sophie; Garza, Sebastian; Katz, Boris
