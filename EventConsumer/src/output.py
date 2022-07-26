import json


def persist_output(json_string, target_path) -> None:
    '''
    The function writes the json string data into given output location
    :param json_string: String
    :param target_path: String
    :return: None
    '''
    with open(target_path, 'a') as outfile:
        json.dump(json_string, outfile)
        outfile.write('\n')
