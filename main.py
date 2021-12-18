# Code Changed, Optimized And Commented By: OZX-OG

from PIL import Image, ImageDraw, ImageFont
import textwrap, requests, json

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return (quote)
    
def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=30)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height


def make_Image():
    image = Image.new('RGB', (1080, 1920), color = (0, 0, 0))
    fontsize = 60  
    font = ImageFont.truetype("arial.ttf", fontsize)
    text1 = "Quote:"
    text2 = get_quote()

    text_color = "white"
    text_start_height = 750
    draw_multiple_line_text(image, text1, font, text_color, text_start_height)
    draw_multiple_line_text(image, text2, font, text_color, (text_start_height + 60))
    image.save('pil_text.jpg')

if __name__ == "__main__":
    make_Image()
