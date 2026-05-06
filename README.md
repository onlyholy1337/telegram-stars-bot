<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/aiogram-3.x-green?style=for-the-badge&logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/Telegram-Stars-gold?style=for-the-badge&logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" />
</p>

<h1 align="center">⭐ Telegram Stars Payment Bot</h1>

<p align="center">
  <b>Минимальный Telegram-бот для приёма оплаты через Telegram Stars</b><br>
  30 строк кода - без платёжных систем, без документов, без комиссий
</p>

---

## Что это?

Простой бот-пример, демонстрирующий оплату через **Telegram Stars** (валюта `XTR`). Пользователь нажимает кнопку → получает инвойс на 1 звезду → после оплаты получает контент.

**Идеально для:**
- Продажи цифровых товаров (гайды, ключи, доступы)
- Подписочных ботов
- Donation-ботов
- Любого бота, где нужна простая оплата

---

## Возможности

-  Инвойс с кнопкой оплаты
-  Оплата через Telegram Stars (XTR)
-  Автоматическое подтверждение платежа
-  Отправка контента после оплаты
-  Чистый, расширяемый код

---

##  Структура проекта

```
telegram-stars-bot/
├── main.py              # Основной файл бота
├── requirements.txt    # Зависимости
├── LICENSE             # MIT лицензия
└── README.md           # Этот файл
```

---

## Быстрый старт

### 1. Клонируй репозиторий
```bash
git clone https://github.com/onlyholy1337/telegram-stars-bot.git
cd telegram-stars-bot
```

### 2. Установи зависимости
```bash
pip install -r requirements.txt
```

### 3. Создай бота
- Открой [@BotFather](https://t.me/BotFather) в Telegram
- Отправь `/newbot`, следуй инструкциям
- Скопируй токен

### 4. Заполни токен бота в main.py
```bash
TOKEN = "СЮДА ТОКЕН"
```

### 5. Запусти
```bash
python main.py
```

## Код бота (main.py)

```python
@router.callback_query(F.data == "buy")
async def send_invoice(callback: CallbackQuery):
    await callback.message.answer_invoice(
        title="Премиум-доступ",
        description="Разблокируй секретный контент за 1 звезду ⭐",
        prices=[LabeledPrice(label="Доступ", amount=1)],
        payload="premium_access",
        currency="XTR",  # XTR = Telegram Stars
    )
```

> **Ключевое:** `currency="XTR"` - это и есть Telegram Stars

---

## 🎨 Кастомизация

Хочешь продавать что-то своё? Измени:

| Параметр | Где | Что делает |
|----------|-----|-----------|
| `title` | `send_invoice()` | Название товара в инвойсе |
| `description` | `send_invoice()` | Описание товара |
| `amount` | `LabeledPrice(amount=1)` | Цена в звёздах |
| `on_payment()` | Внизу файла | Что отправить после оплаты |

---

## 📌 Важно знать

- Telegram Stars работает только для **цифровых товаров**
- Минимальная цена — 1 звезда

---

## 📄 Лицензия

MIT — делай что хочешь, только упомяни автора.

---

<p align="center">
  <b>Если полезно — ставь ⭐ репозиторию!</b><br><br>
  <a href="https://t.me/hatethisproject">📱 Telegram-канал</a> •
  <a href="https://funpay.com/users/4210009/">🛒 FunPay</a> •
  <a href="https://tiktok.com/@wsoeoee">🎵 TikTok</a>
</p>
