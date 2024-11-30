import numpy as np 
class our_HMM:
    # Vocabulary V (it is formed by the given words)
    # A set of N states Q = q1, q2, ..., qN
    # A sequence of T observations O = o1, o2, ..., oN 
    # A transition probability matrix A = a11, ..., aij, aNN
    # A sequence of observation likelihoods B = bi(ot)
    # A initial probability distribution over states π = π1, π2, ..., πN

    def __init__(self, Q, V):
        
        self.tags = Q # tags
        self.words = V # words in the given sentence  
        
        # result probabilities
        self.result = np.zeros((len(self.tags), len(self.words)))
        
        # emission probabilities 
        self.emission = np.random.rand(len(self.tags), len(self.words))
        
        # transition probabilities 
        self.transition = np.random.rand(len(self.tags)+1, len(self.tags)+1) # +1 in both because start and stop states have to be taken into account

        self.previos_max_prob = 0
        self.previos_max_prob_index = 0
    def viterbi_algorithm(self):

        """print(f'Vocabulary: {self.words}')
        print(f'Tags: {self.tags}')
        print(f'Emission features: {self.emission}')
        print(f'Transition features: {self.transition}')
        print(f'Result matrix: {self.result}')"""

        final_result = []
        # for i in tags 
        for i in range(len(self.tags)):
            # for j in words 
            # print(f'Tag: {self.tags[i]}')
            for j in range(len(self.words)):
                # print(f'Word: {self.words[j]}')
                # probability of tag i and word j = 
                #   best probability of the previous word for all tags
                #   emission probability of i tag and j word
                #   transition probability of best previos i tag and actual i tag
                if j != 0:
                    self.result[i,j] = self.previos_max_prob + self.emission[i,j] + self.transition[self.previos_max_prob_index+1,i]

                else: 
                    self.result[i,j] = self.emission[i,j]*self.transition[0,i]
            
            self.previos_max_prob = np.max(self.result[:, j-1])
            self.previos_max_prob_index = np.argmax(self.result[:, j-1])
            # print(f'Previous max prob: {self.previos_max_prob}')
            # print(f'Previous max prob tag: {self.tags[self.previos_max_prob_index]}')
            final_result.append([i,self.previos_max_prob_index])
        
        # Add final probability 
        self.previos_max_prob = np.max(self.result[:, j])
        self.previos_max_prob_index = np.argmax(self.result[:, j])
        final_result.append([i,self.previos_max_prob_index])
        
        return final_result
    
if __name__ == '__main__':

    Q = ["N", "V"]
    V = ["they", "can", "fish"]

    hmm = our_HMM(Q, V)
    final_result = hmm.viterbi_algorithm()
    for cords in final_result:
        x = cords[0]
        y = cords[1]
        print(f'Word: {Q[y]}, tag: {V[x]}')