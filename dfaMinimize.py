from dfa import *
import copy


class Minimize:

    def minimizer(self, dfa: DFA):
        QiQjTable: dict[str, dict] = self.QiQjTableCreator(dfa)

        #  Consider every state pair (Qi, Qj) in the DFA where Qi ∈ F and Qj ∉ F
        #  or vice versa and mark them. [Here F is the set of final states]

        for i in QiQjTable:
            for j in QiQjTable[i]:
                if i in dfa.accept or j in dfa.accept:
                    QiQjTable[i][j] = True


        # If there is an unmarked pair (Qi, Qj), mark it if the pair
        # {δ (Qi, A), δ (Qi, A)} is marked for some input alphabet.

        QiQjTableCopied = copy.deepcopy(QiQjTable)
        for i in QiQjTableCopied:
            for j in QiQjTableCopied[i]:
                if not QiQjTableCopied[i][j]:
                    for alphabet in dfa.sigma:
                        if dfa.delta[i][alphabet] in QiQjTableCopied and dfa.delta[j][alphabet] in QiQjTableCopied[dfa.delta[i][alphabet]]:
                            if (QiQjTableCopied[dfa.delta[i][alphabet]][dfa.delta[j][alphabet]]):
                                QiQjTable[i][j] = True
                        if dfa.delta[j][alphabet] in QiQjTableCopied and dfa.delta[i][alphabet] in QiQjTableCopied[dfa.delta[j][alphabet]]:
                            if (QiQjTableCopied[dfa.delta[j][alphabet]][dfa.delta[i][alphabet]]):
                                QiQjTable[i][j] = True

        tmpNewQ : list[set] = list(set())
        for state in QiQjTable:
            for secondState in QiQjTable[state]:
                if not QiQjTable[state][secondState]:
                    tmpNewQ.append({state,secondState})




        # combine sets in tmpNewQ if they have common elements
        for i in range(len(tmpNewQ)):
            for j in range(len(tmpNewQ)):
                if i != j and len(tmpNewQ[i].intersection(tmpNewQ[j])) != 0:
                    tmpNewQ[i] = tmpNewQ[i].union(tmpNewQ[j])
                    tmpNewQ[j] = set()
        #remove empty sets from tmpNewQ
        tmpNewQ = [x for x in tmpNewQ if x != set()]

        #add other states to tmpNewQ if they are not in any set
        for state in dfa.Q:
            isAdded = False
            for i in range(len(tmpNewQ)):
                if state in tmpNewQ[i]:
                    isAdded = True
            if not isAdded:
                tmpNewQ.append({state})


        listfromtmpNewQ = list(tmpNewQ)
        # soft listfromtmpNewQ based on state name
        for i in range(len(listfromtmpNewQ)):
            listfromtmpNewQ[i] = sorted(listfromtmpNewQ[i])
        listfromtmpNewQ.sort()

        #make new delta
        newDelta = dict()
        for state in listfromtmpNewQ:
            #turn state set to string
            newstate = ''.join(state)
            newDelta[newstate] = dict()
            for alphabet in dfa.sigma:
                for secondState in listfromtmpNewQ:
                    #turn secondState set to string
                    newsecondState = ''.join(secondState)
                    for stateInSet in state:
                        if dfa.delta[stateInSet][alphabet] in secondState:
                            newDelta[newstate][alphabet] = newsecondState
                            break

        #make a new start state
        newStart = set()
        for i in range(len(tmpNewQ)):
            if dfa.initialState in tmpNewQ[i]:
                newStart = tmpNewQ[i]
                break


    # make accept states
        newAccept = list()
        for state in tmpNewQ:
            #turn state set to string
            newstate = ''.join(state)
            for acceptState in dfa.accept:
                if acceptState in state:
                    newAccept.append(newstate)
                    break
        newAccept = set(newAccept)


        print()
        newDFA = DFA(set(newDelta.keys()), dfa.sigma , ''.join(newStart), newAccept, newDelta)

        return newDFA







    def QiQjTableCreator(self, dfa: DFA) -> dict[str, dict]:

        QiQjTable: dict[str, dict] = dict(dict())
        tmpQlist: list = list(copy.copy(dfa.Q))
        tmpQlist.pop(0)
        # print(dfa.Q)
        initialStatesList = list(copy.copy(dfa.Q))
        initialStatesList.pop()
        for state in initialStatesList:
            QiQjTable[state] = dict()
            for tmpState in tmpQlist:
                QiQjTable[state][tmpState] = False
            if len(tmpQlist) != 0:
                tmpQlist.pop(0)
        return QiQjTable

