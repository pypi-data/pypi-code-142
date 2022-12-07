
class DictManipulate:

    def findkeyValue(self,node, kv):
        if isinstance(node, list):
            for i in node:
                for x in self.findkeys(i, kv):
                    yield x

        elif isinstance(node, dict):
            if kv in node:
                yield node[kv]
            for j in node.values():
                for x in self.findkeyValue(j, kv):
                    yield x

    def KeyPathByValue(self,d, search_pattern, prev_datapoint_path=''):
        output = []
        search_pattern = str(search_pattern)
        current_datapoint = d
        current_datapoint_path = prev_datapoint_path
        if type(current_datapoint) is dict:
            for dkey in current_datapoint:
                if search_pattern in str(dkey):
                    c = current_datapoint_path
                    c+="['"+dkey+"']"
                    output.append(c)
                c = current_datapoint_path
                c+="['"+dkey+"']"
                for i in self.KeyPathByValue(current_datapoint[dkey], search_pattern, c):
                    output.append(i)
        elif type(current_datapoint) is list:
            for i in range(0, len(current_datapoint)):
                if search_pattern in str(i):
                    c = current_datapoint_path
                    c += "[" + str(i) + "]"
                    output.append(i)
                c = current_datapoint_path
                c+="["+ str(i) +"]"
                for i in self.KeyPathByValue(current_datapoint[i], search_pattern, c):
                    output.append(i)
        elif search_pattern in str(current_datapoint):
            c = current_datapoint_path
            output.append(c)
        output = filter(None, output)
        return list(output)

    def flatten(self,dd, separator ='_', prefix =''):
        return { prefix + separator + k if prefix else k : v
            for kk, vv in dd.items()
            for k, v in self.flatten(vv, separator, kk).items()
            } if isinstance(dd, dict) else { prefix : dd }

    def splitDict(self,test_dict,K):
        
        res = []
        count = 0
        flag = 0
        indict = dict()
        for key in test_dict:
            indict[key] = test_dict[key]        
            count += 1
            
            # checking for K size and avoiding empty dict using flag
            if count % K == 0 and flag:
                res.append(indict)
                
                # reinitializing dictionary
                indict = dict()
                count = 0
            flag = 1
        return res

