from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from service import *
from keyboards import *

router = Router()


@router.message(F.text == "🌍 Places")
@router.message(Command("places"))
async def show_menu(message: Message):
    await message.answer("Choose category:", reply_markup=await get_category_places_button())







@router.callback_query(F.data.startswith('category_order_'))
async def show_menu_places(callback: CallbackQuery):
    cat_id = callback.data.split("_")[-1]
    await callback.message.answer("Choose a place:", reply_markup=await get_places_order_button(cat_id))
    await callback.answer()
    

    
    