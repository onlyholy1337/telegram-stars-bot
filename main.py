import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import (
    LabeledPrice,
    Message,
    PreCheckoutQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

TOKEN = "not true mode."

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ Купить доступ", callback_data="buy")]
    ])
    await message.answer(
        "демо-бот оплаты через звездочки\n\n"
        "Нажми кнопку ниже, чтобы купить доступ за 1 ⭐",
        reply_markup=kb,
    )


@router.callback_query(F.data == "buy")
async def send_invoice(callback: CallbackQuery):
    await callback.message.answer_invoice(
        title="Премиум-доступ",
        description="Разблокируй секретный контент за 1 звезду ⭐",
        prices=[LabeledPrice(label="Доступ", amount=1)],
        payload="premium_access",
        currency="XTR",
    )
    await callback.answer()


@router.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery):
    await query.answer(ok=True)


@router.message(F.successful_payment)
async def on_payment(message: Message):
    await message.answer(
        "🎉 Оплата прошла! Спасибо за 1 ⭐\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "я сельский дайте денег!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "ээуээээээуууээ)) - @hatethisproject"
    )


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    print("zaebis` work")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
