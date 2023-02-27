import datetime
import src_files.headers as head
import src_files.globals as glob

currencies = ['United States Dollar (USD)', 'Euro (EUR)', 'Japanese Yen (JPY)', 'British Pound (GBP)', 'Swiss Franc (CHF)', 'Canadian Dollar (CAD)', 'Australian Dollar (AUD)', 'New Zealand Dollar (NZD)', 'Chinese Yuan Renminbi (CNY)', 'Hong Kong Dollar (HKD)', 'Singapore Dollar (SGD)', 'South Korean Won (KRW)', 'Indian Rupee (INR)', 'Brazilian Real (BRL)', 'Russian Ruble (RUB)', 'South African Rand (ZAR)']


def log_transaction(sender, reciever, amount, successful: bool = True):
    if successful:
        dyn_text = f"[TRANSACTION SUCCESSFUL] [{sender['account_ownership']}]({sender['account_identification']}) >- [{amount} {head.random.choice(currencies)}] -> [{reciever['account_ownership']}]({reciever['account_identification']})"
        head.styled_coloured_print_centered(
            text=dyn_text,
            instant=True, colour="green")
    else:
        dyn_text = f"[TRANSACTION FAILED] {sender['account_ownership']}'s account ({sender['account_identification']}) has insufficient balance to transfer {amount} {head.random.choice(currencies)}."
        head.styled_coloured_print_centered(
            text=dyn_text,
            instant=True, colour="orange")
    head.write_to_file(text_to_write=f"[{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] {dyn_text}\n", typeOfWrite="a", path_to_file=glob.settings_file_location)
