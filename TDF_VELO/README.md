---
title: Lecture II
...
<div class="container">

```Primo lecture series in mathematics: Lecture II- Tour De Fantasia```

# The Tour De France Fantasy Game

Remember [our friend Tom](../ShannonDemon/)? Yes, the one with a gambling problem. Well, he's back to give you free unsolicited advice on how to build your Tour De France fantasy team. If you followed along last time, you know Tom knows a thing or two about strategy. Without Tom, you're left to your faculty or worse, advice from [these guys](https://www.bicycling.com/tour-de-france/a36843568/tour-de-france-fantasy/). Of course, Tom will also bring his reliable counsellors *Sexy Stephen* and *Bicyclist Ben* along. Now that the stage is set, we briefly review the rules for our young Americans, who might have erased the Tour from their memories. 

```
Disclaimer: At the time of writing, neither the cost of riders nor the race start list were released. We are also not responsible if you lose your life savings based on our advice.  If such a thing happens, we will pretend to be sad, however.
```

## TDF for dummies
The Tour De France is a 21-day bike race. Each day is called a stage. The stage rank of a rider is determined by the order in which they finish a stage. The GC rank of a rider is determined by the sum of their finish time across stages. The lower the aggregate, the better placed the rider (otherwise, it wouldn't be much of a race). Some stages have big mountains, and the skinny riders do well. Some are flat, which lends itself to the "*skinnier than you but still called fat*" peloton riders, often described as sprinters. Some have short hills between flat sections, and only the cycling gods (and our friend Tom) know who's likely to win these. A few other competitions sprinkled throughout the race, such as King of the mountains and points. The frequency and placement of such segments are at the discretion of the masochistic tendencies of the race director, which you can mostly ignore. We will not spend too much time analysing them. 

*PICTURE*

## How do you score points?
You pick a team of nine riders. At the end of each stage, they receive points based on the rules described in this [document](https://www.velogames.com/velogame/2021/scores.php). We review some of the important rules

+ **Winning stages**: Below is how many points you can score if a rider in your team wins a stage. The winner gets 220 points, the second 180 and so on. 
```python
stage_points = [220, 180, 160, 140, 120, 110, 95, 80, 70, 60, 50, 40, 35, 30, 25, 20, 16, 12, 8, 4]
```

+ **Being in a good position overall**: The general classification position of a rider is obtained by summing the finish time of the rider so far and sorting it in ascending order.  Below are how many points you can score by being high in the GC ranks. Every day a rider leads the Tour De France, they are awarded 30 points. 
```python
gc_points = [30, 26, 22, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

```

+ At the end of the tour, the riders are awarded an additional bonus for their final GC position. The rider that finished the race with the lowest aggregate time gets an additional 600 points and so on. 

```python
final_gc = [600, 500, 400, 350, 300, 260, 220, 200, 180, 160, 140, 130, 120, 110, 100, 90, 80, 70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
```

+ Points: Sprinkled across stages over 21 days are sections of road riders sprint for to get points. This contributes towards the points jersey (green jersey). Technically winning a sprint also does, but that gets eaten up in winning GC. **NOTE:** Unlike GC and stage -- you don't get double points for winning sprints and winning a stage. 

```python
intermediate_points = [20, 16, 12, 8, 6, 5, 4, 3, 2, 1]
```

+ Summit Points: Finally, reaching the top of the mountain (depending on the kind of mountain) first gets you some points. Reaching the top of really steep mountains gives you more points than ascending a mountain with a shallow gradient. **OBSERVE: Those skinny GC riders usually win the race by doing well on steep mountains. The excellent GC riders will likely do very well on the steep climbs** The rider that reaches the top of the steep climbs first gets thirty points, second gets twenty-five and so on.

```python
steep_climb_you_and_i_will_not_get_over = [30, 25, 20, 15, 10, 6, 4, 2]
not_so_still_steep_but_steep_for_you_and_me_climb = [15, 10, 6, 4, 2]
```

+ **Breakaway** Not every rider can win stages and ascent mountains first. Some riders accelerate early in the hope of some camera time and lead the race for a while before being caught by the peloton. If you are in a group of 30 riders or less and lead the race at the 50% mark, you get 20 points. **NOTE: These riders don't have to win races or get to the top of the mountain first. They try very hard every day for some camera time, and they get nearly as many points as the rider who gets to the top of the mountains first.** These riders are your friends. There are a handful of riders capable of winning steep climbs. But almost everyone has somewhat of a chance at being in the breakaway. Furthermore, these riders (unless serious GC contenders) are available for cheap. 

+ **Assists**: You get some points if your teammate leads GC, wins a stage or your team is high in the team's classification. If you've picked the GC favourites, you likely have no money left, so choosing the cheapest rider from the same team is an affordable way of getting free points. Once again -- even in this scoring system, you are rewarded for getting GC right. 

## Proxies of a winning team
Suppose you run a sub-4-minute mile, then Bob's your uncle. If you can also ride up a 30 min climb at 6.2Watts/kg, then Bob is also your aunty. In life, we often employ such arbitrary benchmarks to measure goodness. So we asked our friend Tom if he could summarise the science of picking the best fantasy team into some numbers. Biz-ness people love summary statistics. Sure enough, he obliged (indeed, a man of many talents) by writing a simulator that roughly approximates the Velogames scores for different team selections.

If you don't want to read this any further, read this as if you get these metrics, you can be confident that you will win. The real question, of course, is how to make a team that stands a realistic chance at achieving these numbers. 

We look at the 2022 Giro D Italia and 2021 Tour De France and analyse some of the best-performing teams. We also look at winners of local leagues and losers of local leagues. This small sample set guides our intuition. We do not bother with providing evidence of generalisation or writing down theorem/proofs. Whenever possible, we will do some back-of-the-envelope heuristic calculations to justify our decisions. If such analysis does not quench your thirst for scientific rigour, we recommend building your own model and sharing it with us (or perhaps just the profits). 

**GIRO 2022**: we looked at the top 5 teams in the overall competition, 1 team that won a local league and 1 team which did average.  *When reporting means, we'll report the mean and median (to let the reader know if there could be heavy outliers)**

| Metric                                  | Median | Mean |
|-----------------------------------------|--------|------|
| Total score                             | 9975.0 | 10003.4 |
| num riders in top K=10 scoring riders   | 6      | 5.6  |
| num riders in top K=10 GC positions     | 4      | 3.4  |
| num riders in top K=5 scoring riders    | 3      | 3.4  |
| num riders in top K=5 GC positions^[First get GC riders, then try to get the rest]      | 3      | 2.8  |
| num riders in top K=1 scoring riders^[GC winner = Points winner usually]    | 1      |  1   |
| num riders in top K=1 GC positions^[To win, you have to get GC right]      |  1     |  1   |
| number of unique stage podiums          |    7   |  7    |
| number of stage podiums (allow repeats) |   15   |    15.2  |

 To win a local league of about 15 participants, we found a score of 7,331 was competitive. Beyond that, getting the GC winner was the most important.  The local winners among the ones we sampled averaged fourteen total podiums on stages and seven individual podium riders.

The average local team had an MRR of 5,980, failed to pick the GC rider and had 11 podiums with seven unique winners.

Notice that the unique podium winners are not that different across the best teams and average teams. Even the total number of podiums is not definitive. We reason later why this is the case.  The short answer is that this game is about picking the overall GC winners. The more GC winners you choose, the better your chances. Of course, there are many other features, such as time in the breakaway etc., but we focus on these as the heavy hitters. Next, we look at the best-performing teams on last year's tour.

**TDF 2021**

| Metric                                  | Median | Mean |
|-----------------------------------------|--------|------|
| Total score                             | 10471.5| 10436.75|
| num riders in top K=10 scoring riders   | 4      | 4  |
| num riders in top K=10 GC positions     |  3.5     | 3.5  |
| num riders in top K=5 scoring riders    |  3.5     | 3.5  |
| num riders in top K=5 GC positions     |   3.5    | 3.5  |
| num riders in top K=1 scoring riders  |   1    |   1  |
| num riders in top K=1 GC positions  |    1   |   1  |
| number of unique stage podiums          |    7   |  7.25    |
| number of stage podiums (allow repeats) |   16   |    16.25  |


In last year's tour edition, to win, it was just essential to get the 3 GC riders right. If you did that, you would have won your local league. Roglic crashed, which meant this eliminated a large portion of the betting field as well.

## General advice

With all of this out of the way, here's some general advice about picking a team. 

### Always focus on GC

You win by getting points. How do you earn points? You get points through one of the streams: points, stage, GC, Kom etc. Perhaps this was intentional, or maybe the game creator did not put thought into this, but stages, GC and kom, are strongly related. So doing well in GC almost gives you the other two for free. The prime focus of your team is to get as many top 10 riders as possible. Forget sprints, ITT, Kom's and intermediate sprints. If this was not abundantly clear from the above report, look at the case study in the next section. 

### Do not try to find stage hunters

Ok, you have your GC leaders -- but chances are many people will get this correct. How do you differentiate yourself? It would appear that the next trick is to guess the stage winners.  

Not really!

**FACT OF LIFE**: It is impossible to get a good GC result without doing well on stages on average.  The converse, however, is not valid. It is possible to be a stage hunter - win stages and do terribly on GC. 

In fact, in the actual world of professional cycling, winning a stage is more revered than consistently coming top 10 on stages. However, these stage hunters are useless in the nerd fantasy land of Velogames. The reasoning comes from the fact of life.

Matej MOHORIČ won two breakaway stages at the Tour and was the talk of the town. I ask you how did [LUTSENKO Alexey](https://www.procyclingstats.com/rider/aleksey-lutsenko) do? At the top of your head, you probably don't remember -- he came 7th and didn't win a stage. Mohoric ended up with 864 points, and Alexey ended up with 932. He only cost two points more than Mohoric. Additionally, predicting that a rider that is not a unicorn wins two stages of the same tour is quite hard. On the other hand, predicting a top 10 is relatively more straightforward.

 As good GC implies good performance on most stages, those riders will benefit from both the GC scoring stream and the stage scoring stream (and often the KOM scoring system). However, stage hunters will languish at the back of the race on most stages and sacrifice their GC ambitions for the benefit of winning one or maybe even two stages. They don't get the KOM or GC position points for free.

### What about sprinters and points ?

It'd be great if I could fill my team with top 10 GC riders, but they're expensive. I cannot afford them all. So who should I pick after I'm done trying to guess the top two/three GC winners? A sprinter -- there are not that many of them at any given race. Usually, each team has one (and some don't even bother). Teams with a designated sprinter use the other riders to form a sprint train, thereby giving their sprinter the best chance at winning a sprint stage. Sprint stages have a flat finish and are not usually preceded by steep mountains. Sometimes they can be -- and it becomes hard to predict if the race would end up going to a sprinter or a breakaway rider. 

We look back at the last few grand tours to understand how many stages are contested by the GC group, breakaway riders and sprinters. Often before the first proper mountain stage, races are won between punchy sprinters and big boy sprinters. 



**GIRO 2021**

stage 1 winner: GANNA Filippo --> TT
stage 2 winner: MERLIER Tim --> big boy sprinters
stage 3 winner: VAN DER HOORN Taco --> breakaway/punchy sprinters
stage 4 winner: DOMBROWSKI Joe --> breakaway
stage 5 winner: EWAN Caleb --> big boy sprinters
stage 6 winner: MÄDER Gino --> GC group 
stage 7 winner: EWAN Caleb --> big boy sprinters
stage 8 winner: LAFAY Victor --> breakaway
stage 9 winner: BERNAL Egan   --> GC group 
stage 10 winner: SAGAN Peter --> big boy sprinters
stage 11 winner: SCHMID Mauro --> breakaway
stage 12 winner: VENDRAME Andrea --> breakaway
stage 13 winner: NIZZOLO Giacomo --> big boy sprinters
stage 14 winner: FORTUNATO Lorenzo --> breakaway
stage 15 winner: CAMPENAERTS Victor --> breakaway
stage 16 winner: BERNAL Egan  --> GC group 
stage 17 winner: MARTIN Dan  --> GC group 
stage 18 winner: BETTIOL Alberto --> breakaway
stage 19 winner: YATES Simon --> GC group 
stage 20 winner: CARUSO Damiano --> GC group 
stage 21 winner: GANNA Filippo --> TT

**Vuelta 2021**
+ stage 1 winner: ROGLIČ Primož --> TT
+ stage 2 winner: PHILIPSEN Jasper  --> big boy sprinters
+ stage 3 winner: TAARAMÄE Rein  --> breakaway
+ stage 4 winner: JAKOBSEN Fabio --> big boy sprinters
+ stage 5 winner: PHILIPSEN Jasper --> big boy sprinters
+ stage 6 winner: CORT Magnus  --> GC group 
+ stage 7 winner: STORER Michael  --> breakaway
+ stage 8 winner: JAKOBSEN Fabio --> big boy sprinters
+ stage 9 winner: CARUSO Damiano  --> breakaway
+ stage 10 winner: STORER Michael  --> breakaway
+ stage 11 winner: ROGLIČ Primož --> GC group
+ stage 12 winner: CORT Magnus  --> breakaway
+ stage 13 winner: SÉNÉCHAL Florian --> breakaway
+ stage 14 winner: BARDET Romain --> breakaway
+ stage 15 winner: MAJKA Rafał --> breakaway
+ stage 16 winner: JAKOBSEN Fabio --> big boy sprinters
+ stage 17 winner: ROGLIČ Primož  GC group/
+ stage 18 winner: LÓPEZ Miguel Ángel -->  GC group
+ stage 19 winner: CORT Magnus --> breakaway
+ stage 20 winner: CHAMPOUSSIN Clément --> GC group 
+ stage 21 winner: ROGLIČ Primož --> TT

9 breakaway 
4 Gc group
5 Sprinter

Although there are many breakaway wins, the variance across the sprint field podium is much less. It was a lot harder to predict Magnus Corts performance as opposed to JAKOBSEN Fabio. Both won 3 stages. But Fabio was 2nd on the two sprint stages he didn't win. Magnus Cort was not competitive on days he didn't decide to attack.

**TDF 2021**

+ stage 1 winner: ALAPHILIPPE Julian --> punchy sprinters
+ stage 2 winner: VAN DER POEL Mathieu --> punchy sprinters
+ stage 3 winner: MERLIER Tim --> big boy sprinters
+ stage 4 winner: CAVENDISH Mark --> big boy sprinters
+ stage 5 winner: POGAČAR Tadej --> TT
+ stage 6 winner: CAVENDISH Mark --> big boy sprinters
+ stage 7 winner: MOHORIČ Matej --> breakaway
+ stage 8 winner: TEUNS Dylan --> breakaway
+ stage 9 winner: O'CONNOR Ben --> breakaway
+ stage 10 winner: CAVENDISH Mark --> big boy sprinters
+ stage 11 winner: VAN AERT Wout --> breakaway
+ stage 12 winner: POLITT Nils --> breakaway
+ stage 13 winner: CAVENDISH Mark --> big boy sprinters
+ stage 14 winner: MOLLEMA Bauke --> breakaway
+ stage 15 winner: KUSS Sepp --> breakaway
+ stage 16 winner: KONRAD Patrick --> breakaway
+ stage 17 winner: POGAČAR Tadej --> GC
+ stage 18 winner: POGAČAR Tadej --> GC
+ stage 19 winner: MOHORIČ Matej --> breakaway
+ stage 20 winner: VAN AERT Wout -->TT
+ stage 21 winner: VAN AERT Wout --> big boy sprinter

Breakaway wins: 8
Sprinter wins: 7 

Nearly the same number -- there are a lot fewer sprinters than breakaway riders (but sadly you're not allowed to pick many. Here's where picking riders that are not classified as sprinters but can sprint helps. MVDP, Wout, Biniam etc.  )

The nice thing about a sprint stage is that it is an independent event. This implies if your favourite sprinter blows their tits out on Day 1, it has no repercussions towards their next sprint stage win. This means it is hard to go wrong in picking an excellent or above-average sprinter. **NOTE: the only real risk is that they crash as sprints are chaotic**. Additionally, even if they don't win, they'll place relatively high (see below). 

Depending on the profile of the course, picking a sprinter that climbs a little bit can help. It means they are still competitive despite climbing over mid-race lumps. Wout Van Aert, Mathieu Van Der Poel and Biniam Girmay seem to be good shouts.  Speaking of race profiles -- here's what the first seven days look like. 

| 1 | ITT      | 13Km flat short time trial, suits the big aero boys                                                   |
|---|----------|-------------------------------------------------------------------------------------------------------|
| 2 | Flat     | three small climbs where GC won't attack that come quite early, crosswinds and likely big boy sprint |
| 3 | Flat     | Big boy sprint stage                                                                                  |
| 4 | Hilly    | Rolling hills and wind ends with a flat finish.                                                     |
| 5 | Hilly    | Cobbles (19.4Km): suits classics riders; crashes, punctures and high drama are expected.                  |
| 6 | Hilly    | Rolling hills with an up-hillish finish -- could go to breakaway or sprint                |
| 7 | Mountain | Punchy finish up a pretty steep hill: Roglic, Pogacar, Alaphillipe territory                          |

Unless Wout Van Aert crashes -- he is competitive for the first six stages of this race. 
Assuming he comes top 5 in all 6 of them -- he could accumulate about 

**VERDICT**: Wout Van Aert must be in your team. Note he also gets assist points from Roglic or Jonas. 
*Alternatives*: Mathieu Van Der Poel, Biniam Girmay, Climby version of Caleb Ewan (if they're considerably cheaper)

### Unicorns exist for a reason - for you to pick them

If your race start list has the following names and there are no abnormal circumstances surrounding them (like injuries, covid, crashes, clear indication of bad from leading up to the race) -- you have to select as many of them as you can without blowing your budget. 
+ Tadej POGAČAR 
+ Primož ROGLIČ 

**The way they ride, they win by A LOT**

Roglic crashed out on stage 7 of the tour and left with 537 points whereas Magnus Cort finished 56th on the tour and ended up with 489 points. In fact, Roglic finished in the top K of the finishers on the tour.  That's just when one of them crashes. 

Tadej has never crashed out (though probability says then it is imminent) and when Roglic does finish they usually finish with __ points more than the other guys. 

**VERDICT**: Pick both of them.
If you like the all-in strategy, you bet that one, if not both of them, will crash or have a terrible day; You're left with all this money to spend elsewhere. We argue that this is not beneficial -- but if winning the overall is the only satisfactory goal, and you're willing to risk coming last in your local league; your best strategy is to drop both of them. 

**The risk:** This is not top-secret information -- they are usually the most expensive riders. If one of them crashes out, your team's chances of winning are likely toast. However, there's not much wisdom in trying to be clever. Even if one of them did crash out, you still have to predict which rider will perform above their abilities to replace them in the ranking. Good riders crash less frequently than average riders -- this is why they are good riders. Expensive riders are often good riders. So on average, you're better off trying not to be too clever. Of course, our friend Tom only maximises your chances of doing well on expectation. If you want deterministic guarantees, we recommend you consult your horoscope instead.


### Pick a unicorn supporter 

You've picked a unicorn, and they cost you your mortgage, pension and left kidney. Save some costs by choosing the cheapest member from their team to win some assist points. You get to pick nine riders -- not all of them will be equally useful. Trying for them all to be similarly valuable is destined to fail. For night there is the day; for Wout, there is Nathan Van Hooydonck.


</div>
