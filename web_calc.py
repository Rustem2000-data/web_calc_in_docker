import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Docker Calculator", layout="centered")
st.title("🧮 Калькулятор в Docker")

# Инициализируем состояние экрана, если его еще нет
if 'display' not in st.session_state:
    st.session_state.display = ""

# Функция обработки нажатий (логика из вашего кода)
def handle_click(button_text):
    if button_text == "=":
        try:
            # Используем ваш метод вычисления
            st.session_state.display = str(eval(st.session_state.display))
        except Exception:
            st.error("Некорректное выражение")
            st.session_state.display = ""
    elif button_text == "C":
        st.session_state.display = ""
    else:
        st.session_state.display += str(button_text)

# Поле вывода (вместо entry.grid)
st.text_input("Результат", value=st.session_state.display, disabled=True)

# Список кнопок как в вашем коде
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Создание сетки кнопок 4x4
cols = st.columns(4)
for i, button in enumerate(buttons):
    with cols[i % 4]:
        if st.button(button, use_container_width=True):
            handle_click(button)
            st.rerun() # Перезагружаем страницу, чтобы обновить текст в поле ввода