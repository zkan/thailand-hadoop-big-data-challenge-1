# Thailand Hadoop Big Data Challenge #1

Special thanks to [IMC Institute](http://www.imcinstitute.com/) who organized the event.

**Dataset:** [Airline on-time performance](http://stat-computing.org/dataexpo/2009/)

## List Airlines with The Number of Flights

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/top_airlines_mapper.py | sort | python code/top_airlines_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file top_airlines_mapper.py -mapper top_airlines_mapper.py -file top_airlines_reducer.py -reducer top_airlines_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/top_airlines_results_01`

*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
9E  ,262208
AA  ,604885
AQ  ,7800
AS  ,151102
B6  ,196091
CO  ,298455
DL  ,451931
EV  ,280575
F9  ,95762
FL  ,261684
HA  ,61826
MQ  ,490693
NW  ,347652
OH  ,197607
OO  ,567159
UA  ,449515
US  ,453589
WN  ,1201754
XE  ,374510
YV  ,254930
```

## Monthly Avarage Arrival Delay of Top 5 Airlines Having High Number of Flights

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/arrival_delay_mapper.py | sort | python code/arrival_delay_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file arrival_delay_mapper.py -mapper arrival_delay_mapper.py -file arrival_delay_reducer.py -reducer arrival_delay_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/arrival_delay_results_01`

*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
AA-01,15.0719984202
AA-02,18.2534384544
AA-03,17.9307163605
AA-04,13.1040089416
AA-05,14.5590090783
AA-06,24.1428282951
AA-07,14.7706542272
AA-08,12.8398980045
AA-09,4.03176510265
AA-10,2.58369620253
AA-11,-0.222753734374
AA-12,12.6944962889
MQ-01,15.1158569402
MQ-02,17.9009091645
MQ-03,13.7834311147
MQ-04,9.33185138139
MQ-05,7.74805676389
MQ-06,15.8414948454
MQ-07,8.64637385087
MQ-08,5.7304040523
MQ-09,1.65766468935
MQ-10,-0.325552500793
MQ-11,1.85482570123
MQ-12,22.2679806894
OO-01,18.2244686142
OO-02,12.8702328336
OO-03,6.82346684861
OO-04,2.74785166027
OO-05,2.63517583764
OO-06,7.980745073
OO-07,5.14796116505
OO-08,1.33840319604
OO-09,0.517604422323
OO-10,0.0533071647717
OO-11,1.64915295851
OO-12,20.2372327224
US-01,1.82338431179
US-02,5.08655100625
US-03,2.58029536301
US-04,1.55873049627
US-05,0.0316789040812
US-06,6.42482100239
US-07,5.30599215405
US-08,2.67068230277
US-09,0.0278966915204
US-10,-2.07118320611
US-11,1.62077503311
US-12,9.13698438462
WN-01,6.86869050116
WN-02,11.3346839722
WN-03,8.96462660317
WN-04,3.52380714564
WN-05,4.89210281518
WN-06,9.34173138852
WN-07,4.45232768515
WN-08,2.54908990077
WN-09,-2.48378942971
```
