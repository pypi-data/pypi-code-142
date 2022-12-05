import numpy as np
import random
import math
from collections import namedtuple


class BestCandidateNN:
    def __init__(self):
        self.nn_weights = []
        self.bias = 1
        self.last_input = []
        self.last_predicted_class = -1
        self.last_class_act_funct_output = []

    def activation_function(self, x):
        return ((math.exp(x) - math.exp(-1 * x)) / (math.exp(x) + math.exp(-1 * x)))

    def predict_class(self, input):
        class_act_funct_output = []
        predicted_class = -1
        input_vec = input.copy()
        input_vec.append(self.bias)
        self.last_input = input
        if (len(input_vec) != len(self.nn_weights[0][0])):
            print("Error: input vector has a different number of values than the inputs of training data")
        else:
            try:
                for layer_l in range(0, len(self.nn_weights)):
                    layer_l_output = []
                    for node_j in range(0, len(self.nn_weights[layer_l])):
                        layer_l_output_node_j = []
                        for weight_w in range(0, len(self.nn_weights[layer_l][node_j])):
                            layer_l_output_node_j.append(
                                self.nn_weights[layer_l][node_j][weight_w] * float(input_vec[weight_w])
                            )
                        layer_l_output.append(self.activation_function(sum(layer_l_output_node_j)))
                    input_vec = layer_l_output.copy()
                    input_vec.append(self.bias)
                class_act_funct_output = layer_l_output
                predicted_class = layer_l_output.index(max(layer_l_output))
            except Exception as e:
                print("Unexpected error")
                print(e)
                class_act_funct_output = []
                predicted_class = -1
        self.last_class_act_funct_output = class_act_funct_output
        self.last_predicted_class = predicted_class
        return self.last_predicted_class

    def set_weights(self,weights):
        self.nn_weights=weights

    def get_last_input(self):
        return self.last_input

    def get_last_predicted_class(self):
        return self.last_predicted_class

    def get_last_class_act_funct_output(self):
        return self.last_class_act_funct_output


def dataset_minmax(dataset):
    stats = [[min(column), max(column)] for column in zip(*dataset)]
    return stats

def dataset_mean_sd(dataset):
    stats = [[sum(column)/len(column), np.std(column)] for column in zip(*dataset)]
    return stats

def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row) - 1):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
    return dataset

def standardize_data(dataset, mean_sd):
    for row in dataset:
        for i in range(len(row) - 1):
            row[i] = (row[i] - mean_sd[i][0]) / (mean_sd[i][1])
    return dataset

def log_transform_data(dataset,minmax):
    for row in dataset:
        for i in range(len(row) - 1):
            row[i] = np.log(row[i] + minmax[i][0] + 1)
    return dataset


def performance_metrics(actual, predicted, beta=2):
    unique_classes = np.unique(predicted)
    no_of_classes = len(unique_classes)
    precision_values = []
    recall_values = []
    f_beta_score_values = []
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    if (no_of_classes == 2):
        for index in range(len(predicted)):
            if (predicted[index] == 1 and actual[index] == 1):
                true_positive += 1
            elif (predicted[index] == 0 and actual[index] == 0):
                true_negative += 1
            elif (predicted[index] == 1 and actual[index] == 0):
                false_positive += 1
            elif (predicted[index] == 0 and actual[index] == 1):
                false_negative += 1
        accuracy = round((true_positive + true_negative) / len(predicted), 3)
        if (true_positive + false_positive > 0):
            precision = round((true_positive) / (true_positive + false_positive), 3)
        else:
            precision = 0
        if (true_positive + false_negative > 0):
            recall = round((true_positive) / (true_positive + false_negative), 3)
        else:
            recall = 0
        if (precision + recall > 0):
            f_beta_score = round((1 + (beta ** 2)) * (precision * recall) / (precision + recall), 3)
        else:
            f_beta_score = 0
        precision_values.append(precision)
        recall_values.append(recall)
        f_beta_score_values.append(f_beta_score)
    else:
        total_correct = 0
        for i in range(len(predicted)):
            if (predicted[i] == actual[i]):
                total_correct += 1
        accuracy = round(total_correct / len(predicted), 3)
        for class_index in range(len(unique_classes)):
            current_class = unique_classes[class_index]
            for index in range(len(predicted)):
                if (predicted[index] == current_class and actual[index] == current_class):
                    true_positive += 1
                elif (predicted[index] != current_class and actual[index] != current_class):
                    true_negative += 1
                elif (predicted[index] == current_class and actual[index] != current_class):
                    false_positive += 1
                elif (predicted[index] != current_class and actual[index] == current_class):
                    false_negative += 1
            if (true_positive + false_positive > 0):
                precision = round((true_positive) / (true_positive + false_positive), 3)
            else:
                precision = 0
            if (true_positive + false_negative > 0):
                recall = round((true_positive) / (true_positive + false_negative), 3)
            else:
                recall = 0
            if (precision + recall > 0):
                f_beta_score = round((1 + (beta ** 2)) * (precision * recall) / (precision + recall), 3)
            else:
                f_beta_score = 0
            precision_values.append(precision)
            recall_values.append(recall)
            f_beta_score_values.append(f_beta_score)
    return "%.2f" % round(accuracy, 3), "%.2f" % round(np.mean(precision_values), 3), "%.2f" % round(np.mean(recall_values), 3), "%.2f" % round(np.mean(f_beta_score_values), 2)

def activation_function_tanh(x):
    x=min(100,x)
    x=max(-100, x)
    return ((math.exp(x) - math.exp(-1 * x)) / (math.exp(x) + math.exp(-1 * x)))
def activation_function_logistic(x):
    x=min(100,x)
    x=max(-100, x)
    return (1 / (math.exp(x) + math.exp(-1 * x)))
def activation_function_linear(x):
    return x

def euclidean_distance(list1, list2):
    squares = [(p - q) ** 2 for p, q in zip(list1, list2)]
    return sum(squares) ** .5

def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))

def check_stopping_criteria(obj_f_vals, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate):
    stop_training=False
    if (stopping_criteria=='best_candidate_fitness_min'):
        if (max(obj_f_vals)>=min_fitness_best_candidate):
            stop_training=True
    elif(stopping_criteria=='avg_fitness_min'):
        obj_f_vals_mean=sum(obj_f_vals)/len(obj_f_vals)
        if (obj_f_vals_mean>=min_fitness_avg_population):
            stop_training=True
    elif(stopping_criteria=='worst_candidate_fitness_min'):
        if (min(obj_f_vals)>=min_fitness_worst_candidate):
            stop_training=True
    return stop_training

def DE(train, test, activation_functions,n_features, nclasses, iterations,  NP, n_hidden_nodes,  f_score_beta, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate, \
       donor_vec_strategy, CR, F):
    best = Best(0.0, -1, None)
    population = []
    obj_f_vals = []
    for i in range(NP):
        agent = init_agent(train, n_features, nclasses, n_hidden_nodes,activation_functions)
        if agent != None:
            population.append(agent)
            votes = nn_votes(agent, test)
            train_actual = [int(e[-1]) for e in test]
            agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
            obj_f = float(agent_accuracy)
            obj_f_vals.append(obj_f)

            if obj_f > best.value:
                best = Best(obj_f, len(population) - 1, agent)
    abc_indices = range(len(population) - 1)
    for iterc in range(iterations):
        improvements = 0
        for i in range(len(population)):
            agent_x = population[i]
            objf_x = obj_f_vals[i]
            sel_abc = [(j if j < i else j + 1) for j in random.sample(abc_indices, 5)]
            agent_a, agent_b, agent_c, agent_d, agent_e = [population[j] for j in sel_abc]
            vec_x = agent_to_vec(agent_x)
            vec_a = agent_to_vec(agent_a)
            vec_b = agent_to_vec(agent_b)
            vec_c = agent_to_vec(agent_c)
            vec_d = agent_to_vec(agent_d)
            vec_e = agent_to_vec(agent_e)
            vec_best = agent_to_vec(best.agent)
            vec_xt = vec_x.copy()
            cr_mask_rand = random_matrix(1, len(vec_xt))[0]
            for cr_mask_i in range(len(cr_mask_rand)):
                if (cr_mask_rand[cr_mask_i] < CR):
                    if (donor_vec_strategy=='DE/rand/1'):
                        vec_xt[cr_mask_i] = vec_a[cr_mask_i] + F * (vec_b[cr_mask_i] - vec_c[cr_mask_i])
                    elif (donor_vec_strategy=='DE/rand/2'):
                        vec_xt[cr_mask_i] = vec_a[cr_mask_i] + F * (vec_b[cr_mask_i] - vec_c[cr_mask_i]) + F * (vec_d[cr_mask_i] - vec_e[cr_mask_i])
                    elif (donor_vec_strategy=='DE/best/1'):
                        vec_xt[cr_mask_i] = vec_best[cr_mask_i] + F * (vec_b[cr_mask_i] - vec_c[cr_mask_i])
                    elif (donor_vec_strategy=='DE/best/2'):
                        vec_xt[cr_mask_i] = vec_best[cr_mask_i] + F * (vec_b[cr_mask_i] - vec_c[cr_mask_i]) + F * (vec_d[cr_mask_i] - vec_e[cr_mask_i])
                    elif (donor_vec_strategy=='DE/current-to-best'):
                        vec_xt[cr_mask_i] = vec_x[cr_mask_i] + F * (vec_best[cr_mask_i] - vec_c[cr_mask_i]) + F * (vec_d[cr_mask_i] - vec_e[cr_mask_i])
            agent_xt = vec_to_new_agent(vec_xt, agent_x)
            votes = nn_votes(agent_xt, test)
            train_actual = [int(e[-1]) for e in test]
            agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
            objf_xt = float(agent_accuracy)

            if objf_xt > objf_x:
                population[i] = agent_xt
                obj_f_vals[i] = objf_xt
                improvements += 1

                if objf_xt > best.value:
                    best = Best(objf_xt, i, agent_xt)



        stop_this_training=check_stopping_criteria(obj_f_vals, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate)
        if (stop_this_training):
            break





    best_predictions = nn_votes(best.agent, test)
    test_actual = [row[-1] for row in test]
    test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = performance_metrics(test_actual, best_predictions, f_score_beta)
    return best_predictions, best.agent, best.index, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score


def PSO(train, test, activation_functions, n_features, nclasses, iterations,  NP, n_hidden_nodes,  f_score_beta, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate, \
        w_type, w_constant, w_0, w_Tmax, C_personal, C_global):
    best = Best(0.0, -1, None)
    personal_best=list()
    current_velocity=list()
    population = []
    obj_f_vals = []
    for i in range(NP):
        agent = init_agent(train, n_features, nclasses, n_hidden_nodes,activation_functions)
        if agent != None:
            population.append(agent)
            votes = nn_votes(agent, test)
            train_actual = [int(e[-1]) for e in test]
            agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
            obj_f = float(agent_accuracy)
            obj_f_vals.append(obj_f)
            agent_pos=agent_to_vec(agent)
            personal_best.append(PersonalBest(obj_f,len(population) - 1,agent_pos))
            current_velocity.append(list(np.array(random_matrix(1,len(agent_pos))[0])-.5))
            if obj_f > best.value:
                best = Best(obj_f, len(population) - 1, agent)

    for iterc in range(iterations):
        improvements = 0
        for i in range(len(population)):
            agent_x = population[i]
            objf_x = obj_f_vals[i]
            personal_best_x=personal_best[i]
            current_velocity_x=current_velocity[i]
            current_position_x = agent_to_vec(agent_x)
            max_iterations=iterations
            if (w_type=='constant'):
                inertial_weight=w_constant
            elif (w_type=='linear_decreasing'):
                inertial_weight=(w_0-w_Tmax)*((max_iterations-iterc)/max_iterations)+w_Tmax
            elif (w_type=='nonlinear_decreasing'):
                if (personal_best_x.value+objf_x!=0):
                    m_i = (personal_best_x.value - objf_x) / (personal_best_x.value + objf_x)
                else:
                    m_i=0
                inertial_weight=w_0+(w_Tmax-w_0)*((math.exp(m_i)-1)/(math.exp(m_i)+1))
            random_vec1=random_matrix(1,len(current_position_x))[0]
            random_vec2=random_matrix(1,len(current_position_x))[0]
            new_velocity_x=(inertial_weight*np.array(current_velocity_x))+\
                           (np.array(random_vec1)*C_personal*(np.array(personal_best_x.pos)-np.array(current_position_x)))+\
                           (np.array(random_vec2)*C_global*(np.array(agent_to_vec(best.agent))-np.array(current_position_x)))
            new_velocity_x=list(new_velocity_x)
            new_position_x=list(np.array(current_position_x)+np.array(new_velocity_x))
            agent_xt = vec_to_new_agent(new_position_x, agent_x)
            votes = nn_votes(agent_xt, test)
            train_actual = [int(e[-1]) for e in test]
            agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
            objf_xt = float(agent_accuracy)

            population[i] = agent_xt
            obj_f_vals[i] = objf_xt
            if objf_xt > personal_best_x.value:
                personal_best[i]=PersonalBest(objf_xt, i, agent_to_vec(agent_xt))
                improvements += 1
            if objf_xt > best.value:
                best = Best(objf_xt, i, agent_xt)
        stop_this_training=check_stopping_criteria(obj_f_vals, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate)
        if (stop_this_training):
            break
    best_predictions = nn_votes(best.agent, test)
    test_actual = [row[-1] for row in test]
    test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = performance_metrics(test_actual, best_predictions, f_score_beta)
    return best_predictions, best.agent, best.index, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score

def GA(train, test, activation_functions,n_features, nclasses, iterations,  NP, n_hidden_nodes,  f_score_beta, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate, \
            selection_strategy, p_c, p_m, crossover_strategy, mutation_strategy):
    best = Best(0.0, -1, None)
    population = []
    obj_f_vals = []

    for i in range(NP):
        agent = init_agent(train, n_features, nclasses, n_hidden_nodes,activation_functions)
        if agent != None:
            population.append(agent)
            votes = nn_votes(agent, test)
            train_actual = [int(e[-1]) for e in test]
            agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
            obj_f = float(agent_accuracy)
            obj_f_vals.append(obj_f)

            if obj_f > best.value:
                best = Best(obj_f, len(population) - 1, agent)
    abc_indices = range(len(population) - 1)
    for iterc in range(iterations):
        improvements = 0
        for i in range(len(population)):
            agent_x = population[i]
            objf_x = obj_f_vals[i]
            if (selection_strategy=='fitness_proportionate'):
                selection_prob=objf_x/sum(obj_f_vals)
                random_val=random.randrange(100)/100
                if (random_val>selection_prob):
                    replace=True
            elif (selection_strategy=='tournament'):
                random_idx = random.randrange(len(population))
                if (random_idx==i):
                    random_idx = i+1
                objf_random=obj_f_vals[random_idx]
                if (objf_random>objf_x):
                    replace=True
            if (replace):
                agent_x = init_agent(train, n_features, nclasses, n_hidden_nodes,activation_functions)
                votes = nn_votes(agent, test)
                train_actual = [int(e[-1]) for e in test]
                agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
                obj_f = float(agent_accuracy)
                population[i]=agent_x
                obj_f_vals[i]=obj_f

            sel_abc = [(j if j < i else j + 1) for j in random.sample(abc_indices, 3)]
            agent_a, agent_b, agent_c = [population[j] for j in sel_abc]
            vec_x = agent_to_vec(agent_x)
            vec_a = agent_to_vec(agent_a)
            vec_b = agent_to_vec(agent_b)
            vec_c = agent_to_vec(agent_c)
            vec_xt = vec_x.copy()
            random_val = random.randrange(100) / 100
            if (random_val<=p_c):
                if (crossover_strategy=='single_point'):
                    random_idx=random.randrange(len(vec_xt))
                    for vec_xt_pos_i in range(random_idx,len(vec_xt)):
                        vec_xt[vec_xt_pos_i]=vec_a[vec_xt_pos_i]
                elif(crossover_strategy=='two_point'):
                    random_idx1 = random.randrange(len(vec_xt))
                    random_idx2 = random.randrange(len(vec_xt))
                    random_idx_upper = max(random_idx1, random_idx2)
                    random_idx_lower = min(random_idx1, random_idx2)
                    if (random_idx_lower==random_idx_upper):
                        vec_xt[random_idx_lower] = vec_a[random_idx_lower]
                    else:
                        for vec_xt_pos_i in range(random_idx_lower, random_idx_upper):
                            vec_xt[vec_xt_pos_i] = vec_a[vec_xt_pos_i]

            random_val = random.randrange(100) / 100
            if (random_val <= p_m):
                if (mutation_strategy=='random_interchange'):
                    random_idx1 = random.randrange(len(vec_xt))
                    random_idx2 = random.randrange(len(vec_xt))
                    if (random_idx2==random_idx1):
                        if (random_idx2<len(vec_xt)-1):
                            random_idx2=random_idx2+1
                        else:
                            random_idx2=random_idx2-1
                    vec_xt_random_idx1_value = vec_xt[random_idx1]
                    vec_xt_random_idx2_value = vec_xt[random_idx2]
                    vec_xt[random_idx1] = vec_xt_random_idx2_value
                    vec_xt[random_idx2] = vec_xt_random_idx1_value
                elif(mutation_strategy=='random_substitution'):
                    random_idx = random.randrange(len(vec_xt))
                    random_idx_for_random_sub=random.randrange(len(vec_a))
                    vec_xt[random_idx] = vec_a[random_idx_for_random_sub]
            agent_xt = vec_to_new_agent(vec_xt, agent_x)
            votes = nn_votes(agent_xt, test)
            train_actual = [int(e[-1]) for e in test]
            agent_accuracy, agent_precision, agent_recall, agent_f_beta_score = performance_metrics(train_actual, votes, f_score_beta)
            objf_xt = float(agent_accuracy)
            population[i] = agent_xt
            obj_f_vals[i] = objf_xt
            if objf_xt > objf_x:
                improvements += 1
            if objf_xt > best.value:
                best = Best(objf_xt, i, agent_xt)
        stop_this_training=check_stopping_criteria(obj_f_vals, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate)
        if (stop_this_training):
            break

    best_predictions = nn_votes(best.agent, test)
    test_actual = [row[-1] for row in test]
    test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = performance_metrics(test_actual, best_predictions, f_score_beta)
    return best_predictions, best.agent, best.index, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score

def calc_neuron_val(vals, weights, bias):
    return np.dot(vals, weights) + 1.0 * bias

def eval_neural_net(all_layers, input_vec):
    prev_layer_vec = input_vec
    for layer in all_layers:
        act_fun_input = list(map(lambda neuron_weights: calc_neuron_val(prev_layer_vec, neuron_weights[:-1], neuron_weights[-1]),layer.weights))
        layer_vals = []
        for act_fun_i in range(len(act_fun_input)):
            layer_vals.append(layer.act_fun(act_fun_input[act_fun_i]))
        prev_layer_vec = layer_vals
    return layer_vals

def nn_votes(all_layers, dataset):
    votes = []
    for data in dataset:
        data = np.array(data)
        data = data.tolist()
        label, input_vec = (data[-1], data[:-1])
        try:
            output = eval_neural_net(all_layers, input_vec)
        except:
            output=0
        vote = np.argmax(output)
        votes.append(vote)
    return np.asarray(votes)

Layer = namedtuple('Layer', 'weights act_fun')
Best = namedtuple('Best', 'value index agent')
PersonalBest = namedtuple('PersonalBest', 'value index pos')


def init_agent(train, n_features, nclasses, n_hidden_nodes, activation_functions):
    architecture=[n_features]
    for n_hidden_nodes_layer_i in range(0,len(n_hidden_nodes)):
        architecture.append(n_hidden_nodes[n_hidden_nodes_layer_i])
    architecture.append(nclasses)
    all_layers = []
    for l_idx in range(1, len(architecture)):
        l_in = architecture[l_idx - 1]
        l_out = architecture[l_idx]
        l_act = activation_functions[-1]
        if l_idx < len(activation_functions):
            l_act = activation_functions[l_idx]
        layer = Layer(np.random.rand(l_out, l_in + 1) * 2 - 1, l_act)
        all_layers.append(layer)
    return all_layers

def agent_to_vec(agent):
    return np.concatenate([np.ravel(layer.weights) for layer in agent])

def vec_to_new_agent(vec, old_agent):
    from_idx = 0
    new_layers = []
    for layer in old_agent:
        size_weights = 0
        for weight_ in range(len(layer.weights)):
            size_weights = size_weights + len(layer.weights[weight_])
        to_idx = from_idx + size_weights
        new_weights = vec[from_idx:to_idx].copy()
        idx = 0
        new_weights_reshape = []
        for row_ in range(len(layer.weights)):
            row_i = []
            for col_ in range(len(layer.weights[0])):
                row_i.append(new_weights[idx])
                idx += 1
            new_weights_reshape.append(row_i)
        new_layers.append(Layer(new_weights_reshape, layer.act_fun))
        from_idx = to_idx
    return new_layers


def random_matrix(rows, cols):
    rand_matrix = []
    for row in range(rows):
        row_i = []
        for col in range(cols):
            row_i.append(random.randrange(10000000) / 10000000)
        rand_matrix.append(row_i)
    return rand_matrix

def evaluate_algorithm(dataset, algorithm, activation_functions,  *args):
    train_set= list(dataset)
    test_set = list(dataset)
    predicted, final_network, final_network_idx, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = algorithm(train_set, test_set, activation_functions, *args)
    return final_network, final_network_idx, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score


def correct_class_and_impute_and_str_to_float(dataset_, class_col_number, last_feature_column_number, first_feature_column_number, imputation_method, has_header):
    if (has_header == 'yes'):
        dataset_ = dataset_[1:]
    count_missing=0
    count_rows_with_missing=0
    track_columns_with_missing=set()
    correct_class_col=False
    col_sums=list(np.zeros(len(dataset_[0])))
    col_non_missing_count=list(np.zeros(len(dataset_[0])))
    if class_col_number != len(dataset_[0]) - 1 or class_col_number < last_feature_column_number or class_col_number > last_feature_column_number+1 or class_col_number < first_feature_column_number:
        correct_class_col=True

    dataset_final=list()
    unique_classes_set= set()
    unique_classes_list = list()
    for row_i in range(len(dataset_)):
        remove_row=False
        row_current=list(dataset_[row_i])

        if correct_class_col:
            if (class_col_number > first_feature_column_number and class_col_number < last_feature_column_number):
                row_corrected = row_current[first_feature_column_number:class_col_number] + row_current[class_col_number + 1:len(row_current)] + [row_current[class_col_number]]
            else:
                row_corrected = row_current[first_feature_column_number:last_feature_column_number+1] + [row_current[class_col_number]]

            row_current=list(row_corrected)

        row_current_count_missing=0
        for col_i in range(len(row_current)):
            if (col_i == len(row_current)-1):
                if (row_current[col_i] not in unique_classes_set):
                    unique_classes_set.add(row_current[col_i])
                    unique_classes_list.append(row_current[col_i])
                new_class_label=unique_classes_list.index(row_current[col_i])
                row_current[col_i]=new_class_label
            else:
                try:
                    row_current[col_i] = float(row_current[col_i])
                    col_sums[col_i]=col_sums[col_i]+row_current[col_i]
                    col_non_missing_count[col_i]=col_non_missing_count[col_i]+1
                except:
                    count_missing=count_missing+1
                    row_current_count_missing = row_current_count_missing + 1
                    track_columns_with_missing.add(col_i)
                    if (imputation_method=='remove' or row_current_count_missing==len(row_current)-1):
                        remove_row = True
        if remove_row == False:
            dataset_final.append(row_current)

        if (row_current_count_missing>0):
            count_rows_with_missing=count_rows_with_missing+1

    n_columns_with_missing_values=len(unique_classes_list)
    new_class_labels=list(range(len(unique_classes_list)))


    track_columns_with_missing=list(track_columns_with_missing)
    if count_missing>0 and imputation_method!='remove':
        for col_missing_track_idx in range(len(track_columns_with_missing)):
            col_missing_i=track_columns_with_missing[col_missing_track_idx]
            col_missing_i_mean=col_sums[col_missing_i]/col_non_missing_count[col_missing_i]
            if (imputation_method=='mean'):
                col_missing_i_values = [e[col_missing_i] for e in dataset_final]
                for col_missing_i_values_row_idx in range(len(col_missing_i_values)):
                    try:
                        float_test=float(col_missing_i_values[col_missing_i_values_row_idx])
                    except:
                        dataset_final[col_missing_i_values_row_idx][col_missing_i]=col_missing_i_mean
    return dataset_final, unique_classes_list, new_class_labels, count_missing, n_columns_with_missing_values, count_rows_with_missing



def train(data, first_feature_column_number,last_feature_column_number,class_col_number,has_header, train_method,
            imputation_method='mean',transformation_method='None',act_fun_type='tanh',f_score_beta=2,
            stopping_criteria='best_candidate_fitness_min',n_iterations=100,min_fitness_best_candidate=0.99,min_fitness_avg_population=0.99,min_fitness_worst_candidate=0.99,
            n_hidden_nodes=[3,5,3],
            w_type='nonlinear_decreasing',w_constant=0.73,w_0=0.9,w_Tmax=0.5,C_personal=0.5,C_global=0.5,
            NP=100,donor_vec_strategy='DE/rand/1',CR=0.5,F=1,
            p_c=0.8,p_m=0.5,selection_strategy='fitness_proportionate',crossover_strategy='single_point',mutation_strategy='random_substitution'):

    dataset, old_class_labels, new_class_labels, n_missing_values, n_columns_with_missing_values, n_rows_with_missing_values = correct_class_and_impute_and_str_to_float(data, class_col_number-1, last_feature_column_number-1, first_feature_column_number-1, imputation_method, has_header)


    if (transformation_method=='norm'):
        minmax = dataset_minmax(dataset)
        normalize_dataset(dataset, minmax)
    elif (transformation_method=='standardize'):
        mean_sd = dataset_mean_sd(dataset)
        standardize_data(dataset, mean_sd)
    elif (transformation_method=='log'):
        minmax = dataset_minmax(dataset)
        log_transform_data(dataset, minmax)

    if (act_fun_type == 'tanh'):
        activation_functions=(activation_function_tanh,)
    elif (act_fun_type == 'logistic'):
        activation_functions = (activation_function_logistic,)
    elif (act_fun_type == 'linear'):
        activation_functions=(activation_function_linear,)

    n_features = len(dataset[0]) - 1
    n_classes = len(new_class_labels)
    n_observations =len(dataset)


    if (train_method == 'DE'):
        network, network_idx, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = evaluate_algorithm(dataset, DE, activation_functions, n_features, n_classes, n_iterations, NP, n_hidden_nodes, f_score_beta, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate, donor_vec_strategy, CR, F)
    elif (train_method == 'PSO'):
        network, network_idx, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = evaluate_algorithm(dataset, PSO, activation_functions, n_features, n_classes, n_iterations, NP, n_hidden_nodes, f_score_beta, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate, w_type, w_constant, w_0, w_Tmax, C_personal, C_global)
    elif (train_method == 'GA'):
        network, network_idx, test_set_accuracy, test_set_precision, test_set_recall, test_set_f_beta_score = evaluate_algorithm(dataset, GA, activation_functions, n_features, n_classes, n_iterations, NP, n_hidden_nodes, f_score_beta, stopping_criteria, min_fitness_best_candidate, min_fitness_avg_population, min_fitness_worst_candidate, selection_strategy, p_c, p_m, crossover_strategy, mutation_strategy)

    weights_as_list = list()
    for layer_i in range(len(network)):
        weights_as_list_layer_i = list()
        for layer_i_node_j in range(len(network[layer_i][0])):
            layer_i_node_j_weights = network[layer_i][0][layer_i_node_j]
            weights_as_list_layer_i.append(layer_i_node_j_weights)
        weights_as_list.append(weights_as_list_layer_i)

    nn_best = BestCandidateNN()
    nn_best.set_weights(weights_as_list)

    return {
        "best_candidate": nn_best,
        "best_accuracy_in_training": test_set_accuracy,
        "n_features":n_features,
        "n_observations":n_observations,
        "n_classes":n_classes,
        "class_col_number":class_col_number,
        "old_class_labels":old_class_labels,
        "new_class_labels":new_class_labels,
        "n_missing_values":n_missing_values,
        "n_columns_with_missing_values": n_columns_with_missing_values,
        "n_rows_with_missing_values": n_rows_with_missing_values
    }

