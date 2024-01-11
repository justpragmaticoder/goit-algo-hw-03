from utils import (
    OUTPUT_DEFAULT_DIR,
    copy_directory,
    get_directory_path,
    is_interaction_continued,
    extract_arguments,
)


try:
    args = extract_arguments()
    output_dir = args["output_dir"]
    input_dir = args["input_dir"]

    copy_directory(output_dir, input_dir)

    while True:
        is_repeated = is_interaction_continued(
            "Copying has been finished. Do you want to continue with another folders? (yes/no)"
        )

        if not is_repeated:
            print("\nThank you for choosing our script. Have a nice day :)")
            break

        output_dir = get_directory_path(
            "Output directory (dist folder will be created in case of empty argument)",
            OUTPUT_DEFAULT_DIR,
        )
        input_dir = get_directory_path("Directory for copying")

        copy_directory(output_dir, input_dir)
except KeyboardInterrupt:
    print("\nInterrupted by user.")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"\nNon-expected error occured: ${str(e)}")
