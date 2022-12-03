from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models.functions import Lower

def make_certificate(instance, type):
    buffer = BytesIO()
    CERTIFICATE = "CERTIFICATE.png"
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    height, width = A4
    c.drawImage(CERTIFICATE, 0, 0, width=width, height=height)
    # name
    c.setFillColor(HexColor("#024547"))
    c.setFont('Times-BoldItalic', 45, leading=None)
    if type == 'course_done':
        c.drawCentredString(330, 310, instance.process_course.user.full_name)
    else:
        c.drawCentredString(330, 310, "Pham Huu Bang")
    # course_name
    c.setFillColor(HexColor("#444440"))
    c.setFont('Courier-BoldOblique', 19, leading=None)
    if type == 'course_done':
        c.drawCentredString(400, 235, f'"{instance.process_course.course.title}"')
    else:
        c.drawCentredString(400, 235, f'"{instance.title}"')
    
    # date
    c.setFillColor(HexColor("#024547"))
    c.setFont('Times-BoldItalic', 30, leading=None)
    if type == 'course_done':
        c.drawCentredString(230, 150, datetime.now().strftime("%d-%m-%Y"))
    else:
        c.drawCentredString(230, 150, "dd-mm-yyyy") 
    c.save()
    # save pdf
    file_data = ContentFile(buffer.getvalue(),  name='certificate.pdf')
    buffer.close()
    return file_data