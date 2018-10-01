rm = new RiMarkov(3);
// sample = "Denise sees the fleece, Denise sees the fleas. At least Denise could sneeze and feed and freeze the fleas."
sample = "So God created man in his own image, in the image of God created he him; male and female created he them. And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth. And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat. And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so. And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."
rm.loadText(sample);
rm.print();
// var sentences = rm.generateSentences(10);
var sentences = rm.generateTokens(10);
for (var i = 0; i < sentences.length; i++) {
  console.log(sentences[i]);
}
