# Introduction

This is an auxillary post in support of [this
post](http://abiswas3.github.io/blog/EloTriathlon/) which discusses
new methods to rank triathletes. In the previous post we introduced a
generic model for scoring race performances. The score for a given
race was based on the finish position. That score was multiplied by a
discount factor to accomodate for the strength of the field in the
race. We proposed Tommy Rank, a heuristic based ranking system, based
on the intuition of a field expert. In this post, we describe a more
principled appraoch to calculating the strength of the field for a
given race.

## What's the issue with Tommy Rank or other heuristics

In Tommy Rank, the strength of field for a race $r$ is calculated as

$$S(r) = \sum_{a \in X_r} \frac{1}{\text{rank}(a)}$$ where $X_r$
represents the set of athletes that participated in $r$. The immediate
consequence of such a scoring system is as follows - we are claiming
the value of having the top 3 racers race in race is much greater than
having athletes ranked 4-10 race in the same race. It is not clear
this is immediately true. Furthermore, we have provided no empirical
evidence to back this statement. **NOTE: The real version of Tommy
Rank just uses available prize purse. The above formula was used
because we did not have access to that data*. However, prize purse is
also a heuristic. We need to back out from previous race results the
strength of a certain race.

## Plackett-Luce

In 1975, Plackett introduced the [axioms of choice theory](). The
axioms were an attempt to understand how humans made choices when
presented with a multitude of options. A direct consequence of these
axioms, was the proposal of the [Placket-Luce]() model by Marden in
1995. He proved it to be a generalisation of the Bradley Terry model,
which is underlying model for evaluating pairwise competitions like
chess, scrabble, video games, college sports etc. We re-describe the
model in terms of measuring the quality of a triathlete.

Denote the athletes by integers X={1, 2, 3, ..., n}. These integer
assignments are random. They do not represent the actual rank of the
athlete. It is used to make the notation cleaner. WLet $\theta_i$
represent the intrinsic talent of an athlete $i$. We do not know this
value apriori. It needs to be estimated using race results.Then the
probability of of athlete $i$ winning a race when competing with other
athletes in set $A_r \subseteq X$ is given by

$$ P(\text{i wins over A_r}) = \frac{\theta_i}{\sum_{a \in A_r}
\theta_a}$$ EQN 1

Let $\pi(i,r)$ be the race result of athlete $i$ for race $r$.

NOTATION CLEAN UP NEEDED: 

The probability of observing race results
where 1 beats 2, and 2 beats 3 and 3 beats 4 ... and so on is given by

$$ P\Big( \pi(1) \rightarrow \pi(2) \rightarrow ... \pi(k) \Big) = 
\prod_{i=1}^k \frac{\theta_{\pi(i)}}{\theta_{\pi(i)}+ ...+ \theta_{\pi(k)}}$$


Marden (1995) points out that the above model arises from (EQN 1) if
we envision the ranking process as first choosing a winner, then
choosing a second-place finisher as the winner among those that remain
and so on.
