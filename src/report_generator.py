from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer

c=canvas.Canvas('report.pdf',pagesize=A4)
