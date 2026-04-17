
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font

class PhraseTranslator:
    """Клас для перекладу туристичних фраз на різні мови"""
    
    def __init__(self):
        self.languages = {
            'Англійська': 'en',
            'Французька': 'fr', 
            'Німецька': 'de',
            'Іспанська': 'es',
            'Італійська': 'it',
            'Польська': 'pl',
            'Чеська': 'cs',
            'Турецька': 'tr',
            'Японська': 'ja',
            'Китайська': 'zh'
        }
        
        self.phrases = {
            'Привіт': {
                'en': 'Hello',
                'fr': 'Bonjour',
                'de': 'Hallo',
                'es': 'Hola',
                'it': 'Ciao',
                'pl': 'Cześć',
                'cs': 'Ahoj',
                'tr': 'Merhaba',
                'ja': 'こんにちは',
                'zh': '你好'
            },
            'Дякую': {
                'en': 'Thank you',
                'fr': 'Merci',
                'de': 'Danke',
                'es': 'Gracias',
                'it': 'Grazie',
                'pl': 'Dziękuję',
                'cs': 'Děkuji',
                'tr': 'Teşekkürler',
                'ja': 'ありがとう',
                'zh': '谢谢'
            },
            'Скільки це коштує?': {
                'en': 'How much does it cost?',
                'fr': 'Combien ça coûte?',
                'de': 'Wie viel kostet das?',
                'es': '¿Cuánto cuesta?',
                'it': 'Quanto costa?',
                'pl': 'Ile to kosztuje?',
                'cs': 'Kolik to stojí?',
                'tr': 'Bu ne kadar?',
                'ja': 'いくらですか？',
                'zh': '这个多少钱？'
            },
            'Де знаходиться туалет?': {
                'en': 'Where is the bathroom?',
                'fr': 'Où sont les toilettes?',
                'de': 'Wo ist die Toilette?',
                'es': '¿Dónde está el baño?',
                'it': 'Dove si trova il bagno?',
                'pl': 'Gdzie jest toaleta?',
                'cs': 'Kde je toaleta?',
                'tr': 'Tuvalet nerede?',
                'ja': 'トイレはどこですか？',
                'zh': '厕所在哪里？'
            },
            'Я не розумію': {
                'en': 'I don\'t understand',
                'fr': 'Je ne comprends pas',
                'de': 'Ich verstehe nicht',
                'es': 'No entiendo',
                'it': 'Non capisco',
                'pl': 'Nie rozumiem',
                'cs': 'Nerozumím',
                'tr': 'Anlamıyorum',
                'ja': 'わかりません',
                'zh': '我不明白'
            },
            'Допоможіть мені, будь ласка': {
                'en': 'Please help me',
                'fr': 'Aidez-moi s\'il vous plaît',
                'de': 'Bitte helfen Sie mir',
                'es': 'Ayúdeme por favor',
                'it': 'Aiutami per favore',
                'pl': 'Proszę mi pomóc',
                'cs': 'Pomožte mi prosím',
                'tr': 'Lütfen bana yardım edin',
                'ja': '助けてください',
                'zh': '请帮助我'
            },
            'Де готель?': {
                'en': 'Where is the hotel?',
                'fr': 'Où est l\'hôtel?',
                'de': 'Wo ist das Hotel?',
                'es': '¿Dónde está el hotel?',
                'it': 'Dove si trova l\'hotel?',
                'pl': 'Gdzie jest hotel?',
                'cs': 'Kde je hotel?',
                'tr': 'Otel nerede?',
                'ja': 'ホテルはどこですか？',
                'zh': '酒店在哪里？'
            },
            'Рахунок, будь ласка': {
                'en': 'Check, please',
                'fr': 'L\'addition s\'il vous plaît',
                'de': 'Die Rechnung bitte',
                'es': 'La cuenta por favor',
                'it': 'Il conto per favore',
                'pl': 'Rachunek proszę',
                'cs': 'Účet prosím',
                'tr': 'Hesap lütfen',
                'ja': 'お会計をお願いします',
                'zh': '请结账'
            },
            'Вибачте': {
                'en': 'Excuse me',
                'fr': 'Excusez-moi',
                'de': 'Entschuldigung',
                'es': 'Disculpe',
                'it': 'Scusi',
                'pl': 'Przepraszam',
                'cs': 'Promiňte',
                'tr': 'Affedersiniz',
                'ja': 'すみません',
                'zh': '对不起'
            },
            'До побачення': {
                'en': 'Goodbye',
                'fr': 'Au revoir',
                'de': 'Auf Wiedersehen',
                'es': 'Adiós',
                'it': 'Arrivederci',
                'pl': 'Do widzenia',
                'cs': 'Na shledanou',
                'tr': 'Güle güle',
                'ja': 'さようなら',
                'zh': '再见'
            }
        }
    
    def get_translation(self, phrase, language):
        """Повертає переклад обраної фрази на вказану мову"""
        lang_code = self.languages.get(language)
        if lang_code and phrase in self.phrases:
            return self.phrases[phrase].get(lang_code, "Переклад не знайдено")
        return "Переклад не знайдено"

class CountryGuide:
    """Клас для управління інформацією про країни"""
    
    def __init__(self):
        self.countries = {
            'Туреччина': {
                'capital': 'Анкара',
                'currency': 'Турецька ліра (TRY)',
                'language': 'Турецька',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+3',
                'culture': [
                    '🕌 Поважайте релігійні традиції',
                    '👕 Скромний одяг у мечетях та релігійних місцях',
                    '🤝 Рукостискання - звичайне привітання',
                    '🍽️ Чайні традиції дуже важливі',
                    '💰 Торгуйтеся на базарах'
                ],
                'attractions': [
                    '🏛️ Собор Святої Софії (Стамбул)',
                    '🌊 Памуккале',
                    '🏰 Каппадокія',
                    '🏖️ Анталія',
                    '🏺 Ефес'
                ],
                'food': ['Кебаб', 'Долма', 'Баклава', 'Турецька кава', 'Лукум']
            },
            'Польща': {
                'capital': 'Варшава',
                'currency': 'Злотий (PLN)',
                'language': 'Польська',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+1',
                'culture': [
                    '🎭 Багата історична спадщина',
                    '🍺 Культура пива та горілки',
                    '🤝 Формальне спілкування до знайомства',
                    '🌹 Дарування квітів жінкам',
                    '⛪ Католицизм грає важливу роль'
                ],
                'attractions': [
                    '🏰 Вавельський замок (Краків)',
                    '🏛️ Старе місто Варшави',
                    '⛪ Вроцлавські гноми',
                    '🏔️ Закопане та Татри',
                    '🧂 Соляні копальні Величка'
                ],
                'food': ['П\'єроги', 'Бігос', 'Котлет шабовий', 'Журек', 'Мазурек']
            },
            'Німеччина': {
                'capital': 'Берлін',
                'currency': 'Євро (EUR)',
                'language': 'Німецька',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+1',
                'culture': [
                    '⏰ Пунктуальність дуже важлива',
                    '🤝 Міцне рукостискання при знайомстві',
                    '🍺 Культура пивних садів',
                    '♻️ Сортування сміття обов\'язкове',
                    '🚫 Тиша у недільні дні'
                ],
                'attractions': [
                    '🏰 Замок Нойшванштайн',
                    '🚪 Бранденбурзькі ворота',
                    '🍺 Октоберфест (Мюнхен)',
                    '🏛️ Кельнський собор',
                    '🌉 Гейдельберг'
                ],
                'food': ['Шніцель', 'Братвурст', 'Квашена капуста', 'Претцель', 'Штрудель']
            },
            'Італія': {
                'capital': 'Рим',
                'currency': 'Євро (EUR)',
                'language': 'Італійська',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+1',
                'culture': [
                    '🍝 Їжа - це мистецтво та ритуал',
                    '👨‍👩‍👧‍👦 Сім\'я дуже важлива',
                    '🤌 Активна жестикуляція при розмові',
                    '☕ Еспресо п\'ють стоячи біля бару',
                    '💒 Скромний одяг у церквах'
                ],
                'attractions': [
                    '🏛️ Колізей (Рим)',
                    '🎭 Венеція та гондоли',
                    '🌋 Везувій та Помпеї',
                    '🍝 Флоренція - колиска Ренесансу',
                    '🏖️ Амальфітанське узбережжя'
                ],
                'food': ['Піца', 'Паста', 'Ризотто', 'Джелато', 'Тірамісу']
            },
            'Франція': {
                'capital': 'Париж',
                'currency': 'Євро (EUR)',
                'language': 'Французька',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+1',
                'culture': [
                    '🥖 Культура хліба та випічки',
                    '🍷 Винні традиції',
                    '🤝 "Bonjour" обов\'язкове при входженні',
                    '👗 Елегантність у одязі цінується',
                    '🚭 Куріння обмежене у громадських місцях'
                ],
                'attractions': [
                    '🗼 Ейфелева вежа (Париж)',
                    '🖼️ Лувр',
                    '⛪ Собор Паризької Богоматері',
                    '🏰 Версаль',
                    '🍷 Долина Луари'
                ],
                'food': ['Круасан', 'Фуа-гра', 'Еклер', 'Коq-о-вен', 'Рататуй']
            },
            'Іспанія': {
                'capital': 'Мадрид',
                'currency': 'Євро (EUR)',
                'language': 'Іспанська',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+1',
                'culture': [
                    '🌙 Сієста - традиційний денний відпочинок',
                    '🕘 Пізні вечері (після 21:00)',
                    '💃 Фламенко - частина культури',
                    '🏃 Життя не поспішає',
                    '👨‍👩‍👧‍👦 Сімейні цінності важливі'
                ],
                'attractions': [
                    '🏛️ Саграда Фамілія (Барселона)',
                    '🏰 Альгамбра (Гранада)',
                    '🖼️ Прадо (Мадрид)',
                    '🏖️ Ібіца та Майорка',
                    '🚶 Камінo де Сантьяго'
                ],
                'food': ['Паелья', 'Тапас', 'Хамон', 'Гаспачо', 'Чуррос']
            },
            'Греція': {
                'capital': 'Афіни',
                'currency': 'Євро (EUR)',
                'language': 'Грецька',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+2',
                'culture': [
                    '🏛️ Повага до античної історії',
                    '☕ Кава та філософські бесіди',
                    '🧿 Талісман від "поганого ока"',
                    '🎉 Великі сімейні свята',
                    '⛪ Православна традиція'
                ],
                'attractions': [
                    '🏛️ Акрополь (Афіни)',
                    '🏝️ Санторіні',
                    '⛰️ Метеори',
                    '🏖️ Міконос',
                    '🏺 Дельфи'
                ],
                'food': ['Мусака', 'Сувлакі', 'Фета', 'Цацікі', 'Баклава']
            },
            'Чехія': {
                'capital': 'Прага',
                'currency': 'Чеська крона (CZK)',
                'language': 'Чеська',
                'emergency': '112',
                'voltage': '230V',
                'timezone': 'UTC+1',
                'culture': [
                    '🍺 Найбільше споживання пива на душу',
                    '🏰 Збереження історичної архітектури',
                    '🤝 Стриманість у спілкуванні',
                    '🎼 Багата музична традиція',
                    '👞 Зняття взуття вдома'
                ],
                'attractions': [
                    '🏰 Празький град',
                    '🌉 Карлів міст',
                    '⏰ Астрономічний годинник',
                    '🏘️ Чеський Крумлов',
                    '🍺 Пльзень - батьківщина пільзнера'
                ],
                'food': ['Гуляш', 'Кнедлі', 'Шніцель', 'Трдло', 'Пиво Пільзнер']
            }
        }
    
    def get_country_info(self, country_name):
        """Повертає інформацію про обрану країну"""
        return self.countries.get(country_name, None)
    
    def get_countries_list(self):
        """Повертає список доступних країн"""
        return list(self.countries.keys())

class TravelChecklist:
    """Клас для управління списком речей для подорожі"""
    
    def __init__(self):
        self.items = {
            'Документи': ['Паспорт', 'Віза', 'Страховка', 'Квитки', 'Бронь готелю'],
            'Одяг': ['Нижня білизна', 'Сорочки/футболки', 'Штани/спідниці', 'Куртка', 'Взуття'],
            'Гігієна': ['Зубна щітка', 'Зубна паста', 'Шампунь', 'Мило', 'Дезодорант'],
            'Техніка': ['Телефон', 'Зарядка', 'Камера', 'Навушники', 'Перехідник'],
            'Медицина': ['Ліки особисті', 'Пластир', 'Знеболююче', 'Від алергії', 'Термометр'],
            'Інше': ['Гроші', 'Кредитні карти', 'Сонцезахисний крем', 'Окуляри', 'Рюкзак']
        }
        self.checked_items = set()
    
    def get_progress(self):
        """Обчислює прогрес упакування у відсотках"""
        total_items = sum(len(items) for items in self.items.values())
        checked_count = len(self.checked_items)
        return int((checked_count / total_items) * 100) if total_items > 0 else 0
    
    def toggle_item(self, category, item):
        """Змінює стан позначки предмета у списку"""
        item_key = f"{category}:{item}"
        if item_key in self.checked_items:
            self.checked_items.remove(item_key)
            return False
        else:
            self.checked_items.add(item_key)
            return True
    
    def is_checked(self, category, item):
        """Перевіряє, чи позначений предмет у списку"""
        return f"{category}:{item}" in self.checked_items

class TouristHelper:
    """Головний клас програми туристичного помічника"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌍 Туристичний помічник")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f8ff')
        
        # Ініціалізація компонентів програми
        self.translator = PhraseTranslator()
        self.checklist = TravelChecklist()
        self.country_guide = CountryGuide()
        
        # Налаштування шрифтів для інтерфейсу
        self.title_font = font.Font(family="Arial", size=16, weight="bold")
        self.normal_font = font.Font(family="Arial", size=11)
        self.big_font = font.Font(family="Arial", size=14)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Налаштовує графічний інтерфейс програми"""
        # Заголовок програми
        title_label = tk.Label(
            self.root,
            text="🌍 Туристичний помічник",
            font=self.title_font,
            bg='#f0f8ff',
            fg='#2c3e50'
        )
        title_label.pack(pady=10)
        
        # Створення вкладок для різних функцій
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Ініціалізація вкладки перекладача
        self.create_translator_tab()
        
        # Ініціалізація вкладки чек-листа
        self.create_checklist_tab()
        
        # Ініціалізація вкладки путівника
        self.create_guide_tab()
    
    def create_translator_tab(self):
        """Створює вкладку для перекладу фраз"""
        translator_frame = ttk.Frame(self.notebook)
        self.notebook.add(translator_frame, text="🗣️ Перекладач фраз")
        
        # Заголовок вкладки
        tk.Label(
            translator_frame,
            text="Оберіть фразу та мову для перекладу",
            font=self.big_font,
            fg='#34495e'
        ).pack(pady=10)
        
        # Панель для вибору фрази та мови
        selection_frame = tk.Frame(translator_frame, bg='white')
        selection_frame.pack(pady=10, padx=20, fill='x')
        
        # Поле для вибору фрази
        tk.Label(selection_frame, text="Фраза:", font=self.normal_font, bg='white').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.phrase_var = tk.StringVar()
        phrase_combo = ttk.Combobox(
            selection_frame,
            textvariable=self.phrase_var,
            values=list(self.translator.phrases.keys()),
            width=40,
            state='readonly'
        )
        phrase_combo.grid(row=0, column=1, padx=5, pady=5)
        phrase_combo.set(list(self.translator.phrases.keys())[0])
        
        # Поле для вибору мови
        tk.Label(selection_frame, text="Мова:", font=self.normal_font, bg='white').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.language_var = tk.StringVar()
        language_combo = ttk.Combobox(
            selection_frame,
            textvariable=self.language_var,
            values=list(self.translator.languages.keys()),
            width=40,
            state='readonly'
        )
        language_combo.grid(row=1, column=1, padx=5, pady=5)
        language_combo.set(list(self.translator.languages.keys())[0])
        
        # Кнопка для виконання перекладу
        translate_btn = tk.Button(
            selection_frame,
            text="🔄 Перекласти",
            command=self.translate_phrase,
            bg='#3498db',
            fg='white',
            font=self.normal_font,
            padx=20,
            pady=5
        )
        translate_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Поле для відображення результату перекладу
        self.translation_result = tk.Text(
            translator_frame,
            height=8,
            width=70,
            font=('Arial', 14),
            bg='#ecf0f1',
            fg='#2c3e50',
            wrap='word',
            padx=10,
            pady=10
        )
        self.translation_result.pack(pady=20, padx=20)
        self.translation_result.config(state='disabled')
    
    def create_checklist_tab(self):
        """Створює вкладку для управління чек-листом подорожі"""
        checklist_frame = ttk.Frame(self.notebook)
        self.notebook.add(checklist_frame, text="✅ Чек-лист")
        
        # Заголовок та індикатор прогресу
        header_frame = tk.Frame(checklist_frame)
        header_frame.pack(fill='x', pady=10)
        
        tk.Label(
            header_frame,
            text="Чек-лист для подорожі",
            font=self.big_font,
            fg='#34495e'
        ).pack()
        
        # Показник прогресу
        self.progress_var = tk.StringVar()
        self.progress_label = tk.Label(
            header_frame,
            textvariable=self.progress_var,
            font=self.normal_font,
            fg='#27ae60'
        )
        self.progress_label.pack(pady=5)
        
        self.progress_bar = ttk.Progressbar(
            header_frame,
            length=400,
            mode='determinate'
        )
        self.progress_bar.pack(pady=5)
        
        # Область зі скролінгом для елементів чек-листа
        canvas = tk.Canvas(checklist_frame)
        scrollbar = ttk.Scrollbar(checklist_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Створення позначок для кожної категорії
        self.checkboxes = {}
        for category, items in self.checklist.items.items():
            # Назва категорії
            category_label = tk.Label(
                scrollable_frame,
                text=f"📋 {category}",
                font=self.big_font,
                fg='#2c3e50',
                bg='#ecf0f1',
                pady=8
            )
            category_label.pack(fill='x', padx=10, pady=(15, 0))
            
            # Панель для елементів категорії
            category_frame = tk.Frame(scrollable_frame, bg='#ecf0f1')
            category_frame.pack(fill='x', padx=10, pady=(0, 10))
            
            self.checkboxes[category] = {}
            for item in items:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(
                    category_frame,
                    text=item,
                    variable=var,
                    font=self.normal_font,
                    bg='#ecf0f1',
                    activebackground='#d5dbdb',
                    selectcolor='white',
                    command=lambda c=category, i=item, v=var: self.on_checkbox_change(c, i, v)
                )
                checkbox.pack(anchor='w', padx=15, pady=3)
                self.checkboxes[category][item] = var
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Кнопка для скидання чек-листа
        reset_btn = tk.Button(
            checklist_frame,
            text="🔄 Скинути все",
            command=self.reset_checklist,
            bg='#e74c3c',
            fg='white',
            font=self.normal_font,
            padx=20,
            pady=5
        )
        reset_btn.pack(pady=10)
        
        # Оновлення показника прогресу
        self.update_progress()
    
    def translate_phrase(self):
        """Виконує переклад обраної фрази на вибрану мову"""
        phrase = self.phrase_var.get()
        language = self.language_var.get()
        
        translation = self.translator.get_translation(phrase, language)
        
        self.translation_result.config(state='normal')
        self.translation_result.delete(1.0, tk.END)
        
        result_text = f"🇺🇦 Українською: {phrase}\n\n"
        result_text += f"🌍 {language}: {translation}\n\n"
        result_text += "💡 Порада: Збережіть цю фразу або зробіть скріншот!"
        
        self.translation_result.insert(1.0, result_text)
        self.translation_result.config(state='disabled')
    
    def on_checkbox_change(self, category, item, var):
        """Обробляє зміну стану позначки в чек-листі"""
        is_checked = var.get()
        if is_checked:
            self.checklist.checked_items.add(f"{category}:{item}")
        else:
            self.checklist.checked_items.discard(f"{category}:{item}")
        
        self.update_progress()
    
    def update_progress(self):
        """Оновлює прогрес-бар та текстовий показник прогресу"""
        progress = self.checklist.get_progress()
        self.progress_bar['value'] = progress
        self.progress_var.set(f"Готовність до подорожі: {progress}%")
        
        if progress == 100:
            messagebox.showinfo("🎉 Вітаємо!", "Ви готові до подорожі! Гарного відпочинку! 🌴")
    
    def reset_checklist(self):
        """Скидає всі позначки в чек-листі"""
        result = messagebox.askyesno("Підтвердження", "Ви впевнені, що хочете скинути всі відмітки?")
        if result:
            self.checklist.checked_items.clear()
            for category in self.checkboxes:
                for item in self.checkboxes[category]:
                    self.checkboxes[category][item].set(False)
            self.update_progress()
    
    def create_guide_tab(self):
        """Створює вкладку з інформацією про країни"""
        guide_frame = ttk.Frame(self.notebook)  
        self.notebook.add(guide_frame, text="🌍 Путівник")
        
        # Заголовок вкладки
        tk.Label(
            guide_frame,
            text="Путівник по популярних країнах",
            font=self.big_font,
            fg='#34495e'
        ).pack(pady=20)
        
        # Панель для вибору країни
        selection_frame = tk.Frame(guide_frame, bg='#ecf0f1')
        selection_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(selection_frame, text="Оберіть країну:", font=self.normal_font, bg='#ecf0f1').pack(anchor='w', padx=5)
        
        self.country_var = tk.StringVar()
        country_combo = ttk.Combobox(
            selection_frame,
            textvariable=self.country_var,
            values=self.country_guide.get_countries_list(),
            width=30,
            state='readonly'
        )
        country_combo.pack(anchor='w', padx=5, pady=5)
        country_combo.set(self.country_guide.get_countries_list()[0])
        country_combo.bind('<<ComboboxSelected>>', self.on_country_select)
        
        # Область зі скролінгом для інформації про країну
        canvas = tk.Canvas(guide_frame, bg="#ECF0F1")
        scrollbar = ttk.Scrollbar(guide_frame, orient="vertical", command=canvas.yview)
        self.info_frame = ttk.Frame(canvas)
        
        self.info_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.info_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        # Відображення інформації про першу країну
        self.show_country_info()
    
    def on_country_select(self, event=None):
        """Обробляє вибір країни з випадаючого списку"""
        self.show_country_info()
    
    def show_country_info(self):
        """Відображає детальну інформацію про вибрану країну"""
        # Очищення попередньої інформації
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        
        country_name = self.country_var.get()
        country_data = self.country_guide.get_country_info(country_name)
        
        if not country_data:
            return
        
        # Заголовок країни
        title_label = tk.Label(
            self.info_frame,
            text=f"🏴 {country_name}",
            font=self.title_font,
            fg='#2c3e50',
            bg='#ecf0f1',
            pady=10
        )
        title_label.pack(fill='x', padx=150, pady=5)
        
        # Основна інформація про країну
        basic_frame = tk.LabelFrame(
            self.info_frame,
            text="📋 Основна інформація",
            font=self.normal_font,
            fg='#34495e',
            bg='#ecf0f1'
        )
        basic_frame.pack(fill='x', padx=50, pady=5)
        
        basic_info = [
            f"🏛️ Столиця: {country_data['capital']}",
            f"💰 Валюта: {country_data['currency']}",
            f"🗣️ Мова: {country_data['language']}",
            f"🚨 Екстрені служби: {country_data['emergency']}",
            f"⚡ Напруга: {country_data['voltage']}",
            f"🕐 Часовий пояс: {country_data['timezone']}"
        ]
        
        for info in basic_info:
            tk.Label(
                basic_frame,
                text=info,
                font=self.normal_font,
                bg='#ecf0f1',
                anchor='w'
            ).pack(fill='x', pady=2)
        
        # Культурні особливості
        culture_frame = tk.LabelFrame(
            self.info_frame,
            text="🎭 Культурні особливості",
            font=self.normal_font,
            fg='#34495e',
            bg='#f8f9fa'
        )
        culture_frame.pack(fill='x', pady=5)
        
        for tip in country_data['culture']:
            tk.Label(
                culture_frame,
                text=tip,
                font=self.normal_font,
                bg='#f8f9fa',
                anchor='w',
                wraplength=600
            ).pack(fill='x', pady=2)
        
        # Пам'ятки країни
        attractions_frame = tk.LabelFrame(
            self.info_frame,
            text="🏛️ Головні пам'ятки",
            font=self.normal_font,
            fg='#34495e',
            bg='#f8f9fa'
        )
        attractions_frame.pack(fill='x', pady=5)
        
        for attraction in country_data['attractions']:
            tk.Label(
                attractions_frame,
                text=attraction,
                font=self.normal_font,
                bg='#f8f9fa',
                anchor='w'
            ).pack(fill='x', padx=10, pady=2)
        
        # Традиційна кухня
        food_frame = tk.LabelFrame(
            self.info_frame,
            text="🍽️ Традиційна їжа",
            font=self.normal_font,
            fg='#34495e',
            bg='#f8f9fa'
        )
        food_frame.pack(fill='x', pady=5)
        
        food_text = " • ".join(country_data['food'])
        tk.Label(
            food_frame,
            text=f"🍴 {food_text}",
            font=self.normal_font,
            bg='#f8f9fa',
            anchor='w',
            wraplength=600
        ).pack(fill='x', pady=5)
    
    def run(self):
        """Запускає головний цикл програми"""
        self.root.mainloop()


def test_e2e_critical_path():
    # Емуляція запуску головного вікна програми
    app = TouristHelper() 
    # Крок 1: Вибір країни
    app.country_selector.set('Японія')
    # Крок 2: Перевірка відображення капіталу через інтерфейс
    assert app.capital_label.text() == 'Токіо'
    # Крок 3: Перевірка перекладу
    app.phrase_selector.set('Дякую')
    assert app.translation_output.text() == 'ありがとう'

# Запуск програми
if __name__ == "__main__":
    app = TouristHelper()
    app.run()
