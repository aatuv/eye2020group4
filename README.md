
# I-DT algorithm + data processing from raw gaze data (implemented for the EYE2020 group project)

## IMPORTANT: Add train.csv to the working directory!

## How to run the code
Run `main.py`
Enter settings for the I-DT algorithm in command line. 
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
