# Simple test of the used library: Fill PDF, Reparaturblatt with Demo-Data

from PyPDFForm import PdfWrapper

filled = PdfWrapper("Reparaturblatt_A4_template_form.pdf").fill(
    {
        "Beschreibung_Defekt": "Kristall hat nicht genug Leistung",
        "Datum_1": "07.03.2026",
        "Datum_2": "07.03.2026",
        "Gegenstand": "Laserschwert",
        "Marke": "UseTheForce",
        "Name": "Luke Skywalker",
        "Number": "007",
        "Reparierender": "Obi Wan Kenobi",
        "emailadress": "luke@skywalker.tatooine",
        "check_newsletter": True,
        "check_plakat": True,
        "check_socialmedia": True,
        "check_zeitung": True,
        "info_konsumentenschutz": True,
        "info_repaircafe": True,
    },
    flatten=True   # optional, set to True to flatten the filled PDF form
)

filled.write("Reparaturblatt_filled2.pdf")
