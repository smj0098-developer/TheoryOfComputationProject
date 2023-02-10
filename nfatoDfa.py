import copy


class NFA:
    def __init__(self, Q: set[str], sigma: set[str], initialState: str, accept: set[str], delta: dict):
        self.Q = Q
        self.sigma = sigma
        self.initialState = initialState
        self.accept = accept
        self.delta = delta

    def nfaToDfa(self):

        for state in self.delta:
            for alphabet in self.sigma-{'e'}:
                headList = []
                headList.append(alphabet)
                headList.append('e')  # as lambda
                self.closure(headList,state,alphabet)




    def closure(self,headList,state,head):

        for alpha in headList:
            newHeadList = copy.deepcopy(headList)
            if(alpha!='e'):
                newHeadList.remove(alpha)
            if alpha in self.delta[state].keys():
                for item in self.delta[state][alpha]:
                    print(state , alpha, item,head)

                    self.closure(newHeadList,item,head)



