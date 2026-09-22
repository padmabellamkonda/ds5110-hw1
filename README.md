## How to run

    bash run.sh
Results are written to `analysis/`.
## What was broken

### 1. 
The notebook read the CSV from an absolute path on the author's machine:

    df = pd.read_csv("/Users/jmwaura/Desktop/analysis/coffee_sales.csv")

That folder doesn't exist on any other computer, so the first cell that
touched the data failed immediately. The same problem showed up again
further down, where the chart was saved to that same Desktop folder.

I changed both to point inside the repo. In the final script the paths are
built from the script's own location, so they work no matter which
directory you run the command from.

### 2. 

`avg_daily` was printed in a cell above the one that defines it. The author
probably ran the lower cell first, then scrolled up and ran the print. that
works on their machine because the value is still sitting in the kernel,
but not on a fresh run. You normally run top to bottom, and top to bottom.

I moved the daily revenue cell above the print.

### 3.
The 50/50 split used `df.sample(frac=1)` with no seed, so it picked
different rows every run:

    Run 1 — Group A 56.60, Group B 48.90
    Run 2 — Group A 52.32, Group B 53.18

I added `random_state=30`, which makes it produce the same shuffle every
time, so the numbers are repeatable.

### 4. 

The CSV only existed locally on the author's computer, so a fresh clone of
the project would have had no data to run on at all. I committed it to
`data/raw/`. 

## Conclusion

The notebook concluded that drip coffee brings in the most revenue. It
doesn't, lattes do.

## Use of generative AI

What it was used for:
- Explaining concepts I hadn't met before: virtual environments, random
  seeds, `Path(__file__)` for anchoring paths, and what `matplotlib.use("Agg")`
  does

