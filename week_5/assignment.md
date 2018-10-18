# Bias in Machine Learning
*by Guillermo Montecinos, Generative Music Class, ITP Fall 2018.*

Bias in Machine Learning is a thing since it exists due it's a set of mathematical rules arbitrary stablished by a human mind, but became a problem when the designed models started to output undesirable or unexpected results. As I could learn from a brief research, in ML there are many places for bias as layers are in the process of design and train a model, and interpret its results.
All these three places are: 1) the model itself, 2) the data used for training the model, and 3) the perception process in which we -humans- try to give sense to ML results.

## Model Bias
A model is just a model, it's not a truth or a dogma. That is what I learnt at school when in optimization class I realized the only way to develop a model that could approach a truly version of a phenomena was by adding infinite variables. A model is an abstraction of the world thought by a person -probably in most cases a white male- who attempts to represent through his/hers vision of the world the logic behind certain phenomena. And it's also a limited version of his/hers world abstraction because since computing power is limited, model must be limited.

Thus, it is mandatory to be aware of the original goal the model was developed for, because a model designed for estimate credit risk of bank costumers will behave differently of a model developed for estimate terrorist behaviors, and there is a bias embedded in the model's logic.

## Training Data Bias
On the other hand, independent of the inherent bias the model could have, the training data plays a main role in the bias that a ML process may output, and a lot has been written about it. Since ML models are basically statistical prediction systems, they attempt to predict the future by looking the past, so as in history it depends of which past we tell to the model how it well behave in the future.

There are many examples of biased ML or AI outputs due to biased datasets used to train those models, but I'd like to mention two of them. The first is Microsoft's twitter bot *Tay*, a ML/AI experiment released in 2015 that attempted to simulate the behavior of an US-American female teenager on twitter. Tay was designed to learn from her network, so as she computed her followers behavior she became extremely fast into a anti-semite, pro-Hitler and pro-Trump Twitter user. The change on her was so extreme that Microsoft had to close the account after one day.

The other example corresponds to IBM Watson, an AI machine designed to supply easy ML service to the clients through a *close* chat box. With that goal in mind, IBM developers used *Urban Dictionary* as a training dataset for the model, clearly intending to incorporate informal idioms to Watson. The problem came when the machine learnt violent expressions.

## Perception Bias
Finally, the third layer of bias in ML is the perception process whereby we try to assign a meaning to something. I found an interesting post by [Memo Atken](https://medium.com/artists-and-machine-intelligence/ami-residency-part-1-exploring-word-space-andprojecting-meaning-onto-noise-98af7252f749) in which he talks about bias in ML processes. I won't extensively describe what he states, but I want to focus on the idea of *"projecting meaning into noise"* which talks about when we have a trained model -any kind of model, let's say an image generation one-, what we really have is an array of nodes that take an input and reorganize it according with what it learnt from a bunch of patterns we passed to it.

So, for example if we trained a model for creating Rorschach's Test style images and we input it an array of random pixels, it will probable output a Rorschach-style shape -generated from noise. So, what Atken states is that the meaning of the ML output is not inherent to the result itself but is given by our perception system trying to find patterns in the shape -because in the core it's just random noise sorted following patterns (the training dataset). And during this process what we are actually doing is projecting all our biases in order to find a mining -or project a meaning- into noise.

## Conclusion
Bias in ML -as in any other science- is a multi-variable problem that can't be addressed from only one direction. Dataset bias is a thing -very important by the way- but is a problem embedded into another problem which -the bias in the model conception. In order to be fair regarding the bias on a ML output, we always have to be aware of all the layers that are in front of us and recognize that under no circumstances an output of a mathematical process can be objective.
