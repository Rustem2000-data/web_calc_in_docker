import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Docker Calculator", layout="centered")
st.title("🧮 Калькулятор в Docker")

# Инициализируем состояние экрана
if 'display' not in st.session_state:
    st.session_state.display = ""


# Функция обработки нажатий
def handle_click(button_text):
    current_text = st.session_state.display

    if button_text == "=":
        try:
            # Вычисляем выражение
            # replace нужен, чтобы правильно обрабатывать деление и умножение, если символы отличаются
            expression = current_text.replace('×', '*').replace('÷', '/')
            st.session_state.display = str(eval(expression))
        except Exception:
            st.error("Ошибка!")
            st.session_state.display = ""

    elif button_text == "C":
        # Очистить всё
        st.session_state.display = ""

    elif button_text == "⌫":
        # Удалить последний символ
        st.session_state.display = current_text[:-1]

    else:
        # Добавить символ
        st.session_state.display += str(button_text)


# Поле вывода (сделали шрифт покрупнее визуально через markdown, если нужно, или просто input)
st.text_input("Результат", value=st.session_state.display, disabled=True, key="display_input")

# Структура кнопок (список списков для рядов)
button_rows = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '⌫', '+'],  # Добавили кнопку стирания
    ['=']  # Равно на всю ширину
]

# Отрисовка кнопок
for row in button_rows:
    # Если в ряду 1 кнопка (например "="), делаем одну колонку, иначе 4
    cols = st.columns(len(row))
    for i, button_text in enumerate(row):
        with cols[i]:
            if st.button(button_text, use_container_width=True):
                handle_click(button_text)
                st.rerun()