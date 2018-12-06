# Generative Music
This document contains the documentation of the work developed at the class Generative Music attended during the fall 2018 term at ITP, NYU. Also, under this repo can be found all the code written.

## Generative Music Examples

### [OK Go - Needing/Getting](https://www.youtube.com/watch?v=MejbOFk7H6c)
This piece is an interesting experience of a system designed to make music which works only mechanically when the car moves in a certain direction. One execution is a destructive process that probably won't allow the system to make the same music pattern within other play. I selected this piece as generative music because is a system with certain rules and a way of play it in order to make music.

### [Laurie Spiegel](http://www.electronicbeats.net/the-feed/laurie-spiegel-score/)
Even I didn't find a performed version of this piece I got very impressed of the notation used for composing it. This is a piece for two modular synths composed by Spiegel in 1970. It is interesting how the music sheet turns into a drawing paper -well, in essence it is a drawing paper- who supports expressive shapes: for example the noise -I think it is noise- is a dense bunch of lines who moves in the space and mixed to get fused in the end of the piece.
![](http://www.electronicbeats.net/app/uploads/2016/09/Laurie-Spiegel-score.jpg)

### Listen to Terry Tiley's 'in C'
I listened a few versions of 'in C' I found in youtube. The one I liked the most is the version performed bay Brooklyn Raga Massive, a Brooklyn based collective of raga enthusiastic musicians who gather to listen and play raga music. Raga is an Indian style of music that can be defined as 'a melodic framework for improvisation. Each raga is an array of melodic structures with musical motifs, considered in the Indian tradition to have the ability to "color the mind" and affect the emotions of the audience' (source: [wikipedia](https://en.wikipedia.org/wiki/Raga)). [Brooklyn Raga Massive: Terry Riley In C.](https://www.youtube.com/watch?v=FX1vzJQMxzk)

Other versions I listened:

* [Terry Riley: In C, performed on 2012 Jan. 31 at CEU, Budapest](https://www.youtube.com/watch?v=yNi0bukYRnA)
* [Terry Riley - In C (1968) FULL ALBUM](https://www.youtube.com/watch?v=tbTn79x-mrI)
* [Terry Riley & s t a r g a z e – 'In C' – Boiler Room Amsterdam Live Performance](https://www.youtube.com/watch?v=lJPJywWfyGo)
* [In C (for solo electric guitar and electronics) by Terry Riley](https://www.youtube.com/watch?v=9JUslBFZXfo)

## Nicolasa
*Data sonification performance by Guillermo Montecinos for Generative Music class, NYU ITP Fall 2018.*

*Nicolasa* is a data sonification piece created from the real operation of the Chilean electric power system. The daily generation of the biggest dam power plants are used to create a sound landscape in which the voice of Nicolasa Quintremán demands to the Chilean Government and the Spanish Company Endesa to respect the territory of the Mapuche in southern Chile.

The original idea for this performance was to sonify the data of the entire Chilean power system in order to describe the internal interactions between the different kind of technologies that compose it. For that purpose, hydropower plants were going to be mapped to high pitch notes played by instruments as strings or piano, whilst thermal power plants -as coal or gas- were going to be mapped to low pitch notes, played by analog -robust- synths.

During my investigation I realized that this performance was an opportunity to unveil the political issues that underlie the development of the Chilean power system. In many cases, the construction of power plants has had an irreversible impact for the communities that live in the area before the projects were designed. This is the case of many small fishing creeks that were deeply affected by coal thermal power plants constructed in the shore near them, which used sea water to refresh their system, killing the fishes of the area. Similar cases occurred in southern areas were wind farms attempted to be installed in sacred land for indigenous communities which are protected by the [Convention C169](https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C169).

The most emblematic case is Ralco, a hydro power plant developed by the Spanish company Endesa which in the process of construction forced an entire community of Mapuche people to move from their land and flooded an ancestral graveyard. The construction of this project was supported by the Chilean Government.
Nicolasa Quintremán was the Mapuche leader who fought against Endesa and the Government and in her words can be found the proud and respect for her culture and her homeland. *"We will never get out of here, unless we are dead. Because we own the right, we own the mother, is a live mother, is the land. Mi mother died, but the land is alive and will live forever."*

For this performance, the music was built from the Chilean power system real performance data. Three MIDI tracks were created using [MIDIUtil](https://pypi.org/project/MIDIUtil/) for Python, for three different instruments. A base track contains the base harmony of the song, which is built using the data of eight dam power plants of Chile. A MIDI note was assigned to each plant depending on the maximum power of it, whilst the daily generation was mapped to the velocity of the MIDI note.
The main melody of the piece is "played" by Ralco, which daily generation was mapped to the possible MIDI notes centered in 60, following the C maj scale. Velocity for this track is fixed in 100.
To complete the sound landscape a bass line was added which pitch is mapped from the daily generation of the coal thermal plant Bocamina II. This power plant is located in the bay area of Lota/Coronel in southern Chile, near Concepción, one of the most polluted areas in the country due to thermal plants.

The midi file generated in the process was exported to Ableton Live, where VST were assigned to play piano in the case of dam plants and cello in the case of Ralco. Both of them were also processed with a Digidelay pedal. The bass line was used to control a Moog Minitaur via MIDI. To complete the piece, the voice of Nicolasa Quintremán was imported as samples in order to the narrative of the piece. All the samples were taken from the video documentary [Ralco](https://www.youtube.com/watch?v=qci-M7_Xmo8) by Esteban Larraín.

The full piece can be found [here](https://soundcloud.com/guillemontecinos/nicolasa).

## Bias in Machine Learning
*by Guillermo Montecinos, Generative Music Class, ITP Fall 2018.*

Bias in Machine Learning is a thing since it exists due it's a set of mathematical rules arbitrary stablished by a human mind, but became a problem when the designed models started to output undesirable or unexpected results. As I could learn from a brief research, in ML there are many places for bias as layers are in the process of design and train a model, and interpret its results.
All these three places are: 1) the model itself, 2) the data used for training the model, and 3) the perception process in which we -humans- try to give sense to ML results.

### Model Bias
A model is just a model, it's not a truth or a dogma. That is what I learnt at school when in optimization class I realized the only way to develop a model that could approach a truly version of a phenomena was by adding infinite variables. A model is an abstraction of the world thought by a person -probably in most cases a white male- who attempts to represent through his/hers vision of the world the logic behind certain phenomena. And it's also a limited version of his/hers world abstraction because since computing power is limited, model must be limited.

Thus, it is mandatory to be aware of the original goal the model was developed for, because a model designed for estimate credit risk of bank costumers will behave differently of a model developed for estimate terrorist behaviors, and there is a bias embedded in the model's logic.

### Training Data Bias
On the other hand, independent of the inherent bias the model could have, the training data plays a main role in the bias that a ML process may output, and a lot has been written about it. Since ML models are basically statistical prediction systems, they attempt to predict the future by looking the past, so as in history it depends of which past we tell to the model how it well behave in the future.

There are many examples of biased ML or AI outputs due to biased datasets used to train those models, but I'd like to mention two of them. The first is Microsoft's twitter bot *Tay*, a ML/AI experiment released in 2015 that attempted to simulate the behavior of an US-American female teenager on twitter. Tay was designed to learn from her network, so as she computed her followers behavior she became extremely fast into a anti-semite, pro-Hitler and pro-Trump Twitter user. The change on her was so extreme that Microsoft had to close the account after one day.

The other example corresponds to IBM Watson, an AI machine designed to supply easy ML service to the clients through a *close* chat box. With that goal in mind, IBM developers used *Urban Dictionary* as a training dataset for the model, clearly intending to incorporate informal idioms to Watson. The problem came when the machine learnt violent expressions.

### Perception Bias
Finally, the third layer of bias in ML is the perception process whereby we try to assign a meaning to something. I found an interesting post by [Memo Atken](https://medium.com/artists-and-machine-intelligence/ami-residency-part-1-exploring-word-space-andprojecting-meaning-onto-noise-98af7252f749) in which he talks about bias in ML processes. I won't extensively describe what he states, but I want to focus on the idea of *"projecting meaning into noise"* which talks about when we have a trained model -any kind of model, let's say an image generation one-, what we really have is an array of nodes that take an input and reorganize it according with what it learnt from a bunch of patterns we passed to it.

So, for example if we trained a model for creating Rorschach's Test style images and we input it an array of random pixels, it will probable output a Rorschach-style shape -generated from noise. So, what Atken states is that the meaning of the ML output is not inherent to the result itself but is given by our perception system trying to find patterns in the shape -because in the core it's just random noise sorted following patterns (the training dataset). And during this process what we are actually doing is projecting all our biases in order to find a mining -or project a meaning- into noise.

### Conclusion
Bias in ML -as in any other science- is a multi-variable problem that can't be addressed from only one direction. Dataset bias is a thing -very important by the way- but is a problem embedded into another problem which -the bias in the model conception. In order to be fair regarding the bias on a ML output, we always have to be aware of all the layers that are in front of us and recognize that under no circumstances an output of a mathematical process can be objective.

## Yes I'm Feelings
*Generative music piece built with Machine Learning from Radiohead's data by Sofía Suazo and Guillermo Montecinos for Generative Music class, NYU ITP Fall 2018.*

<p align="center">
  <a href="https://soundcloud.com/guillemontecinos/yeah-i-feelings">
    <img src="https://github.com/guillemontecinos/itp_fall_2018_generative_music/blob/master/week_6/documentation/yeah_I_feelings.jpg" align="middle" width="50%">
  </a>
</p>

Yes I'm feelings is 2:19 minutes a musical piece inspired in Radiohead's [Fitter Happier](https://www.youtube.com/watch?v=My10FLH5DT0) song from the album *Ok Computer*. It was build by predicting Radiohead-styled lyrics and melodies from two databases, which were live triggered from two computers. This piece was collaboration with [Sofía Suazo](https://www.sofialuisa.xyz/) for the midterm of the Generative Music class at NYU ITP, Fall 2018.

The piece's text were generated by a Markov Chain trained with Radiohead's lyrics and triggered in the browser using the library [p5.speech](http://ability.nyu.edu/p5.js-speech/), as is explained in the following [post](https://github.com/sofialuisa/GENERATIVE-MUSIC/tree/master/second_performance).

Besides, the music was generated using a [long short-term memory (LSMT)](https://en.wikipedia.org/wiki/Long_short-term_memory) recurrent neural network (RRN) trained with data collected from MIDI files. The original idea was to compose a Thom Yorke-styled melody from of a bunch of Radiohead's songs but the difficulty of properly interpreting time from MIDI files brought us to reinterpret the result of the prediction process.

### Data collection
For addressing the goal of predicting a Radiohead-style melody a [dataset](https://github.com/guillemontecinos/itp_fall_2018_generative_music/tree/master/week_6/dataset/radiohead/midi) of 18 MIDI files were collected from internet. Due to the MIDI protocol is old there is a huge variety and quality of files for the same song which brought us to manually clean the data set by listening every file using [MuseScore](https://musescore.com/) and checking the quality -or presence- of a melody in a separated track. After that process we came to a sub dataset composed by the following songs -which can be found in the dataset folder:

* 4_faust_arp
* 10_optimistic
* 11_everything_is_in_its_right_place
* 18_fake_plastic_trees
* 19_idioteque
* 21_knives_out
* codex
* exit_music_for_a_film
* just
* no_surprises
* paranoid_android
* videotape

### Data processing
For training the LSTM model MIDI data was converted into text sequences, process in which only two parameters were collected: pitch and time. The python library mido to import each MIDI message from a file and get from them the pitch and time of each note using this [script](https://github.com/guillemontecinos/itp_fall_2018_generative_music/blob/master/week_6/process_midi.py).

Each song was interpreted into a concatenation of words that were composed by the MIDI pitch in values from 0 - 127, and the time in ticks -each note looked like "66_238". The processed data can be found [here](https://github.com/guillemontecinos/itp_fall_2018_generative_music/blob/master/week_6/assets/). Finally, as the model training script used requires a unified dataset as an input, all songs were concatenated into one file called *input.txt*.

### Model training and simulations with ml5.js
For the model training process the [LSTM training framework](https://github.com/handav/lstm_training_and_generation) developed by Hannah Davis was used. This model was trained with the data gotten from the main melody of 12 Radiohead songs.

The melody was generated by running a JavaScript file in which through ml5.js' commands the model was used to generate new text sequences. Ten sequences were generated and then curated based on how similar they sound to Radiohead's melodies. Those sequences were used to trigger strings and drums in Ableton Live.

## Magenta: Exploring MelodyRNN
During week 11 I continued exploring the generation of melodies based on Radiohead's data but with Magenta's model MelodyRNN.

I trained the model with data collected from the LAKH dataset and the MIDI files used for the last performance which summarized 39 files. The training process took about 30 minutes, was set with 2000 steps and the final loss was of 0.49556.
