In full spelling, Universal Dependency gammar and Surface Syntax Universal Dependency grammar.

# Tools
[AllenNLP Demo](https://demo.allennlp.org/dependency-parsing)
[CoreNLP Tool](https://corenlp.run/)

# Concepts

- UD: universal dependency
- SUD: (surface) syntactic universal dependency

## UD
*Dependency grammar* (DG) is an approach to the study of the syntax and grammar of natural languages that is quite distinct from *phrase structure grammar* (PSG), which is also known as *constituency grammar*. The modern history of DG begins with [Lucien Tesnière](https://en.wikipedia.org/wiki/Lucien_Tesni%C3%A8re)'s major oeuvre (1959), whereas the modern history of PSG begins arguably with [Noam Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky)'s first prominent work (1957).

DG views linguistic structures in terms of a *one-to-one mapping* of atomic linguistic units to the nodes in structure, whereas PSG assumes a *one-to-one-or-more mapping*. The distinction is clearly visible when one compares the tree structures. The next trees are taken from the [Wikipedia article on DG](https://en.wikipedia.org/wiki/Dependency_grammar):

![[Dependency&Constituency.png]]

## SUD
[Surface Syntactic Universal Dependencies (SUD) | SUD](https://surfacesyntacticud.github.io/
SUD is an annotation scheme for syntactic dependency treebanks, and has a nearly perfect degree of two-way convertibility with the Universal Dependencies scheme (UD). Contrary to UD, it is based on syntactic criteria (favoring functional heads) and the relations are defined on distributional and functional bases.

![Untitled](SUD.png)

### General principles of SUD
- The definition of relations is based on syntactic positions rather than semantic positions.
- Functional heads (instead of lexical heads): The head of a unit is the distributional head, that is, the element that control the distribution of the unit.
- SUD relations are organized in taxonomic hierarchy: A relation that is the daughter of another one inherits its syntactic properties with the addition of specific properties. Indeed, sometimes, we cannot take into account all possible distinctions, either because of the conversion from different treebanks not containing enough information, or because a sentence does not allow to make a clear decision.
- It is possible to distinguish between **arguments** and **modifiers**: Although this distinction involves semantic criteria (an argument of a lexical unit L is an obligatory participant in the semantic description of L), we consider that it is hard to avoid, because especially for verb dependents, most language have special functions.
- A **multiple coordination**, such as *John, Mary and Peter*, is analyzed as a chain instead of a bouquet: One of the main argument for the chain-analysis is that it reduces the dependency length.

### Specific SUD relations
SUD has 4 specific syntactic relations and a few extended relations:
- [subj](https://surfacesyntacticud.github.io/guidelines/u/relations/subj)
- [udep](https://surfacesyntacticud.github.io/guidelines/u/relations/udep)
- [comp](https://surfacesyntacticud.github.io/guidelines/u/relations/comp)
    - [comp:aux](https://surfacesyntacticud.github.io/guidelines/u/relations/comp_aux)
    - [comp:cleft](https://surfacesyntacticud.github.io/guidelines/u/relations/comp_cleft)
    - [comp:obj](https://surfacesyntacticud.github.io/guidelines/u/relations/comp_obj)
    - [comp:obl](https://surfacesyntacticud.github.io/guidelines/u/relations/comp_obl)
    - [comp:pred](https://surfacesyntacticud.github.io/guidelines/u/relations/comp_pred)
- [mod](https://surfacesyntacticud.github.io/guidelines/u/relations/mod)