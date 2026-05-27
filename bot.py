# ============================================================
#  GUNGNIR — Recruitment Bot
#  python-telegram-bot v20+
#  pip install python-telegram-bot
# ============================================================

import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ConversationHandler, filters, ContextTypes
)

TOKEN   = "8916685212:AAGygsqJka323jWBa8iMNDWrLOYuXDbiU5E"
CHAT_ID = -1003918420875  # GUNGNIR | Анкети

logging.basicConfig(level=logging.INFO)

# ===== Кроки анкети =====
(
    NAME, AGE, CITY, PHONE, MESSENGER, RELOCATION,
    MIL_SERVICE, MIL_COMBAT, MIL_UNITS, MIL_VOS, UAV_EXP,
    HEALTH, WARZONE, BAD_HABITS, STRESS,
    EDUCATION, PROFESSION, SKILLS,
    MOTIVATION, STRENGTHS, ROLE, SERVICE_MEANING,
    DRIVER_LIC, OWN_CAR, PASSPORT, INTERVIEW,
    UAV_TYPES, SOLDERING, HEAVY_BOMBERS, NIGHT_FLIGHTS, SOFTWARE, UAV_THEORY,
    CONFIRM
) = range(33)

YES_NO = [["Так", "Ні"]]
YES_NO_MARKUP = ReplyKeyboardMarkup(YES_NO, resize_keyboard=True, one_time_keyboard=True)

STRESS_MARKUP = ReplyKeyboardMarkup(
    [["1","2","3"],["4","5","6"],["7","8","9"],["10"]],
    resize_keyboard=True, one_time_keyboard=True
)

SKILLS_MARKUP = ReplyKeyboardMarkup(
    [["ІТ", "Електроніка"],["Водіння", "Інженерія"],["Інше / Немає"]],
    resize_keyboard=True, one_time_keyboard=True
)

CONFIRM_MARKUP = ReplyKeyboardMarkup(
    [["✅ Надіслати анкету", "❌ Скасувати"]],
    resize_keyboard=True, one_time_keyboard=True
)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    await update.message.reply_text(
        "👋 Вітаємо у системі відбору *GUNGNIR*\n\n"
        "Підрозділ важких ударних безпілотних бомберів.\n\n"
        "Анкета складається з 7 блоків і займе ~5 хвилин.\n"
        "Відповідай чесно — це в твоїх інтересах.\n\n"
        "Почнемо? Введи своє *Прізвище, ім'я та по батькові:*",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    return NAME

async def get_name(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["name"] = update.message.text
    await update.message.reply_text("Вік:")
    return AGE

async def get_age(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["age"] = update.message.text
    await update.message.reply_text("Місто проживання:")
    return CITY

async def get_city(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["city"] = update.message.text
    await update.message.reply_text("Контактний номер телефону:")
    return PHONE

async def get_phone(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["phone"] = update.message.text
    await update.message.reply_text("Telegram або Signal (username або номер):")
    return MESSENGER

async def get_messenger(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["messenger"] = update.message.text
    await update.message.reply_text(
        "Чи готові до переїзду або відряджень?",
        reply_markup=YES_NO_MARKUP
    )
    return RELOCATION

async def get_relocation(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["relocation"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 2 — Військовий досвід*\n─────────────────\n\n"
        "Чи проходили військову службу?",
        parse_mode="Markdown",
        reply_markup=YES_NO_MARKUP
    )
    return MIL_SERVICE

async def get_mil_service(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["mil_service"] = update.message.text
    await update.message.reply_text("Чи маєте бойовий досвід?", reply_markup=YES_NO_MARKUP)
    return MIL_COMBAT

async def get_mil_combat(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["mil_combat"] = update.message.text
    await update.message.reply_text(
        "У яких підрозділах служили? (або 'Не служив')",
        reply_markup=ReplyKeyboardRemove()
    )
    return MIL_UNITS

async def get_mil_units(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["mil_units"] = update.message.text
    await update.message.reply_text("Ваша військова спеціальність / ВОС (або 'Немає'):")
    return MIL_VOS

async def get_mil_vos(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["mil_vos"] = update.message.text
    await update.message.reply_text("Чи є досвід роботи з БПЛА?", reply_markup=YES_NO_MARKUP)
    return UAV_EXP

async def get_uav_exp(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["uav_exp"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 3 — Фізична та психологічна готовність*\n─────────────────\n\n"
        "Чи маєте обмеження по здоров'ю?",
        parse_mode="Markdown",
        reply_markup=YES_NO_MARKUP
    )
    return HEALTH

async def get_health(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["health"] = update.message.text
    await update.message.reply_text("Чи готові працювати в зоні бойових дій?", reply_markup=YES_NO_MARKUP)
    return WARZONE

async def get_warzone(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["warzone"] = update.message.text
    await update.message.reply_text("Чи маєте шкідливі звички?", reply_markup=YES_NO_MARKUP)
    return BAD_HABITS

async def get_bad_habits(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["bad_habits"] = update.message.text
    await update.message.reply_text(
        "Як оцінюєте свою стресостійкість від 1 до 10?",
        reply_markup=STRESS_MARKUP
    )
    return STRESS

async def get_stress(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["stress"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 4 — Цивільні навички*\n─────────────────\n\n"
        "Освіта (школа / технікум / вища / інше):",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    return EDUCATION

async def get_education(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["education"] = update.message.text
    await update.message.reply_text("Основна цивільна професія:")
    return PROFESSION

async def get_profession(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["profession"] = update.message.text
    await update.message.reply_text(
        "Навички корисні підрозділу (можна написати своє):",
        reply_markup=SKILLS_MARKUP
    )
    return SKILLS

async def get_skills(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["skills"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 5 — Мотивація*\n─────────────────\n\n"
        "Чому хочете приєднатись саме до GUNGNIR?",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    return MOTIVATION

async def get_motivation(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["motivation"] = update.message.text
    await update.message.reply_text("Ваші сильні сторони:")
    return STRENGTHS

async def get_strengths(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["strengths"] = update.message.text
    await update.message.reply_text("Яку роль бачите для себе у підрозділі?")
    return ROLE

async def get_role(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["role"] = update.message.text
    await update.message.reply_text("Що для вас означає служба?")
    return SERVICE_MEANING

async def get_service_meaning(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["service_meaning"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 6 — Додатково*\n─────────────────\n\n"
        "Водійське посвідчення — які категорії? (або 'Немає')",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    return DRIVER_LIC

async def get_driver_lic(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["driver_lic"] = update.message.text
    await update.message.reply_text("Чи є власне авто?", reply_markup=YES_NO_MARKUP)
    return OWN_CAR

async def get_own_car(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["own_car"] = update.message.text
    await update.message.reply_text("Чи є закордонний паспорт?", reply_markup=YES_NO_MARKUP)
    return PASSPORT

async def get_passport(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["passport"] = update.message.text
    await update.message.reply_text(
        "Чи готові пройти співбесіду та перевірку?",
        reply_markup=YES_NO_MARKUP
    )
    return INTERVIEW

async def get_interview(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["interview"] = update.message.text
    await update.message.reply_text(
        "─────────────────\n*Блок 7 — Спеціалізація БПЛА*\n─────────────────\n\n"
        "З якими типами дронів працювали? (або 'Не працював')",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove()
    )
    return UAV_TYPES

async def get_uav_types(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["uav_types"] = update.message.text
    await update.message.reply_text("Чи маєте досвід пайки / ремонту електроніки?", reply_markup=YES_NO_MARKUP)
    return SOLDERING

async def get_soldering(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["soldering"] = update.message.text
    await update.message.reply_text("Чи працювали з важкими бомберами?", reply_markup=YES_NO_MARKUP)
    return HEAVY_BOMBERS

async def get_heavy_bombers(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["heavy_bombers"] = update.message.text
    await update.message.reply_text("Чи маєте досвід нічних польотів?", reply_markup=YES_NO_MARKUP)
    return NIGHT_FLIGHTS

async def get_night_flights(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["night_flights"] = update.message.text
    await update.message.reply_text(
        "Які програми або софт використовували? (або 'Не використовував')",
        reply_markup=ReplyKeyboardRemove()
    )
    return SOFTWARE

async def get_software(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["software"] = update.message.text
    await update.message.reply_text("Чи розумієте принципи роботи БПЛА?", reply_markup=YES_NO_MARKUP)
    return UAV_THEORY

async def get_uav_theory(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["uav_theory"] = update.message.text
    d = ctx.user_data
    preview = (
        f"─────────────────\n"
        f"📋 *Перевір свою анкету*\n"
        f"─────────────────\n\n"
        f"👤 *{d.get('name')}*\n"
        f"Вік: {d.get('age')} | Місто: {d.get('city')}\n"
        f"Телефон: {d.get('phone')} | {d.get('messenger')}\n"
        f"Переїзд: {d.get('relocation')}\n\n"
        f"🪖 Служба: {d.get('mil_service')} | Бойовий досвід: {d.get('mil_combat')}\n"
        f"Підрозділи: {d.get('mil_units')}\n"
        f"ВОС: {d.get('mil_vos')} | БПЛА досвід: {d.get('uav_exp')}\n\n"
        f"❤️ Здоров'я: {d.get('health')} | ЗБЗ: {d.get('warzone')}\n"
        f"Шкідливі звички: {d.get('bad_habits')} | Стрес: {d.get('stress')}/10\n\n"
        f"🎓 Освіта: {d.get('education')}\n"
        f"Професія: {d.get('profession')} | Навички: {d.get('skills')}\n\n"
        f"💬 Мотивація: {d.get('motivation')[:80]}...\n\n"
        f"🚗 Права: {d.get('driver_lic')} | Авто: {d.get('own_car')} | Закордонний: {d.get('passport')}\n\n"
        f"🚁 Дрони: {d.get('uav_types')}\n"
        f"Пайка: {d.get('soldering')} | Бомбери: {d.get('heavy_bombers')} | Ніч: {d.get('night_flights')}\n"
        f"Софт: {d.get('software')} | Теорія: {d.get('uav_theory')}"
    )
    await update.message.reply_text(
        preview + "\n\n─────────────────\nНадіслати анкету?",
        parse_mode="Markdown",
        reply_markup=CONFIRM_MARKUP
    )
    return CONFIRM

async def confirm(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "✅ Надіслати анкету":
        d = ctx.user_data
        u = update.message.from_user
        card = (
            f"🟡 *НОВА АНКЕТА — GUNGNIR*\n"
            f"─────────────────────\n\n"
            f"👤 *{d.get('name')}*\n"
            f"Telegram: @{u.username or '—'} | ID: `{u.id}`\n\n"
            f"*1 / ЗАГАЛЬНЕ*\n"
            f"Вік: {d.get('age')}\n"
            f"Місто: {d.get('city')}\n"
            f"Телефон: {d.get('phone')}\n"
            f"Месенджер: {d.get('messenger')}\n"
            f"Переїзд/відрядження: {d.get('relocation')}\n\n"
            f"*2 / ВІЙСЬКОВИЙ ДОСВІД*\n"
            f"Служба: {d.get('mil_service')}\n"
            f"Бойовий досвід: {d.get('mil_combat')}\n"
            f"Підрозділи: {d.get('mil_units')}\n"
            f"ВОС: {d.get('mil_vos')}\n"
            f"Досвід БПЛА: {d.get('uav_exp')}\n\n"
            f"*3 / ФІЗИЧНА ТА ПСИХОЛОГІЧНА ГОТОВНІСТЬ*\n"
            f"Обмеження здоров'я: {d.get('health')}\n"
            f"Готовність до ЗБЗ: {d.get('warzone')}\n"
            f"Шкідливі звички: {d.get('bad_habits')}\n"
            f"Стресостійкість: {d.get('stress')}/10\n\n"
            f"*4 / ЦИВІЛЬНІ НАВИЧКИ*\n"
            f"Освіта: {d.get('education')}\n"
            f"Професія: {d.get('profession')}\n"
            f"Навички: {d.get('skills')}\n\n"
            f"*5 / МОТИВАЦІЯ*\n"
            f"Чому GUNGNIR: {d.get('motivation')}\n"
            f"Сильні сторони: {d.get('strengths')}\n"
            f"Роль у підрозділі: {d.get('role')}\n"
            f"Служба для мене: {d.get('service_meaning')}\n\n"
            f"*6 / ДОДАТКОВО*\n"
            f"Водійські права: {d.get('driver_lic')}\n"
            f"Власне авто: {d.get('own_car')}\n"
            f"Закордонний паспорт: {d.get('passport')}\n"
            f"Готовність до співбесіди: {d.get('interview')}\n\n"
            f"*7 / БПЛА СПЕЦІАЛІЗАЦІЯ*\n"
            f"Типи дронів: {d.get('uav_types')}\n"
            f"Пайка/ремонт: {d.get('soldering')}\n"
            f"Важкі бомбери: {d.get('heavy_bombers')}\n"
            f"Нічні польоти: {d.get('night_flights')}\n"
            f"Програми/софт: {d.get('software')}\n"
            f"Теорія БПЛА: {d.get('uav_theory')}\n"
            f"─────────────────────"
        )
        await ctx.bot.send_message(
            chat_id=CHAT_ID,
            text=card,
            parse_mode="Markdown"
        )
        await update.message.reply_text(
            "✅ *Анкету надіслано!*\n\n"
            "Ми розглянемо її та зв'яжемось з тобою протягом 24 годин.\n\n"
            "Слава Україні! 🇺🇦",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await update.message.reply_text(
            "Анкету скасовано. Якщо передумаєш — напиши /start",
            reply_markup=ReplyKeyboardRemove()
        )
    ctx.user_data.clear()
    return ConversationHandler.END

async def cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    await update.message.reply_text(
        "Анкету скасовано. Напиши /start щоб почати заново.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def main():
    app = Application.builder().token(TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME:           [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            AGE:            [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
            CITY:           [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
            PHONE:          [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            MESSENGER:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_messenger)],
            RELOCATION:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_relocation)],
            MIL_SERVICE:    [MessageHandler(filters.TEXT & ~filters.COMMAND, get_mil_service)],
            MIL_COMBAT:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_mil_combat)],
            MIL_UNITS:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_mil_units)],
            MIL_VOS:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_mil_vos)],
            UAV_EXP:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_uav_exp)],
            HEALTH:         [MessageHandler(filters.TEXT & ~filters.COMMAND, get_health)],
            WARZONE:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_warzone)],
            BAD_HABITS:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_bad_habits)],
            STRESS:         [MessageHandler(filters.TEXT & ~filters.COMMAND, get_stress)],
            EDUCATION:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_education)],
            PROFESSION:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_profession)],
            SKILLS:         [MessageHandler(filters.TEXT & ~filters.COMMAND, get_skills)],
            MOTIVATION:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_motivation)],
            STRENGTHS:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_strengths)],
            ROLE:           [MessageHandler(filters.TEXT & ~filters.COMMAND, get_role)],
            SERVICE_MEANING:[MessageHandler(filters.TEXT & ~filters.COMMAND, get_service_meaning)],
            DRIVER_LIC:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_driver_lic)],
            OWN_CAR:        [MessageHandler(filters.TEXT & ~filters.COMMAND, get_own_car)],
            PASSPORT:       [MessageHandler(filters.TEXT & ~filters.COMMAND, get_passport)],
            INTERVIEW:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_interview)],
            UAV_TYPES:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_uav_types)],
            SOLDERING:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_soldering)],
            HEAVY_BOMBERS:  [MessageHandler(filters.TEXT & ~filters.COMMAND, get_heavy_bombers)],
            NIGHT_FLIGHTS:  [MessageHandler(filters.TEXT & ~filters.COMMAND, get_night_flights)],
            SOFTWARE:       [MessageHandler(filters.TEXT & ~filters.COMMAND, get_software)],
            UAV_THEORY:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_uav_theory)],
            CONFIRM:        [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )
    app.add_handler(conv)
    print("Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()
