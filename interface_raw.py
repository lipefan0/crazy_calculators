from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None: pass

# Definir a regra de construção das demais classes que é implementada
    
class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Email: {message}")

# Definir a regra de construção das demais classes que é implementada

class SMSNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
      print(f"SMS: {message}")

class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)
    
obj = Notificator(EmailNotificationSender())
obj.send("Hello, World!")