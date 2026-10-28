# Before starting R: choose the matching R module and set R_LIBS_USER.
# Create that writable library directory before launching R.
install.packages("ggplot2", repos = "https://cloud.r-project.org")
library(ggplot2)
print(packageVersion("ggplot2"))

# If entering these commands interactively, finish with q(save = "no").
# This returns to the shell without an R-workspace save question.
# Type exit at the shell prompt when ready to release the setup allocation.

# For an actual project, install only its required packages.
# CRAN example: install.packages("Seurat", repos = "https://cloud.r-project.org")
# Bioconductor example:
# install.packages("BiocManager", repos = "https://cloud.r-project.org")
# BiocManager::install("DESeq2", ask = FALSE, update = FALSE)
