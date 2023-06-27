def search_first_unique_symbol(text: str) -> str:
    # Приймаємо текст та розбиваємо його на слова
    list_words_of_text = text.split()
    # Масив для найпершого символу
    unique_symbol_list = []
    # Пробігаємо по списку слів
    for word in list_words_of_text:
        # Словник для зберігання кількості кожного символа
        counter_symbol_dict = {}
        # Перебираємо символи в словах
        for symbol in word:
            if symbol.isalpha():
                # Перераховуємо кожен символ в слові
                counter_symbol_dict[symbol] = counter_symbol_dict.get(symbol, 0) + 1
        # print(counter_symbol_dict)

        # Отримуємо найперший символ який НЕ повторюється в слові та додаємо його в масив
        for unique_symbol in word:
            if unique_symbol.isalpha() and counter_symbol_dict.get(unique_symbol) == 1:
                unique_symbol_list.append(unique_symbol)
                break
        # print(unique_symbol_list)

    # Отримуємо із набору символів найперший унікальний символ
    for unique_symbol in unique_symbol_list:
        if unique_symbol_list.count(unique_symbol) == 1:
            return unique_symbol
