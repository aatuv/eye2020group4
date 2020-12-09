# huom: Lisää train.csv tiedosto kansioon

## I-DT pseudo code

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
