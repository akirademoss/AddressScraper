import PyPDF2
import re

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text
    
def parse_text(text, keyword):
    """
    Parses text based on a keyword and extracts relevant information.

    Args:
        text (str): The text to parse.
        keyword (str): The keyword to search for.

    Returns:
        list: A list of strings containing the extracted information.
    """
    results = []
    keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    for line in text.splitlines():
      if keyword_pattern.search(line):
        results.append(line.strip())
    return results

if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('test.pdf')
    keyword_email = "email: "
    keyword_street = "street: "
    keyword_city = "city: "
    keyword_zip = "zip: "
    keyword_state = "state: "
    #output = parse_text(extracted_text, keyword_to_find)
    #print(extracted_text)
    client_address_info = []
    for text in extracted_text:
        email = parse_text(text, keyword_email)
        if email:
            client_address_info.append(email)
        street = parse_text(text, keyword_street)
        if street:
            client_address_info.append(street)
        city = parse_text(text, keyword_city)
        if city:
            client_address_info.append(city)
        zip = parse_text(text, keyword_zip)
        if zip:
            client_address_info.append(zip)
        state = parse_text(text, keyword_state)
        if state:
            client_address_info.append(state)

        print(client_address_info)
        #print(text)