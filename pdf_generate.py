
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_pdf(itinerary_text, filename="trip.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph(itinerary_text.replace("\n", "<br/>"), styles["Normal"])
    )

    doc.build(story)
