import random
import streamlit as st
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# --- FIX: stable Streamlit state ---
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

raw_guess = st.text_input("Enter your guess:")

submit = st.button("Submit Guess 🚀")
new_game = st.button("New Game 🔁")

if new_game:
    st.session_state.clear()
    st.rerun()

if st.session_state.status != "playing":
    st.stop()

if submit:
    ok, guess, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess)

        outcome, message = check_guess(guess, st.session_state.secret)
        st.warning(message)

        st.session_state.score = update_score(
            st.session_state.score, outcome, st.session_state.attempts
        )

        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
            st.success(
                f"You won! Secret: {st.session_state.secret} | "
                f"Score: {st.session_state.score}"
            )
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(
                f"Game over! Secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )
