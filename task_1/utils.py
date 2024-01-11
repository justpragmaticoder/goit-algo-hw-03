import os
import shutil
import argparse
from pathlib import Path

OUTPUT_DEFAULT_DIR = "./dist"


def is_path_exists(path_str: str):
    return Path(path_str).exists()


def prepare_dir(path: str):
    os.makedirs(path, exist_ok=True)


def get_directory_path(message: str, default_dir=None):
    while True:
        dir_path = input(f"\n${message}: ").strip()

        if len(dir_path) == 0 and default_dir:
            prepare_dir(default_dir)
            return default_dir

        if is_path_exists(dir_path):
            return dir_path

        print(
            "Sorry, but your path is invalid (directory not exist). Please, try again."
        )


def extract_arguments():
    parser = argparse.ArgumentParser(
        description="Copy files from one directory to another."
    )
    parser.add_argument("--input-dir", help="Input directory path", required=True)
    parser.add_argument(
        "--output-dir", help="Output directory path", default=OUTPUT_DEFAULT_DIR
    )

    args = parser.parse_args()

    output_dir = args.output_dir.strip()
    input_dir = args.input_dir.strip()

    if not is_path_exists(input_dir):
        raise ValueError("input-dir path doesn't exist")

    prepare_dir(output_dir)

    return {"output_dir": args.output_dir, "input_dir": args.input_dir}


def is_interaction_continued(message: str):
    allowed_positive_values = ["y", "yes"]
    allowed_negative_values = ["n", "no"]

    while True:
        input_value = input(f"\n${message}: ").strip().lower()

        if input_value in allowed_positive_values:
            return True
        elif input_value in allowed_negative_values:
            return False
        else:
            print("Wrong answer. Plz, choose y/yes or n/no. Thanks.")


def copy_directory(output_dir, input_dir):
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1][1:]
            dir_path = os.path.join(output_dir, file_extension)
            prepare_dir(dir_path)
            shutil.copy(file_path, os.path.join(dir_path, filename))

        if os.path.isdir(file_path):
            try:
                copy_directory(output_dir, file_path)
            except Exception as e:
                print(
                    f"\nNon-expected error occured while trying to copy file ${filename}: ${str(e)}"
                )
