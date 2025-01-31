class InsufficientFundsException(Exception):
    """
    Виключення, яке виникає при недостатній кількості коштів на рахунку.
    """

    def __init__(self, required_amount: float, current_balance: float, currency: str = "USD",
                 transaction_type: str = "transaction") -> None:
        """
        Ініціалізація виключення InsufficientFundsException.

        :param required_amount: Грошова сума, необхідна для виконання операції.
        :param current_balance: Поточний баланс рахунку.
        :param currency: Валюта рахунку (за замовчуванням "USD").
        :param transaction_type: Тип транзакції (за замовчуванням "transaction").
        """
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
        message = (
            f"Insufficient funds for {transaction_type} in {currency}.\n"
            f"Required: {required_amount}, Available: {current_balance}"
        )
        super().__init__(message)


def process_transaction(account_balance: float, amount: float, currency: str = "USD",
                        transaction_type: str = "transaction") -> float:
    """
    Виконує транзакцію, якщо на рахунку достатньо коштів.

    Args:
        account_balance: Поточний баланс рахунку.
        amount: Сума операції.
        currency: Валюта рахунку (за замовчуванням "USD").
        transaction_type: Тип транзакції (за замовчуванням "transaction").

    Return:
    Новий баланс рахунку після транзакції.

    Raises:
         InsufficientFundsException: Якщо на рахунку недостатньо коштів.
    """
    if amount > account_balance:
        raise InsufficientFundsException(amount, account_balance, currency, transaction_type)

    account_balance -= amount
    print(f"\n{transaction_type.capitalize()} successfully completed!\nNew balance: {account_balance} {currency}.")
    return account_balance


try:
    balance: float = 200.0  # Поточний баланс
    withdrawal_amount: float = 200.1  # Сума операції
    balance = process_transaction(balance, withdrawal_amount, "UAH", "purchase")
except InsufficientFundsException as e:
    print(f"Transaction failed: {e}")

try:
    balance: float = 500.0  # Поточний баланс
    withdrawal_amount: float = 250  # Сума операції
    balance = process_transaction(balance, withdrawal_amount, "UAH", "purchase")
except InsufficientFundsException as e:
    print(f"Transaction failed: {e}")
