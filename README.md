# RNN Science titles
--------------------------------
A recurrent neural network with long short term memory to predict titles of scientific articles. Uses karpathy's [char-rnn](https://github.com/karpathy/char-rnn) as the base implementation. 

There is a quick [presentation](http://thoppe.github.io/RNN_science_titles/HnT_RNN_arXiv.html) on the project, but if all you really want is the 

## Raw data

The titles used as input and the auto-generated titles can be found in the [/samples](/samples) directory.

----------------------------------

Due to space contraints the models are not stored in this repo.

## Instructions

Place all journal titles, new line separated with extension `*.txt` in the [`raw_input`](/raw_input) directory.

Run `python src/wrangle.py` to convert a limited character map (uses unidecode) and copies them into [`input`](/input) directory.

Use `python build_run_script.py` to build scripts to run the torch commands.






