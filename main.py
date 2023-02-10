from dfa import *
from dfaMinimize import *
from nfatoDfa import *

dfa1 = DFA(
    Q={'q0', 'q1', 'q2','q3','q4','q5'},
    sigma={'a', 'b'},
    initialState='q0',
    accept={'q2'},
    delta={
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q3', 'b': 'q2'},
        'q2': {'a': 'q3', 'b': 'q3'},
        'q3': {'a': 'q3', 'b': 'q3'},
        'q4': {'a': 'q2', 'b': 'q1'},
        'q5': {'a': 'q1', 'b': 'q2'}

    }
)

dfa2 = DFA(
    Q={'A', 'B', 'C','D'},
    sigma={'a', 'b'},
    initialState='A',
    accept={'B','D'},
    delta={
        'A': {'a': 'C', 'b': 'B'},
        'B': {'a': 'B', 'b': 'A'},
        'C': {'a': 'D', 'b': 'D'},
        'D': {'a': 'A', 'b': 'D'}
    }
)
# phase 1
# class defined
print(dfa2.acceptsornot("abab"))
print(dfa2.isEmpty())
print(dfa2.isLangInfinite())
dfa2.numberOfElementsInLang()
dfa2.shortestString()
dfa2.longestString()
print(dfa2.complimentDFA())


# phase 2
print(dfa1.union(dfa2))
# print(DFA.union(dfa1,dfa2))

print(dfa1.intersection(dfa2))
# print(DFA.intersection(dfa1,dfa2))

print(dfa1.subtract(dfa2))
# print(DFA.subtract(dfa1,dfa2))

# print(dfa1.isSubset(dfa2))
# print(DFA.isSubset(dfa1,dfa2))

# print(dfa1.areSeparatedSets(dfa2))
# print(DFA.areSeparatedSets(dfa1,dfa2))


# phase 3

# myMinimizer = Minimize()
# minimizedDFA = myMinimizer.minimizer(dfa1)
# print(minimizedDFA.delta)




#
# nfa1 = NFA(
#     Q={'q0', 'q1', 'q2','q3','q4','q5'},
#     sigma={'a', 'b','e'}, # e stands for lambda
#     initialState='q0',
#     accept={'q2'},
#     delta={
#         'q0': {'a': {'q1'}, 'e': {'q3'}},
#         'q1': {'a': {'q3','q2'}},
#         'q2': {'a': {'q3'}, 'b': {'q3'}},
#         'q3': {'a': {'q4'}},
#         'q4': {'a': {'q2'}, 'b': {'q1'}},
#         'q5': {'a': {'q1','q4'}, 'b': {'q2'}}
#
#     }
# )
#
# nfa1.nfaToDfa()






