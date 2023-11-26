from fpdf import FPDF
from PIL import Image


def main():
    name=input("Name: ")

    with Image.open("shirtificate.png") as img:
        image_width, image_height = img.size

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_font("helvetica", "", 52)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")

    pdf.image("shirtificate.png",  x = ((210*0.2) / 2), y = 100, w = image_width*( 0.8/(image_width/210) ), h = image_height*( 0.8/(image_width/210) ))

    pdf.set_text_color(255,255, 255)
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(-190, 300, text=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
