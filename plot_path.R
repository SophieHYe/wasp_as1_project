library(tidyverse)
library(scales)

d <- read_csv("flightlog_20180519_191322.csv", col_names=F)

angle <- seq(-pi, pi, length = 50)
r <- 0.05
df <- data.frame(x = r*sin(angle), y = r*cos(angle))

ggplot(d) +
    geom_polygon(data = df, aes(x, y),  inherit.aes = F, alpha=0.4) +
    geom_polygon(data = df, aes(x+1, y),  inherit.aes = F, alpha=0.4) +
    geom_polygon(data = df, aes(x+1, y+1),  inherit.aes = F, alpha=0.4) +
    geom_polygon(data = df, aes(x, y + 1),  inherit.aes = F, alpha=0.4) +
    geom_polygon(data = df, aes(x+0.5, y + .5),  inherit.aes = F, alpha=0.4) +
    geom_path(aes(x=X6, y=X7), color="red") +
    geom_path(aes(x=X10, y=X11)) +
    scale_x_continuous(breaks=pretty_breaks(n=10)) +
    scale_y_continuous(breaks=pretty_breaks(n=10)) +
    theme_classic() +
    xlab("x") +
    ylab("y")


