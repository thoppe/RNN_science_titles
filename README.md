# RNN Science titles
--------------------------------
A recurrent neural network with long short term memory to predict titles of scientific articles. Uses karpathy's [char-rnn](https://github.com/karpathy/char-rnn) as the base implementation. 

Due to space contraints the titles are not stored in this repo.

## Instructions

Place all journal titles, new line separated with extension `*.txt` in the [`raw_input`](/raw_input) directory.

Run `python src/wrangle.py` to convert a limited character map (uses unidecode) and copies them into [`input`](/input) directory.

Use `python build_run_script.py` to build scripts to run the torch commands.






