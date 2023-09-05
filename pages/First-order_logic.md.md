---
title: First-order_logic.md
---
# First-order Logic (FOL)

First-order logic (FOL), also known as first-order predicate calculus or simply predicate logic, is a formal system used in mathematics, philosophy, linguistics, computer science, and artificial intelligence to reason about the behavior of objects and their relationships. FOL extends propositional logic by introducing quantifiers and variables, allowing for precise and structured reasoning.

## Syntax of First-order Logic

The syntax of FOL consists of three fundamental components: terms, formulas, and logical symbols. 

### Terms

A term refers to an object in the domain of discourse. It can be a constant, a variable, or a function applied to a set of arguments. Constants represent fixed objects, while variables range over the objects in the domain. Functions take arguments, which can be terms themselves.

### Formulas

Formulas in FOL are constructed using atomic formulas, logical connectives, quantifiers, and variables. Atomic formulas are statements that express relationships between terms using predicates, which are essentially relations. Logical connectives, such as conjunction (AND), disjunction (OR), implication (IF-THEN), and negation (NOT), allow for the composition of more complex formulas. Quantifiers, namely existential quantifier (∃) and universal quantifier (∀), express the scope of variables within a formula.

### Logical Symbols

In addition to the components mentioned above, FOL uses a set of logical symbols to facilitate reasoning. These symbols include:

- ( ) parentheses: used for grouping subformulas
- ¬ negation: represents logical negation
- → implication: expresses logical implication
- ∧ conjunction: denotes logical AND
- ∨ disjunction: represents logical OR
- ∀ universal quantifier: asserts that a formula holds for all objects
- ∃ existential quantifier: asserts that there exists an object for which the formula holds

## Semantics of First-order Logic

The semantics of FOL define the interpretation and meaning of the formulas. It involves defining a domain of discourse, assigning meanings to the predicates, functions, and constants, and interpreting the logical symbols. The semantics determine the truth or falsity of a formula in a given interpretation.

### Models and Satisfaction

A model in FOL represents an interpretation of the formulas in a specific domain. It assigns meaning to the terms, predicates, functions, and constants. Given a model, we can evaluate the truth value of a formula under that interpretation. If a formula is true in a certain model, we say that the model satisfies the formula.

### Soundness and Completeness

Soundness refers to the property that if a formula is provable in FOL using a specific proof system, it is true in all models. Completeness, on the other hand, means that every valid formula that is true in all models can be proven within the system.

## Applications

First-order logic has various applications in different fields, such as:

- Mathematics: FOL provides a foundation for rigorous mathematical reasoning and proofs. It allows mathematicians to express and reason about mathematical structures precisely.
- Philosophy: FOL is used in philosophy for analyzing arguments, formalizing ontologies, and expressing philosophical theories precisely. It helps in logical reasoning and clarifying the meaning of statements.
- Linguistics: FOL is utilized to represent the structure and meaning of natural language sentences. It enables linguists to study sentence structure, meaning, and ambiguity.
- Computer Science and Artificial Intelligence: FOL is fundamental in knowledge representation, automated reasoning, theorem proving, and natural language processing. It serves as the basis for formal logic programming languages, such as Prolog.

## See Also

- [Propositional Logic](Propositional_logic.md)
- [Formal Logic](Formal_logic.md)