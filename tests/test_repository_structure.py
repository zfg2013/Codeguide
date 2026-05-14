from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TutorialSiteStructureTest(unittest.TestCase):
    def test_required_files_and_directories_exist(self):
        required_paths = [
            "mkdocs.yml",
            "README.md",
            "requirements.txt",
            ".github/workflows/deploy.yml",
            "docs/index.md",
            "docs/tutorials/index.md",
            "docs/notebooks/index.md",
            "notebooks/marimo_example.py",
        ]

        missing = [path for path in required_paths if not (ROOT / path).exists()]
        self.assertEqual(missing, [])

    def test_removed_jupyter_and_colab_assets_are_absent(self):
        removed_paths = [
            "docs/tutorials/example-python-workflow.md",
            "notebooks/example_python_workflow.ipynb",
        ]
        still_present = [path for path in removed_paths if (ROOT / path).exists()]
        self.assertEqual(still_present, [])

        searchable_files = [
            *ROOT.glob("*.md"),
            ROOT / "mkdocs.yml",
            ROOT / ".github" / "workflows" / "deploy.yml",
            *sorted((ROOT / "docs").rglob("*.md")),
        ]
        combined_text = "\n".join(
            path.read_text(encoding="utf-8") for path in searchable_files
        )
        for forbidden in [
            "Colab",
            "colab",
            "colab-badge.svg",
            "example_python_workflow.ipynb",
            "example-python-workflow.md",
            "Example Python Workflow",
            "Jupyter",
            "ipynb",
        ]:
            self.assertNotIn(forbidden, combined_text)

    def test_mkdocs_uses_material_and_expected_sections(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

        self.assertIn("name: material", config)
        for section in [
            "Home",
            "Tutorials",
            "Notebooks",
        ]:
            self.assertRegex(config, rf"\b{re.escape(section)}\b")

    def test_landing_page_links_to_marimo_wasm_notebooks(self):
        index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")

        self.assertIn("grid cards", index)
        self.assertIn("marimo WASM", index)
        self.assertIn("notebooks/marimo-example/", index)

    def test_docs_link_to_marimo_wasm_exports(self):
        marimo_notebooks = sorted((ROOT / "notebooks").glob("*.py"))
        self.assertTrue(marimo_notebooks)

        docs_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [
                ROOT / "docs" / "index.md",
                ROOT / "docs" / "notebooks" / "index.md",
                ROOT / "docs" / "tutorials" / "index.md",
            ]
        )
        for notebook in marimo_notebooks:
            export_name = notebook.stem.replace("_", "-")
            self.assertIn(f"notebooks/{export_name}/", docs_text)

    def test_workflow_deploys_pages_and_exports_marimo_wasm(self):
        workflow = (ROOT / ".github" / "workflows" / "deploy.yml").read_text(
            encoding="utf-8"
        )

        for expected in [
            "for notebook in notebooks/*.py",
            "export_name=$(basename",
            "marimo export html-wasm",
            "--mode run",
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v3",
            "actions/deploy-pages@v4",
        ]:
            self.assertIn(expected, workflow)

    def test_markdown_files_have_titles(self):
        markdown_files = sorted((ROOT / "docs").rglob("*.md"))
        missing_title = [
            str(path.relative_to(ROOT))
            for path in markdown_files
            if not path.read_text(encoding="utf-8").lstrip().startswith("# ")
        ]

        self.assertEqual(missing_title, [])

    def test_docs_tree_contains_only_marimo_site_sources(self):
        allowed_markdown = {
            "docs/index.md",
            "docs/notebooks/index.md",
            "docs/tutorials/index.md",
        }
        markdown_files = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "docs").rglob("*.md")
        }

        self.assertEqual(markdown_files, allowed_markdown)


if __name__ == "__main__":
    unittest.main()
