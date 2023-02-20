---
title: New Rankings

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
systems represent rank actual people with feelings and were developed
by a different set of humans (also with feelings), I have tried to
remain as neutral as possible in my discourse. In the off chance
someone is offended, I apologise.  </div>

## Recap 

In 2020, the PTO deployed a system for ranking triathletes which many
perceived to be complicated and
unfair[^1]. [See](https://abiswas3.github.io/sportsMaths/ProblemStatement/index.html)
for a refresher. At the heart of this ranking malarky lies a simple
question -- "How do you compare the performance of two athletes who
did not race each other on the same day?". One cannot sort two
performances by finish time as they vary across courses. The problem
is not unique to triathlon either. This question has plagued social
choice theory since the 1950s, so it's unlikely any proposed solution
will resolve all outstanding issues. Similar measurement issues arise
in marathon running, tennis, chess, golf and many other sports. Thus,
the PTO employed a committee of athletes, who after a year of
discussion and deliberation, came up with a new system that resolves
this question in fair manner. A key motif behind doing over the old
system was to simplify how ranking points were calculated and to
re-align the rankings to better represent the athlete values.. [A
clear description of the new system can be found
here](https://protriathletes.org/pto-world-ranking-system/) and thus
there is no need to go over the details again.


[^1]: Searching for PTO rankings on Twitter should 


At this point, as far as the PTO is concerned, this ranking problem
appears solved. The athletes were affected by the rankings, and they
decided to devise a system that prioritised their interests. The
people decided for the people, and democracy won and as Bernard Shaw
famously stated -- "Democracy is a device that ensures we shall be
governed no better than we deserve." Thus this manuscript, unlike its
predecessors does not try to propose an alternate system. It simply
tries to model the consequences of such a system. The remainder of
this document is written from the perspective of an imaginary
triathlete Bob, who isn't that great at swim, bike or run. However,
much like his namesake[^2], Bob will look to lie and cheat to find
ways to boost his ranking. In other words, what is the maximum
triathlon ranking Bob can get without actually investing any time in
being good at triathlon? 

<!-- The hope is that the search for Bob's strategies will highlight the -->
<!-- pathological tendencies of the new ranking system. It should not be -->
<!-- read as a critique of the current system. All ranking systems (even -->
<!-- provably optimal ones) lead to unavoidable social -->
<!-- situations. Typically a group of humans will look at the odds of that -->
<!-- situation arising and accept it as an unavoidable risk. Bob's attacks -->
<!-- might be shown to be improbable, and that should strengthen the trust -->
<!-- in the new system. -->

[^2]: [Lies, God-damned lies and Bob Dylan](https://www.thedailybeast.com/bob-dylan-why-we-can-never-know-him)

## The New System

From the outset it would appear that the new system considers a
diverse set of facets of a race and then weight them to compute a
final score. However, closer examination of the point system reveals
that the new system is really based around one central concept -- the
committees' definition of strength of field. There are 3 ways to
accumulate points during a triathlon race, namely:

+ **Finishing higher up in big races** -- akin to how winning the
  Olympic gold should matter more than winning your local park
  run. The Bigness of a race is determined by the athletes, race
  organisers and how much cash is up for grabs. There are five types
  of races, each with a base score and a drop-off rate. Let $b$ be the
  base score and $r$ be the drop off rate for a type of race. Then the
  winner gets $b$ points, the next athlete is $r\%$ lower than the
  person ahead of them. The group scores are as follows:
	+ Diamond: (100, 2)
	+ Platinum: (95, 2)
	+ Gold: (90, 5)
	+ Silver: (80, 8)
	+ Bronze (70, 11)


+ **Race the best to be the best** -- Each race has a strength of
  field (SOF) score which is meant to reflect hardness to win. The
  higher the SOF the harder it is to win this race. Regardless of your
  final race position, if you took part in this race, you get an
  additive offset of $0.3*SOF$ added to your final score. The SOF
  score is just the average of the PTO rank score for the top 5
  athletes that start the race.
  
+ **Finishing unreasonably quickly should be rewarded** -- Finish time
  is not a reliable metric in comparing across different races. Wind,
  road surface, rain, heat, hills are some of the miscellaneous
  factors that act as counterfactuals that bias time. However, if you
  ask athletes, they'll often tell you words like *"That's a really
  fast time for this course"*. So, very believably, they have
  instinctive feel for what is fast or a superhuman performance. They
  would like to reward an athlete for such a performance. They do so
  by calculating how much faster (or slower) an athlete went from a
  base time (quite similar to AIT) as a percentage. So if the base
  time was 100s and I complete the race 104s. Then I went 4% faster
  and for every 1% I went faster I get an additional 6 bonus points on
  top of the baseline points.

Finally they take the score from each category and add them up with
different weights. Shown below is a screen grab from [this
article](https://www.triathlete.com/culture/news/new-2023-pto-rankings-revealed-dissected/)
which goes over the arithmetic.

![An illustration of how points are calcuated](pngs/Screenshot 2023-02-17 at 12.04.48.png)

<!-- PS: There is a harmless arithmetic error in the [PTO Website -->
<!-- description](https://protriathletes.org/pto-world-ranking-system/) -->

<!-- ``` -->
<!-- An athlete’s final Race Time Score is calculated by starting with the Baseline Score and adding or deducting 6 points for every 1% that they’re faster or slower than the Baseline Time. An athlete’s Race Time Score cannot fall below 0 regardless of how far behind the Baseline Time they finish a race -->
<!-- ``` -->

<!-- And then they work out an example: -->

<!-- ![[pngs/Screenshot 2023-02-17 at 12.12.22.png]] -->

<!-- $Base = 3:58:17$ -->
<!-- First finisher $= 3:44:40$ -->

<!-- They are faster than baseline should be  $\frac{| Base - finish|}{Base}$ but instead $\frac{| Base - finish|}{finish}= 6.06\%$. The error is harmless as everything is linear, and it shouldn't matter that much :-)   -->

## The weights do not matter

Although the final score is claimed to be a mixture of three different features (position, strength of field and time); this is merely an illusion. The three features are highly correlated, and as a result only one feature really matters -- strength of field. Let $T$ represent the points awarded based on the finish position given the race tier. Let $SOF$ represent the pre-determined SOF for a race.


![The figure above plots the tier on the Y-axis and the SOF on the
X-axis. It is easy to see that the two are positively correlated. For
a fixed tier, one might observe that the SOF has enormous variance (we
will get to this later) but if you do well in a high tiered race, you
will almost always do well in the SOF category as well. This makes sense -- The tiering of a race is based on prize money and prestige, and thus the best athletes end up wanting to participate. ](pngs/plot1.png)


Let $T$ represent the position based tier score for an athlete and $SOF$ represent the strength of field for the given race. The timing feature is supposed to reward an athlete based on the difference
between their time and the time of the top finishers. Let $\Delta$
represent this time difference[^3]. The score for finishing really fast is determined as
$0.3(B + \Delta)$, where $B = (T_1 + SOF)/2$, where $T_1$ is the tier score of the winner. **Note $B$ has nothing to do with your actual performance. $B$ is determined even before the race starts.**

Thus the final score $S$

\begin{align}
S &= 0.4\times T + 0.3\times SOF + 0.3(B + \Delta) \\
&= 0.4\times T + 0.3\times SOF + 0.3((T_1 + SOF)/2 + \Delta) \\
&= 0.4\times T + 0.3\times SOF + 0.15\times T_1 + 0.15\times SOF + 0.3\times\Delta \\
&= 0.4\times T + 0.3\times\Delta + (0.45\times SOF + 0.15 T_1)
\end{align}

[^3]: More specifically, $\Delta$ is the fraction the athlete was off from the averagae performance of the top 5 athletes times 6.

We already know that $T_1$ and $SOF$ are high for the big races. Even $T$ is biased towards the big races. So if you're an upcoming new athlete participating in a local race because you cannot afford to go to Europe all the time, then $\Delta$ is the only lever which gives you any control over your final score. So how much can you squeeze out of $\Delta$? Observe the plot below which shows $\Delta$ (X-axis) as a function
of race finish position (Y-axis) for different tiered races [^6]

[^6]: PTO canadian open is not included in the results as the website does not report SOF for the women's field. As I have a generic webscraper that pulls this data from the PTO website, I could not be arsed to manually fix this.

![The biggest difference an athlete made by virtue of finishing further ahead of second place is about 10pts. An that 10pts is a rare event. On average the races are tight and the gains are few and far between. So most of the time, an athlete makes about 2-3 pts by winning a race outright. When you weigh this against the other features, it has negligible contribution in ranking.](pngs/plot2.png)

## The Times, They Are A Changin

As mentioned in the disclaimer, the goal of this document was to really understand the incentives of the new ranking system. First thing to note is that the way triathlon dealt with the problem of comparing performances across different courses is to do away with the problem in the first place. The incentives are clear -- "to be the best, athletes must race the best". If everyone showed up for the races, ranking athletes is a trivial from a mathematical perspective. If you're an established pro athlete this seems to be the fairest possible system. None of that $AIT$ malarkey and none of that convex optimisation [ELO](https://abiswas3.github.io/sportsMaths/PrimoRank/) scores either. Simple and Straight -- that's what everyone wanted.

In fact this is not even the first time such a model has been used in pro sport. Tennis[^5] and Golf rankings are very similar in essence. Win Wimbledon and all the glory is yours. There is one issue however. The economics of triathlon and tennis are not the same. Your neighbour, local Bob, does not step out onto the grass courts of Wimbledon with Novak Djokovic. However, they do pay an exorbitant amount of money to ride up and down the high streets of Bolton with Lucy Charles Barclay. By putting all the ranking eggs in the PTO and championship races, your local Bob might not enjoy as much pro time. As more cash flows into the system, it seems like Triathlon is headed towards more mainstream sports, where the pro's live a distinctive different life from the amateurs. I guess this is necessary for any sport to grow economically ?!? I cannot say, I am not an economist. I'm also not sure how this affects an upcoming pro who is low on funds or athletes that are not from the EU/USA. There is definitively less value in racing smaller races now. [Journalists have also noted](https://twitter.com/Timheming/status/1627706043579916288?s=20) that the sports focus is really on the top athletes and making sure they are fairly compensated.

All in all, I do not have an opinion on the social implications of such changes. The mathematical problem is no longer so interesting. All things change, and triathlon seems to be in transition.

[^5]: If I remember correctly, this was an intentional goal for the PTO. To make triathlon more like the ATP or WTA circuit.

## Other Miscellaneous Observations

+ There are few other things that stood out. The choice of top 5 for SOF seemed rather arbitrary. It is perhaps why there is such a high variance in the strength of field even across the same tiers of races. Perhaps a smoothing function or something more robust to outliers like median would have made more sense. My guess is 5 seemed like a good fair number and was picked heuristically.

+ Similarly, the calculation for $\Delta$ seems ad hoc. There are cases where the Base time is calculated using just the winners time. In that case the winner by definition cannot get any positive $\Delta$ points and everyone else gets negative points. However, as the final rankings are a function of top 3 performances, giving others negative points does not help an athlete. Those athletes might as well drop this performance and do well somewhere else. However the athlete that indeed won the race got nothing from winning the race. In the cases where $\Delta$ is calculated from a base line time of top 3-5 times, this issue is still prevalent as the winning athletes time offsets the baseline. As shown in the plots above, it could be why it makes so little difference to an athletes final score.



</div>
