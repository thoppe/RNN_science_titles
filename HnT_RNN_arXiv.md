# RNN arXiv
_bro, do you even science?_

*[Travis Hoppe](http://thoppe.github.io/)*
----------
[https://github.com/thoppe/RNN_science_titles](https://github.com/thoppe/RNN_science_titles)

====

## New machine learning hotness
#### Recurrent Neural Network (RNN) with the Long Short Term Memory (LSTM)

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

====+
<br>
!(figures/gifs/mb3.gif)<<height:220px; transparent>>
!(figures/gifs/mb2.gif)<<height:220px; transparent>>
!(figures/gifs/mb4.gif)<<height:220px; transparent>>

Really, go read this post -- it's amazing!


====*

## `char-rnn`, Andrej Karpathy
Lua/torch [library](https://github.com/karpathy/char-rnn) to implement a RNN-LSTM.
!(figures/charseq.jpeg)<<height:500px; transparent>> 20 second introduction to RNN

====
## [arXiv.org](http://arxiv.org/)
preprint server for physics, mathematics & CS (160+ categories!)
!(figures/arXiv_cap.png) <<height:600px; transparent>> 
====*
## [arXiv.org/astro.ph](http://arxiv.org/list/astro-ph/recent)
titles are short learnable "patterns"
!(figures/arXiv_titles.png) <<height:600px>>
=====
## Data Wrangling

spider arXiv $\rightarrow$ unidecode ($\beta \rightarrow b$) $\rightarrow$ 
strip all characters except `[a-z][A-Z][0-9][_-()]`

## Machine Learning
Trained all categories on the same set of hyperparameters:

`1024` RNN size, `2` layers, `30` max epochs, `0.5` dropout,
`50` sequence length, `0.002` learning rate, `0.97` decay, `50` batch size

Took top cross-validated model (sometimes error exploded!).

=====
# Size Matters!
!(figures/validation_vs_input.png) <<height:600px>> Fixed hyperparameters for all models, exponential fit
====
## Examples (low quality)
====*
## Examples (medium quality)
====*
## Examples (high quality)
====*
### Bro, do you even science?
examples...
====

# What's next?
Any large, consistent corpus of text...

[Political speeches](http://users.wfu.edu/louden/Political%20Communication/Class%20Information/SPEECHES.html)
Political treaties (eg. [TPP](https://ustr.gov/tpp/))
[DNA](http://www.ncbi.nlm.nih.gov/genbank/), [RNA](http://rnacentral.org/), [protein sequences](http://www.uniprot.org/)
[Rap lyrics](http://rap.genius.com/) & [poems](https://www.poets.org/)
[Paper abstracts](http://www.scopus.com/)


====
# Thanks, you!
Tweet more ideas to [@metasemantic](https://twitter.com/metasemantic)!
