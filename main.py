# Code Changed, Optimized And Commented By: OZX-OG

from PIL import Image, ImageDraw, ImageFont
import textwrap, requests, json

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
    resolution = (1080, 1920)
    background_color = (0, 0, 0) #black
    fontsize = 60  
    text_color = "white"
    text_start_height = 750

    image = Image.new('RGB', resolution, color = background_color)
    font = ImageFont.truetype("arial.ttf", fontsize)
    text_q = "Quote:"
    text = get_quote()

    draw_multiple_line_text(image, text_q, font, text_color, text_start_height)
    draw_multiple_line_text(image, text, font, text_color, (text_start_height + 60))
    image.save('Image.jpg')

if __name__ == "__main__":
    make_Image()

if __name__ == "__main__":
    make_Image()
