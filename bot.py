import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configurando o logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Função chamada quando o comando /start é recebido
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Comando /start recebido.")
    await update.message.reply_text('Olá! Este é o SerpaCrewBot. Como posso ajudar?')

# Função principal para configurar o bot
async def main():
    token = os.getenv("TELEGRAM_API_KEY")
    
    # Inicializando o bot
    application = ApplicationBuilder().token(token).build()

    # Adicionando o handler do comando /start
    application.add_handler(CommandHandler("start", start))

    logger.info("Bot iniciado e aguardando comandos.")

    # Executando o bot com polling
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
