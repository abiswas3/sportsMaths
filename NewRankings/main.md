---
title: A Brief Reflection On The New Ranking System
...

<div class="container">
<div class="important"> 

**<u>Disclaimer</u>**: I am not an athlete nor can I claim to be a
hardcore triathlon fan. I am not directly affected by the outcome of
different ranking strategies, financially or spiritually. My interest
in the problem is purely from an algorithmic game theory
standpoint. Ranking strategies often lead to pathological behaviours
([see](https://youtu.be/TM_QFmQU_VA?t=494) for an
example). Understanding and analysing the mathematical underpinnings
of such behaviour is a personal research interest. Note as these
systems rank actual people with feelings and were developed
by a different set of humans (also with feelings), I have tried to
remain as neutral as possible in my discourse. In the off chance
someone is offended, I apologise.  </div>

## Recap 

In 2020, the PTO deployed a system for ranking triathletes which many
perceived to be complicated and
unfair[^1]. [See](https://abiswas3.github.io/sportsMaths/ProblemStatement/index.html)
for a refresher. At the heart of this ranking malarkey lies a simple
question -- "How do you compare the performance of two athletes who
did not race each other on the same day?". One cannot sort two
performances by finish time as they vary across courses. The problem
is not unique to triathlon either. Similar measurement issues arise
in marathon running, tennis, chess, golf and many other sports. This question has plagued social
choice theory since the 1950's, so it's unlikely any proposed solution
will resolve all outstanding issues. 


Thus in 2023, the PTO employed a committee of athletes, who after a year of discussion and deliberation, came up with a new system that aims to  simplify how ranking points were calculated and to re-align them to better represent the athlete values. [A
clear description of the new system can be found
here](https://protriathletes.org/pto-world-ranking-system/) and thus
there is no need to go over the details again.


[^1]: Searching for PTO rankings on Twitter should reveal Twitter rants about how unfair the old system was perceived to be.


At this point, as far as the PTO is concerned, this ranking problem
appears solved. The old rankings negatively affected athletes, and, thus they
were the ones who devised a new system that prioritised their interests. The
people decided for the people; democracy won [^12]. **This manuscript, unlike its
predecessors does not try to propose an alternate system. It simply
tries to understand the consequences of the new system.**
 
[^12]: and as Bernard Shaw famously stated -- "Democracy is a device that ensures we shall be
governed no better than we deserve."

## The New System

<figure>
  <img src="pngs/Screenshot 2023-02-17 at 12.04.48.png" alt="Trulli" style="width:80%">
  <figcaption>Shown above is a screen grab from [this
triathlon news article](https://www.triathlete.com/culture/news/new-2023-pto-rankings-revealed-dissected/)
which describes how the new points are calculated.</figcaption>
</figure>


Roughly the idea is as follows, there are three features, namely,

+ a tier based finish score (race position score in the figure above).
+ the strength of the race you are participating in (sof in the figure above).
+ how much faster you were from the top few athletes (race time score in the figure above). 

You get points along each of these features and finally your score is a weighted average of these features. From the outset it would appear that the new system does not over prioritise a single aspect of a race performance (such as AIT score in the old system). However, closer examination of the point system reveals that the new system is really based around one feature only -- is the race one of the PTO designated big tier races?

## The weights do not matter

As advertised on the PTO website, the first feature accounts for $40\%$ of your score, the second feature accounts for $30\%$ of your score and the third feature contributes to $30\%$ of your score. Thus the claim is that the final score is a mixture of three different features (position, strength of field and time); this is merely an illusion. The three features are highly correlated, and as a result only one feature really matters -- the race tiering i.e. how important does the PTO think this race is (akin to how grand slams work in tennis). 


<figure>
  <img src="pngs/plot1.png" alt="Trulli" style="width:80%">
  <figcaption>The figure above plots the tier on the Y-axis and the SOF on the
X-axis. It is easy to see that the two are positively correlated. For
a fixed tier, one might observe that the SOF has enormous variance (we
will get to this later) but if you do well in a high tiered race, you
will almost always do well in the SOF category as well. This makes sense -- The tiering of a race is based on prize money and prestige, and thus the best athletes end up wanting to participate. </figcaption>
</figure>


Let $T$ represent the position based tier score for an athlete and $SOF$ represent the strength of field for the given race. The timing feature is supposed to reward an athlete based on the difference
between their time and the time of the top finishers -- called the "baseline time". Let $\Delta$
represent the points obtained (or lost) compared to the baseline time[^3]. Thus relating to the features above:

+ $T$ : Race position time / Tier score (Feature 1)
+ $SOF$ : Strength of Field  (Feature 2)
+ $\Delta$ : Points gained by racing quicker than the baseline time. In the figure above $\Delta$ for the second placed athlete is $12.16$ points.


 The score for finishing really fast (or slow) is determined as a function of $\Delta$ and $B$ where $B = (T_1 + SOF)/2$, where $T_1$ is the tier score of the winner (so 100 if are in a diamond race, 95 if you are in platinum race and so on). Specifically, you get $0.3(B + \Delta)$ points for your finish time. **Note $B$ has nothing to do with your actual performance. $B$ is determined even before the race starts. Moreover the magnitude of $B$ far exceeds the magnitude of $\Delta$ with very high probability.**

Thus the final score $S$

\begin{align}
S &= 0.4\times T + 0.3\times SOF + 0.3(B + \Delta) \\
&= 0.4\times T + 0.3\times SOF + 0.3((T_1 + SOF)/2 + \Delta) \\
&= 0.4\times T + 0.3\times SOF + 0.15\times T_1 + 0.15\times SOF + 0.3\times\Delta \\
&= 0.4\times T + 0.3\times\Delta + (0.45\times SOF + 0.15 T_1)
\end{align}

[^3]: More specifically, $\Delta$ is the fraction the athlete was off from the average performance of the top 5 athletes times 6.

We already know that $T_1$ and $SOF$ are high for the big races. Moreover these have nothing do with your race performance either. You get them for free for entering the race (you must be able to get in the race first, which requires a high ranking[^11]). Thus in a way this system enforces that the rich have more chances to get richer. Also note that as the final ranking is the best 3 races out of however many you do, the system does not have a natural tendency of relegation. Good performances are rewarded and bad performances are forgotten (as long as a good performance happens sometime again). A direct consequence of such a system is that good athletes are never really hurt by a one off bad performance -- which is a really nice property of the system.

[^11]: The big races have [restricted spots](https://twitter.com/Timheming/status/1627961692876316673?s=20) so in order to get in, you must have a high ranking. To have a high ranking you must do these races.

Even $T$ is biased towards the big races (finishing 14th in a platinum race is the same as second in a silver race). This might seem bizarre as there are silver races with comparable SOF's to Platinum races. So if you're an upcoming new athlete participating in a local race because you cannot afford to go to Europe/USA all the time, then $\Delta$ is the only lever which gives you any control over increasing your final rank. So how much can you squeeze out of $\Delta$? The answer is not much! Observe the plot below which shows $\Delta$ (X-axis) as a function
of race finish position (Y-axis) for different tiered races [^6]

[^6]: PTO canadian open is not included in the results as the website does not report SOF for the women's field. As I have a generic webscraper that pulls this data from the PTO website, I could not be arsed to manually fix this.

<figure>
  <img src="pngs/plot2.png" alt="Trulli" style="width:80%">
  <figcaption>The biggest difference an athlete made by virtue of finishing further ahead of second place is about 10pts. An that 10pts is a rare event. On average the races are tight and the gains are few and far between. So most of the time, an athlete makes about 2-3 pts by winning a race outright. When you weigh this against the other features, it has negligible contribution in ranking.</figcaption>
</figure>

</body>

## The Times, They Are A Changin

As mentioned in the disclaimer, the goal of this document was to really understand the incentives of the new ranking system. First thing to note is that the way triathlon dealt with the problem of comparing performances across different courses is to do away with the problem in the first place. The incentives are clear -- "to be the best, athletes must race the best". If everyone showed up for the races, ranking athletes is a trivial from a mathematical perspective. **If you're an established pro athlete this seems to be the fairest possible system you could ask for.** None of that $AIT$ malarkey and none of that convex optimisation [ELO](https://abiswas3.github.io/sportsMaths/PrimoRank/) scores either. Simple and Straight -- that's what everyone wanted. **Note: This new system is almost identical to [Tommy Rank](https://abiswas3.github.io/sportsMaths/TommyRank/) which I had recommended a year ago.** A clear improvement from the older system is that the consequences we are about to discuss were likely intentional. That's typically what you want from a system -- you know why and where it goes wrong.

Tennis[^5] and Golf rankings are very similar in essence. Win Wimbledon and all the glory is yours. There is one issue however. The economics of triathlon and tennis are not the same. Your neighbour, local Bob, does not step out onto the grass courts of Wimbledon with Novak Djokovic. However, they do pay an exorbitant amount of money to ride up and down the high streets of Bolton with Lucy Charles Barclay. By putting all the ranking eggs in the PTO and championship races, your local Bob might not enjoy as much pro time any more. It would appear that Triathlon is headed in the direction of other mainstream sports. LeBron James is not as relatable nor accessible as say Lionel Sanders. It seems that the new system would lead to a larger gap between the professionals and age groupers (unless the age groupers are willing to pay a higher premium to keep up their old lifestyle). It is likely that this is necessary for any sport to scale economically. I cannot say, I am not an economist. I certainly do not begrudge anyone  asking for more in return for exercising 30 hours a week and/or winning Olympic gold medals[^7]. This is a debate for experts who understand the trade-offs between [capitalism](https://www.amazon.co.uk/Capitalism-Ghost-Story-Arundhati-Roy/dp/1784780944) and [socialism](https://www.amazon.com/dp/0156835207?tag=thestrategistsite-20&ascsubtag=[]st[p]cjsz8amqa007co7y6spqo4ac8[i]5qy0dx[v]a[u]1[t]w[r]google.com[d]D[z]m). It is beyond my skill set.

[^7]: Better they make money than those pesky chat GPT billionaire freaks.

I'm also not sure how this could affect an upcoming pro who is low on funds or athletes that are not from the Eu/USA. There is measurably less value in racing smaller races now. Empirically if you looked at races in 2023, there is not that many high valued races in Oceania, Asia or Africa (though there is likely not a high supply of athletes from these places yet). The potential unfairness of older systems acted like a regularising feature for the athletes with less access. They could only beat the athletes in races they had access to and could still somehow earn a small living by appearing to be ranked high. [Journalists have also noted](https://twitter.com/Timheming/status/1627706043579916288?s=20) that the sports focus is really on the top athletes and making sure they are fairly compensated. This seems in line with the trend in other sports like football where the star players are bought and sold for incredibly high wages and the lower league athletes have second jobs.

All in all, as far as the rankings are concerned, the maths is cut and dry. The system heavily biases towards athletes that show up and race the races deemed "big" by the establishment. Showing up to big races and doing "ok"[^10] is more important than doing "very well" in smaller races. If everyone is present at a given race, then sorting by finish position gives you a fair ranking. The SOF is a constant offset for everyone and the $\Delta$ gains from time are monotone with finish position. **So the final ranking is essentially just your average finish position in the biggest 3 races of the year**. The points allotments makes it impossible to have a meaningful score unless you get into the races the PTO have declared to be important. Just like your and my average day job, triathlon now has upper management. There is nothing morally questionable about such a system. Hospitals and schools have centralised structure. Big money sports like NBA and EPL have central bodies with far more questionable morals. Often finding a fair solution is impossible without a centralised source of control[^13]. It's just that triathlon is now closer to EPL than it is to ultra running. It's no longer the hipster sport where an odd bunch of people raced in random locations and no one actually knew who was best till they met in Kona. Although they're still an odd bunch, all things must change, and perhaps it is triathlons time for change. For the athletes that could not make at least 3 of the big races -- you can still make pennies on the dollar by going to other races. But likely say goodbye to your hopes of a top 20 finish.

[^13]: Just take a look at how many hard is to even get [consensus](https://en.wikipedia.org/wiki/Byzantine_fault) without a central party

[^5]: If I remember correctly, this was an intentional goal for the PTO. To make triathlon more like the ATP or WTA circuit.

[^10]: It is always hard to actually measure how an "OK" performance in a big race compares to winning a small race. This was why the problem was hard in the first place. The points system describes the current committees value system. It is neither right or wrong -- just what we would call [inductive bias](https://en.wikipedia.org/wiki/Inductive_bias).

## Other Miscellaneous Observations

There are few other things that stood out to me but I doubt they make a significant difference.

+  The choice of top 5 for SOF seemed rather arbitrary. Due to travel/cost/training circumstances, not all athletes show up to all silver and gold races. Hence there is a high variance in the strength of field even across the same tiers of races. Perhaps [a smoothing function](https://en.wikipedia.org/wiki/Winsorizing) or something more robust to outliers like [median](https://en.wikipedia.org/wiki/Robust_statistics) would have made more sense. In my experience using explicit clipping like top-$K$ always causes issues in the long run, unless $K$ has been cross validated with test sets. My guess is 5 seemed like a good fair number and was picked heuristically. Then on running simulations not much changed, so 5 was kept. **There is likely an exploit/attack on the system here:** Given races in the same tier, find a race with the highest SOF where is easiest to finish 6th. As the SOF only concerns the top 5 athletes, the remaining athletes in the race have no effect on the "free" points available. Alternatively, find races in the same tier that have one or two of the top 5 athletes in the world. As the SOF is the average of Top 5 scores, the sof of the race will be susceptible to outliers i.e the really good athletes will bump up the SOF for the race. Then look to finish 4th or 5th if possible. Is this attack likely? Almost certainly yes! Look at the first plot and consider the variance across SOF for races with the same Tier. With a little bit of optimisation, it should not be hard to find a sweet spot that gives you a lot of points. I do not have access to athlete scores at the start of race so it isn't possible for me to run a full simulation. However, I can leave with you an idea of what the attack looks like. Consider two Gold full IM races, lets call them Race A and Race B. They are both the same tier of races so your score is just given by finishing higher. So let's say your goal is to finish 4th. Which race is it easier to finish fourth in? *Hint: Presence of outliers really bias mean estimates.*
  + **Race A (Sof: 85.772)**: PATRICK LANGE,  DANIEL BAEKKEGARD, LEON CHEVALIER,  JOE SKIPPER,  BEN KANUTE,  BRADEN CURRIE, MIKI MOERCK TAAGHOLT, CLEMENT MIGNON,  JASON WEST,  RUDY VON BERG, STEVEN MCKENNA

  + **Race B (SofL 86.77)**: KRISTIAN BLUMMENFELT,  GUSTAV IDEN,  CHRIS LEIFERMAN, BEN HOFFMAN, 
 PIETER HEEMERYCK,  KEVIN MAUREL, MARTIN ULLOA, FERNANDO TOLDI,  HENRIK GOESCH

It might be that a race like this not naturally occurring but if athletes were malicious and formed a coalition, then it's trivial to find scenarios where one can boost their score by schedule hacking. All the maths they need is be able to solve a system of linear equations. Anytime a start list is deep there will be athletes say ranked 6, 7, 8 and 9 who will not affect the SOF at all. On the contrary anytime a start list is shallow but includes the top 2 athletes, it will boost the sof artificially. In fact it is in Gustav and Kristian's interest to go to as many gold races together, to boost the sof and pick up ranks one and two.

+ Similarly, the calculation for $\Delta$ seems ad hoc. There are cases[^8] where the base time is calculated using just the winners time. In that case the winner by definition cannot get any positive $\Delta$ points[^9] and everyone else gets negative points. However, as the final rankings are a function of top 3 performances over the year, giving others negative points does not help an athlete. Those athletes might as well drop this performance and do well somewhere else. However the athlete that indeed won the race got nothing positive from winning the race. This seems like a systemic issue. In the cases where $\Delta$ is calculated from a base line time of top 3-5 times, this issue is still prevalent as the winning athletes time is included to compute the baseline, and therefore biases their score closer to 0. As shown in the plots above, computing $\Delta$ this way hardly makes a difference. There is a valid argument to be made to drop this feature completely as it adds more noise than signal.

+ Like almost all sane ranking systems (and this certainly a very reasonable system), the top few athletes are largely unaffected by policy changes. The robustness of any system should be measured based on how sensitive the rankings are for mid-tiered athletes. You do not need mathematics to prove that Gustav Iden or Ashleigh Gentle is very very good.

[^8]: When not pro enough athletes finish.

[^9]: You cannot be head of the average if you are the average. Everyone is now behind the average.

</div>
