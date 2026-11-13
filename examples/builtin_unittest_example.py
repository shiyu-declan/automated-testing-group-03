import unittest


def clean_task_name(text: str):
    return text.strip()


class TestCleanTaskName(unittest.TestCase):
    def test_removes_outer_spaces(self):
        self.assertEqual(clean_task_name("  Read notes  "), "Read notes")

    def test_keeps_normal_text(self):
        self.assertEqual(clean_task_name("Read notes"), "Read notes")

    def test_spaces_become_empty_text(self):
        self.assertEqual(clean_task_name("   "), "")


if __name__ == "__main__":
    unittest.main()