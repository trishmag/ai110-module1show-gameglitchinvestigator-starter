# logic_utils.py

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw))
        return True, value, None
    except ValueError:
        return False, None, "That is not a number."


def check_guess(guess: int, secret: int):
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        return current_score + max(100 - 10 * attempt_number, 10)

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
