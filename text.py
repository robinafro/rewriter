from rewrite import send_request
import docx

def autocorrect_text(text):
    return send_request(text)["data"]["message"]

def transform_docx_file(file_path):
    doc = docx.Document(file_path)

    # Iterate through each paragraph in the document
    for paragraph in doc.paragraphs:
        # Check if the paragraph has a unique style
        for run in paragraph.runs:
            # Apply your autocorrection function to the paragraph text
            if run.text.strip() == "":
                continue
            
            print("Autocorrecting:", run.text)

            run.text = autocorrect_text(run.text)

            print("Autocorrected:", run.text)

    # Save the modified document
    doc.save(file_path)

def transform_txt_file(input_file, output_file):
    with open(input_file, 'r') as file:
        input_text = file.read()

    output_text = autocorrect_text(input_text)

    with open(output_file, 'w') as file:
        file.write(output_text)

transform_docx_file('test_folder/input.docx')