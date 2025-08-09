import pdfplumber

async def read_file(file_name):
    with pdfplumber.open(file_name) as pdf, open(f"{file_name}_output.txt", "w", encoding="utf-8") as f:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                f.write(t + '\n')