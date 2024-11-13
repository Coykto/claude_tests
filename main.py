import os
from pathlib import Path

from gitdiff import write_git_diff

skip_folders = [
    '__pycache__',
    '.git',
    '.idea',
    'venv',
    '.pytest_cache',
    'kube',
    'docs',
    '.github',
    'dev-kit',
    'tests',
    '.vscode',
    '.github',
    'pages',
    'conda_recipe',

]
skip_extensions = [
    '.pyc',
    '.pyo',
    '.pyd',
    '.pyi',
    '.lock',
    '.md',
    '.yaml',
    '.txt',
    '.toml',
    '.coveragerc',
    '.gitignore',
    'Dockerfile',
    '__init__.py',
    '.pickle',
    '.csv',
    '.xml',
    '.xlsx',
    '.txt',
    '.tar.gz',
    '.tar',
    '.gz',
    '.zip',
    '.editorconfig',
    '.gitattributes',
    '.gitignore',
    'LICENSE',
    'old.py',
]

only_extensions = [
   '.py',
]


def generate_document(folder_path, output_file: Path):
    with open(output_file.resolve(), 'w', encoding='utf-8') as doc:
        doc.write("# Table of Contents\n\n")
        traverse_folder(folder_path, doc, 0, "")

def traverse_folder(folder_path, doc, level, relative_path):
    items = os.listdir(folder_path)
    folders = [item for item in items if os.path.isdir(os.path.join(folder_path, item)) if item not in skip_folders]
    files = [item for item in items if os.path.isfile(os.path.join(folder_path, item)) if
             not item.endswith(tuple(skip_extensions))]

    if only_extensions:
        files = [file for file in files if file.endswith(tuple(only_extensions))]

    for file in files:
        file_path = os.path.join(folder_path, file)
        relative_file_path = os.path.join(relative_path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                doc.write(f"{'  ' * level}- {relative_file_path}\n")
                doc.write(f"\n## File: {relative_file_path}\n\n")
                doc.write(content)
                doc.write("\n\n")
        except UnicodeDecodeError:
            # Skip files that are not UTF-8 readable
            pass

    for folder in folders:
        subfolder_path = os.path.join(folder_path, folder)
        relative_subfolder_path = os.path.join(relative_path, folder)
        doc.write(f"{'  ' * level}- {relative_subfolder_path}/\n")
        traverse_folder(subfolder_path, doc, level + 1, relative_subfolder_path)


if __name__ == '__main__':
    folder_path = ""
    output_file = Path("./combined_document.md")


    generate_document(folder_path, output_file)
    # write_git_diff(
    #     repo_path=folder_path,
    #     output_file=Path("./gitdiff.txt"),
    #     left_branch="feature/DSDS-853_target-search-improvement"
    # )
