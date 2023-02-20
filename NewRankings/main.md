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
for a refresher. At the heart of this ranking malarkey lies a simple
question -- "How do you compare the performance of two athletes who
did not race each other on the same day?". One cannot sort two
performances by finish time as they vary across courses. The problem
is not unique to triathlon either. This question has plagued social
choice theory since the 1950's, so it's unlikely any proposed solution
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
people decided for the people; democracy won and as Bernard Shaw
famously stated -- "Democracy is a device that ensures we shall be
governed no better than we deserve." Thus this manuscript, unlike its
predecessors does not try to propose an alternate system. It simply
tries to understand the consequences of such a system.
 <!-- The remainder of
this document is written from the perspective of an imaginary
triathlete Bob, who isn't that great at swim, bike or run. However,
much like his namesake[^2], Bob will look to lie and cheat to find
ways to boost his ranking. In other words, what is the maximum
triathlon ranking Bob can get without actually investing any time in
being good at triathlon?  -->

<!-- The hope is that the search for Bob's strategies will highlight the -->
<!-- pathological tendencies of the new ranking system. It should not be -->
<!-- read as a critique of the current system. All ranking systems (even -->
<!-- provably optimal ones) lead to unavoidable social -->
<!-- situations. Typically a group of humans will look at the odds of that -->
<!-- situation arising and accept it as an unavoidable risk. Bob's attacks -->
<!-- might be shown to be improbable, and that should strengthen the trust -->
<!-- in the new system. -->

<!-- [^2]: [Lies, God-damned lies and Bob Dylan](https://www.thedailybeast.com/bob-dylan-why-we-can-never-know-him) -->

## The New System

![Shown above is a screen grab from [this
article](https://www.triathlete.com/culture/news/new-2023-pto-rankings-revealed-dissected/)
which goes how the new points are calculated](pngs/Screenshot 2023-02-17 at 12.04.48.png)

Informally there are three features -- your tier based finish position score, the strength of the race you are participating in and how much faster you were from the top few athletes. You get points along each of these directions and finally your score is a weighted average of these features. From the outset it would appear that the new system considers a multiple facets of a race and then weights them to compute a
final score.
 However, closer examination of the point system reveals
that the new system is really based around one central concept -- the
committees' definition of strength of field. 


## The weights do not matter

The first feature accounts for $40\%$ of your score, the second feature accounts for $30\%$ of your score and the third feature contributes to $30\%$ of your score. Although the final score is claimed to be a mixture of three different features (position, strength of field and time); this is merely an illusion. The three features are highly correlated, and as a result only one feature really matters -- strength of field.

![The figure above plots the tier on the Y-axis and the SOF on the
X-axis. It is easy to see that the two are positively correlated. For
a fixed tier, one might observe that the SOF has enormous variance (we
will get to this later) but if you do well in a high tiered race, you
will almost always do well in the SOF category as well. This makes sense -- The tiering of a race is based on prize money and prestige, and thus the best athletes end up wanting to participate. ](pngs/plot1.png)


Let $T$ represent the position based tier score for an athlete and $SOF$ represent the strength of field for the given race. The timing feature is supposed to reward an athlete based on the difference
between their time and the time of the top finishers. Let $\Delta$
represent this time difference[^3]. The score for finishing really fast is determined as
$0.3(B + \Delta)$, where $B = (T_1 + SOF)/2$, where $T_1$ is the tier score of the winner (so 100 if are in a diamond race, 95 if you are in platinum race). **Note $B$ has nothing to do with your actual performance. $B$ is determined even before the race starts.**

Thus the final score $S$

\begin{align}
S &= 0.4\times T + 0.3\times SOF + 0.3(B + \Delta) \\
&= 0.4\times T + 0.3\times SOF + 0.3((T_1 + SOF)/2 + \Delta) \\
&= 0.4\times T + 0.3\times SOF + 0.15\times T_1 + 0.15\times SOF + 0.3\times\Delta \\
&= 0.4\times T + 0.3\times\Delta + (0.45\times SOF + 0.15 T_1)
\end{align}

[^3]: More specifically, $\Delta$ is the fraction the athlete was off from the average performance of the top 5 athletes times 6.

We already know that $T_1$ and $SOF$ are high for the big races. Even $T$ is biased towards the big races (finishing 14th in a platinum race is the same as second in a silver race). This might seem bizarre as there are silver races with comparable SOF's to Platinum races. So if you're an upcoming new athlete participating in a local race because you cannot afford to go to Europe/USA all the time, then $\Delta$ is the only lever which gives you any control over increasing your final rank. So how much can you squeeze out of $\Delta$? The answer is not much! Observe the plot below which shows $\Delta$ (X-axis) as a function
of race finish position (Y-axis) for different tiered races [^6]

[^6]: PTO canadian open is not included in the results as the website does not report SOF for the women's field. As I have a generic webscraper that pulls this data from the PTO website, I could not be arsed to manually fix this.

<figure>
  <img src="pngs/plot2.png" alt="Trulli" style="width:80%">
  <figcaption>The biggest difference an athlete made by virtue of finishing further ahead of second place is about 10pts. An that 10pts is a rare event. On average the races are tight and the gains are few and far between. So most of the time, an athlete makes about 2-3 pts by winning a race outright. When you weigh this against the other features, it has negligible contribution in ranking.</figcaption>
</figure>

</body>

## The Times, They Are A Changin

As mentioned in the disclaimer, the goal of this document was to really understand the incentives of the new ranking system. First thing to note is that the way triathlon dealt with the problem of comparing performances across different courses is to do away with the problem in the first place. The incentives are clear -- "to be the best, athletes must race the best". If everyone showed up for the races, ranking athletes is a trivial from a mathematical perspective. **If you're an established pro athlete this seems to be the fairest possible system you could ask for.** None of that $AIT$ malarkey and none of that convex optimisation [ELO](https://abiswas3.github.io/sportsMaths/PrimoRank/) scores either. Simple and Straight -- that's what everyone wanted.

Tennis[^5] and Golf rankings are very similar in essence. Win Wimbledon and all the glory is yours. There is one issue however. The economics of triathlon and tennis are not the same. Your neighbour, local Bob, does not step out onto the grass courts of Wimbledon with Novak Djokovic. However, they do pay an exorbitant amount of money to ride up and down the high streets of Bolton with Lucy Charles Barclay. By putting all the ranking eggs in the PTO and championship races, your local Bob might not enjoy as much pro time any more. It seems like Triathlon desires to be closer to other mainstream sports. LeBron James is not as relatable nor accessible as say Lionel Sanders. It seems like with the new system we would observe a clearer gap between the amateurs and age groupers (unless the age groupers are willing to pay a higher premium to keep up their old lifestyle). I guess this is necessary for any sport to scale economically ?!? I cannot say, I am not an economist. I also do not begrudge the professional wanting more elite status in return for exercising 30 hours a week[^7].

[^7]: Better they make money than those pesky chat GPT billionaire freaks.

I'm also not sure how this could affect an upcoming pro who is low on funds or athletes that are not from the EU/USA. There is definitively less value in racing smaller races now. There is not that many high valued races in Oceania. Asia and Africa are largely excluded (though there is likely not a high supply of athletes from these places yet).

The potential unfairness of older systems acted like a regularising feature for the athletes with less access. They could only beat the athletes in races they had access to and could still somehow earn a small living by appearing to be ranked high. [Journalists have also noted](https://twitter.com/Timheming/status/1627706043579916288?s=20) that the sports focus is really on the top athletes and making sure they are fairly compensated. This seems in line with the trend in other sports like football where the star players are bought and sold for incredibly high wages and the lower league athletes have second jobs.

All in all, as far as the rankings are concerned, the maths is cut and dry. The system heavily biases towards athletes that show up and race the races deemed "big" by the establishment. Showing up to big races and doing "ok"[^10] is more important than doing "very well" in smaller races. If everyone is present, sorting by finish position gives you a fair ranking. The SOF is a constant offset for everyone and the $\Delta$ gains from time are monotone with finish position. So the ranking is basically just your finish position. For the athletes that could not make at least 3 of the big races -- you can make pennies on the dollar by going to other races. But likely say goodbye to your hopes of a top 20 finish.

[^5]: If I remember correctly, this was an intentional goal for the PTO. To make triathlon more like the ATP or WTA circuit.

[^10]: It is always hard to actually measure how an "OK" performance in a big race compares to winning a small race. This was why the problem was hard in the first place. The points system describes the current committees value system. It is neither right or wrong -- just what we would call [inductive bias](https://en.wikipedia.org/wiki/Inductive_bias).

## Other Miscellaneous Observations

There are few other things that stood out to me but I doubt they make a significant difference.

+  The choice of top 5 for SOF seemed rather arbitrary. Due to travel/cost/training circumstances, not all athletes show up to all silver and gold races. Hence there is a high variance in the strength of field even across the same tiers of races. Perhaps [a smoothing function](https://en.wikipedia.org/wiki/Winsorizing) or something more robust to outliers like [median](https://en.wikipedia.org/wiki/Robust_statistics) would have made more sense. My guess is 5 seemed like a good fair number and was picked heuristically. Then on running simulations not much changed, so 5 was kept. 

+ Similarly, the calculation for $\Delta$ seems ad hoc. There are cases[^8] where the sase time is calculated using just the winners time. In that case the winner by definition cannot get any positive $\Delta$ points[^9] and everyone else gets negative points. However, as the final rankings are a function of top 3 performances, giving others negative points does not help an athlete. Those athletes might as well drop this performance and do well somewhere else. However the athlete that indeed won the race got nothing positive from winning the race. This seems like a systemic issue. In the cases where $\Delta$ is calculated from a base line time of top 3-5 times, this issue is still prevalent as the winning athletes time is included to compute the baseline, and therefore biases his score closer to 0. As shown in the plots above, computing $\Delta$ this way hardly makes a difference. There is a valid argument to be made to drop this feature completely as it adds more noise than signal.



[^8]: When not pro enough athletes finish.

[^9]: You cannot be head of the average if you are the average. Everyone is now behind the average.

</div>
