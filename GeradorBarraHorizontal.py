from PIL import Image, ImageDraw
import os

# Caminhos para os arquivos de entrada e saída
input_image_path = "C:/Users/Magvia/Documents/TccDan/html-css-js-portfolio-main/Vector 2.png"
output_directory = "C:/Users/Magvia/Documents/TccDan/html-css-js-portfolio-main/progress_bars"


# Criar diretório de saída se não existir
os.makedirs(output_directory, exist_ok=True)

# Carregar a imagem base
base_image = Image.open(input_image_path)
width, height = base_image.size

# Calcular a largura de cada incremento
increment_width = width // 100

# Gerar 99 imagens de barras de progresso
for i in range(1, 100):
    # Criar uma cópia da imagem base
    img = base_image.copy()
    draw = ImageDraw.Draw(img)
    
    # Calcular a área branca
    white_area = (0, 0, i * increment_width, height)
    
    # Desenhar a área branca
    draw.rectangle(white_area, fill="white")
    
    # Salvar a imagem
    img.save(f"{output_directory}/progress_{i}.png")

print("Imagens geradas com sucesso.")
