def send_message(client, chat_id, message):
    """
    Sends a message to a specified chat in Telegram.

    :param client: The Telegram client instance.
    :param chat_id: The ID of the chat to send the message to.
    :param message: The message content to send.
    """
    async def _send():
        await client.send_message(chat_id, message)
    
    return _send()

def fetch_media(client, chat_id, message_id):
    """
    Fetches media from a specified message in Telegram.

    :param client: The Telegram client instance.
    :param chat_id: The ID of the chat containing the message.
    :param message_id: The ID of the message to fetch media from.
    :return: The media object if available, else None.
    """
    async def _fetch():
        message = await client.get_message(chat_id, message_id)
        return message.media if message.media else None
    
    return _fetch()