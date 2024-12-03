def fusionner_dicts(dict1,dict2):
    dict=dict1
    for i in dict2:
        if i in dict:
            dict[i]=dict[i]+dict2[i]
        else:
            dict[i]=dict2[i]
    return dict
dict1 = {"a": 1, "b": 2, "c": 3}  
dict2 = {"b": 2, "c": 4, "d": 5}
print(fusionner_dicts(dict1,dict2))