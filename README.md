
# I-DT algorithm + data processing from raw gaze data (implemented for the EYE2020 group project)

## IMPORTANT: Add train.csv to the working directory!

## How to run the code
Run main.py
To change the parameters for the I-DT algorithm, change `dis_threshold` (visual degrees) and `dur_threshold` (milliseconds) values in `main.py`. By default dispersion threshold is 1° and duration threshold is 100 ms.

### I-DT pseudo code

```
I-DT(dataset, dispersion threshold, duration threshold):
While available data samples:
Initialize window over first samples to cover the duration threshold
     if dispersion of window samples <= threshold
         add samples to window
         Note a fixation at the centroid of window samples
         Remove window points from samples
     else
         remove first point from points
return fixations
```
