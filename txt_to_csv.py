import spacy
import csv
import os

def extract_entities_from_text(text):
    nlp = spacy.load("en_core_web_sm")  # Load small English model
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def txt_to_entities_csv(txt_file_path, csv_file_path):
    if not os.path.isfile(txt_file_path):
        print(f"Error: File '{txt_file_path}' not found.")
        return

    with open(txt_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    entities = extract_entities_from_text(text)

    if not entities:
        print("No entities found in the text.")
        return

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Entity', 'Label'])  # Header
        writer.writerows(entities)

    print(f"Entities written to '{csv_file_path}'.")

if __name__ == "__main__":
    txt_file = "input.txt"      # Replace with your actual input file
    csv_file = "output.csv"     # Output CSV file
    txt_to_entities_csv(txt_file, csv_file)
