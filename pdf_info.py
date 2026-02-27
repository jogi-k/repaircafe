# Simple test of the used library: export form-data to json

import json
from PyPDFForm import PdfWrapper

pdf_form_schema = PdfWrapper("Reparaturblatt_A4_template_for_pdf_form.pdf").schema

print(json.dumps(pdf_form_schema, indent=4, sort_keys=True))


