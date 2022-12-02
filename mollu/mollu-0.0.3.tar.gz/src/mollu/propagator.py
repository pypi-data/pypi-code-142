from copy import deepcopy
from itertools import product
import numpy as np

from .map import Map

class Propagator(object):
    
    status_code_annihilated = -2
    
    def __init__(self, stage, stage_name):
        
        N_mobs = len(stage['indices_node_mobs'])
        N_boss = 1
        N_oppo = N_boss + N_mobs
        
        # [NOTE] change `index_node` to `indices_node`
        indices_node_dtype = ('index_node', 'i4') 
        
        # [NOTE] change `index_node_start` to `indices_node_start`
        indices_node_start = stage['index_node_start'] 
        N_start_nodes = -1
        if hasattr(indices_node_start, '__len__'):
            N_start_nodes = len(indices_node_start)
        else:
            assert type(indices_node_start) is int
            N_start_nodes = 1
        assert N_start_nodes > 0
        indices_node_shape = (N_start_nodes,)
        indices_node_dtype += (indices_node_shape,)
        
        dtype = [
            indices_node_dtype,
            ('indices_unit_moved','i4',(N_start_nodes,)),
            ('index_node_boss', 'i4'),
            ('indices_node_mobs', 'i4', (N_mobs,)),
            ('index_node_box','i4'),
            ('map','O'),
            #### [NOTE] The first element of `indices_unit_target_oppo` 
            #### is for j_unit_target of the boss,
            #### and the other elements are those of the mobs.
            ('indices_unit_target_oppo','i4', (N_oppo,)),
        ]
        
        self.stage = stage
        self.N_mobs = N_mobs
        self.N_oppo = N_oppo
        self.state_dtype = dtype
        self.stage_name = stage_name
        
        
    @staticmethod
    def update_j_unit_target_of_oppo_caution(
        j_unit_target, j_node_oppo_caution, map_, indices_node_unit):
        """
        #### This should be called for every events by the player
        #### - moving a unit of the player
        #### - transposition between two units of the player
        ####   - note that, in case of exchanging posiiton among three or more units,
        ####     run this for every transposition invovled.
        """
        
        if j_node_oppo_caution < 0:
            j_unit_target_ = -1
            return j_unit_target_
        
        #### Check if there is already a targetted unit
        if j_unit_target >= 0:
            #### The target unit had already been determined.
            #### Check if the targetted unit is still nearby
            j_node_target = indices_node_unit[j_unit_target]
            
            distance_is_1 = 1 == map_.distance_by_indices(j_node_target, j_node_oppo_caution)
            if (j_node_target >= 0) and (distance_is_1):
                #### the targetted unit(j_node_target) 
                #### ... is still nearby of the opponent(j_node_oppo_caution)
                #### In this case, keep `j_node_target` unchanged.
                return j_unit_target
            else:
                #### the targetted unit(j_node_target) 
                #### ... is not anymore nearby of the opponent
                #### In this case, invalidate `j_unit_target`
                j_unit_target = -1
        else:
            assert j_unit_target == -1

        #### Check whether there is any unit nearby
        #### and set the target unit if possible
        assert j_unit_target == -1
        #### [NOTE] Since `j_node_oppo_caution >= 0`, 
        #### ... it is fine to have negative elements in `indices_node_unit`.
        #### The indices of the negative elements of `indices_node_unit` 
        #### ... will not appear in `indices_unit_distance_one`
        indices_unit_distance_one = np.fromiter((
            j_unit for j_unit, j_node_unit in enumerate(indices_node_unit) 
            if (j_node_unit >= 0) and (map_.distance_by_indices(j_node_unit, j_node_oppo_caution) == 1)), dtype='i4')
        
        num_indices_unit_distance_one = indices_unit_distance_one.size
        if num_indices_unit_distance_one == 0:
            j_unit_target = -1
        elif num_indices_unit_distance_one == 1: 
            j_unit_distance_one, = indices_unit_distance_one
            j_unit_target = int(j_unit_distance_one)
        elif num_indices_unit_distance_one > 1: 
            raise NotImplementedError(
                f"num_indices_unit_distance_one"
                f" = {num_indices_unit_distance_one} > 1")
        else: 
            raise ValueError(
                f"Unexpected value of num_indices_unit_distance_one"
                f" = {num_indices_unit_distance_one}") 
        if type(j_unit_target) is not int:
            raise TypeError(f"type(j_unit_target) = {type(j_unit_target)} != int")

        return j_unit_target
        
    
    def get_nodes_to_be_generated(self):
        nodes_generator = self.stage.get('nodes_generator')
        nodes_to_be_generated = []
        if nodes_generator is not None:
            assert type(nodes_generator) is dict
            nodes_to_be_generated = list(nodes_generator.values())
        return nodes_to_be_generated
        
    
    @staticmethod
    def get_the_unit_index(indices_unit):
        indices_node_unit = indices_unit
        indices_unit, = np.where(~(indices_node_unit < 0))
        
        # [NOTE] This statement checks whether there is only one unit
        j_unit, = indices_unit 
        
        return j_unit

    
    def _move_unit(self, state, j_node_next, j_unit, copy=True, use_portal=False):

        if copy: state_next = deepcopy(state)
        else: state_next = state
            
        if state[()]['index_node_boss'] < 0:
            return state_next
        
        
        j_node_now = state_next[()]['index_node'][j_unit]
        this_unit_moves = j_node_now != j_node_next
        
        
        ## Update the position of the unit
        state_next[()]['index_node'][j_unit] = j_node_next
        
        ## Update `indices_unit_moved`
        if this_unit_moves and (use_portal == False):
            indices_unit_moved_list = [j_unit_moved for j_unit_moved in state_next[()]['indices_unit_moved'] if j_unit_moved >= 0]
            if j_unit in indices_unit_moved_list: 
                raise ValueError(f"j_unit(={j_unit}) should not appear in indices_unit_moved_list = {indices_unit_moved_list}"
                                 f"\nstate_next = \n{state_next}")
            else: indices_unit_moved_list.append(j_unit)
            N_unit_moved = len(indices_unit_moved_list)
            state_next[()]['indices_unit_moved'][:N_unit_moved] = indices_unit_moved_list
                
        
        ## Aliasing the map
        map_next = state_next[()]['map']
        
            
        ## Update light and visibility of nodes
        index_node_light = self.stage.get('index_node_light')
        if self.stage_name[-1] == 'N': pass
        elif self.stage_name[-1] == 'H':
            if j_node_next == index_node_light: map_next.turn_on_light()
            else: map_next.nodes_visible[map_next.get_neighbors(j_node_next, n=1)] = True
        else: raise ValueError(f"Unexpected stage_name: {self.stage_name}")
            
            
        ## Remove the Box if found
        indices_node_box_matched, = np.where(state_next[()]['index_node_box']==j_node_next)
        if indices_node_box_matched.size > 0:
            state_next['index_node_box'] = -1


        ## Remove mobs and boss if encountered
        indices_mobs_matched, = np.where(state_next[()]['indices_node_mobs']==j_node_next)
        if indices_mobs_matched.size > 0:
            try:
                j_mob, = indices_mobs_matched
            except ValueError as e:
                print(state)
                raise e
            state_next['indices_node_mobs'][j_mob] = -1
            j_oppo = 1+j_mob
            state_next['indices_unit_target_oppo'][j_oppo] = -1

        if j_node_next == state_next[()]['index_node_boss']:
            state_next['index_node_boss'] = -1
            j_oppo = 0 # [NOTE] the index of the boss in the space of all opponents
            state_next['indices_unit_target_oppo'][j_oppo] = -1
            

        ## Update generator nodes
        nodes_generator = self.stage.get('nodes_generator')
        if nodes_generator is None: nodes_generator = {}
        node_index_to_be_generated = nodes_generator.get(j_node_next)
        if (node_index_to_be_generated is not None) and (map_next.nodes_exist[node_index_to_be_generated] == False):
            map_next.update_node_existence(node_index_to_be_generated, True)
        

        ## Update annihilation nodes
        nodes_annihilation = self.stage.get('nodes_annihilation')
        if nodes_annihilation is None: nodes_annihilation = {}
        j_node_to_be_annihilated = nodes_annihilation.get(j_node_next)
        if (j_node_to_be_annihilated is not None) and (map_next.nodes_exist[j_node_to_be_annihilated] == True):
            map_next.update_node_existence(j_node_to_be_annihilated, False)
            ## Remove mobs on the annihilated node, if any
            indices_mobs_on_annihilated_node, = np.where(state_next[()]['indices_node_mobs']==j_node_to_be_annihilated)
            if indices_mobs_on_annihilated_node.size > 0:
                j_mob_on_annihilated_node, = indices_mobs_on_annihilated_node
                state_next['indices_node_mobs'][j_mob_on_annihilated_node] = self.status_code_annihilated
            ## Remove boss on the annihilated node, if any
            if state_next[()]['index_node_boss'] == j_node_to_be_annihilated:
                state_next['index_node_boss'] = self.status_code_annihilated
            
        return state_next
    
    
    def _move_opponents(self, state):
        
        # [NOTE] 
        # This is essential 
        # since the boss can be removed in the previous step (e.g. `self._move_unit()`).
        # In this case, other mobs as well as the boss should not move 
        # and terminate its propagation.
        if state[()]['index_node_boss'] < 0:
            return state
        
        state_next = state
        map_next = state[()]['map']
        mask_indices_node_units_all = ~(state[()]['index_node'] < 0)
        indices_active_unit, = np.where(mask_indices_node_units_all)
        indices_node_units = state[()]['index_node'][mask_indices_node_units_all]
    
        
        #### Prepare variable in opponents space (boss and mobs combined)
        indices_node_oppo = np.concatenate((
            [state_next[()]['index_node_boss']], 
            state_next[()]['indices_node_mobs']), dtype='i4')
        indices_unit_target_oppo = state_next[()]['indices_unit_target_oppo']
        map_ = state_next[()]['map']
        
        
        #### Move caution-type opponents
        cautions_oppo = np.concatenate((
            [self.stage['boss_caution']], 
            self.stage['mobs_caution']), dtype='?')
        
        for j_oppo, j_node_oppo in enumerate(indices_node_oppo):
            
            j_unit_target = indices_unit_target_oppo[j_oppo]
            j_node_unit_target = state_next[()]['index_node'][j_unit_target]
            if (j_node_oppo < 0) or (j_unit_target < 0) or (j_node_unit_target < 0) or (cautions_oppo[j_oppo] == False): continue
            
            #### Check the distance between the caution-type opponent and its target unit is 1
            dist_unit_target_and_oppo = map_.distance_by_indices(j_node_unit_target, j_node_oppo)
            if dist_unit_target_and_oppo != 1:
                raise ValueError(f"dist_unit_target_and_oppo(={dist_unit_target_and_oppo}) != 1"
                                 f"\nstate_next = \n{state_next}")
            
            #### Move the caution-type opponent and remove it since it encounters a unit
            if cautions_oppo[j_oppo] and (j_unit_target >= 0):
                if j_oppo == 0: 
                    state_next['index_node_boss'] = j_node_unit_target
                    state_next['index_node_boss'] = -1
                elif j_oppo < self.N_oppo:
                    j_mob = j_oppo - 1
                    assert j_mob >= 0
                    state_next['indices_node_mobs'][j_mob] = j_node_unit_target
                    state_next['indices_node_mobs'][j_mob] = -1
                else: raise ValueError(f"Unexpected value of j_oppo = {j_oppo} "
                                       f"where N_oppo = {self.N_oppo}")
                state_next['indices_unit_target_oppo'][j_oppo] = -1
    
    
        #### Move dash-type opponents
        dashes_oppo = np.concatenate((
            [self.stage['boss_dash']], 
            self.stage['mobs_dash']), dtype='?')
    
        for j_oppo, j_node_oppo in enumerate(indices_node_oppo):
            
            j_unit_target = indices_unit_target_oppo[j_oppo]
            j_node_unit_target = state_next[()]['index_node'][j_unit_target]
            if (j_node_oppo < 0) or (j_unit_target < 0) or (j_node_unit_target < 0) or (dashes_oppo[j_oppo] == False): continue
            
            paths = map_next.path_exists(j_node_oppo, j_node_unit_target, visible_only=False)
            indices_node_oppo_except_self = np.empty((self.N_oppo - 1,), dtype='i4')
            if j_oppo == 0:
                indices_node_oppo_except_self[:] = state_next[()]['indices_node_mobs']
            elif j_oppo < self.N_oppo:
                j_node_mob = j_node_oppo
                indices_node_other_mobs = [j_node_mob_ for j_node_mob_ in state_next[()]['indices_node_mobs'] if j_node_mob_ != j_node_mob]
                indices_node_oppo_except_self[:] = np.concatenate(([state_next[()]['index_node_boss']],indices_node_other_mobs))
            else: raise ValueError(f"Unexpected value of j_oppo = {j_oppo} "
                                   f"where N_oppo = {self.N_oppo}")
            paths = [path for path in paths if path[1] not in indices_node_oppo_except_self]

            #### Determine which node to step next
            index_nearest_path = -1
            min_path_len = -1
            if len(paths) > 0:
                min_path_len = min((len(path) for path in paths))
                paths_with_min_len = [path for path in paths if len(path) == min_path_len]
                assert len(paths_with_min_len) > 0
                if len(paths_with_min_len) == 1:
                    path_with_min_len, = paths_with_min_len
                    index_nearest_path = path_with_min_len[1]
                elif len(paths_with_min_len) > 1:
                    
                    indices_next_node = set([path[1] for path in paths_with_min_len])
                    assert len(indices_next_node) >= 1
                    if len(indices_next_node) == 1:
                        index_nearest_path, = indices_next_node
                    else:                            
                        print(f"[LOG] len(paths_with_min_len) = {len(paths_with_min_len)} > 1."
                              f"\n[LOG] paths_with_min_len = {paths_with_min_len}"
                              f"\n[LOG] state_next = \n{state_next}", file=stderr)
                        if j_oppo == 0: pass
                        elif j_oppo >= 1:
                            for j_unit in indices_active_unit:
                                overridden = False
                                if (j_oppo >= 1) and (self.stage_name == '5-5-N') and (state_next[()]['index_node'][j_unit] == 8) and np.all(state_next[()]['indices_node_mobs'] == [-1,  2,  7]) and (state_next[()]['index_node_boss'] == 9):
                                    indices_nearest_paths = [6]
                                    overridden = True
                                elif (j_oppo >= 1) and (self.stage_name == '3-4-N') and (state_next[()]['index_node'][j_unit] == 4) and np.all(state_next[()]['indices_node_mobs'] == [-1,  2]) and (state_next[()]['index_node_boss'] == 8):
                                    indices_nearest_paths = [6]
                                    overridden = True

                                if overridden: 
                                    index_nearest_path, = indices_nearest_paths
                                    print(f"[WARNING] indices_nearest_paths is overriden to {indices_nearest_paths}", file=stderr)
                                else:
                                    print(f"[ERROR] state_next:\n{state_next}"
                                          f"\n[ERROR] paths_found_total = {paths}"
                                          f"\n[ERROR] paths_total_with_min_len = {paths_with_min_len} with path_len_min = {min_path_len}", 
                                          file=stderr)
                                    raise NotImplementedError(f"len(paths_with_min_len) = {len(paths_with_min_len)} > 1")
                        else: raise NotImplementedError()


            if index_nearest_path >= 0:
                encountered = np.any(indices_node_units == index_nearest_path)
                j_node_oppo_next = -1 if encountered else index_nearest_path
                if j_oppo == 0:
                    state_next['index_node_boss'] = j_node_oppo_next
                elif j_oppo < self.N_oppo:
                    j_mob = j_oppo - 1
                    state_next['indices_node_mobs'][j_mob] = j_node_oppo_next
                else: raise ValueError(f"Unexpected value of j_oppo = {j_oppo} "
                                       f"where N_oppo = {self.N_oppo}")

                if encountered:
                    state_next['indices_unit_target_oppo'][j_oppo] = -1

        return state_next
    
        
    def _check_state(self, state):
        return state.shape == () and state.dtype == self.state_dtype
        
        
    def _propagate_with_two_units(self, state):
        
        indices_unit, = np.where(~(state[()]['index_node'] < 0))
        N_units = indices_unit.size
        assert N_units == 2
        
        state_pool = [state]
        
        if state[()]['index_node_boss'] < 0:
            return state_pool
        
        
        #### Branch-off if the two units are adjacent so that they can swap each other
        distance_between_two_units = state[()]['map'].distance_by_indices(*state[()]['index_node'])
        if distance_between_two_units == 1:
            state_swapped = deepcopy(state)
            state_swapped['index_node'] = np.flip(state_swapped['index_node'])
            self.update_indices_unit_target_of_oppo(state_swapped)
            state_pool.append(state_swapped)
            
    
        #### Move each unit
        perms = [(0,1), (1,0)]
        state_pool_addit = []
        for state_ in state_pool:
            for perm in perms:
                
                #### Propgate one of the two units
                j_unit = indices_unit[perm[0]]
                state_pool_ = self._propagate_with_one_unit(state_, j_unit)
                
                ## [NOTE] For states in `state_pool_`, 
                ## ... there is no need for `self.update_j_unit_target_of_oppo_caution()`
                ## ... since `self.update_j_unit_target_of_oppo_caution()` has already applied 
                ## ... inside `self._propagate_with_one_unit()`.
                ## ... Same goes for the second `self._propagate_with_one_unit()` below.
                
                #### Branch off if a swap between the two units can be made
                state_pool_swapped = []
                for state__ in state_pool_:
                    if state__[()]['map'].distance_by_indices(*state__[()]['index_node']) == 1:
                        state__swapped = deepcopy(state__)
                        state__swapped['index_node'] = np.flip(state__swapped['index_node'])
                        self.update_indices_unit_target_of_oppo(state__swapped)
                        state_pool_swapped.append(state__swapped)
                        
                state_pool_.extend(state_pool_swapped)
    
                #### Propagate the other unit
                j_unit_ = indices_unit[perm[1]]
                state_pool_addit_ = []
                for state__ in state_pool_:
                    state_pool__ = self._propagate_with_one_unit(state__, j_unit_)
                    state_pool_addit_.extend(state_pool__)
                state_pool_.extend(state_pool_addit_)
                
                #### Branch off if a swap between the two units can be made
                state_pool_swapped = []
                for state__ in state_pool_:
                    if state__[()]['map'].distance_by_indices(*state__[()]['index_node']) == 1:
                        state__swapped = deepcopy(state__)
                        state__swapped['index_node'] = np.flip(state__swapped['index_node'])
                        self.update_indices_unit_target_of_oppo(state__swapped)
                        state_pool_swapped.append(state__swapped)
                state_pool_.extend(state_pool_swapped)
                
                #### Add the branches to the additional pool
                state_pool_addit.extend(state_pool_)
                
        #### Replace the old pool with the propagated pool
        state_pool = np.unique(state_pool_addit)

        return state_pool
        
        
    def propagate(self, state):
        
        assert self._check_state(state)
        
        #### Initialize 'indices_unit_moved' at each turn
        state = deepcopy(state)
        state[()]['indices_unit_moved'] = -1
        
        # [NOTE] to be generalized to include the cases of N_units >= 3
        N_units = (~(state['index_node'] < 0)).sum()
        
        state_pool = None
        if N_units == 1:
            j_unit = self.get_the_unit_index(state['index_node'])
            state_pool = self._propagate_with_one_unit(state, j_unit)

        elif N_units == 2:
            state_pool = self._propagate_with_two_units(state)

        else: raise NotImplementedError()
        assert state_pool is not None
        
        
        #### Move the opponents depending on each state
        for state in state_pool:
            
            # [NOTE] it does not make a copy, but does inplace operation
            self._move_opponents(state) 
            
            #### [NOTE] It seems, there is no need to update indices of target units
            #### since they will be renewed at the next turn of the units of the player
        
        return state_pool
    
    
    def update_indices_unit_target_of_oppo_caution(self, state):
        
        indices_unit_target_oppo = state[()]['indices_unit_target_oppo']
        indices_node_oppo = np.concatenate((
            [state[()]['index_node_boss']], 
            state[()]['indices_node_mobs']))
        oppo_caution = np.concatenate((
            [self.stage['boss_caution']], 
            self.stage['mobs_caution']))
        map_ = state[()]['map']
        indices_node_unit = state[()]['index_node']
        for j_oppo, caution in enumerate(oppo_caution):
            if not caution: continue
            indices_unit_target_oppo[j_oppo] = self.update_j_unit_target_of_oppo_caution(
                indices_unit_target_oppo[j_oppo], indices_node_oppo[j_oppo], map_, indices_node_unit)
            
        state[()]['indices_unit_target_oppo'][:] = indices_unit_target_oppo
        
        
    def update_indices_unit_target_of_oppo_dash(self, state):
        
        indices_unit_moved = state[()]['indices_unit_moved']
        
        indices_unit_target_oppo = state[()]['indices_unit_target_oppo']
        indices_node_oppo = np.concatenate((
            [state[()]['index_node_boss']], 
            state[()]['indices_node_mobs']))
        oppo_dash = np.concatenate((
            [self.stage['boss_dash']], 
            self.stage['mobs_dash']))
        map_ = state[()]['map']
        indices_node_unit = state[()]['index_node']
        for j_oppo, dash in enumerate(oppo_dash):
            if not dash: continue
            indices_node_oppo_others = [j_oppo_ for j_oppo_ in indices_node_oppo if j_oppo_ != j_oppo]
            indices_unit_target_oppo[j_oppo] = self.update_j_unit_target_of_oppo_dash(
                indices_unit_target_oppo[j_oppo], indices_node_oppo[j_oppo], 
                indices_node_oppo_others, map_,
                indices_node_unit, indices_unit_moved
            )
            
        state[()]['indices_unit_target_oppo'][:] = indices_unit_target_oppo
        
        
    def _propagate_with_one_unit(self, state, j_unit):
        
        state_pool = [state]
        
        if state[()]['index_node_boss'] < 0:
            return state_pool
        
        nodes_portal = self.stage.get('nodes_portal')
        if nodes_portal is None: nodes_portal = {}
            
            
        #### Branch off if there is a portal at the current position
        j_node_unit = state[()]['index_node'][j_unit]
        j_node_portal_dest_start = nodes_portal.get(j_node_unit)
        if j_node_portal_dest_start is not None:
            assert type(j_node_portal_dest_start) is int
            another_unit_is_at_dest = any([j_node_portal_dest_start == j_node_unit_ for j_unit_, j_node_unit_ in enumerate(state[()]['index_node']) if (j_unit_ != j_unit) and (j_node_unit_ >= 0)])
            if another_unit_is_at_dest: pass
            else:
                #### There is a portal at where the unit is standing at `state['index_node']`.
                state_using_portal = self._move_unit(state, j_node_portal_dest_start, j_unit, 
                                                     copy=True, use_portal=True)
                self.update_indices_unit_target_of_oppo(state_using_portal)
                state_pool.append(state_using_portal)
        
        
        #### Update each state
        indices_unit, = np.where(state[()]['index_node'] >= 0)
        indices_node_unit_others = [state[()]['index_node'][j_unit_] 
                                    for j_unit_ in indices_unit if j_unit_ != j_unit]

        state_pool_addit = []
        for state_ in state_pool:
            j_node_unit_ = state_[()]['index_node'][j_unit]
            indices_node_next = [j_node for j_node 
                                 in state_[()]['map'].get_neighbors(j_node_unit_, n=1) 
                                 if j_node not in indices_node_unit_others]
    
            for j_node_next in indices_node_next:
                try:
                    state_next = self._move_unit(state_, j_node_next, j_unit, copy=True)
                except ValueError as e:
                    print(f"j_node_next = {j_node_next}, j_unit = {j_unit}, state_ = \n{state_}")
                    raise e
                self.update_indices_unit_target_of_oppo(state_next)
                state_pool_addit.append(state_next)
                
        state_pool = state_pool_addit
        
        
        #### Branch off if there is a portal at the destination
        state_pool_addit = []
        for state_ in state_pool:
            j_node_portal_dest = nodes_portal.get(state_[()]['index_node'][j_unit])
            if (j_node_portal_dest is not None) and (state_[()]['index_node'][j_unit] != j_node_unit):
                assert type(j_node_portal_dest) is int
                another_unit_is_at_dest = any([j_node_portal_dest == j_node_unit_ for j_unit_, j_node_unit_ in enumerate(state_[()]['index_node']) if (j_unit_ != j_unit) and (j_node_unit_ >= 0)])
                if another_unit_is_at_dest: pass
                else:
                    state_using_portal = self._move_unit(state_, j_node_portal_dest, j_unit, 
                                                         copy=True, use_portal=True)
                    self.update_indices_unit_target_of_oppo(state_using_portal)
                    state_pool_addit.append(state_using_portal)
                
        state_pool.extend(state_pool_addit)
        
        return state_pool

    
    def total_distance(self, states, per_unit=False):

        #### Determine the number of phases
        indices_step_boss_removed = np.where(states['index_node_boss'] < 0)[0]
        N_phase_this = -1
        if indices_step_boss_removed.size > 0:
            j_step_boss_removed = indices_step_boss_removed[0]
            N_phase_this = j_step_boss_removed + 1
        else: N_phase_this = states.size
            
        if N_phase_this == 0: return 0
        assert N_phase_this > 0

        #### Prepare portal map, if any
        nodes_portal = self.stage.get('nodes_portal')
        if nodes_portal is None: nodes_portal = {}

        #### Determine the number of units
        N_units = states['index_node'].shape[-1]

        mask_existing_units = np.all(states[()]['index_node'] >= 0, axis=0)
        indices_existing_units, = np.where(mask_existing_units)
        indices_non_existing_units, = np.where(~mask_existing_units)
        for j_non_existing_unit in indices_non_existing_units:
            assert np.all(states[()]['index_node'][:,j_non_existing_unit] < 0)
        dist_units = np.full((N_units,), -1, dtype='i4')
        for j_unit in range(N_units):
            if j_unit in indices_existing_units:
                dist_units[j_unit] = np.sum(states[()]['indices_unit_moved'] == j_unit)
        tot_dist = dist_units[dist_units >= 0].sum()
        
        if per_unit: return tot_dist, dist_units
        else: return tot_dist
        

    @staticmethod
    def update_j_unit_target_of_oppo_dash(
        j_unit_target, j_node_oppo_dash, indices_node_other_oppo, map_, 
        indices_node_unit, indices_unit_moved): # mask_units_moved
        """
        indices_node_unit: array-like
            The length of `indices_node_unit` is the same as the number of start nodes.
        indices_unit_moved: array-like
            The `indices_unit_moved` consists of the indices of units that moved during the turn of the player.
            If there is no element in `indices_unit_moved`, it means no unit of the player moved.
            If there is one or more elements in `indices_unit_moved`, 
            it means that the first element moved first and the second moved second and so on.
        """
        
        #### If the opponent with index `j_node_oppo_dash` does not exist
        #### ... return -1.
        if j_node_oppo_dash < 0:
            j_unit_target_ = -1
            return j_unit_target_

        #### Determine which units exist
        indices_unit_exist, = np.where(indices_node_unit >= 0)

        #### All units that moved should exist
        indices_unit_moved = [j_unit_moved for j_unit_moved in indices_unit_moved 
                              if j_unit_moved >= 0]
        assert all((j_unit_moved in indices_unit_exist 
                    for j_unit_moved in indices_unit_moved))

        N_unit_exist = indices_unit_exist.size
        #### If there is no unit, there is not target, thus returning -1.
        if N_unit_exist == 0:
            j_unit_target_ = -1
            return j_unit_target_

        assert N_unit_exist > 0
        min_lengths_of_paths_to_units_exist = np.full((N_unit_exist,), -1, dtype='i4')
        for index, j_unit in enumerate(indices_unit_exist):

            #### Find paths connecting the opponent with dash and the unit with `j_unit`
            j_node_unit = indices_node_unit[j_unit]
            assert j_node_unit >= 0
            paths = map_.path_exists(j_node_oppo_dash, j_node_unit, visible_only=False)

            #### Drop paths where there is another opponent on the first step
            paths = [path for path in paths if path[1] not in indices_node_other_oppo]

            #### Find the minimal length among all paths
            min_length = -1
            if len(paths) > 0:
                #### Select paths with the minimal length
                min_length = min((len(path) for path in paths))

            #### Store the minimal length and the paths with the minimal length 
            #### ... to their respective container
            min_lengths_of_paths_to_units_exist[index] = min_length

        mask_existing_units_path_exist = min_lengths_of_paths_to_units_exist >= 0
        min_lengths_of_paths_to_units_exist_path_exist = min_lengths_of_paths_to_units_exist[mask_existing_units_path_exist]
        
        global_min_len = -1
        if min_lengths_of_paths_to_units_exist_path_exist.size > 0:
            global_min_len = min_lengths_of_paths_to_units_exist_path_exist.min()
            
        if global_min_len == -1: return -1
        else: assert global_min_len > 0
            
        indices_existing_units_with_global_min_len_path, = np.where(min_lengths_of_paths_to_units_exist == global_min_len)
        N_unit_exist_with_global_min_len_path = indices_existing_units_with_global_min_len_path.size
        if N_unit_exist_with_global_min_len_path == 0:
            #### There is no unit accesible 
            #### ... from the currrent location (`j_node_oppo_dash`) of the opponent
            j_unit_target_ = -1
            return j_unit_target_
        elif N_unit_exist_with_global_min_len_path == 1:
            #### There is a unique unit accesible, thus the unit is targetted.
            j_exising_unit_target, = indices_existing_units_with_global_min_len_path
            j_unit_target_ = indices_unit_exist[j_exising_unit_target]
            return j_unit_target_
        elif N_unit_exist_with_global_min_len_path >= 2:
    
            indices_existing_units_with_global_min_len_path_and_not_moved = indices_existing_units_with_global_min_len_path[
                np.where([j_existing_unit not in indices_unit_moved for j_existing_unit in indices_existing_units_with_global_min_len_path])[0]
            ]
            N_unit_exist_with_global_min_len_path_and_not_moved = indices_existing_units_with_global_min_len_path_and_not_moved.size
            N_unit_exist_with_global_min_len_path_moved = N_unit_exist_with_global_min_len_path - N_unit_exist_with_global_min_len_path_and_not_moved

            if N_unit_exist_with_global_min_len_path_and_not_moved == 0:
                #### There two or more units with_global_min_len_path and moved
                assert len(indices_unit_moved) >= N_unit_exist_with_global_min_len_path_moved

                for j_existing_unit_with_global_min_len_path in indices_existing_units_with_global_min_len_path:
                    j_unit_with_global_min_len_path = indices_unit_exist[j_existing_unit_with_global_min_len_path]
                    assert j_unit_with_global_min_len_path in indices_unit_moved

                return indices_unit_moved[0]

            elif N_unit_exist_with_global_min_len_path_and_not_moved == 1:
                j_existing_unit_with_global_min_len_path_and_not_moved, = indices_existing_units_with_global_min_len_path_and_not_moved
                return j_existing_unit_with_global_min_len_path_and_not_moved

            elif N_unit_exist_with_global_min_len_path_and_not_moved >= 2:
                if j_unit_target >= 0: return j_unit_target
                else: raise NotImplementedError()

            else: raise ValueError(f"Unexpected value of N_unit_moved = {N_unit_moved}")

        else: raise ValueError(f"Unexpected value of N_unit_exist_with_global_min_len_path"
                               f" = {N_unit_exist_with_global_min_len_path}")

                        
    def update_indices_unit_target_of_oppo(self, state):
        self.update_indices_unit_target_of_oppo_caution(state)
        self.update_indices_unit_target_of_oppo_dash(state)

        
    def propagate_recursively(self, states_pool, j_step, N_phase):

        if j_step == 0:
            self.N_phase_found = 0

        if (j_step == (N_phase - 1)) or (j_step == (self.N_phase_found - 1)):
            states_pool_boss_removed = [states for states in states_pool if states[j_step]['index_node_boss'] < 0]
            return states_pool_boss_removed

        states_pool_per_states_list = []
        for states in states_pool:

            state_pool = self.propagate(states[j_step])

            states_pool_per_states = np.empty((len(state_pool), N_phase), dtype=states.dtype) # prop.state_dtype
            for j_state, state in enumerate(state_pool):
                states_pool_per_states[j_state][:] = states
                states_pool_per_states[j_state,j_step+1] = state

            exist_state_all_oppo_and_box_removed = any((
                states[j_step+1]['index_node_boss'] < 0 
                and states[j_step+1]['index_node_box'] < 0 
                and np.all(states[j_step+1]['indices_node_mobs'] == -1) 
                for states in states_pool_per_states
            ))

            if exist_state_all_oppo_and_box_removed:
#                print(f"exist_state_all_oppo_and_box_removed = {exist_state_all_oppo_and_box_removed}")
                self.N_phase_found = j_step + 1

            states_pool_per_states_ = self.propagate_recursively(states_pool_per_states, j_step+1, N_phase)
            states_pool_per_states_list.extend(states_pool_per_states_)

        return states_pool_per_states_list
    
    
    def setup_initial_states(self):
    
        state = np.empty((), dtype=self.state_dtype)

        index_node_box = self.stage.get('index_node_box')
        if index_node_box is None: index_node_box = -1

        indices_node_start = self.stage['index_node_start']
        if type(indices_node_start) is int: indices_node_start = [indices_node_start]
        indices_node_unit_init = np.asarray(indices_node_start.copy())
        assert np.any(indices_node_unit_init >= 0)

        if type(self.stage['index_node_start']) is int:
            N_node_start = 1
        else: N_node_start = len(self.stage['index_node_start'])


        #### Construct the initial state of the map
        map_inital = Map(
            self.stage['nodes'], 
            not_shown=self.get_nodes_to_be_generated(),
            indices_node_light=self.stage.get('index_node_light')
        )


        indices_unit_moved = np.full_like(indices_node_unit_init, -1, dtype='i4')
        state[()] = (
            indices_node_unit_init, 
            indices_unit_moved,
            self.stage['index_node_boss'], 
            self.stage['indices_node_mobs'], 
            index_node_box, 
            map_inital,
            [-1] * self.N_oppo,
        )


        #### Evaluate the initial `indices_unit_target_oppo`
        self.update_indices_unit_target_of_oppo_caution(state)
        self.update_indices_unit_target_of_oppo_dash(state)


        #### Add branches for the cases where a subset of the start nodes is not occupied
        N_units = len(np.where(indices_node_unit_init >= 0)[0])
        assert np.all(state[()]['index_node'] >= 0)
        state_init_list = [state]
        if N_units == 1: pass
        elif N_units == 2:

            #### Add states where only one unit is present.
            #### There are two cases as there are two start nodes for a single unit.
            state_0_only = deepcopy(state)
            j_unit_slot_empty = 1
            state_0_only['index_node'][j_unit_slot_empty] = -1
            state_init_list.append(state_0_only)

            state_1_only = deepcopy(state)
            j_unit_slot_empty = 0
            state_1_only['index_node'][j_unit_slot_empty] = -1
            state_init_list.append(state_1_only)

        else: raise ValueError(f"Unexpected N_units: {N_units}")


        #### Initialize the light and the visibility of nodes
        index_node_light = self.stage.get('index_node_light')
        if index_node_light is None: index_node_light = -1
        assert self.stage_name[-1] in ('N','H')
        for state in state_init_list:
            state[()]['map'].nodes_visible[:] = True if self.stage_name[-1] == 'N' else False
            indices_unit, = np.where(state[()]['index_node'] >= 0)
            for j_unit in indices_unit:
                if state[()]['index_node'][j_unit] == index_node_light: state[()]['map'].turn_on_light()
                else: state[()]['map'].nodes_visible[state[()]['map'].get_neighbors(state[()]['index_node'][j_unit], n=1)] = True

        return state_init_list
    

    def propagate_branches(self, state_init_list, N_step_max: int):
        
        states_pool = []
        for state_init in state_init_list:
            states = np.empty((N_step_max,), dtype=self.state_dtype)
            states['index_node'] = -1
            states[0] = state_init
            states_pool.append(states)

        states_pool_next = self.propagate_recursively(states_pool, 0, N_step_max)

        if not (self.N_phase_found > 0): raise ValueError("N_phase_found not found")
        else: N_phase = self.N_phase_found
            
        return states_pool_next
    
    
    def search(self, N_step_max):
        state_init_list = self.setup_initial_states()
        states_pool = self.propagate_branches(state_init_list, N_step_max)
        return states_pool
