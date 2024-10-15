from streamlit.testing.v1 import AppTest
at = AppTest.from_file("pages/Playground.py")

at.run()

at.selectbox[0].set_value("gpt-4o").run()

at.chat_input[0].set_value("Hello").run()
at.slider[0].set_value(0.3).run()
at.slider[1].set_value(0.7).run()

mock_session_state = at.session_state
# Assertions
assert mock_session_state['chat_history'][0]['role'] == 'user'
assert mock_session_state['chat_history'][0]['content'] == 'Hello'
assert mock_session_state['chat_history'][1]['role'] == 'assistant'
assert len(mock_session_state['chat_history'][1]['content']) > 0
assert mock_session_state['temperature'] == 0.3
assert mock_session_state['selected_model'] == 'gpt-4o'
assert mock_session_state['top_p'] == 0.7

print("All test passed")