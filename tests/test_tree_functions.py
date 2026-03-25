from pathlib import Path

from main import format_tree, get_all_files, get_all_subdirectories, tree_to_markdown


def test_get_all_subdirectories_returns_only_directories(tmp_path: Path) -> None:
    (tmp_path / "folder_a").mkdir()
    (tmp_path / "folder_b").mkdir()
    (tmp_path / "note.txt").write_text("hello", encoding="utf-8")

    result = get_all_subdirectories(str(tmp_path))

    names = {item.name for item in result}
    assert names == {"folder_a", "folder_b"}
    assert all(item.is_dir() for item in result)


def test_get_all_files_returns_only_files(tmp_path: Path) -> None:
    (tmp_path / "one.txt").write_text("1", encoding="utf-8")
    (tmp_path / "two.md").write_text("2", encoding="utf-8")
    (tmp_path / "nested").mkdir()

    result = get_all_files(str(tmp_path))

    names = {item.name for item in result}
    assert names == {"one.txt", "two.md"}
    assert all(item.is_file() for item in result)


def test_format_tree_contains_root_and_nested_items(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide.md").write_text("guide", encoding="utf-8")
    (tmp_path / "app.py").write_text("print('ok')", encoding="utf-8")

    tree = format_tree(str(tmp_path))

    lines = tree.splitlines()
    assert lines[0] == tmp_path.name
    assert any("app.py" in line for line in lines)
    assert any("docs" in line for line in lines)
    assert any("guide.md" in line for line in lines)
    assert any("├──" in line or "└──" in line for line in lines[1:])


def test_tree_to_markdown_writes_code_fence_and_message(tmp_path: Path) -> None:
    output_file = tmp_path / "tree.md"
    sample_tree = "root\n└── file.txt"

    tree_to_markdown(sample_tree, str(output_file))

    content = output_file.read_text(encoding="utf-8")
    assert content.startswith("```\n")
    assert sample_tree in content
    assert content.endswith(
        "Copy the Snippet above (including backtics) to import to your README!"
    )
