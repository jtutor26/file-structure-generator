import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import main


def test_main_cli_generates_default_output_file(tmp_path: Path, monkeypatch) -> None:
    (tmp_path / "folder").mkdir()
    (tmp_path / "folder" / "file.txt").write_text("content", encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["generate-tree", str(tmp_path)])

    main.main()

    output_file = tmp_path / "tree.md"
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "```" in content
    assert tmp_path.name in content
    assert "folder" in content
    assert "file.txt" in content


def test_main_cli_generates_custom_output_file(tmp_path: Path, monkeypatch) -> None:
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("print('hello')", encoding="utf-8")

    custom_name = "structure.md"
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate-tree", str(tmp_path), "--output", custom_name],
    )

    main.main()

    output_file = tmp_path / custom_name
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "```" in content
    assert tmp_path.name in content
    assert "src" in content
    assert "main.py" in content
