# Przetwarzanie zdjęć z OpenAI GPT-4o

## Opis projektu

Ten projekt umożliwia automatyczne przetwarzanie plików JPG z folderu o nazwie `foto` oraz przesyłanie ich do modelu GPT-4o za pomocą OpenAI API. Skrypt generuje opis zawartości zdjęcia zgodnie z szablonem wiadomości, który koncentruje się na wyciągnięciu konkretnych informacji na temat zdjęcia.

Skrypt iteruje przez wszystkie pliki JPG w podanym folderze, koduje je do formatu base64, a następnie przesyła je do API OpenAI, aby uzyskać zwięzły opis zdjęcia. Wynikowy opis jest zapisywany w pliku tekstowym o tej samej nazwie co plik zdjęcia, ale z rozszerzeniem `.txt`.

## Jak działa skrypt?

1. **Folder `foto`:** Skrypt przetwarza pliki JPG znajdujące się w folderze o nazwie `foto`. Jeśli folder nie istnieje, zostanie automatycznie utworzony.
2. **Przetwarzanie zdjęć:** Każde zdjęcie jest kodowane w formacie base64 i dodawane do wiadomości, która następnie jest wysyłana do modelu GPT-4o.
3. **Zapytanie do OpenAI API:** Skrypt wykorzystuje OpenAI API (konkretnie model GPT-4o) do wygenerowania odpowiedzi na temat zawartości zdjęcia, zgodnie z predefiniowanym szablonem wiadomości.
4. **Zapis wyniku:** Odpowiedź z modelu jest zapisywana w pliku tekstowym o tej samej nazwie, co oryginalne zdjęcie, ale z rozszerzeniem `.txt`. Plik ten zawiera opis zdjęcia wygenerowany przez model AI.
5. **Obsługa plików:** Obsługiwane są tylko pliki z rozszerzeniem `.jpg`. Inne formaty są ignorowane.

## Wymagania

1. **OpenAI API Key:** Wymagany jest klucz API OpenAI, który powinien być przechowywany jako zmienna środowiskowa `OPEN_AI_API_KEY`.
2. **Zależności:**
   - `requests`: Biblioteka do wykonywania zapytań HTTP do API OpenAI.
   - `os`: Do obsługi operacji na plikach i folderach.
   - `base64`: Do kodowania zdjęć w formacie base64.
   - `tempfile`: Do zarządzania katalogiem tymczasowym.
   - `dotenv`: Do wczytywania klucza API z pliku `.env`.

Aby zainstalować zależności, możesz użyć następującego polecenia:

```bash
pip install -r requirements.txt
