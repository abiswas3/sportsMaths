---
title: Lectur I
...
<div class="container">

```Primo lecture series in mathematics: Lecture I- Shannon's Demon```

# My friend Tom

My friend Tom is a real man's man. He fears no man, surfs with sharks, descends on a bike without using his hands and goes even as far as opening his worldle without vowels. It was only a matter of time, before such a man found himself on the roulette tables of the Cambridge Stock Exchange(CSE). With a gun in his holster and cowboy boots from Essex, he will certainly not be investing in the diversified public the market or be tracking index funds. No, not our Tom. He's here to bet on individual volatile stocks - like those pictures of crypto cats. He sees things that no one else sees. The question is, what does he really see?
 
## The setup

The CSE is a very simple market place -- it has a single stock whose price either doubles or halves everyday with equal probability. At the tables of this exchange we have three characters -- *Sexy Steve*, *Bicyclist Ben* and our friend Tom. Tied at the hip since birth, these three punters do everything together. All three of them observe that on average they stand to gain $1.25$ dollars per 1 dollar invested.

Let $Y$ be the random variable depicting how much money I have after one day and $X$ denote how much money I start with. We have 

\begin{align}
\mathbb{E}[Y] &= \frac{1}{2}\text{ Money double } + \frac{1}{2}\text{ half } \\
&= X + \frac{1}{4}X \\
&= 1.25X
\end{align}

Setting $X=1$ we see we get $1.25$ dollars per $1$ dollar invested on average.


## Sexy Steve and Bicylist Ben have a go

*Sexy Steve*, known in the rougher parts of Cambridgeshire as a ladies man decides to invest first. *Deceitful Doug* tells him about the benefits of compound interest, and observing that he makes a profit on average he decides to let his $1$ dollar sit for a long time.

*Bicyclist Ben* has spent years in the professional cycling peloton splitting his valuable time between recreational drug users and miserable sports dopers. He knows how to spot bad advice from miles out. He knows to get compound interest to work, the geometric expectation of the random variable must be positive. Above we only have the arithmetic expectation to be positive. More on what those fancy words mean later, but this is what Ben does. Regardless of the outcome of the day, he cashes out everyday, and puts a fresh $1$ dollar into the pot. "Madness!" shouts *Sexy Steve*, "haven't you heard of compound interest??"

Below we show a uniform sub sample of all the possible outcomes for Steve and Ben. A green line indicates that a profit has been made. The dreaded red indicates those money-grabbing sleazebags at CSE have won.



Despite having a net positive daily expectation; *Sexy steve* either makes it big or goes bust with equal probability. He did get all the benefits of compound interest with all drawbacks of losing money equally equally. With this strategy, Stephen is playing roulette.

<img src="pngs/steve.png" width=50% height=50%></img>

Benjamin on the other hand, almost never loses any money on the long run. The shrewd bike rider avoided all the pot holes and crashes only to get linear growth in pay. While Benjamin grew richer almost certainly, he only gained enough riches to afford himself 1 day at the go karts after days of saving -- but taking inflation into account, poor old Ben did not even get his day at the races.

<img src="pngs/ben.png" width=50% height=50%></img>


## Re-balance and diversify

Tom opts for the simple strategy which he borrowed from Claude Shannon when they met in the gambling tables of Las Vegas in the early 50s. He takes his 1 dollar and invests half of it. The rest he saves. At the end of the day, he adds his earnings and then invests half; and saves the other half. He repeats this process every-day. Can Tom be exponentially rich without any risks?

<img src="pngs/tom.png" width=50% height=50%></img>

Oh yes he can :-). His chances of going into the red are significantly lower, while his potential to make exponential money remains the same.


### Why does the arithmetic mean not work

We all saw that Steve stood to make 1.25 for every dollar he spent. Then on average why does he go bust so often. One way to think about it is that averages are not robust to outliers. In event Steve tossed HEADS for $N$ rounds, he makes an enormous sum of money. This enormous sum would bias the final average of all the bankrolls that could be achieved, despite it being extremely unlikely that he tosses $N$ coins in a row. Due to the nature of compound interest or exponential growth, there is always a chance to make mega bucks. However, this mega buck figure biases the average away from what is most likely to happen. The most likely event is that steve tosses $\frac{N}{2}$ HEADS and $\frac{N}{2}$ TAILS. The geometric mean is the amount of money steve stands to make in that case. Which is a little bit over 0.

### What just happened ?

Well if you talk to a financial expert they might throw out words like Kelly's principle or volatility drag or Parrando paradox or variance reduction. These are all accurate summarisations of the phenomenon described above. To be fair, I never did read the original paper by Kelly nor do I know what Parrando paradox or volatility drag means. Luckily we do not to know the consequences of such words to understand simple probability or compound interest. Before outlining why Tom's strategy is superior in the long run let me describe a simpler game instead. 


* The game consists of $N$ rounds. 
* The house tosses a coin with probability of HEADS $p$
* If HEADS you win your bet i.e. the house gives you $W$ dollars for every dollar you bet.
* If TAILS you lose your bet i.e. the house takes your money.

You start with a bankroll of $B$. The question is what fraction $f$ of your bankroll should you bet? All of it $f=1$? Half of it $f=\frac{1}{2}$? None of it $f=0$? Let's look at an example:

* In the first round you bet $fB$, the house flips a coin it turns out HEADS. Your new bankroll is

\begin{align*} 
B_1 &= B + WfB \\
&= B(1 + fW)
\end{align*}

* In the second round you bet $fB$ again, the house flips a coin it turns out HEADS. Your new bankroll is

\begin{align*} 
B_2 &= B_1 + WfB_1 \\
&= B(1 + fW) + WfB(1 + fW)\\
&= B(1 + fW)^2
\end{align*}

* In the third round you bet $fB$ again, the house flips a coin it turns out TAILS. Your new bankroll is

\begin{align*} 
B_3 &= B_2 - WfB_2 \\
& = B_2(1 - fW) \\
& = B(1 + fW)^2(1 - fW)
\end{align*}


Say the game goes on like this for $N$ rounds, your final bank roll is

\begin{align*} 
B_N &=  B(1 + fW)^h(1 - fW)^t\\
\end{align*}

where $h$ denotes the number of HEADS and $t$ denotes the number of TAILS in $N$ coin tosses. Your relative gain in wealth is simply the ratio of what you have to what you started with.

\begin{align*} 
\frac{B_N}{B} &=  (1 + fW)^h(1 - fW)^t\\
&= G_N
\end{align*}

Also note that your bankroll is increasing exponentially as opposed to linearly (thus you're getting the benefits of compound interest). The game was to figure out how much of your wealth you should have bet i.e. what is the best value for $f$. Well the best value for $f$ is the value that maximises your gain $G_N$ after $N$ rounds -- on average (as this is after all a random game). Remember we said something about geometric means before? This is where we define the intuition behind using the geometric mean. We have already described, why not to use the arithmetic mean. 

We toss a coin $N$ times with a probability of showing HEADS being $p$. Thus on average we expect $Np$ HEADS and $N(1-p)$ TAILS. The geometric mean of the random variable $G_N$ is the gain we would incur if that event occurred i.e. we had $Np$ HEADS and $N(1-p)$ TAILS. Thus when you have exponential growth or compound interest, the geometric mean describes the average case outcome. Shown below is the formal derivation of this statement. You may ignore it, if calculus is not your cup of tea.

The geometric mean of k values $x_1, x_2 \dots x_k$ is simply $(x_1\times x_2\dots x_k)^{\frac{1}{k}}$. The expectation the geometric mean of the gain as $N$ becomes very large i.e. it tends to infinity

\begin{align*} 
\mathbb{E}[G_N] &=  \lim_{N \rightarrow \infty}(1 + fW)^{\frac{h}{N}}(1 - fW)^{\frac{t}{N}}\\
&= (1 + fW)^{p}(1 - fW)^{1-p}\\
&= G
\end{align*}

You can take my word for the last line of the equation as it comes from the [law of large numbers](https://www.wikiwand.com/en/Law_of_large_numbers). What the above set of equations is saying, is that on average in every round of the game you'll make a gain of $G$ - the process has an expected geometric mean of $G$. In that case your bank roll would be

\begin{align*} 
B_N &=  BG^N\\
\end{align*}

which is exactly bank roll you'd be left with if you had lost exactly $N(1-p)$ games and won $Np$ games -- which is the average case behavior. Now to maximise this gain, you can use a bit of calculus, take the derivative of $G$ with respect to $f$ and set both sides to 0 and solve for $f$. If you trust that I did this properly, the optimal $f$ turns out to be $p - \frac{1-p}{W}$.

Now if you google what [Kelly Criterion](https://www.wikiwand.com/en/Kelly_criterion) you get the exact same formula. As a side note, if we had taken the log of $G_N$ and done a simple average (arithmetic mean), we would have reached the same outcome. 

<div class="important"> So if the word geometric mean confuses you but you know what a simple average is: The log of the geometric mean of a random
variable equals the arithmetic mean of the log of
that variable</div>	

In his [economics paper](https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf), Kelly argues
these gambling strategies are related to human utility and claims human utility preferences are log shaped. Thus he is simply maximising the utility by maximising the geometric mean.

Here we see why arithmetic mean is so deceiving

Under the Kelly criterion, after 10 rounds (assuming $B = 1$)

* Expected (mean) final wealth = 3.25
* Median final wealth = 1.80

By comparison, recall that if we bet all the money $(f = 1)$. After 10 rounds (assuming B = 1)

* Expected (mean) final wealth = 57.67
* Median final wealth = 0


### Back to our problem of investing

Now our problem is only slightly more complicated than the one described above.

* The game consists of $N$ rounds. 
* The house tosses a coin with probability of HEADS $p$
* If HEADS you win your bet i.e. the house gives you $W$ dollars for every dollar you bet.
* <del>If TAILS you lose your bet i.e. the house takes your money.</del> **If TAILS you lose $L$ dollars for every dollar in the market.**

Let's write down the equations like that again. Assume the coin tosses are HEADS, TAILS, HEADS.

\begin{align*} 
B_1 &= B + WfB_1 \\
B_2 &= B_1 - LfB_1 \\
B_3 &= B_2 + WfB_2 \\
& = B(1 - fW)^{h}(1 - fL)^{t} \\
\end{align*}

Once again as the bankrolling is compounding, we use the geometric mean. Do the calculus, and now the Kelly Criterion for maximising the geometric mean is given by $f=\frac{p}{L} - \frac{q}{W}$. Remember, our money doubled i.e. $W=1$. Also our money halved, so $L=0.5$. We have $p=q=0.5$, plugging them in, we get $f=0.5$. Thus Tom's strategy of investing only half his money at every round is optimal if he is looking to maximise the geometric mean of his relative gain.

## Sexy Steve disagrees

Sexy Steve stands up and says - BULLSHIT! I'm better off investing all my money. I could have become a mega billionaire. Is he wrong? It might appear from the analysis above that he is wrong but he actually isn't. Nowhere in the analysis so far, have we considered our players tolerance to risk or their relative utilities. It maybe that making a little more money on average adds no value to Steve's life. He'd rather go bust; after all he's only spending a dollar. Finally that brings us to our final lesson - that neither Ben, Tom or Steve was wrong: They just bet different strategies based on their risk tolerance. The famous saying is as follows:

```If I maximize the expected square-root of
wealth and you maximize expected log of
wealth, then after 10 years you will be richer
90% of the time. But so what, because I will
be much richer the remaining 10% of the
time. After 20 years, you will be richer 99% of
the time, but I will be fantastically richer the
remaining 1% of the time. 
```

## One last bit

Real markets do not swing like a random walk. They follow unpredictable trends that no one can actually predict. Sadly I do not know how to there is no secret to getting wealthy beyond already being wealthy. In summary, there is no hope for our friend Tom, but at least he won't pay a hedge fund scam that claims they can beat the market

</div>
