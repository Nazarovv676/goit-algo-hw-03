import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dest_dir):
    """
    Рекурсивно читає файли у вихідній директорії, копіює їх у нову директорію та сортує за розширенням.
    """
    try:
        # Перевірка, чи існує вихідна директорія
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"Вихідна директорія '{src_dir}' не знайдена.")

        # Створення директорії призначення, якщо вона не існує
        os.makedirs(dest_dir, exist_ok=True)

        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1][1:].lower()  # Отримати розширення файлу (без крапки)

                # Якщо у файлу немає розширення, використовуємо "no_extension"
                if not file_extension:
                    file_extension = "no_extension"

                # Шлях до піддиректорії в директорії призначення
                extension_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(extension_dir, exist_ok=True)

                # Копіювання файлу в відповідну піддиректорію
                dest_file_path = os.path.join(extension_dir, file)
                shutil.copy2(file_path, dest_file_path)
                print(f"Скопійовано: {file_path} -> {dest_file_path}")

    except Exception as e:
        print(f"Помилка: {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів і сортування за розширенням.")
    parser.add_argument("src", help="Шлях до вихідної директорії.")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist).")
    args = parser.parse_args()

    # Виклик функції копіювання і сортування
    copy_and_sort_files(args.src, args.dest)

if __name__ == "__main__":
    main()