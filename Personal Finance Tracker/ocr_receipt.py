import pytesseract
from PIL import Image
import re

def extract_total_from_receipt(image_path):
    # Load and convert image
    image = Image.open(image_path).convert("RGB")

    # OCR
    text = pytesseract.image_to_string(image)

    # Extract total amount using regex
    match = re.search(r"Total\s+([0-9]+\.?[0-9]*)", text, re.IGNORECASE)

    if match:
        return match.group(1)
    else:
        return None
