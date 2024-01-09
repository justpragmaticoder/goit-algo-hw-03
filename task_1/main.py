from utils import copy_directory, get_directory_path, is_interaction_continued


try:
    while True:
        print("\nLet's start our work on copiyng files :)")
        output_dir = get_directory_path(
            "Output directory (dist folder will be created in case of empty argument)",
            "./dist",
        )
        input_dir = get_directory_path("Directory for copying")

        copy_directory(output_dir, input_dir)

        is_countinued = is_interaction_continued(
            "Copying has been finished. Do you want to continue with another folders? (yes/no)"
        )

        if not is_countinued:
            print("\nThank you for choosing our script. Have a nice day :)")
            break

except KeyboardInterrupt:
    print("\nInterrupted by user.")
except Exception as e:
    print(f"\nNon-expected error occured: ${str(e)}")
