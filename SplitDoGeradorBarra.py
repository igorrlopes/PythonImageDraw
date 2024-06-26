from PIL import Image
import os

# Caminhos para os arquivos de entrada e saída
output_directory = "C:/Users/Magvia/Documents/TccDan/html-css-js-portfolio-main/progress_bars"
split_output_directory = "C:/Users/Magvia/Documents/TccDan/html-css-js-portfolio-main/progress_bars_split"

# Criar diretório de saída se não existir
os.makedirs(split_output_directory, exist_ok=True)

# Dimensões para cortar as imagens
crop_width = 234
crop_height = 48

# Função para cortar e salvar a imagem em três partes
def split_image(image_path, base_name):
    img = Image.open(image_path)
    for i, part in enumerate(["Inicio", "Meio", "Fim"]):
        left = i * crop_width
        right = left + crop_width
        cropped_img = img.crop((left, 0, right, crop_height))
        cropped_img.save(f"{split_output_directory}/{part}{base_name}.png")

# Processar cada imagem gerada
for i in range(1, 100):
    base_name = f"Progress_{i}"
    image_path = f"{output_directory}/{base_name}.png"
    split_image(image_path, base_name)

"Imagens cortadas e salvas com sucesso."
