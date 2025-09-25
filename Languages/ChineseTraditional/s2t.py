import os
import opencc

def convert_file(file_path, converter):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        converted = converter.convert(content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(converted)
        print(f"S: {file_path}")
    except Exception as e:
        print(f"F: {file_path}, E: {e}")

def traverse_and_convert(root_dir, config="s2twp.json"):
    converter = opencc.OpenCC(config)
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith((".txt", ".xml")):
                file_path = os.path.join(dirpath, filename)
                convert_file(file_path, converter)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    traverse_and_convert(script_dir, config="s2t.json")
