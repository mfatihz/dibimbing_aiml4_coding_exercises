def create_dictionary_zip(keys, values):
    if type(keys) is not list or type(values) is not list:
        raise Exception("'keys' and 'values' not list")
    if len(keys) != len(values):
        raise Exception(f"length of keys ({len(keys)}) different from length of values ({len(keys)})")
    
    return dict(zip(keys, values))

def create_dictionary_dict_comprehension(keys, values):
    if type(keys) is not list or type(values) is not list:
        raise Exception("'keys' and 'values' not list")
    if len(keys) != len(values):
        raise Exception(f"length of keys ({len(keys)}) different from length of values ({len(keys)})")
    
    return {k:v for k,v in zip(keys, values)}

#_dict = create_dictionary_zip(['a','b'],[1,2])
_dict = create_dictionary_dict_comprehension(['a','b'],[1,2])
print(_dict)