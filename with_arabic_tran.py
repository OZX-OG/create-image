from PIL import Image, ImageDraw, ImageFont
import textwrap, requests, json, arabic_reshaper
from deep_translator import GoogleTranslator
from bidi.algorithm import get_display

def get_quote():
    response = requests.get("https://zenquotes.io/api/random") #request the quote
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return (quote) 
    
def draw_multiple_line_text(image, text, font, text_color, text_start_height, arab=False):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=30)
    for line in lines:
        line_width, line_height = (font.getsize(line))
        line_width *= 1
        if arab: line_height *= -1
        else: line_height *= 1
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height

def make_Image():
    resolution = (1080, 1920) #resolution of the image
    background_color = (0, 0, 0) #black
    fontsize = 60  
    text_color = (255,255,255)
    text_start_height = 750

    image = Image.new('RGB', resolution, color = background_color) #make new image
    font = ImageFont.truetype("arial.ttf", fontsize) #set the font
    text_q = "| Quote <==> اقتبس |"
    text_en = get_quote()

    translated = GoogleTranslator(source='auto', target='ar').translate(text_en)# translate quote to arabic
    reshaper_text = arabic_reshaper.reshape(translated)
    bidi_text_ar = get_display(reshaper_text)

    reshaper_text = arabic_reshaper.reshape(text_q)
    bidi_text_ar_q = get_display(reshaper_text)

    draw_multiple_line_text(image, bidi_text_ar, font, text_color, (text_start_height - 80), True) #arabic
    draw_multiple_line_text(image, bidi_text_ar_q, font, (200,0,0), text_start_height) #write 'Quote <==> اقتبس'
    draw_multiple_line_text(image, text_en, font, text_color, (text_start_height + 80)) #write quote

    image.save('Image.jpg')

if __name__ == "__main__":
    make_Image()
