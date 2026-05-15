from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

TUTORIAL_PAGES = [
    "docs/tutorials/statistical-theory.md",
    "docs/tutorials/sequencing.md",
    "docs/tutorials/machine-learning.md",
    "docs/tutorials/molecular-design-engineering.md",
]

NOTEBOOKS = [
    "notebooks/01_statistical_theory.py",
    "notebooks/02_01_getting_data_from_sequencer.py",
    "notebooks/02_02_sequence_alignment.py",
    "notebooks/02_03_counting_mapped_annotated_reads.py",
    "notebooks/02_04_exploratory_data_analysis.py",
    "notebooks/02_05_differential_analysis.py",
    "notebooks/02_06_enrichment_analysis.py",
    "notebooks/02_07_cross_validation.py",
    "notebooks/03_01_what_is_machine_learning.py",
    "notebooks/03_02_exploratory_data_analysis.py",
    "notebooks/03_03_implementing_ml_tools_and_decisions.py",
    "notebooks/03_04_cross_validating_ml_tools.py",
    "notebooks/03_05_from_ml_to_experimentation.py",
    "notebooks/04_01_techniques_strategies_molecular_design.py",
    "notebooks/04_02_designing_first_molecular_library.py",
    "notebooks/04_03_screening_first_molecular_library.py",
    "notebooks/04_04_further_lead_hit_qc.py",
    "notebooks/04_05_hit_selection_for_experimentation.py",
]


def export_name(notebook_path):
    return Path(notebook_path).stem


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
            *TUTORIAL_PAGES,
            *NOTEBOOKS,
        ]

        missing = [path for path in required_paths if not (ROOT / path).exists()]
        self.assertEqual(missing, [])

    def test_removed_jupyter_colab_and_old_export_paths_are_absent(self):
        removed_paths = [
            "docs/tutorials/example-python-workflow.md",
            "notebooks/example_python_workflow.ipynb",
            "notebooks/marimo_example.py",
            "docs/notebooks/marimo-example",
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
            "notebooks/marimo-example/",
        ]:
            self.assertNotIn(forbidden, combined_text)

    def test_mkdocs_uses_material_and_expected_curriculum_nav(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

        self.assertIn("name: material", config)
        for section in [
            "Home",
            "Tutorials",
            "Notebook Library",
            "Statistical Theory",
            "Sequencing",
            "Machine Learning",
            "Molecular Design Engineering",
        ]:
            self.assertRegex(config, rf"\b{re.escape(section)}\b")

    def test_docs_link_to_html_exports(self):
        root_docs = [
            ROOT / "docs" / "index.md",
            ROOT / "docs" / "notebooks" / "index.md",
        ]
        tutorial_index_docs = [
            ROOT / "docs" / "tutorials" / "index.md",
        ]
        tutorial_module_docs = [
            *(ROOT / page for page in TUTORIAL_PAGES),
        ]

        root_text = "\n".join(path.read_text(encoding="utf-8") for path in root_docs)
        tutorial_index_text = "\n".join(
            path.read_text(encoding="utf-8") for path in tutorial_index_docs
        )
        tutorial_module_text = "\n".join(
            path.read_text(encoding="utf-8") for path in tutorial_module_docs
        )

        for notebook in NOTEBOOKS:
            name = export_name(notebook)
            self.assertIn(f"marimo/{name}.html", root_text)
            self.assertIn(f"../../marimo/{name}.html", tutorial_module_text)

        self.assertIn("../../marimo/<name>.html", tutorial_index_text)

        all_docs = root_text + "\n" + tutorial_index_text + "\n" + tutorial_module_text
        self.assertNotRegex(all_docs, r"\]\([^)]*notebooks/marimo-example/")
        self.assertNotRegex(all_docs, r"\]\([^)]*notebooks/[^)]*\.html")
        self.assertNotRegex(tutorial_module_text, r"\]\(\.\./marimo/[^)]*\.html\)")

    def test_tutorial_pages_have_required_placeholders(self):
        for page in TUTORIAL_PAGES:
            text = (ROOT / page).read_text(encoding="utf-8")
            for heading in [
                "## Learning Goals",
                "## Prerequisites",
                "## Notebooks",
                "## Exercises",
            ]:
                self.assertIn(heading, text)

    def test_notebooks_are_valid_marimo_scaffolds(self):
        for notebook in NOTEBOOKS:
            text = (ROOT / notebook).read_text(encoding="utf-8")
            self.assertIn("import marimo", text)
            self.assertIn("app = marimo.App", text)
            self.assertIn("if __name__ == \"__main__\":", text)
            self.assertIn("mo.md", text)
            self.assertIn("# ", text)
            for section in [
                "Learning goals",
                "Background",
                "Interactive example",
                "Exercise",
                "Notes for future editing",
            ]:
                self.assertIn(section, text)
            self.assertRegex(text, r"sample_values|example_count|example_total")

    def test_workflow_builds_then_exports_all_marimo_notebooks(self):
        workflow = (ROOT / ".github" / "workflows" / "deploy.yml").read_text(
            encoding="utf-8"
        )

        build_index = workflow.index("mkdocs build --strict")
        export_index = workflow.index("marimo export html-wasm")
        self.assertLess(build_index, export_index)

        for expected in [
            "for notebook in notebooks/*.py",
            "site/marimo",
            "marimo export html-wasm",
            "--mode run",
            "${export_name}.html",
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

    def test_docs_tree_contains_only_curriculum_sources(self):
        allowed_markdown = {
            "docs/index.md",
            "docs/notebooks/index.md",
            "docs/tutorials/index.md",
            *TUTORIAL_PAGES,
        }
        markdown_files = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "docs").rglob("*.md")
        }

        self.assertEqual(markdown_files, allowed_markdown)


if __name__ == "__main__":
    unittest.main()
