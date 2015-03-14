# Thailand Hadoop Big Data Challenge #1

Special thanks to [IMC Institute](http://www.imcinstitute.com/) who organized the event.

**Dataset:** [Airline on-time performance](http://stat-computing.org/dataexpo/2009/)

## List the airlines with the number of flights being used

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
