import os
from PIL import Image
from pyzbar.pyzbar import decode


def decode_qr_from_file(file_path):
    if not os.path.exists(file_path):
        raise ValueError(f"Ошибка: Файл '{file_path}' не найден.")

    try:
        # Открываем изображение
        img = Image.open(file_path)
        # Декодируем QR-код
        decoded_objects = decode(img)

        if not decoded_objects:
            raise ValueError("Ошибка: QR-код на изображении не обнаружен.")

        print("\n=== Результат декодирования ===")
        for obj in decoded_objects:
            text_data = obj.data.decode("utf-8")
            print(f"Полная ссылка: {text_data}")

            # Автоматически ищем и выводим только секретный ключ для KeePassXC
            if "secret=" in text_data:
                # Извлекаем часть после secret= до следующего знака & (если он есть)
                secret_part = text_data.split("secret=")[1].split("&")[0]
                print(f"\nКлюч для KeePassXC: {secret_part}")

    except Exception as e:
        raise ValueError(f"Произошла ошибка при обработке файла: {e}")


if __name__ == "__main__":
    file_path = "qr_code_totp.png"

    decode_qr_from_file(file_path)
