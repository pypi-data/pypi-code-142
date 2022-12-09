import numpy as np
from scipy.special import expit as sigmoid
from qrl_graph.graph_env.graph import Graph
from qrl_graph.utils import array2binary
from argparse import Namespace
from sysflow.utils.common_utils.file_utils import load
import wandb

class PolicyGradient:
    """Policy Gradient Agent
    
    The first version of the policy is naive, we treat the action to be a length of (n-1)n / 2 
    vector, where n is the number of nodes in the graph. The action is the probability of each 
    edge to be selected. For the parametrized policy, we make this vector to be trainable. And 
    the policy gradient is pushed to the direction of the gradient of the log of the probability. 
    
    """
    def __init__(self, n, data_folder=None, config=None): 
        self.config = Namespace(**config)
        self.learning_rate = self.config.learning_rate
        self.data_folder = data_folder
        
        self.use_wandb = self.config.use_wandb
        self.n = n
        
        self.N = n * (n-1) // 2
        # this is the trainable parameter
        self.param = np.zeros(self.N)
        
        # book-keeping the protocol to reward 
        # TODO (jim): change the dict to array 
        # self.pro2rew = {}
        
        # this is the new implementation
        self.pro2rew = np.zeros(2**self.N)
    
    def check_proto(self, sample): 
        """Check if the protocol is in the book-keeping."""
        return self.pro2rew[array2binary(sample)] != 0

    def get_proto_reward(self, sample): 
        """Retrieve the reward for the protocol."""
        return self.pro2rew[array2binary(sample)]
        
    def book_keeping(self, sample, reward):
        """Book keeping the protocol to reward.
        
        Args:
            sample: the sample to be book kept. the format of the sample is a numpy 
                array of shape (n * (n-1) // 2, ), in the storage, the sample is 
                converted to integer in the binary format.
            reward: the reward of the sample.
        """
        self.pro2rew[array2binary(sample)] = reward
        
        # for sample, reward in zip(samples, rewards):
        #     self.pro2rew[tuple(sample)] = reward    
    
    def sample(self, batch_size):
        
        # converting the param to the probability of each edge
        prob = sigmoid(self.param)
        n = self.n
        coin_toss = np.random.rand(n * (n-1) // 2 * batch_size)
        coin_toss = np.reshape(coin_toss, (batch_size, n * (n-1) // 2))
        sample = coin_toss < prob
        return sample.astype(int)

    def sample2graph(self, sample):
        """Convert the sample to the graph."""
        n = self.n
        g = np.zeros((n, n))
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                g[i, j] = sample[count]
                g[j, i] = g[i, j]
                count += 1
        return g
    
    def get_reward(self, samples):
        """Get the reward for the samples.
        
        Use the classical time and quantum time to get the reward.
        
        we use the book-keeping to accelerate the process and avoid the repeated calculation.
        """
        reward_list = []
        for sample in samples: 
            if self.check_proto(sample): 
                reward = self.get_proto_reward(sample)
            else: 
                if self.data_folder:
                    # load the reward from the data folder
                    graph_id = ''.join([str(i) for i in sample])
                    try: 
                        data = load(self.data_folder + f'/graph_{graph_id}.pkl')
                        reward = data['quantum_speedup']
                    except:
                        reward = -1
                else: 
                    g = self.sample2graph(sample)
                    reward = Graph(g).get_objective()
                self.book_keeping(sample, reward)
            reward_list.append(reward)
        
        return np.array(reward_list)
    
    def optimize(self):
        """Optimize the policy."""
        # TODO(jim): implement this
       
        history_max = 0 
        for i in range(self.config.iterations):
            samples = self.sample(batch_size=self.config.batch_size)
            rewards = self.get_reward(samples)
            if max(rewards) > history_max:
                history_max = max(rewards)
                print("The max reward is {} and configure is {}".format(history_max, samples[np.argmax(rewards)]))
            self.gradient_update(rewards, samples)
            print("Iteration: {}, reward_mean: {:.3f}, reward_max: {:.3f}, reward_history_best: {:.3f}".format(i, np.mean(rewards), np.max(rewards), history_max))
            
            if self.use_wandb:
                wandb.log({'reward_mean': np.mean(rewards), 'reward_max': np.max(rewards), 'reward_history_best': history_max})

    def gradient_update(self, rewards, samples):
        """Use the gradient to update the parameters."""
        # if sample is 1, then the gradient is positive; if sample is 0, then the gradient is negative
        grads = (1 - sigmoid(self.param * ( 2 * samples - 1 ))) * ( 2 * samples - 1 )
        
        grads = grads * np.reshape((rewards - np.mean(rewards, axis=0)) / (np.std(rewards, axis=0) + 1e-4), (-1, 1)) 
        grads = np.mean(grads, axis=0)
        
        self.param += self.learning_rate * grads # the gradient ascent
        
        
