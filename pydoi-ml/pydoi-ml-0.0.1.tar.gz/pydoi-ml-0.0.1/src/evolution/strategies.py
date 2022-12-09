STATE_SPACE = [
    dict(name='hidden_state', values=list(range(2)), count=2),
    dict(
        name='primitives',
        values=['sep_3x3', 'sep_5x5', 'sep_7x7', 'avg_3x3', 'max_3x3', 'identity'],
        count=2
    ),
    dict(name='combinations', values=['add', 'concat'], count=1),
]

BLOCK_STATE_SPACE_IDS = [0, 0, 1, 1, 2]
BLOCK_SIZE = len(BLOCK_STATE_SPACE_IDS)

class ParentSelectionStrategies(object):
    def __init__(self, child_params) -> None:
        self.elementary_strategies = [
            'best',
            'best_and_random',
            'top_two',
        ]
        self.strategies = {
            'best': self.best,
            'best_and_random': self.best_and_random,
            'top_two': self.top_two,
        }
        self.child_params = child_params

    def best_and_random(self, num_candidates):
        best_parent = num_candidates - 1
        random_parent = random.randrange(num_candidates-1)

        return [best_parent, random_parent]

    def top_two(self, num_candidates):
        return [num_candidates-1, num_candidates-2]

    def best(self, num_candidates):
        best_parent = num_candidates - 1
        return [best_parent, best_parent]

    def get(self, name='best_and_random'):
        return self.strategies[name]

class MutationStrategies(object):
    def __init__(self, child_params) -> None:
        self.child_params = child_params
        self.elementary_strategies = ['point', 'block_swap']
        self.strategies = {
            'point': self.point,
            'block_swap': self.block_swap,
            'mixed': self.mixed,
            'gene_shuffle': self.gene_shuffle,
        }

    def point(self, config):
        cell_shape = (self.child_params['blocks'], BLOCK_SIZE)
        (block_id, state_id) = tuple(map(randrange, cell_shape))
        state_space_id = BLOCK_STATE_SPACE_IDS[state_id]
        random_mutation = randrange(len(STATE_SPACE[state_space_id]['values']))
        print('Mutation:', block_id, state_id, random_mutation)

        config[(block_id, state_id)] = random_mutation

        return config

    def block_swap(self, config):
        coordinates = list(map(
            randrange, [self.child_params['blocks']]*2
        ))
        config[coordinates] = config[list(reversed(coordinates))]

        return config

    def mixed(self, config):
        strategy_id = randrange(len(self.elementary_strategies))

        return self.strategies[self.elementary_strategies[strategy_id]](config)

    def gene_shuffle(self, config):
        blocks = config.shape[0]
        block_indices = list(range(blocks))
        random.shuffle(block_indices)

        # Select Genes
        selected = config[block_indices[:self.child_params['blocks']]]
        return selected

    def get(self, name='point'):
        return self.strategies[name]

class MergeStrategies(object):
    def __init__(self, child_params, mix_strategy) -> None:
        self.elementary_strategies = [
            'pick_first',
            'mix_two',
            'center_merge'
        ]
        self.strategies = {
            'pick_first': self.pick_first,
            'mix_two': self.mix_two,
            'center_merge': self.center_merge
        }
        self.mix_strategy = mix_strategy
        self.child_params = child_params

    def pick_first(self, *parents):
        return parents[0]

    def mix_two(self, *parents):
        first, second = parents
        return np.array(list(
            map(
                lambda c: self.mix_strategy(np.concatenate(c)),
                zip(first, second)
            )
        ))

    def center_merge(self, *parents):
        first, second = parents
        left_merge_point = self.child_params['blocks']//2
        right_merge_point = (self.child_params['blocks']+1)//2
        merge_point = random.choice([left_merge_point, right_merge_point])

        return np.array(list(
            map(
                lambda c: np.concatenate([c[0][:merge_point], c[1][merge_point:]]),
                zip(first, second)
            )
        ))

    def get(self, name='pick_first'):
        return self.strategies[name]

# mutation_strategies = MutationStrategies(CHILD_PARAMS)
# mutation_strategy = mutation_strategies.get('block_swap')
# merge_strategies = MergeStrategies(
#     CHILD_PARAMS,
#     mutation_strategies.get('gene_shuffle')
# )
# merge_strategy = merge_strategies.get('center_merge')
# parent_selection_strategies = ParentSelectionStrategies(CHILD_PARAMS)
# parent_selection_strategy = parent_selection_strategies.get(
#     CONTROLLER_PARAMS['parent_selection_strategy']
# )

# configs = [
#     np.array([
#         [
#             [0, 0, 3, 5, 1],
#             [1, 1, 3, 2, 1],
#             [1, 1, 0, 2, 0],
#             [1, 0, 4, 2, 1],
#             [0, 0, 3, 4, 0],
#             [1, 0, 4, 4, 1],
#             [0, 1, 0, 1, 0],
#             [0, 0, 3, 5, 1],
#             [1, 1, 0, 4, 0],
#             [1, 1, 5, 2, 1],
#             [1, 1, 1, 0, 1],
#         ],
#         [
#             [1, 1, 1, 4, 0],
#             [1, 1, 1, 0, 1],
#             [0, 1, 4, 4, 0],
#             [0, 0, 2, 4, 0],
#             [1, 1, 1, 0, 1],
#             [0, 0, 4, 1, 1],
#             [1, 1, 1, 2, 1],
#             [1, 0, 4, 3, 1],
#             [0, 1, 1, 4, 0],
#             [0, 1, 5, 4, 0],
#             [0, 0, 5, 5, 0],
#         ]
#     ]),
#     np.array([
#         [
#             [1, 0, 4, 4, 1],
#             [0, 1, 0, 1, 0],
#             [0, 0, 3, 5, 1],
#             [1, 1, 0, 4, 0],
#             [1, 1, 5, 2, 1],
#             [1, 1, 5, 4, 1],
#             [1, 1, 1, 4, 1],
#             [0, 0, 5, 0, 0],
#             [0, 1, 3, 4, 1],
#             [1, 0, 0, 2, 1],
#             [0, 0, 5, 0, 0],
#         ],
#         [
#             [0, 0, 4, 1, 1],
#             [1, 1, 1, 2, 1],
#             [1, 0, 4, 3, 1],
#             [0, 1, 1, 4, 0],
#             [0, 1, 5, 4, 0],
#             [1, 0, 1, 3, 1],
#             [1, 1, 5, 1, 0],
#             [1, 1, 5, 2, 0],
#             [0, 0, 5, 5, 0],
#             [1, 0, 3, 4, 1],
#             [1, 0, 3, 4, 1],
#         ]
#     ]),
#     np.array([
#         [
#             [1, 1, 5, 4, 1],
#             [1, 1, 1, 4, 1],
#             [0, 0, 5, 0, 0],
#             [0, 1, 3, 4, 1],
#             [1, 0, 0, 2, 1],
#         ],
#         [
#             [1, 0, 1, 3, 1],
#             [1, 1, 5, 1, 0],
#             [1, 1, 5, 2, 0],
#             [0, 0, 5, 5, 0],
#             [1, 0, 3, 4, 1],
#         ]
#     ])
# ]
# merge_strategy(configs[0], configs[1])
# # mutation_strategy(configs[0][0])

# #0 [0, 0, 3, 5, 1],
# #1 [1, 1, 3, 2, 1],
# #2 [1, 1, 0, 2, 0],
# #3 [1, 0, 4, 2, 1],
# #4 [0, 0, 3, 4, 0],
# #5 [1, 0, 4, 4, 1],
# #6 [0, 1, 0, 1, 0],
# #7 [0, 0, 3, 5, 1],
# #8 [1, 1, 0, 4, 0],
# #9 [1, 1, 5, 2, 1]
# #10 [1, 1, 1, 0, 1],

# #0 [1, 0, 4, 4, 1],
# #1 [0, 1, 0, 1, 0],
# #2 [0, 0, 3, 5, 1],
# #3 [1, 1, 0, 4, 0],
# #4 [1, 1, 5, 2, 1],
# #5 [1, 1, 5, 4, 1],
# #6 [1, 1, 1, 4, 1],
# #7 [0, 0, 5, 0, 0],
# #8 [0, 1, 3, 4, 1],
# #9 [1, 0, 0, 2, 1],
# #10 [0, 0, 5, 0, 0],

