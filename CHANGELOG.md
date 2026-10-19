# Changelog

## 2026-08-26: Update to UD v2.18

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
