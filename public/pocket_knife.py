import argparse
import os
import re


def normalize_date(filename):
    date_pattern = r'(\d{2})-(\d{2})-(\d{4})'
    match = re.search(date_pattern, filename)
    if match:
        month, day, year = match.groups()
        return filename.replace(match.group(0), f"{year}-{month}-{day}")
    return None

# ----- main ------- #

def main():
    parser = argparse.ArgumentParser(description="Pocket Knife File Tool")
    subparsers = parser.add_subparsers(dest="command")

    #Date sub-command
    date_parser = subparsers.add_parser("date", help="Normalize date in filenames")
    date_parser.add_argument("file", help="The file to process")
    date_parser.add_argument("-d", "--dry-run", action="store_true", help="Preview changes")

    args = parser.parse_args()

    if args.command == "date":
        if not os.path.exists(args.file):
            print(f"Error: {args.file} not found.")
            return
        
        new_name = normalize_date(args.file)

        if new_name:
            if args.dry_run:
                print(f"[DRY-RUN] Would rename: {args.file} -> {new_name}")
            else:
                os.rename(args.file, new_name)
                print(f"Success: {args.file} -> {new_name}")
        else:
            print(f"Status: No MM-DD-YYYY pattern identified in '{args.file}'.")


if __name__ == "__main__":
    main()
