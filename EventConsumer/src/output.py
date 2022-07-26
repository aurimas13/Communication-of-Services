# Created by Aurimas A. Nausedas on 07/24/22.
# Updated by Aurimas A. Nausedas on 07/25/22.

import json


def persist_output(json_string, target_path):
    # Directly from dictionary
    i = 0
    with open(target_path, 'a') as outfile:
        if i == 0:
            json.dump(json_string, outfile)
            outfile.write('\n')
            i += 1
        else:
            json.dump(json_string, outfile)
            outfile.write('\n')
