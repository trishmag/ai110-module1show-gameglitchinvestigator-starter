# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
I put 50 and the game said to go lower when the secret number was 72.
In the box to enter your guess it says press enter to apply, I pressed enter, and nothing happened.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI tools I used on this project were Gemini and Copilot.
- Give one example of an AI suggestion you accepted and why.
Copilot suggested refactoring the core game logic out of app.py and into logic_utils.py. I accepted this suggestion because it made the code easier to test, reduced duplication, and clearly separated UI code from game logic.
- Give one example of an AI suggestion you changed or rejected and why.
Copilot  suggested a fix for the hint logic that passed basic tests but still produced incorrect hints during gameplay. I rejected that version because it didn’t fully account for how guesses were compared to the secret number.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided if a bug was fixed only when it was resolved in two ways:
the automated pytest passed, and
the behavior was correct when I manually played the game in Streamlit.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I added a pytest that checked whether a guess of 60 against a secret number of 50 returned the hint "Too High". The test passed which confirmed that the comparison logic was working correctly and no longer reversed.
- Did AI help you design or understand any tests? How?
AI helped me better understand how targeted tests can confirm a specific fix.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number was kept changing because Streamlit reran the script after each guess.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire script from top to bottom whenever the user interacts with the userface/website.
- What change did you make that finally gave the game a stable secret number?
I stored the secret number in st.session_state and only generated it if it didn’t already exist so that the number would stay the same.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to continue writing small, targeted tests for each bug I fix instead of relying only on manual testing.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I would do a double take on verifying AI suggestions instead of assuming they were correct just because they looked reasonable.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI-generated code is a starting point, not an answer. It’s my responsibility as a developer to question, test, and refine what the AI produces.
