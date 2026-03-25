from pathlib import Path
import argparse

'''
Takes in main directory path and returns a list of all subdirectories
'''
def get_all_subdirectories(directory_path:str)-> list:
    sub_dirs = []
    main_dir = Path(directory_path)
    for item in main_dir.iterdir():
        if item.is_dir():
            sub_dirs.append(item)
    return sub_dirs

'''
Takes in main directory path and returns list of all files
'''
def get_all_files(directory_path:str)->list:
    files = []
    main_dir = Path(directory_path)
    for item in main_dir.iterdir():
        if item.is_file():
            files.append(item)
    return files

'''
Given a directory path, it addes each line of the tree to a list called "lines"
It then uses recursion to loop through all subdirectories to find all files
Then, all the lines in the "lines" list are joined with \n
'''
def format_tree(directory_path:str, prefix:str = '')-> str:
    # Visual Branch Vars
    tee       :str  = '├── '
    last      :str  = '└── '
    pipe      :str  = '│   '
    empty     :str  = '    '
    lines     :list = []
    sub_dirs  :list = get_all_subdirectories(directory_path)
    files      :list = get_all_files(directory_path)
    all_items :list = files + sub_dirs

    if prefix == '':
        lines.append(Path(directory_path).name)

    for i, item in enumerate(all_items):
        is_last:bool = (i == len(all_items) - 1)
        current_branch:str = last if is_last else tee
        extension:str = empty if is_last else pipe
        lines.append(prefix + current_branch + item.name)
        if item in sub_dirs:
            lines.append(format_tree(item, prefix + extension))

    return '\n'.join(lines)


'''
Takes a tree from the format tree function and writes it to a md file.
'''
def tree_to_markdown(tree:str, output_file:str = "tree.md")-> None:
    message = 'Copy the Snippet above (including backtics) to import to your README!'
    with open(output_file, "w") as file:
        file.write('```\n'+ tree + '\n```')
        file.write('\n'+message)


def main():
    # 1. Initialize the parser
    parser = argparse.ArgumentParser(
        description="Generate a markdown file tree from a directory."
    )
    
    # 2. Define the expected arguments
    parser.add_argument(
        "path", 
        type=str, 
        help="The absolute or relative path to the target directory"
    )
    
    # Optional: Add a flag for the output file name
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="tree.md", 
        help="Name of the output markdown file (default: tree.md)"
    )

    # 3. Parse the command line input
    args = parser.parse_args()

    # 4. Execute your logic using the parsed arguments
    tree = format_tree(args.path)
    tree_to_markdown(tree, args.output)


if __name__ == '__main__':
    main()