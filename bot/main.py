diff --git a/bot/main.py b/bot/main.py
index 470e45b9e2057558c3ec5667d581fcb3ab8a445f..540aba18066d153c3d6b606b7deefe62495938a1 100644
--- a/bot/main.py
+++ b/bot/main.py
@@ -1,16 +1,30 @@
 import os
+from dotenv import load_dotenv
 from telegram import Update
 from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
+
+load_dotenv()
 TOKEN = os.getenv("BOT_TOKEN")
+ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
+
 async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text("Бот запущен.")
+
 async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
+    if update.effective_user.id != ADMIN_ID:
+        await update.message.reply_text("У вас нет прав для выполнения этой команды.")
+        return
     await update.message.reply_text(update.message.text)
+
 def main():
-    if not TOKEN: raise RuntimeError("BOT_TOKEN not set")
+    if not TOKEN or not ADMIN_ID:
+        raise RuntimeError("BOT_TOKEN or ADMIN_ID not set")
     app = Application.builder().token(TOKEN).build()
     app.add_handler(CommandHandler("start", start))
     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
     app.run_polling()
-if __name__ == "__main__": main()
+
+if __name__ == "__main__":
+    main()
+
 # ci test 2025-08-23T21:46:55Z
