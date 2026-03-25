from pathlib import Path

'Takes in main directory path and returns a list of all subdirectories'
def get_all_subdirectories(directory_path:str)-> list:
    sub_dirs = []
    main_dir = Path(directory_path)
    for item in main_dir.iterdir():
        if item.is_dir():
            sub_dirs.append(item)
    return sub_dirs

'Takes in main directory path and returns list of all files'
def get_all_files(directory_path:str)->list:
    files = []
    main_dir = Path(directory_path)
    for item in main_dir.iterdir():
        if item.is_file():
            files.append(item)
    return files

'Takes a base directory path, and starts with an initial depth of 1.'
'Recures through each subdirctory, using the depth arg for spacing'
'Should try adding visual branches later, so it actually looks like a tree'
def format_tree(directory_path:str, depth:int = 1)-> str:
    lines = []
    indent = '  ' * depth
    sub_dirs = get_all_subdirectories(directory_path)
    files = get_all_files(directory_path)
    lines.append(indent + Path(directory_path).name)
    for file in files:
        lines.append(indent + '  ' + file.name)
    for dir in sub_dirs:
        lines.append(format_tree(dir, depth + 1))

    return '\n'.join(lines)

'Takes a tree from the format tree function and writes it to a md file.'
def tree_to_markdown(tree:str, output_file:str = "tree.md")-> None:
    message = 'Copy the Snippet above (including backtics) to import to your README!'
    with open(output_file, "w") as file:
        file.write('```\n'+ tree + '\n```')
        file.write('\n'+message)


if __name__ == '__main__':
    tree_to_markdown(format_tree(str(input())))