import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Docker Calculator Pro", layout="centered")

# Убираем лишние отступы и меню
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Calculator Pro")

# HTML/JS Компонент
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: transparent; /* Прозрачный фон для интеграции */
        display: flex;
        justify-content: center;
        align-items: start;
        height: 100vh;
        margin: 0;
    }
    .calculator {
        background-color: #22252d;
        width: 100%;
        max-width: 320px; /* Чуть компактнее */
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    #display {
        width: 100%;
        height: 70px;
        background-color: #2a2d36;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        font-size: 36px;
        text-align: right;
        padding: 15px;
        box-sizing: border-box;
        margin-bottom: 20px;
        font-family: monospace;
        outline: none; /* Убираем синюю обводку */
    }
    .buttons {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
    }
    button {
        padding: 15px;
        font-size: 20px;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        background-color: #2a2d36;
        color: white;
        transition: all 0.1s;
        font-weight: bold;
        user-select: none; /* Чтобы текст не выделялся при быстром клике */
    }
    /* Эффект нажатия */
    button:active, button.pressed { 
        transform: scale(0.95); 
        filter: brightness(1.2);
    }

    .btn-operator { color: #26e6a9; }

    /* Кнопка равно */
    .btn-equal { 
        background-color: #26e6a9; 
        color: #22252d; 
        grid-column: span 2; 
    }
    .btn-equal:hover { background-color: #1fc28e; }
    .btn-equal:active, .btn-equal.pressed { background-color: #1aa679; }

    .btn-clear { color: #ff5e5e; }
    .btn-delete { color: #ff5e5e; }
</style>
</head>
<body>

<div class="calculator">
    <input type="text" id="display" readonly autofocus>
    <div class="buttons">
        <button class="btn-clear" id="btn-ac" onclick="clearDisplay()">AC</button>
        <button class="btn-delete" id="btn-del" onclick="deleteChar()">⌫</button>
        <button class="btn-operator" onclick="append('/')">÷</button>
        <button class="btn-operator" onclick="append('*')">×</button>

        <button onclick="append('7')">7</button>
        <button onclick="append('8')">8</button>
        <button onclick="append('9')">9</button>
        <button class="btn-operator" onclick="append('-')">−</button>

        <button onclick="append('4')">4</button>
        <button onclick="append('5')">5</button>
        <button onclick="append('6')">6</button>
        <button class="btn-operator" onclick="append('+')">+</button>

        <button onclick="append('1')">1</button>
        <button onclick="append('2')">2</button>
        <button onclick="append('3')">3</button>

        <button onclick="append('0')">0</button>
        <button onclick="append('.')">.</button>
        <button class="btn-equal" id="btn-equal" onclick="calculate()">=</button>
    </div>
</div>

<script>
    const display = document.getElementById('display');
    const btnEqual = document.getElementById('btn-equal');

    // Функция добавления символа
    function append(value) {
        display.value += value;
        // Прокручиваем вправо, если цифр много
        display.scrollLeft = display.scrollWidth; 
    }

    function clearDisplay() {
        display.value = '';
    }

    function deleteChar() {
        display.value = display.value.toString().slice(0, -1);
    }

    function calculate() {
        try {
            if (display.value) {
                // Безопасное вычисление через eval
                // Разрешаем только цифры и мат. знаки
                // (хотя eval сам по себе тут в песочнице)
                const result = eval(display.value);

                // Проверка на деление на ноль (Infinity)
                if (result === Infinity || result === -Infinity) {
                    display.value = 'Ошибка';
                    setTimeout(() => display.value = '', 1000);
                } else {
                    display.value = result;
                }
            }
        } catch (error) {
            display.value = 'Error';
            setTimeout(() => display.value = '', 1000);
        }
    }

    // Слушатель клавиатуры
    document.addEventListener('keydown', function(event) {
        const key = event.key;

        // Фокус на дисплей, чтобы работало удаление и т.д.
        display.focus();

        if (/[0-9]/.test(key)) {
            // Ищем кнопку с такой цифрой, чтобы подсветить (по желанию)
            append(key);
        }
        if (['+', '-', '*', '/', '.'].includes(key)) append(key);

        if (key === 'Enter') {
            event.preventDefault(); // Чтобы форма не отправлялась (если она есть)

            // 1. Вызываем расчет
            calculate();

            // 2. Визуально "нажимаем" кнопку Равно
            btnEqual.classList.add('pressed');
            setTimeout(() => {
                btnEqual.classList.remove('pressed');
            }, 150); // Убираем эффект через 150мс
        }

        if (key === 'Backspace') deleteChar();
        if (key === 'Escape') clearDisplay();
    });
</script>

</body>
</html>
"""

# Рендерим HTML блок. Высоту можно подстроить.
components.html(html_code, height=500)