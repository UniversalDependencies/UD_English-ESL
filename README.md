# Summary

UD English-ESL / Treebank of Learner English (TLE) contains manual POS tag and dependency annotations for 5,124 English as a Second Language (ESL) sentences drawn from the Cambridge Learner Corpus First Certificate in English (FCE) dataset.

# Introduction

UD English-ESL/TLE is a collection of 5,124 English as a Second Language (ESL) sentences (97,681 words), manually annotated with POS tags and dependency trees in the Universal Dependencies formalism. Each sentence is annotated both in its original and error corrected forms. The annotations follow the standard English UD guidelines, along with a set of supplementary guidelines for ESL. The dataset represents upper-intermediate level adult English learners from 10 native language backgrounds, with over 500 sentences for each native language. The sentences were randomly drawn from the Cambridge Learner Corpus First Certificate in English (FCE) corpus. The treebank is split randomly to a training set of 4,124 sentences, development set of 500 sentences and a test set of 500 sentences. 

A query engine and further information on the treebank is available at <https://lacclab-esl-treebank.dds.technion.ac.il>.

# Obtaining the text and a treebank of error corrected sentences

Due to FCE licensing restrictions, the annotations are released without the text.

To merge the annotations with the corresponding FCE sentences, please follow these steps (require python).
1) Download the FCE dataset from <https://www.ilexir.co.uk/datasets/index.html>
to the current directory, thereby signing the FCE license agreement.
2) Unzip the downloaded file fce-released-dataset.zip.
3) Run "python merge.py" to obtain the annotation files with the FCE sentences. 

The downloaded folder will also contain a parallel treebank of error corrected sentences.

# Metadata

* sent_id = [folder_name]-[file_name]-[sent_index]: sentence identifier.
/folder_name/file_name is the path to the FCE document from which the sentence was obtained.
sent_index is the sentence number (with respect to the automatic sentence tokenization).

# Changelog

## 2026-11-15 v2.18
The UD English-ESL treebank was revised to bring the annotation into compliance with the current UD v2.18 validation requirements. Corrections were based on the original manually annotated treebank and the original MIT ESL annotation guidelines wherever possible.

### SYNTAX changes

#### Dependency structure corrections

- Manually reviewed and corrected dependency structures reported as invalid by the UD validator.
- Corrected `leaf-det` configurations in which a token attached with the `det` relation incorrectly governed a dependent that is not permitted under a determiner. Such dependents were reattached or the surrounding structure was reanalysed according to the original manual annotation.
- Corrected `obl-should-be-nmod` configurations. Dependents annotated as `obl` under non-predicative nominal heads were changed to `nmod`, following the UD distinction between oblique dependents of predicates and nominal modifiers.
- Other erroneous attachment structures were manually checked against the original annotation and corrected rather than modified automatically.

#### UPOS–dependency relation compatibility

- Reviewed all validator errors in which a dependency relation was incompatible with the dependent token's UPOS.
- Corrected incompatible `det` annotations so that the relation and the POS analysis agree.
- Corrected incompatible `case` annotations, including cases where tokens with nominal, adjectival, or determiner POS tags had incorrectly been assigned the `case` relation.
- Corrected incompatible `advmod`, `aux`, `mark`, `cc`, and related relation/POS combinations where present.
- Corrected mismatches between `PUNCT` and the `punct` relation.
- Each mismatch was resolved using the original manual annotation and sentence context rather than by blindly replacing either the UPOS tag or dependency relation.

These changes address the validator's `rel-upos-*` family of checks.

#### Multiple subjects and objects in learner constructions

- Manually reviewed predicates annotated with more than one ordinary `nsubj`/`csubj`, which trigger the `too-many-subjects` validation check.
- Manually reviewed predicates annotated with more than one `obj`, which trigger the `too-many-objects` validation check.
- Where the original structure reflects an ESL production in which an additional constituent can be interpreted as a subject or object, the dependency tree was reanalysed into a UD-valid structure.
- The original learner-oriented interpretation was retained in MISC using:
  - `Note=parses_as_nsubj`
  - `Note=parses_as_obj`

The MISC notes document the alternative interpretation of the learner construction; they are not used as substitutes for a valid basic dependency structure.

#### Punctuation

- Reviewed punctuation attachments throughout the treebank against the original MIT annotation guidelines and current UD punctuation constraints.
- Corrected punctuation attachments that introduced non-projectivity or in which the punctuation token itself was attached non-projectively.
- Corrected cases in which the `punct` relation and the token's UPOS disagreed.
- Preserved the original intended punctuation structure whenever it was compatible with current UD requirements.

These changes address, where applicable, the `punct-causes-nonproj`, `punct-is-nonproj`, `rel-upos-punct`, and `upos-rel-punct` validation checks.

### MORPHO changes

#### `goeswith` structures

- Reannotated tokenized typographical errors and accidentally separated word parts according to current UD `goeswith` guidelines.
- The first component of each interrupted word is treated as the head of the `goeswith` structure and retains the word's lexical and morphological annotation.
- Subsequent components are attached to the first component with `goeswith`.
- Non-initial `goeswith` components were changed to `UPOS=X`.
- Morphological features were removed from non-initial `goeswith` components so that the word-level morphology is represented only on the first component.
- `goeswith` groups were checked to ensure that all components are contiguous, genuinely separated by whitespace, and attached in the correct left-to-right direction.

These changes address the validator's `goeswith-upos`, `goeswith-feats`, `goeswith-lemma`, `goeswith-gap`, `goeswith-nospace`, and related `goeswith` checks.

#### Typographical errors

- Added `Typo=Yes` to the FEATS of heads of `goeswith` structures, as required by current UD validation when morphological features are present.
- Added `Typo=Yes` to applicable typographical errors identified in the original learner annotation.
- Automatically converted identifiable typo annotations from the source representation, followed by manual verification.

This specifically resolves the `goeswith-missing-typo` validation condition for split-word errors.

### FEATS changes

- Populated the previously sparse FEATS column using morphological information converted from the original manually annotated source.
- Added UD morphological features to tokens for which corresponding morphological information is available in the source annotation.
- Added required `PronType` values to pronouns and determiners where applicable, avoiding `pron-det-without-prontype` validation warnings once the treebank contains morphological features.
- Preserved and integrated existing features such as `Foreign=Yes` and `Polarity=Neg`.
- Ensured that FEATS are attached to the appropriate component of `goeswith` structures rather than duplicated across split word parts.
- Automatically converted feature values were manually checked for consistency with their UPOS tags and sentence context.

### MISC changes

- Populated MISC with information needed to preserve analyses of learner-specific constructions that cannot be represented directly by the validator-compliant basic dependency tree.
- Added `Note=parses_as_obj` where an ESL construction contains a constituent that can naturally be interpreted as an additional direct object but cannot remain as a second `obj` under the same predicate.
- Added `Note=parses_as_nsubj` where an ESL construction contains a constituent that can naturally be interpreted as an additional subject but cannot remain as a second ordinary `nsubj` under the same predicate.
- These annotations preserve information about the original learner construction without deliberately retaining dependency structures rejected by current UD validation.

## 2018-11-15 v2.3
 - transitioned to v2 guidelines.
 - fixes to miscellaneous syntactic issues.

## 2016-11-15 v1.4
 - changed UPOS of indefinite, totality and negative pronouns from NOUN to PRON.
 - changed UPOS of demonstrative pronouns from DET to PRON.

# Acknowledgments

The dataset and the annotation guidelines were developed at MIT and at the Technion University by Yevgeni Berzak, Jessica Kenney, Carolyn Spadine, Jing Xian Wang, Lucia Lam, Keiko Sophie Mori, Sebastian Garza, Boris Katz, Margarita Misirpashayeva and Rivkah Bazlov.

# Citation

You are encouraged to cite the following papers when using the TLE:

    @inproceedings{berzak2016tle,
      author    = {Berzak, Yevgeni and Kenney, Jessica and Spadine, Carolyn and Wang, Jing Xian and Lam, Lucia and Mori, Keiko Sophie and Garza, Sebastian and Katz, Boris},
      title     = {Universal Dependencies for Learner English},
      booktitle = {Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
      year      = {2016},
      publisher = {Association for Computational Linguistics},
      pages     = {737--746},
      url       = {http://www.aclweb.org/anthology/P16-1070}
    }

    @inproceedings{yannakoudakis2011fce,
     title={A new dataset and method for automatically grading ESOL texts},
     author={Yannakoudakis, Helen and Briscoe, Ted and Medlock, Ben},
     booktitle={Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies-Volume 1},
     pages={180--189},
     year={2011},
     organization={Association for Computational Linguistics}
    }

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v1.3
License: CC BY-SA 4.0
Includes text: no
Parallel: no
Genre: learner-essays
Lemmas: automatic
UPOS: manual native
XPOS: manual native
Features: converted from manual
Relations: manual native
Contributors: Berzak, Yevgeni; Kenney, Jessica; Spadine, Carolyn; Wang, Jing Xian; Lam, Lucia; Mori, Keiko Sophie; Garza, Sebastian; Katz, Boris; Misirpashayeva, Margarita; Bazlov, Rivkah;
Contributing: elsewhere
Contact: r_udp@bazlov.uk; berzak@technion.ac.il
===============================================================================
</pre>

