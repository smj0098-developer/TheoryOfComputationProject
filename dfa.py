import itertools
import copy


class DFA:
    def __init__(self, Q: set[str], sigma: set[str], initialState: str, accept: set[str], delta: dict):
        self.Q = Q
        self.sigma = sigma
        self.initialState = initialState
        self.accept = accept
        self.delta = delta

    def acceptsornot(self, input: str) -> bool:
        currentState = self.initialState
        for char in input:
            currentState = self.delta[currentState][char]
        if currentState in self.accept:
            return True
        else:
            return False

    def isEmpty(self):
        allpermutationslist = []
        for n in range(1, len(self.Q)):
            allpermutationslist += ["".join(p) for p in itertools.product(self.sigma, repeat=n)]
        for item in allpermutationslist:
            if (self.acceptsornot(item)):
                return False
        return True

    def isLangInfinite(self):
        allpermutationslist = []
        for n in range(len(self.Q), 2 * len(self.Q)):
            allpermutationslist += ["".join(p) for p in itertools.product(self.sigma, repeat=n)]
        for item in allpermutationslist:
            if (self.acceptsornot(item)):
                return (True, item)
        return False

    def numberOfElementsInLang(self):
        elementCounter = 0
        if (self.isLangInfinite()):
            print("The language is infinite")
        else:
            allpermutationslist = []
            for n in range(1, len(self.Q)):
                allpermutationslist += ["".join(p) for p in itertools.product(self.sigma, repeat=n)]
            for item in allpermutationslist:
                if (self.acceptsornot(item)):
                    elementCounter += 1
            print(elementCounter, "element(s) are in this language")

    def shortestString(self):
        if (self.isEmpty()):
            print("The language is empty")
        else:
            allpermutationslist = []
            for n in range(1, len(self.Q)):
                allpermutationslist += ["".join(p) for p in itertools.product(self.sigma, repeat=n)]
            for item in allpermutationslist:
                if (self.acceptsornot(item)):
                    print("The shortest string is", len(item), "character(s) long")
                    break

    def longestString(self):
        if (self.isLangInfinite()):
            print("The language is infinite")
        else:
            allpermutationslist = []
            for n in range(1, len(self.Q)):
                allpermutationslist += ["".join(p) for p in itertools.product(self.sigma, repeat=n)]
            for item in allpermutationslist[::-1]:
                if (self.acceptsornot(item)):
                    print("The longest string is", len(item), "character(s) long")
                    break

    def complimentDFA(self):
        complimentDFA = copy.deepcopy(self)
        complimentDFA.accept = self.Q - self.accept
        return complimentDFA

    def union(self, anotherDFA):
        # generating states for Q and the transition function delta
        newQ = set()
        newdelta = {}
        for state in self.Q:
            for state2 in anotherDFA.Q:
                newQ.add(state + state2)
                newdelta[state + state2] = {"a": self.delta[state]["a"] + anotherDFA.delta[state2]["a"],
                                            "b": self.delta[state]["b"] + anotherDFA.delta[state2]["b"]}
        # print(newQ)

        # generating states for accept
        newaccept = set()
        for state in self.accept:
            for state2 in anotherDFA.Q:
                newaccept.add(state + state2)
        for state in self.Q:
            for state2 in anotherDFA.accept:
                newaccept.add(state + state2)

        # print(newaccept)

        newDFA = DFA(
            Q=newQ,
            sigma={'a', 'b'},
            initialState=self.initialState + anotherDFA.initialState,
            accept=newaccept,
            delta=newdelta
        )
        return newDFA

    def intersection(self, anotherDFA):
        # generating states for Q and the transition function delta
        newQ = set()
        newdelta = {}
        for state in self.Q:
            for state2 in anotherDFA.Q:
                newQ.add(state + state2)
                newdelta[state + state2] = {"a": self.delta[state]["a"] + anotherDFA.delta[state2]["a"],
                                            "b": self.delta[state]["b"] + anotherDFA.delta[state2]["b"]}
        # print(newQ)

        # generating states for accept
        newaccept = set()
        for state in self.accept:
            for state2 in anotherDFA.accept:
                newaccept.add(state + state2)
        # print(newaccept)

        newDFA = DFA(
            Q=newQ,
            sigma={'a', 'b'},
            initialState=self.initialState + anotherDFA.initialState,
            accept=newaccept,
            delta=newdelta
        )
        return newDFA

    def subtract(self, anotherDFA):
        # generating states for Q and the transition function delta
        newQ = set()
        newdelta = {}
        for state in self.Q:
            for state2 in anotherDFA.Q:
                newQ.add(state + state2)
                newdelta[state + state2] = {"a": self.delta[state]["a"] + anotherDFA.delta[state2]["a"],
                                            "b": self.delta[state]["b"] + anotherDFA.delta[state2]["b"]}
        # print(newQ)

        # generating states for accept
        newaccept = set()
        for state in self.accept:
            for state2 in anotherDFA.Q:
                newaccept.add(state + state2)
        for state in self.Q:
            for state2 in anotherDFA.accept:
                newaccept.discard(state + state2)

        newDFA = DFA(
            Q=newQ,
            sigma={'a', 'b'},
            initialState=self.initialState + anotherDFA.initialState,
            accept=newaccept,
            delta=newdelta
        )
        return newDFA

    def isSubset(self, anotherDFA):
        subtractedDFA = self.subtract(anotherDFA)
        if (subtractedDFA.isEmpty()):
            return True
        else:
            return False

    def areSeparatedSets(self, anotherDFA):
        intersectionDFA = self.intersection(anotherDFA)
        if (not intersectionDFA.isEmpty()):
            return False
        else:
            return True


def union(self, thisDFA, anotherDFA):
    # generating states for Q and the transition function delta
    newQ = set()
    newdelta = {}
    for state in thisDFA.Q:
        for state2 in anotherDFA.Q:
            newQ.add(state + state2)
            newdelta[state + state2] = {"a": thisDFA.delta[state]["a"] + anotherDFA.delta[state2]["a"],
                                        "b": thisDFA.delta[state]["b"] + anotherDFA.delta[state2]["b"]}
    # print(newQ)

    # generating states for accept
    newaccept = set()
    for state in thisDFA.accept:
        for state2 in anotherDFA.Q:
            newaccept.add(state + state2)
    for state in thisDFA.Q:
        for state2 in anotherDFA.accept:
            newaccept.add(state + state2)

    # print(newaccept)

    newDFA = DFA(
        Q=newQ,
        sigma={'a', 'b'},
        initialState=thisDFA.initialState + anotherDFA.initialState,
        accept=newaccept,
        delta=newdelta
    )
    return newDFA


def intersection(self, thisDFA, anotherDFA):
    # generating states for Q and the transition function delta
    newQ = set()
    newdelta = {}
    for state in thisDFA.Q:
        for state2 in anotherDFA.Q:
            newQ.add(state + state2)
            newdelta[state + state2] = {"a": thisDFA.delta[state]["a"] + anotherDFA.delta[state2]["a"],
                                        "b": thisDFA.delta[state]["b"] + anotherDFA.delta[state2]["b"]}
    # print(newQ)

    # generating states for accept
    newaccept = set()
    for state in thisDFA.accept:
        for state2 in anotherDFA.accept:
            newaccept.add(state + state2)
    # print(newaccept)

    newDFA = DFA(
        Q=newQ,
        sigma={'a', 'b'},
        initialState=thisDFA.initialState + anotherDFA.initialState,
        accept=newaccept,
        delta=newdelta
    )
    return newDFA


def subtract(self, thisDFA, anotherDFA):
    # generating states for Q and the transition function delta
    newQ = set()
    newdelta = {}
    for state in thisDFA.Q:
        for state2 in anotherDFA.Q:
            newQ.add(state + state2)
            newdelta[state + state2] = {"a": thisDFA.delta[state]["a"] + anotherDFA.delta[state2]["a"],
                                        "b": thisDFA.delta[state]["b"] + anotherDFA.delta[state2]["b"]}
    # print(newQ)

    # generating states for accept
    newaccept = set()
    for state in thisDFA.accept:
        for state2 in anotherDFA.Q:
            newaccept.add(state + state2)
    for state in thisDFA.Q:
        for state2 in anotherDFA.accept:
            newaccept.discard(state + state2)

    newDFA = DFA(
        Q=newQ,
        sigma={'a', 'b'},
        initialState=thisDFA.initialState + anotherDFA.initialState,
        accept=newaccept,
        delta=newdelta
    )
    return newDFA


def isSubset(firstDFA, anotherDFA):
    subtractedDFA = firstDFA.subtract(anotherDFA)
    if (subtractedDFA.isEmpty()):
        return True
    else:
        return False


def areSeparatedSets(firstDFA, anotherDFA):
    intersectionDFA = firstDFA.intersection(anotherDFA)
    if (not intersectionDFA.isEmpty()):
        return False
    else:
        return True
