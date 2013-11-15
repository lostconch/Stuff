mini <- FALSE

#============================== Setup for running on Gauss... ==============================#

args <- commandArgs(TRUE)

cat("Command-line arguments:\n")
print(args)

####
# sim_start ==> Lowest possible dataset number
###

###################
sim_start <- 1000
###################

if (length(args)==0){
  sim_num <- sim_start + 1
  set.seed(121231)
} else {
  # SLURM can use either 0- or 1-indexing...
  # Lets use 1-indexing here...
  sim_num <- sim_start + as.numeric(args[1])
  sim_seed <- (762*(sim_num-1) + 121231)
}

cat(paste("\nAnalyzing dataset number ",sim_num,"...\n\n",sep=""))

# Find r and s indices:

#============================== Run the simulation study ==============================#

# Load packages:
library(nnet)
library(BH)
library(bigmemory.sri)
library(bigmemory)
library(biganalytics)

# I/O specifications:
datapath <- "/home/pdbaines/data"
outpath <- "output/"

# mini or full?
if (mini){
	rootfilename <- "blb_lin_reg_mini"
} else {
	rootfilename <- "blb_lin_reg_data"
}

# Filenames:
# Set up I/O stuff:
# Attach big.matrix :
mydata <- attach.big.matrix("blb_lin_reg_data.desc",path = datapath)

# Remaining BLB specs:
gamma <- 0.7
n <- length(mydata[,1])
m <- length(mydata[1,])
b <- floor(n^gamma)

# Compute s_index and r_index
s_index <- floor((sim_num-1000-1)/50)+1
r_index <- sim_num - 1000 - (s_index-1)*50

# Extract the subset:
v <- c(1:n)
if (s_index > 1){
    for (i in 1:(s_index-1)){
	    set.seed(762*(1000+50*(i-1)) + 121231)
 	    J <- sample(v,b)
  	    v <- v [! v %in% J]
    }
}
# Make sure each job with the same s_index draws identical b rows
set.seed(762*(1000+50*(s_index-1)) + 121231)
I <- sample(v,b)

y <- mydata[I,m]
X <- mydata[I,1:(m-1)]

# Reset simulation seed:
set.seed(sim_seed)

# Bootstrap dataset:
M <- rmultinom(1,n,1/b*rep(1,b))

# Fit lm:
z <- lm(y ~ X - 1,weights = M)
theta <- as.numeric(z$coefficients)

# Output file:
outfile = paste0("output/","coef_",sprintf("%02d",s_index),"_",sprintf("%02d",r_index),".txt") 

# Save estimates to file:
write.table(theta, file = outfile, sep=",", col.names=F, row.names=F)
    
