# 911 Calls Data Manipution & Visualization
---
This project uses the data from [911.csv](911.csv). This dataset was found [here](https://www.kaggle.com/mchirico/montcoalert).

## Code Files:

* [911-calls.ipynb](911-calls.ipynb) - My jupyter notebook showing my exploration of this dataset
* [911-calls.py](911-calls.py) - A command line runnable .py script that imitates the jupyter notebook

## Pre-Requisites:

* Make sure to have [911.csv](911.csv) in the same location as the [911-calls.py](911-calls.py) script

## How it Works:

1. Import numpy, pandas, matplotlib.pyplot, seaborn, and sqlite3 into the script
2. Read the csv file into a DataFrame, import it into an SQL Databse using sqlite3, then query just the 'title' and 'timestamp' columns. Export that query to a new dataframe.
3. Create new column labeled 'reason' that includes only the first word in the 'title' column
4. Change the 'timeStamp' column from string type to datetime type
5. Create new columns labeled 'hour', 'month', and 'dayofweek' by taking that information from the 'timeStamp' column
6. Remap the 'dayofweek' column so that it has three letter abbreviations for each day rather than numbers 0-6
7. Create a violin plot that shows the distribution of calls by hour for each reason - then save that plot as [hourbyreason_vp.png](hourbyreason_vp.png)
8. Create a facet grid that has seperate plots for each reason, looking at the distribution of calls by hour - then save that plot as [hourbyreason_dp.png](hourbyreason_dp.png)
9. Create three plots and save each seperately - a boxplot for each reason looking at the distribution of calls by hour, by day of the week - saved as follows:
    * [ems_bp.png](ems_bp.png)
    * [fire_bp.png](fire_bp.png)
    * [traffic_bp.png](traffic_bp.png)
10. Create a heatmap to visualize the number of calls by month and reason - then save plot as [monthbyreason_hm.png](monthbyreason_hm.png)

## Analysis

### Hour by Reason Violin Plot

![hourbyreason_vp.png](hourbyreason_vp.png)

* If you were to look at this data as a boxplot, you'd notice that plots for all 3 reasons look very similar. The median for each reason is at either hour 13 (1:00 PM) or hour 14 (2:00 PM). The 1st and 3rd quartile are also similarly located. 
* When you look at this as a violin plot, however, you notice the difference in the distribution thanks to the Kernel Density Estimation (KDE) line. 
    * EMS calls have a more likely chance to happen between midnight and 5:00 AM than either of the other two reasons. 
    * EMS peaks around 10:00 AM, whereas Fire peaks between 5:00 and 6:00 PM. 
    * You can also notice that Traffic has two distinct humps - one between 7:00 and 8:00 AM (morning rush hour) and one between 4:00 and 5:00 PM (evening rush hour).

### Hour by Reason Distribution Plot

![hourbyreason_dp.png](hourbyreason_dp.png)

* Looking at a seperate Histogram for each reason, you can more clearly see the points made above by looking at the violin plot.
* One thing you'll notice now, however, is that EMS gets more calls than Traffic, and much more than Fire. Seeing all three reasons plotted with the same Y axis helps put into perspective the difference in total call volume.

### Box Plots by Reason (Call Distrobution by Hour, for Each Day of the Week)

![ems_bp.png](ems_bp.png)
![fire_bp.png](fire_bp.png)
![traffic_bp](traffic_bp.png)

* The plots above show that for each call reason, there are not too many differences by day of the week. There are a few details that this visual can point out though.
    * The median of call distribution for EMS happen at the same hour, regardless of the day of the week. Saturday also has the widest distribution, as the Q1 is located 8:00 AM and the Q3 is located at 6:00 PM
    * For Fire, the Q3 for each day of the week is at 6:00 PM. The Q1, however, is more sporadic. This might mean that the Fire Response team have very unpredicatble mornings, but should be able to expect a similar volume of calls in the afternoons/evenings regardless of what day of the week it is.

### Heatmap for Month and Reason

![monthbyreason_hm.png](monthbyreason_hm.png)

* This last plot is a heatmap that shows the density of call volume by month for each reason using a color gradient scale.
* One intresting thing to not here is that for both EMS and Traffic calls, there is significantly less volume during August and December than throughout the rest of the year.

---

# Thank you for visiting my 911 Calls project repository!