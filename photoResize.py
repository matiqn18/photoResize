from PIL import Image
import os


def make_square(image_path, output_path, size=1080):
    """
    Przekształca obraz na kwadrat o zadanym rozmiarze, wyśrodkowując go
    na przezroczystym tle i zachowując przezroczystość (RGBA).

    Parametry:
    - image_path: ścieżka do pliku wejściowego
    - output_path: ścieżka do zapisu pliku wyjściowego
    - size: docelowy rozmiar boku kwadratu (domyślnie 1080)
    """

    # Wczytanie obrazu i konwersja do RGBA (zachowanie przezroczystości)
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size

    # Tworzymy nowy kwadratowy obraz z przezroczystym tłem
    square = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    # Skalujemy obraz, żeby zmieścił się w obrębie kwadratu bez rozciągania
    img.thumbnail((size, size), Image.LANCZOS)

    # Obliczamy pozycję, by wyśrodkować obraz w kwadracie
    offset_x = (size - img.size[0]) // 2
    offset_y = (size - img.size[1]) // 2

    # Wklejamy obraz na kwadrat, używając kanału alfa (przezroczystość jako maska)
    square.paste(img, (offset_x, offset_y), img)

    # Zapisujemy wynik do pliku PNG (zachowanie przezroczystości)
    square.save(output_path, format="PNG")
    print(f"Zapisano: {output_path}")


# Foldery wejściowy i wyjściowy
input_folder = "input"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Przetwarzanie wszystkich obrazów z folderu input
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_filename)
        make_square(input_path, output_path)
