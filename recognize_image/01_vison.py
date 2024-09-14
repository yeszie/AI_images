import os
import requests
import base64
from tempfile import gettempdir

# Konfiguracja API
api_key = "OPEN_AI_API_KEY_____________________________________________________________________"
base_url = "https://api.openai.com/v1/chat/completions"
model_name = "gpt-4o"
max_tokens = 4096

# Zaktualizowana treść wiadomości dostosowana do portalu geodezyjnego
message_template = """
Opis zdjęcia: Co przedstawia to zdjęcie?
Jakie informacje można wyczytać z tego zdjęcia?
Nie opisuj pogody, staraj się zwięźle streścić.
"""

# Funkcja do kodowania obrazów w base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

# Funkcja do przetwarzania obrazów JPG
def process_jpg_image(image_path):
    print(f"Przetwarzanie pliku JPG: {image_path}")
    return [image_path]

# Funkcja do przetwarzania wszystkich plików w folderze
def process_files_in_folder(folder_path):
    input_folder = os.path.join(folder_path, "foto")
    output_folder = gettempdir()

    # Utworzenie folderu input, jeśli nie istnieje
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Utworzono folder: {input_folder}")

    # Iterowanie przez pliki w folderze input
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if filename.lower().endswith('.jpg'):
            print(f"Przetwarzanie pliku JPG: {filename}")
            image_paths = process_jpg_image(file_path)
        else:
            print(f"Nieobsługiwany plik: {filename}")
            continue

        # Przygotowanie treści wiadomości z opisem
        message_text = message_template

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message_text
                    }
                ]
            }
        ]

        # Dodanie obrazów z wyraźnym wskazaniem kolejności stron
        for i, image_path in enumerate(image_paths, start=1):
            encoded_image = encode_image_to_base64(image_path)
            image_message = {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Zdjęcie {i} geodezyjne:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
            messages.append(image_message)

        # Przygotowanie payload
        payload = {
            "model": model_name,
            "messages": messages,
            "max_tokens": max_tokens
        }

        # Nagłówki żądania
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Wysłanie żądania POST do API
        response = requests.post(base_url, json=payload, headers=headers)

        # Sprawdzenie odpowiedzi
        if response.status_code == 200:
            response_json = response.json()
            content = response_json.get('choices', [{}])[0].get('message', {}).get('content', '')
            print(content)
            
            # Zapis odpowiedzi do pliku
            output_file_path = os.path.splitext(file_path)[0] + ".txt"
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(content)
            print(f"Odpowiedź zapisana w pliku: {output_file_path}")
        else:
            print(f"Żądanie nie powiodło się. Status code: {response.status_code}")
            print("Treść błędu:", response.text)

# Uruchomienie przetwarzania plików w folderze
if __name__ == "__main__":
    process_files_in_folder(os.path.dirname(__file__))
