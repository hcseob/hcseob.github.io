import json
import os

import fire
import openai
import re


def update_dictionary_with_list(dictionary, update_list):
    if not update_list:
        print(f"No new links created.")
    else:
        print("Links in page:")
        print(update_list)
    for item in update_list:
        if item in dictionary:
            if dictionary[item] > 0:
                dictionary[item] += 1
        else:
            dictionary[item] = 1

def find_linked_pages(file_path):
    unique_link_texts = set()

    with open(file_path, 'r') as file:
        content = file.read()
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'  # Pattern to match link text and link path
        
        matches = re.findall(pattern, content)
        
        for match in matches:
            link_text, link_path = match
            if not link_path.startswith(('http://', 'https://')):
                unique_link_texts.add(link_text)
    
    return list(unique_link_texts)


def load_creation_priority(fname):
    # Open the file containing the dictionary
    with open(fname, 'r') as f:
        # Load the dictionary from the file
        creation_priority = json.load(f)
    
    return creation_priority

def save_creation_priority(fname, creation_priority):
    with open(fname, 'w') as f:
        json.dump(creation_priority, f)

def create_page_text(page_name, new_links):
    openai.api_key = os.environ["OPENAI_API_KEY"]


    if new_links:
        user_content = f"Create a wikipeda page, using markdown language, for the topic {page_name}. Include links to pages that would typically have their own page using markdown links. An example would be to create link for Europe as [Europe](Europe.md)"
    else:
        user_content = f"Create a wikipeda page, using markdown language, for the topic {page_name}."
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": 'You are a wikipedia super contributor and write excellent wikipedia pages from scratch. You write these pages using the markdown format.'},
                          {"role": "user", "content": user_content}
                ])
    with open(f"pages/{page_name}.md", 'w') as f:
        f.write(f"---\ntitle: {page_name}\n---\n")
        f.write(response.choices[0].message.content)

    # UPDATE THE DICTIONARY
    linked_pages = find_linked_pages(f"pages/{page_name}.md")

    return linked_pages


def create_page(creation_priority, new_links):
    # Find the largest integer and corresponding key
    page_name = max(creation_priority, key=creation_priority.get)
    max_value = creation_priority[page_name]
    
    if max_value > 0:
        print(f"Creating page for '{page_name}' which is pointed to by {max_value} deadlinks.")
        
        # Set that value to -1
        creation_priority[page_name] = -1

        linked_pages = create_page_text(page_name, new_links)
        update_dictionary_with_list(creation_priority, linked_pages)

        print(f"Updated value for '{page_name}' to -1 and added new links to the creation_priority dictionary.\n")


def dead_link_exists(creation_priority):
    for page_name in creation_priority:
        if creation_priority[page_name] > 0:
            return True
    return False


def main(page_count=1, new_links=True, fname_cp='pages/creation_priority.json'):    
    creation_priority = load_creation_priority(fname_cp)

    for n in range(page_count):
        if dead_link_exists(creation_priority):
            create_page(creation_priority, new_links)
        else:
            print(f"No positive keys, nothing to do. Created {n} out of {page_count} pages.")
            break

    save_creation_priority(fname_cp, creation_priority)
    print(f"Saved the creation_priority dictionary back to {fname_cp}. Exiting.\n")

if __name__ == "__main__":
    fire.Fire(main)