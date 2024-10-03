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
    await update.message.reply_text('Olá! Este é o SerpaCrewBot. Como posso ajudar?')

# Função principal para inicializar o bot
async def main():
    token = os.getenv("TELEGRAM_API_KEY")  # Obtendo a chave da API do Telegram a partir da variável de ambiente

    # Criando a aplicação do bot
    application = ApplicationBuilder().token(token).build()

    # Adicionando o handler para o comando /start
    application.add_handler(CommandHandler("start", start))

    # Iniciando o bot
    logger.info("Bot está sendo iniciado...")
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

# Este é um novo comentário para testar o deploy no Azure.
# Este é um novo comentário para testar o deploy no Azure.
# Este é um novo comentário para testar o deploy no Azure.;;
