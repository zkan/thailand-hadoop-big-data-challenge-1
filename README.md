# Thailand Hadoop Big Data Challenge #1

Special thanks to [IMC Institute](http://www.imcinstitute.com/) who organized the event.

**Dataset:** [Airline on-time performance](http://stat-computing.org/dataexpo/2009/)

**Results:** [Thailand Hadoop Big Data Challege #1](http://zkan.github.io/thailand-hadoop-big-data-challenge-1/)

## List Airlines with The Number of Flights

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/top_airlines_mapper.py | sort | python code/top_airlines_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file top_airlines_mapper.py -mapper top_airlines_mapper.py -file top_airlines_reducer.py -reducer top_airlines_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/top_airlines_results`

*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
9E  ,262208
AA  ,604885
AQ  ,7800
AS  ,151102
B6  ,196091
...
```

## Monthly Avarage Arrival Delay of Top 5 Airlines Having High Number of Flights

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/arrival_delay_mapper.py | sort | python code/arrival_delay_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file arrival_delay_mapper.py -mapper arrival_delay_mapper.py -file arrival_delay_reducer.py -reducer arrival_delay_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/arrival_delay_results`

*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
AA-01,15.0719984202
AA-02,18.2534384544
AA-03,17.9307163605
AA-04,13.1040089416
AA-05,14.5590090783
...
```

## Avarage Arrival Delay and Departure Delay for Each Origin Airport

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/origin_airports_with_delay_mapper.py | sort | python code/origin_airports_with_delay_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file origin_airports_with_delay_mapper.py -mapper origin_airports_with_delay_mapper.py -file origin_airports_with_delay_reducer.py -reducer origin_airports_with_delay_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/origin_airports_results`

*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
ABE,7.74105988798,7.74493752693
ABI,5.03749043611,6.88714613619
ABQ,4.46167820494,7.41437128689
ABY,11.8300835655,10.9749303621
ACK,28.6038186158,29.8544152745
...
```

## How Well Weather Delay Causes Arrival Delay and Departure Delay?

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/weather_causing_delay_mapper.py | sort | python code/weather_causing_delay_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file weather_causing_delay_mapper.py -mapper weather_causing_delay_mapper.py -file weather_causing_delay_reducer.py -reducer weather_causing_delay_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/weather_causing_delay_results`
*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
1,62.8828250401,54.8512573569
10,59.7282229965,45.2933797909
100,124.34939759,111.530120482
101,124.285714286,110.851648352
102,126.764705882,114.518716578
...
```

## Best Day to Travel?

**On Local:** `cat data/2008_with_1000_first_records.csv | python code/best_day_to_travel_mapper.py | sort | python code/best_day_to_travel_reducer.py`

**On Hadoop:** `hadoop jar ~/contrib/streaming/hadoop-streaming.jar -file best_day_to_travel_mapper.py -mapper best_day_to_travel_mapper.py -file best_day_to_travel_reducer.py -reducer best_day_to_travel_reducer.py -input /user/Kan/data/2008.csv -jobconf mapred.reduce.tasks=1 -output /user/Kan/best_day_to_travel_results`

*Note:* The command above is run under the same directory with the code.

**Results from Hadoop:**

```
1,8.21085049486,10.2226107893
2,7.48120760404,8.91644565762
3,6.52201731572,8.23387332288
4,8.41159915808,9.73943693983
5,10.9534400796,12.1011089613
...
```
