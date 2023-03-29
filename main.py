import unittest


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["adam.nowak@wat.edu.pl", False, True, "Adam", "Nowak"],
            ["magdalena.zielinska@student.wat.edu.pl", True, False, "Magdalena", "Zielinska"],
            ["michal.janowski@student.wat.edu.pl", True, True, "Michal", "Janowski"],
            ["dorota.kaminska@wat.edu.pl", False, False, "Dorota", "Kaminska"],
            ["kamil.kruk@wat.edu.pl", False, True, "Kamil", "Kruk"],
            ["maria.zawadzka@wat.edu.pl", False, False, "Maria, "Zawadzka"],
            ["lukasz.wojtas@student.wat.edu.pl", True, True, "Lukasz", "Wojtas"],
            ["katarzyna.wlodarczyk@wat.edu.pl", False, False, "Katarzyna", "Wlodarczyk"],
            ["marek.pawlowski@student.wat.edu.pl", True, True, "Marek", "Pawlowski"],
            ["anna.lewandowska@student.wat.edu.pl", True, False, "Katarzyna", "Babacka"],]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                mail = x[0]
                to
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest(): to
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surntoame, extractor.get_surname())