"""Read a tiny synthetic input and save an easily checked result."""
from pathlib import Path
import pandas as pd

samples = pd.read_csv("data/samples.csv")
summary = pd.DataFrame({
    "samples": [len(samples)],
    "total_reads": [int(samples["reads"].sum())],
})
Path("results").mkdir(exist_ok=True)
summary.to_csv("results/summary.csv", index=False)
print(summary.to_string(index=False))
print("Saved results/summary.csv")
