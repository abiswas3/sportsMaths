<div class="container">
# Introduction

A friend recently introduced me to [World Triathlon
Rankings](https://stats.protriathletes.org/rankings/women). It got me
thinking about how these rankings are calculated. The Professional
Triathlete Organisation (PTO) provides an explanation
[here](https://protriathletes.org/the-pto-world-rankings-explained/).
The immediate question that I had was, how do you compare athletes who
never race each other on the same course. Unlike Formula 1 or the
Premier League where each racer/team competes with each other across a
season, long course athletes rarely compete with each other. Shown
below is $N$ x $N$ normalised co-occurence matrix of how often the
best athletes actually race each other. Here $N$ depicts the top
$N=35$ women professional triathletes as of May 22, 2021. The men
follow a similar co-occurrence distribution.

<img src="pngs/co-occurence.png" alt="drawing" width="800"/>

There were 160 half ironman or ironman races from in 2019, 2020
and 2021. A cell score of 1 would mean those 2 athletes raced all 160
races together. The figure above indicates a high score of .035 which
would indicated two athletes shared a race $ceil(0.035*160)$ times out
of 160 races and this is the most frequently two athletes compete
against each other on the long course over 3 years. This makes
intuitive sense and is unlikely to change in the future. Endurance
events are physically draining. Long course athletes cannot compete at
an optimal level every month. Furthermore, traveling for triathlon is
an expensive ordeal. Athletes in Australia do not usually compete in
the major European races. Barring a handful of races like Hawaii,
Challenge Daytona and 70.3 Worlds, it is unlikely athletes will
assemble for the same race. More about this later.

The primary blocker to figuring out how to rank professional
triathletes - is to come up with a solution to compare two separate
race performances on the same scale. Athletes live in different parts
of the world and cannot always travel to major races. This implies
that neither the strength of the field nor the number of professionals
attending a race is the same every race. Shown below is a the
attendance distribution of 70.3 and Ironman races across the last
three years for professional womens sport.

<img src="pngs/num_athletes_distribution.png" alt="drawing" width="800"/>

As discussed earlier, we observe that not a lot of professional
athletes show up to every race. Next we look at the strength of field
of races. The formula to compute the strength of a field for a race is
slightly contrived. For a given race $r$,

$$ Strength(r) = \sum_{a \in r} \frac{1}{rank(a)}$$

For a given race, we just sum the reciprocal of the world ranking of
the athlete. For an athlete not in the top 100, we give them all a
rank of 101. This implies, if an athlete is not in the top 100, they
have the same impact on the strength of the field regardless of their
rank. The general idea is borrowed from [Mean Reciprocal
Rank](https://en.wikipedia.org/wiki/Mean_reciprocal_rank) used to
evaluate Search Retrieval Systems.

<img src="pngs/strength_of_field.png" alt="drawing" width="800"/>

**NOTE: I need to think this through a bit more. MRR doesn't really
apply here. Also I use the current world rankings and not the world
rankings at the time of race. This doesn't really change the shape of
the distribution and important races do end up having a higher
score. However, we need to think this through further.**

Using the above formula, IM Hawaii 2019, the world championship had a
strength of $2.67$ wheras IM Ireland had a score of $0.059$.

Such a variance in strength of field prevents us from using simple
scoring systems like they use in Formula 1; where the winner of a race
is awarded 25 pts, second 18 pts and so on. Most triathletes would
agree that winning the world championship is more impressive than
winning a regional race like IM Wisconsin. Some athletes would argue
hilly courses suit them while others argue windy ones suit them. So we
cannot weight performances of all races equally. If we did, we
incentivise athletes to seek out the weakest fields and races that
suit them. This prevents the sport from having the best compete with
the best, thereby reducing triathlons value as a spectator sport.

Given what we have discussed, this problem is non trivial to solve. In
the next section we look to understand how the current athlete scores
and ranks are computed. How did the PTO navigate the issues we just
discussed?

## The Current System

For any race $r$, there is an expected finish time
$\mathbb{E}[r]$. Let $\overline{\mathbb{E}[r]}$ be the estimate of
this expectation (the PTO website calls this number AIT). We defer the
discussion of how this estimate is computed. Assume it exists and is a
fair number for all races $r \in R$, where $R$ is the set of
races. The PTO claim that this number is adjusted for courses - hilly,
windy, cold etc. For now we assume this is true. We will defer the
veracity of that claim for a later post.

Let the finish time of athlete $a$ for race $r$ be $f(a,r)$. The score
or world ranking points for that race for athlete $a$ is defined as:

$$S(a, r) = 100 + (\overline{\mathbb{E}[r]} - f(a,r))/\delta$$ where
$\delta = 0.15\%*\overline{\mathbb{E}[r]}$.

In words (from the PTO website), If an athlete equals the AIT for any
eligible race, they receive 100 World Ranking Points. If an athlete is
faster than the AIT, they are awarded an additional World Ranking
Point or fraction of a point for each .15\% by which they beat the AIT
-- where AIT is $\overline{\mathbb{E}[r]}$ in our notation.

See worked out example:
```
-----------------------------------
2019 IM Hawaii Women AIT:  09:01:46
----------------------------------
Anne Haug finish time - 8:40:10
Lucy Charles finish time - 8:46:44

Using the formula described above, delta = 48.75899999999999

----------------------------------
Scores:
----------------------------------
Ann Haug : 100 + [1296/48.758] = 126.57
Lucy Charles: 100 + [902/48.758] = 118.49
```
We verify our estimate  with the reported number on the site.

<img src="pngs/score_calc.png" alt="drawing" width="800"/>

The final score for an athlete is the sum of an athletes best 3 races
in a year, as quoted by the
[website](https://stats.protriathletes.org/points). The Collins cup
qualifying has a slightly more complicated protocol but it is still
based on points calculated of AIT and can be found
[here](http://abiswas3.github.io/blog/PTO_Scoring/)

```The PTO World Rankings shall be determined by the aggregate number
of World Ranking Points an athlete has earned for their three best
races for 2021, with the final rankings on December 31, 2021,
determining the pay-out to PTO Professionals under the PTO Annual
Bonus System.
```

## Some immediate consequences of such a system

The PTO's approach is to use AIT or an estimate of expected finish
time to normalise across races. Under the current system, given a race
$r$, to maximise one's chances to improve their PTO rank, each athlete
should try and beat the AIT of a race. Racing other athletes is
secondary. Such a scheme leads to the following scenario. Consider the
following example:

```
Athelte A and B are competing for the same PTO world ranking

A and B's history of points so far  looks like the following:

A : 99, 100, 88
B : 101, 97, 86

Yearly points:
A: (99 + 100 + 88)/3 = 95.66
B: (101+97+86)/3 = 94.66

B needs to get 3 points more than A in a race to win.
```

Looking at the scores so far one would assume $A$ and $B$ are very evenly
matched i.e. in all races so far, they have had similar finish times.
The last race of the year should be a decider for who should take the
spot they are competing for. Now they are racing a course on a really
windy and rainy day. Lots of races have wind and rain variance across
the years. All athletes are way off the expected finish time.

Everyone is suffering, but $B$ manages to beat $A$ by a good 30
minutes. In professional Ironman, such a gap is considered to be a
demolition. Intuitively, for two evenly matched athletes, $B$ having
won the decider decisively, $B$ should get the higher spot. They raced
4 times, A won twice marginally, B won once marginally and once
decisively.

However based on the PTO scoring system, $B$ does not usurp
$A$. Despite $B$ winning the race, and $A$ having a terrible race --
the race conditions meant that all athetes were way off the AIT. Thus
the maximum points to be gained from this race is much lower than
their historical scores. The PTO takes only the top 3 races.

At this point the reader might be wondering if such a situation really
happens? Can you win a race and still get really low race points? The
answer is YES! It happens all the time. Shown below is the
distribution of the race winners points for long serving races. For
races that have been organised annually for at least 5 years in a row,
we examine the distribution of winner points.

<img src="pngs/winner_pts.png" alt="drawing" width="800"/>

On the Y axis is the race points won by the women's winner of the
race. On the X axis are different popular races. Multiple races like
IM-UK, have had winners vary from the scores 20 to 80 over a span of 5
years or more. On the contrary, the winner at Hawaii has consistenly
outdone the expected finish time. It also appears that AIT points
prefer certain courses like Roth over courses like IM UK. The reader
might infer that this is because Roth usually has a stronger
field. However, we show later in this document that, this is not the
case. Intuitively, the above formula for scoring does not take into
account the strength of field. (**NOTE: The AIT computation might
indirectly, but as we show later it is not really represented in the
data)**.

It should be noted that the score obtained by an athlete is based
purely on the AIT time. Winning a race with a very strong field gives
you no advantage in your world rankings. The only incentive to be
ranked higher is to beat the predicted time. Also so far we have
ignored, how accurate this predicted time actually is. From the figure
above, it would seem it is not very good at predicting the race winner
time. Ideally the race winner should on average be close to 100
pts. However, when we look at the distribution of winner finish times
in 2018 and 2019, it seems that AIT overestimates athlete performance
consistently. Shown below is the winner pts distribution for the
women's pro field across all races that had an AIT in 2018 and 2019

<img src="pngs/winner_dist_2019.png" alt="drawing" width="800"/>

<img src="pngs/winner_dist_2018.png" alt="drawing" width="800"/>

It seems that on average the winner of pro race in the women's field
receives 80 points, thereby missing the expected time for a race most
of the time. **Important: **Despite showing that the current system
has very high variance, our results so far do not indicate the current
system is dysfunctional. All we have shown that under certain
circumstances, the current system might disadvantage athletes. We are
yet to show that points system has actually hurt athlete rankings in
practice or quantify how likely the sytem might screw someone over. We
do this next.

### I beat the best athletes and was worse off for it

In this section we show how the avg points awarded to the top 3
participants vary with the strength of the field. We use the formula
defined above. While it is not callibrated properly, it is still
monotonic with perceived strength of field and serves to illustrate
why the current system could be problematic. The blocks shown in red,
are races where racers achieved high scores while winning in a weaker
field compared to the green box. The green box race winners scored
equal if not lower points while beating much stiffer competition.

As qualitative reference for understanding these numbers we reference
to the two races below. We let the readers decide which race was more
stacked, and which one should regarded more.

<img src="pngs/screwy_ness.png" alt="drawing" width="800"/>

The reader might notice that at the extreme right there are few
scatter points flying around.  Those represent the world championships
and challenge daytona.  Really big races rarely have low scores. This
is natural. Assume the probability of an elite top 20 athlete having a
misfire is $\epsilon$.  The probability all of them misfire is
$\epsilon^{20}$. Say $\epsilon$ is very high like $30\%$ i.e an elite
athlete bonks in 3 out of 10 races, the probability that we still see
a high score is $99.99\%$. This is desirable, we want to reward
athletes winning stacked races. The issue is on the other end. There
are plenty of races with much weaker fields that where winning is
rewarded on the same scale as winning the bigger races.

Let us look at the case of Holly Lawrence. In 2019, Holly was ranked
5th in the world and in that entire year she had won every race
barring two. In the two she had not won, she had lost to only Daniela
Ryf - the world number 1. In fact she had beaten the following
athletes ranked above her.

```
4 Sarah Crowley 1.0
3 Anne Haug 1.0
2 Lucy Charles-Barclay 1.0
```

So in a year where Holly had beaten all athletes ranked above her
excepting Daniela, she still got ranked 5th. Why? It is because Lucy,
Anne and Sarah ran some other race Holly did not race and beat the AIT
by a bigger margin. Athletes are not aware of the AIT before a race,
so they have no idea if they can beat it.

## A slight detour: Understanding the incentives of the sport

Any ranking system is inherently transitive. If you rank A, B and C in
ascending order. It says on average A would best B and B would best C,
thereby indicating A would best C by the transitive property.

Before we try and design/evaluate a system that pits athletes against
each other, it is important to understand how athletes think and what
they value in the sport. **Disclaimer**: I am not an athlete. This is
an attempt at summarising my understanding of how professionals
race. This information is gathered through face to face conversations,
viewing official races and race interviews. It appears that for an
elite athlete, there is one primary goal -- to qualify for and win the
world championship. For the Ironman distance, this race is Kona. The
70.3 has an annual world championship every year as well. Winning the
aforementioned long course races is considered the pinnacle of
sporting achievement. Throughout the rest of the season the focus of
the athletes is to get a spot in one of these races. Once a spot is
secured, the focus shifts to ensuring a peak performance in
Kona. Whether this assumption is true or not can be debated by people
who actually race for a living. It should be noted that the system
before 2017 was based on points accumulated during a season. Ironman
spcifically went away from that system to prevent athletes from
burning out before the big race. For now assume my assumptions hold,
and let us understand how the current system is misaligned with how
athletes race. After building this intuition through qualitative
analysis, we will look at the empirical comparison of top 5 athletes
at kona and end of the year world rankings.

We first begin with how Kona qualification works.There are plenty of
[blog
posts](https://www.triathlete.com/culture/news/the-good-and-the-bad-of-the-new-ironman-world-championship-pro-qualifying-system/)
out there describing how this works. Some athletes do not need to
qualify for Kona:

* Last years winner of Kona. 
* Last years Kona podium athletes.
* Last years 70.3 winner.

**However, these athletes must still complete a “validating” race,
where they complete the distance within the racing year.**

Let's pause and think about what the implications of that one
statement are. The above list of athletes are elite - they have won
the bloody thing last year. Rankings are re-done every year. So in
this new year, these athletes just have to finish some race, to make
sure they can go to Kona again. There is no incentive to win or post a
fast time. Why bother? There might be risk of injury. Going to a race
has a lot of faff to it. However in this race they will be awarded (or
not awarded) points. It might be still be considered for computing
rankings. One could argue that the PTO only uses the top 3 races in a
year. So these races won't be considered. Such a statement is only
true if an elite athlete races a lot more than 3 times a year. We will
look into how often professional athletes race in a later section.

Now for those who did not get an automatic slot, we copy this excerpt
from a post describing qualifying

```For Kona qualifying, there is one slot per gender at most races,
two at regional championships, plus extra “floating slots” allocated
to specific races, usually regional champions or bigger races Ironman
chooses. (You can see the full pro calendar with its allocations) This
is where it gets a little confusing. The two floating slots will
either be split evenly between men and women or will both go to one
gender, based on how many men and women are on the start line that
day. There are 100 slots total.```

There appears to be some controversy regarding how floating slots are
assigned but it is beyond the scope of this document. The big takeway
from the quoted text is the following -- to get to Kona you must win a
race and that gets you to the championship. Nowhere does it say, you
are better off if you go faster. Under the current ranking system, one
is always encouraged to go faster. One could argue, that going fast
and winning are extremely correlated. Does that not equate to the same
thing? The short answer is "yes but not really". Athletes do not
always need to push themselves to the maximum in every race. Let's
consider the following example:

Shown below are the results for Ironman Tulsa on May 23rd, 2021.

<img src="pngs/tulsa_results.png" alt="drawing" width="800"/>

Before the race started, the following athletes were already Kona
qualified. There were two spots available for qualification in this
race.

* Daniela Ryf
* Kat Matthews
* Sky Moensch
* Heather Jackson
* Sarah Crowley
* Ruth Astle
* Meredith Kessler

Just Gurutze Frades Larralde, Kimberley Morrison and Tara Grosvenor
were not qualified going in. Kimberley Morrison was awarded a Kona
Spot for this race. She came off the bike in second place but her real
incentive was to not be crossed by more than 1 athlete without a Kona
Qualification spot. That was the safer strategy given the goal of the
sport and knowing a lot can go wrong in the marathon leg of an
ironman. Similarly Daniela Ryf came out nearly 20 minutes ahead on the
bike. She does not need to run the marathon at her maximum effort to
secure podium. Athletes race each other. They swim/bike/run as fast as
they need to secure podium. Should their efforts be judged against
some arbitrary predefined time for completion? Post race, Kat Matthews
(I cannot find a link to the interview), declared her goal was Kona
from here on. She would not be racing any long course events from here
on. She might do some 70.3 races to stay in shape.

At this point we have hopefully convinced you that most athletes do
not need to race each race to their fullest ability and that most
athletes want to peak for Kona. What this implies is, that even the
strategy of best 3 races in a year is likely sub optimal. This makes
the problem of ranking triathletes even harder. Not only do they not
compete against each other often; even when they do - they might have
different incentives.

In the next section, we look at how often athletes race once
qualification is secured.

### Do world ranking represent Kona behaviour

Kona is the one race the best athletes race each other on the same
course with the same incentives - TO WIN.

Shown below are the end of they year world rankings for the top 5 men
athletes at Kona. On inspection it might not look too bad. It would
seem like the world rankings system is pretty good at picking the top
3 athletes. However, this is an artifact of having two very dominant
champions over a long time i.e. Jan Frodeno and Sebastien Kienle. When
you have a champion like Jan who is so dominant, the ranking system
does not matter. Whatever the sytem, they usually always win. As an
exercise we leave the reader to look up how positions 5-10 align with
world rankings to convince themselves.

| Year | 1st | 2nd | 3rd | 4th | 5th |
|------|-----|-----|-----|-----|-----|
| 2019 | 1   | 10  | 4   | 6   | 11  |
| 2018 | 4   | 8   | 9   | 18  | 14  |
| 2017 | 4   | 1   | 14  | 3   | 7   |
| 2016 | 1   | 2   | 29  | 4   | 12  |
| 2015 | 1   | 15  | 3   | 4   | 34  |
| 2014 | 3   | 13  | 1   | 12  | 37  |


The women's table:

| Year | 1st | 2nd | 3rd | 4th | 5th |
|------|-----|-----|-----|-----|-----|
| 2019 | 3   | 2   | 4   | 8   | 9   |
| 2018 | 1   | 2   | 3   | 14  | 19  |
| 2017 | 1   | 7   | 6   | 3   | 19  |
| 2016 | 1   | 8   | 5   | 20  | 21  |
| 2015 | 1   | 2   | 20  | 16  | 10  |
| 2014 | 1   | 3   | 2   | 6   | 4   |

Once again it might not look egregious. Both tables have some outliers
or surprises. The women's fielf has had dominant champions in Daniela
Ryf, Lucy Charles, Anne Haug and Mirinda Carfrae. In sport whenever
you have dominant champions, the ranking sytem for those athletes
becomes redundant. They come out on top on with all systems. The more
interesting distribution are the athletes ranked 5-15 in both
genders. It remains a philosophical question how much the championship
should dictate world rankings. Under the current system, it has the
same weight as all other races. That seems unfair given not all races
have the same field nor the same incentives. We could also base the
entire ranking off of Kona performance, which seems unfair as
well. Someone who has been consistent all year could have an off
day. Should their entire career ranking depend on one race?


## Is there a better system? How can we evaluate its fairness?

### What works for the current system

Before discussing alternate rankings we would like to point out some
strengths of the current system. 

* It is quite simple. If we assume the AIT is a fair time, then the
  scoring is deterministic and interpretable. This is a very important
  feature of ranking systems. Fans and athletes crave simplicity.
  
* Given that the AIT is unknown before race time it is actually quite
  hard to manipulate. An athlete may try to enter a weaker field and
  win it, but end up having a lower win score anway. They might
  succeed at a high score also. There seems to be no easy way to tell
  from the winner distributions. Some could view this as a con as
  well. How can an athlete strategise, how they move up in rankings if
  they do not know at all.
  
* One of the biggest strengths the current system is that prevents
  lower ranked athletes from taking advantage of a bonk. The world of
  ELO i.e.  chess, scrabble, college football, major league baseball
  is based on head to head to battles. So if a much weaker team/player
  were to beat a much stronger player their ranking improves
  dramatically. If Wigan were to beat Manchester United, it's a big
  deal. If Manchester United were to beat Wigan, people would consider
  it as standard. This makes a lot of sense in a sport that is
  actually pairwise head to head. However, in triathlon athletes race
  a field of $N$ athletes. If we artificially create ${n \choose x}$
  pairings out of $N$ plyaers, this system could go horribly
  wrong. Consider the example where Daniel Ryf had an off day in Kona
  2019. Lower ranked athletes who had a normal race were able to beat
  her because she performed really poorly, not because they beat her
  on a good day. Now should athletes benefit from not having an above
  average performance just because someone ranked really high had a
  bad performance? This is where Triathlon differs from all head to
  head ranking systems. In classic head to head systems, we can say
  with high confidence the other persons peformance caused the top
  ranked athlete to fail. However we cannot say that in
  triathlon. Thus having athletes race against the clock is a
  reliable around.

* Finally, despite critiquing the scoring for most of the document,
  this is a reasonable baseline. The problem of ranking athletes that
  do not race each other frequently is a hard maths problem. In the
  subsequent series, we will go through the historical relevance of
  this problem. Scientists have been trying for over a 100 years.

### Where are we going

If you have reached this far, we have hopefully convinced you why
there is a need for a fairer sysystem of scoring. In the next part of
this series, we discuss alternate methods of evaluation. Surprisingly,
the world of chess and video games have already established solutions
to some of the problems discssued above. We modify the famous
[Elo](https://en.wikipedia.org/wiki/Elo_rating_system) rating and
Microsoft XBox's [True Skill](https://en.wikipedia.org/wiki/TrueSkill).

So far the scoring is based on an expected finish time. We assume
athletes would like some of the following traits in their scoring
system.

* A race won in a really strong field should count more than a race
  won in a weaker field. Athletes race each other. People work
  together on the bike, sit on feet in the swim and employ different
  run strategies. Some athletes have a good kick. Others put the
  hammer down early. These strategies are based on the course and the
  field, not the predicted time that's decided beforehand.
  
* There should be no course bias. Certain courses should not give you
  more points than other independent of the field strength.
  
* Scoring should be memoryless i.e. every year we reset the
  scores. You don't get to rest on your laurels for too long.
  
* Probably some more??

</div>
