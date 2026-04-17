"""
Лабораторна робота №2 — Unit Tests
Проект: Туристичний помічник (Tourist Helper)
Тести для класів: PhraseTranslator, CountryGuide, TravelChecklist
"""

import unittest
from unittest.mock import MagicMock, patch


# ──────────────────────────────────────────────
# Копії бізнес-класів (без tkinter-залежностей)
# ──────────────────────────────────────────────

class PhraseTranslator:
    def __init__(self):
        self.languages = {
            'Англійська': 'en', 'Французька': 'fr', 'Німецька': 'de',
            'Іспанська': 'es', 'Італійська': 'it', 'Польська': 'pl',
            'Чеська': 'cs', 'Турецька': 'tr', 'Японська': 'ja', 'Китайська': 'zh'
        }
        self.phrases = {
            'Привіт': {
                'en': 'Hello', 'fr': 'Bonjour', 'de': 'Hallo', 'es': 'Hola',
                'it': 'Ciao', 'pl': 'Cześć', 'cs': 'Ahoj', 'tr': 'Merhaba',
                'ja': 'こんにちは', 'zh': '你好'
            },
            'Дякую': {
                'en': 'Thank you', 'fr': 'Merci', 'de': 'Danke', 'es': 'Gracias',
                'it': 'Grazie', 'pl': 'Dziękuję', 'cs': 'Děkuji',
                'tr': 'Teşekkürler', 'ja': 'ありがとう', 'zh': '谢谢'
            },
            'Скільки це коштує?': {
                'en': 'How much does it cost?', 'fr': 'Combien ça coûte?',
                'de': 'Wie viel kostet das?', 'es': '¿Cuánto cuesta?',
                'it': 'Quanto costa?', 'pl': 'Ile to kosztuje?',
                'cs': 'Kolik to stojí?', 'tr': 'Bu ne kadar?',
                'ja': 'いくらですか？', 'zh': '这个多少钱？'
            },
            'До побачення': {
                'en': 'Goodbye', 'fr': 'Au revoir', 'de': 'Auf Wiedersehen',
                'es': 'Adiós', 'it': 'Arrivederci', 'pl': 'Do widzenia',
                'cs': 'Na shledanou', 'tr': 'Güle güle', 'ja': 'さようなら', 'zh': '再见'
            },
            'Вибачте': {
                'en': 'Excuse me', 'fr': 'Excusez-moi', 'de': 'Entschuldigung',
                'es': 'Disculpe', 'it': 'Scusi', 'pl': 'Przepraszam',
                'cs': 'Promiňte', 'tr': 'Affedersiniz', 'ja': 'すみません', 'zh': '对不起'
            },
        }

    def get_translation(self, phrase, language):
        lang_code = self.languages.get(language)
        if lang_code and phrase in self.phrases:
            return self.phrases[phrase].get(lang_code, "Переклад не знайдено")
        return "Переклад не знайдено"


class CountryGuide:
    def __init__(self):
        self.countries = {
            'Туреччина': {
                'capital': 'Анкара', 'currency': 'Турецька ліра (TRY)',
                'language': 'Турецька', 'emergency': '112',
                'voltage': '230V', 'timezone': 'UTC+3',
                'culture': ['🕌 Поважайте релігійні традиції'],
                'attractions': ['🏛️ Собор Святої Софії (Стамбул)'],
                'food': ['Кебаб', 'Долма', 'Баклава']
            },
            'Польща': {
                'capital': 'Варшава', 'currency': 'Злотий (PLN)',
                'language': 'Польська', 'emergency': '112',
                'voltage': '230V', 'timezone': 'UTC+1',
                'culture': ['🎭 Багата історична спадщина'],
                'attractions': ['🏰 Вавельський замок (Краків)'],
                'food': ["П'єроги", 'Бігос']
            },
            'Японія': {
                'capital': 'Токіо', 'currency': 'Єна (JPY)',
                'language': 'Японська', 'emergency': '110',
                'voltage': '100V', 'timezone': 'UTC+9',
                'culture': ['🎌 Глибока повага до традицій'],
                'attractions': ['⛩️ Храм Фушімі Інарі'],
                'food': ['Суші', 'Рамен']
            },
        }

    def get_country_info(self, country_name):
        return self.countries.get(country_name, None)

    def get_countries_list(self):
        return list(self.countries.keys())


class TravelChecklist:
    def __init__(self):
        self.items = {
            'Документи': ['Паспорт', 'Віза', 'Страховка', 'Квитки', 'Бронь готелю'],
            'Одяг':      ['Нижня білизна', 'Сорочки/футболки', 'Штани/спідниці', 'Куртка', 'Взуття'],
            'Гігієна':   ['Зубна щітка', 'Зубна паста', 'Шампунь', 'Мило', 'Дезодорант'],
            'Техніка':   ['Телефон', 'Зарядка', 'Камера', 'Навушники', 'Перехідник'],
            'Медицина':  ['Ліки особисті', 'Пластир', 'Знеболююче', 'Від алергії', 'Термометр'],
            'Інше':      ['Гроші', 'Кредитні карти', 'Сонцезахисний крем', 'Окуляри', 'Рюкзак'],
        }
        self.checked_items = set()

    def get_progress(self):
        total_items = sum(len(v) for v in self.items.values())
        checked_count = len(self.checked_items)
        return int((checked_count / total_items) * 100) if total_items > 0 else 0

    def toggle_item(self, category, item):
        key = f"{category}:{item}"
        if key in self.checked_items:
            self.checked_items.remove(key)
            return False
        else:
            self.checked_items.add(key)
            return True

    def is_checked(self, category, item):
        return f"{category}:{item}" in self.checked_items


# ══════════════════════════════════════════════════════════════
#  1. ТЕСТИ ДЛЯ PhraseTranslator
# ══════════════════════════════════════════════════════════════

class TestPhraseTranslator(unittest.TestCase):

    def setUp(self):
        """Крок налаштування: створення об'єкта перед кожним тестом (Test Fixture)."""
        self.translator = PhraseTranslator()

    # --- Позитивні сценарії ---

    def test_translate_hello_to_english(self):
        """Тест 1: Коректний переклад 'Привіт' → англійська."""
        result = self.translator.get_translation('Привіт', 'Англійська')
        self.assertEqual(result, 'Hello')

    def test_translate_thank_you_to_french(self):
        """Тест 2: Коректний переклад 'Дякую' → французька."""
        result = self.translator.get_translation('Дякую', 'Французька')
        self.assertEqual(result, 'Merci')

    def test_translate_price_to_japanese(self):
        """Тест 3: Переклад фрази про ціну на японську."""
        result = self.translator.get_translation('Скільки це коштує?', 'Японська')
        self.assertEqual(result, 'いくらですか？')

    def test_translate_goodbye_to_german(self):
        """Тест 4: Переклад 'До побачення' → німецька."""
        result = self.translator.get_translation('До побачення', 'Німецька')
        self.assertEqual(result, 'Auf Wiedersehen')

    def test_translate_excuse_me_to_chinese(self):
        """Тест 5: Переклад 'Вибачте' → китайська."""
        result = self.translator.get_translation('Вибачте', 'Китайська')
        self.assertEqual(result, '对不起')

    # --- Негативні сценарії (граничні умови) ---

    def test_unknown_phrase_returns_not_found(self):
        """Тест 6: Невідома фраза повертає повідомлення про відсутність перекладу."""
        result = self.translator.get_translation('Неіснуюча фраза', 'Англійська')
        self.assertEqual(result, 'Переклад не знайдено')

    def test_unknown_language_returns_not_found(self):
        """Тест 7: Невідома мова повертає повідомлення про відсутність перекладу."""
        result = self.translator.get_translation('Привіт', 'Клінгонська')
        self.assertEqual(result, 'Переклад не знайдено')

    def test_languages_count(self):
        """Тест 8: Словник містить рівно 10 мов."""
        self.assertEqual(len(self.translator.languages), 10)

    def test_all_phrases_have_english_translation(self):
        """Тест 9: Кожна фраза має переклад на англійську (перевірка повноти даних)."""
        for phrase in self.translator.phrases:
            with self.subTest(phrase=phrase):
                result = self.translator.get_translation(phrase, 'Англійська')
                self.assertNotEqual(result, 'Переклад не знайдено')

    def test_translation_is_string(self):
        """Тест 10: Результат перекладу завжди є рядком."""
        result = self.translator.get_translation('Привіт', 'Іспанська')
        self.assertIsInstance(result, str)

    # --- Mock-тест ---

    def test_get_translation_uses_languages_dict(self):
        """Тест 11 (Mock): Метод звертається до словника мов (перевірка поведінки)."""
        mock_languages = MagicMock()
        mock_languages.get = MagicMock(return_value='en')
        self.translator.languages = mock_languages

        self.translator.get_translation('Привіт', 'Англійська')

        mock_languages.get.assert_called_once_with('Англійська')


# ══════════════════════════════════════════════════════════════
#  2. ТЕСТИ ДЛЯ CountryGuide
# ══════════════════════════════════════════════════════════════

class TestCountryGuide(unittest.TestCase):

    def setUp(self):
        self.guide = CountryGuide()

    def test_get_existing_country(self):
        """Тест 12: Метод повертає словник для існуючої країни."""
        result = self.guide.get_country_info('Туреччина')
        self.assertIsNotNone(result)

    def test_country_has_required_fields(self):
        """Тест 13: Інформація про країну містить всі обов'язкові поля."""
        country = self.guide.get_country_info('Польща')
        required_fields = ['capital', 'currency', 'language', 'emergency', 'voltage', 'timezone']
        for field in required_fields:
            with self.subTest(field=field):
                self.assertIn(field, country)

    def test_get_nonexistent_country_returns_none(self):
        """Тест 14: Запит неіснуючої країни повертає None."""
        result = self.guide.get_country_info('Марс')
        self.assertIsNone(result)

    def test_get_countries_list_returns_list(self):
        """Тест 15: Метод get_countries_list повертає список."""
        result = self.guide.get_countries_list()
        self.assertIsInstance(result, list)

    def test_countries_list_not_empty(self):
        """Тест 16: Список країн не порожній."""
        result = self.guide.get_countries_list()
        self.assertGreater(len(result), 0)

    def test_turkey_capital_is_ankara(self):
        """Тест 17: Столиця Туреччини — Анкара."""
        country = self.guide.get_country_info('Туреччина')
        self.assertEqual(country['capital'], 'Анкара')

    def test_food_is_list(self):
        """Тест 18: Поле 'food' є списком."""
        country = self.guide.get_country_info('Японія')
        self.assertIsInstance(country['food'], list)

    def test_all_countries_have_emergency(self):
        """Тест 19: Кожна країна має номер екстреної служби."""
        for name in self.guide.get_countries_list():
            country = self.guide.get_country_info(name)
            with self.subTest(country=name):
                self.assertIn('emergency', country)
                self.assertTrue(len(country['emergency']) > 0)


# ══════════════════════════════════════════════════════════════
#  3. ТЕСТИ ДЛЯ TravelChecklist
# ══════════════════════════════════════════════════════════════

class TestTravelChecklist(unittest.TestCase):

    def setUp(self):
        self.checklist = TravelChecklist()

    def test_initial_progress_is_zero(self):
        """Тест 20: На початку прогрес пакування = 0%."""
        self.assertEqual(self.checklist.get_progress(), 0)

    def test_toggle_item_adds_to_checked(self):
        """Тест 21: toggle_item позначає предмет та повертає True."""
        result = self.checklist.toggle_item('Документи', 'Паспорт')
        self.assertTrue(result)
        self.assertTrue(self.checklist.is_checked('Документи', 'Паспорт'))

    def test_toggle_item_twice_unchecks(self):
        """Тест 22: Подвійне натискання знімає позначку та повертає False."""
        self.checklist.toggle_item('Документи', 'Паспорт')
        result = self.checklist.toggle_item('Документи', 'Паспорт')
        self.assertFalse(result)
        self.assertFalse(self.checklist.is_checked('Документи', 'Паспорт'))

    def test_progress_increases_after_check(self):
        """Тест 23: Прогрес зростає після позначки предмета."""
        self.checklist.toggle_item('Документи', 'Паспорт')
        progress = self.checklist.get_progress()
        self.assertGreater(progress, 0)

    def test_full_checklist_is_100_percent(self):
        """Тест 24: Якщо позначено всі предмети — прогрес 100%."""
        for category, items in self.checklist.items.items():
            for item in items:
                self.checklist.checked_items.add(f"{category}:{item}")
        self.assertEqual(self.checklist.get_progress(), 100)

    def test_is_checked_returns_false_for_unchecked(self):
        """Тест 25: is_checked повертає False для непозначеного предмета."""
        self.assertFalse(self.checklist.is_checked('Одяг', 'Куртка'))

    def test_items_contain_all_categories(self):
        """Тест 26: Список містить всі 6 категорій."""
        expected = {'Документи', 'Одяг', 'Гігієна', 'Техніка', 'Медицина', 'Інше'}
        self.assertEqual(set(self.checklist.items.keys()), expected)

    def test_clear_checked_items(self):
        """Тест 27: Очищення checked_items скидає прогрес до 0."""
        self.checklist.toggle_item('Документи', 'Паспорт')
        self.checklist.toggle_item('Одяг', 'Куртка')
        self.checklist.checked_items.clear()
        self.assertEqual(self.checklist.get_progress(), 0)

    def test_item_key_format(self):
        """Тест 28: Ключ предмета у форматі 'Категорія:Предмет'."""
        self.checklist.toggle_item('Медицина', 'Пластир')
        self.assertIn('Медицина:Пластир', self.checklist.checked_items)

    # --- Stub-тест (заглушка) ---

    def test_get_progress_with_stub_items(self):
        """Тест 29 (Stub): Підміна items для перевірки логіки get_progress."""
        # Stub: замінюємо реальні дані спрощеними
        self.checklist.items = {'Тест': ['А', 'Б']}  # 2 предмети
        self.checklist.checked_items = {'Тест:А'}     # 1 з 2 позначено
        self.assertEqual(self.checklist.get_progress(), 50)



# ══════════════════════════════════════════════════════════════
#  4. "ЗЛАМАНИЙ" ТЕСТ (Крок 5 лабораторної — навмисна помилка)
# ══════════════════════════════════════════════════════════════

class TestBrokenOnPurpose(unittest.TestCase):
    """
    КРОК 5: Навмисно зламаний тест для демонстрації роботи системи тестування.
    Щоб продемонструвати FAIL — розкоментуйте метод нижче.
    Щоб всі тести були зеленими — залиште закоментованим.
    """

    def test_broken_translation(self):
        """Навмисна помилка: очікуємо неправильний переклад."""
        translator = PhraseTranslator()
        result = translator.get_translation('Привіт', 'Англійська')
       # НАВМИСНА ПОМИЛКА: 'Hello' != 'Bye'
        self.assertEqual(result, 'Bye')   # AssertionError: 'Hello' != 'Bye'

    #def test_placeholder_for_broken_demo(self):
        #"""Заглушка — знімається коментар вище для демонстрації FAIL."""
        #self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)