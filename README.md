# TXT TO CSV Setup Instructions

1. Install spaCy (if you haven’t yet):
pip install spacy

2. Download English language model:
python -m spacy download en_core_web_sm

3. Usage:
Place your .txt file in the same folder as the script and name it input.txt, or change the filename in the script.

4. Run the script:
python txt_to_entities_csv.py

5. Output:
It will generate a output.csv file containing two columns: Entity and Label.
