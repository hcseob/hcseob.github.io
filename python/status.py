import fire
import json

def load_creation_priority(fname):
    # Open the file containing the dictionary
    with open(fname, 'r') as f:
        # Load the dictionary from the file
        creation_priority = json.load(f)
    
    return creation_priority


def main(fname_cp='pages/creation_priority.json'):    
    creation_priority = load_creation_priority(fname_cp)


    pages_to_create = [cp for cp in creation_priority if creation_priority[cp] != -1]
    print(f"There are {len(pages_to_create)} pages remaining to create.")
    print(f"The pages remaining are:")
    print(pages_to_create)

    dict = {}
    for cp in creation_priority:
        key = creation_priority[cp]
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    
    keys = list(dict.keys())
    keys.sort()
    for key in keys:
        if key == -1:
            print(f"There have been {dict[key]} pages created.")
        else:
            print(f"There are {dict[key]} pages with {key} deadlinks.")


if __name__ == "__main__":
    fire.Fire(main)