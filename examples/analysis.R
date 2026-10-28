# Read a tiny synthetic input and write a result that is easy to check.
samples <- read.csv("data/samples.csv")
summary <- data.frame(samples = nrow(samples), total_reads = sum(samples$reads))
dir.create("results", showWarnings = FALSE)
write.csv(summary, "results/summary_R.csv", row.names = FALSE)
print(summary)
cat("Saved results/summary_R.csv\n")
print(sessionInfo())
