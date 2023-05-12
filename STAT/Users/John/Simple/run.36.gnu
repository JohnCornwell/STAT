set term pdf color
set xlabel "Timestep"
set ylabel "Demand"
set output "run.36.stepdemandtask0.pdf"
set title "Demand and Delivered, Task 0"
plot "run.36.stepdemand" using 2:5 title "Demand"  w lines,\
     "run.36.stepdemand" using 2:8 title "Delivered" w lines
set output "run.36.stepdemandtask1.pdf"
set title "Demand and Delivered, Task 1"
plot "run.36.stepdemand" using 2:17 title "Demand"  w lines,\
     "run.36.stepdemand" using 2:20 title "Delivered" w lines
unset size
unset title

set term pdf color
set output "run.36.stepsummary.steplen.pdf"
set title "Change in each step"
set xlabel "Timestep"
set ylabel "Change"
plot [-2:] "run.36.stepsummary" using 2:($13 + $31) title "Target" w line,\
     "run.36.stepsummary" using 2:($15 + $33) title "Tracker" w line lc 3
unset xlabel
unset ylabel
unset title

set term pdf color
set output "run.36.stepsummary.paths.task0total.pdf"
set title "Target and Tracker Total Action for Task 0"
plot[-2:]\
     "run.36.stepsummary" using 2:5 title "Target Total" w line,\
     "run.36.stepsummary" using 2:7 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.36.stepsummary.paths.task1total.pdf"
set title "Target and Tracker Total Action for Task 1"
plot[-2:]\
     "run.36.stepsummary" using 2:23 title "Target Total" w line,\
     "run.36.stepsummary" using 2:25 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.36.stepsummary.paths.simtotal.pdf"
set title "Target and Tracker Total Action for Sim"
plot[-2:]\
     "run.36.stepsummary" using 2:($5 + $23) title "Target Total" w line,\
     "run.36.stepsummary" using 2:($7 + $25)  title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set size ratio 0.5
set output "run.36.stepsummary.task0accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.36.stepsummary" using 2:19 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.36.stepsummary.task1accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.36.stepsummary" using 2:37 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.36.stepsummary.swarmperformance.pdf"
set title "Performance of Swarm"
set xlabel "Timestep"
set ylabel "Swarm Performance"
plot [-2:] "run.36.stepsummary" using 2:48 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.36.stepsummary.switch.percentactors.pdf"
set title "Percent task switches relative to number of actors"
set xlabel "Timestep"
set ylabel "Percent task switches"
plot [-2:][0:200] "run.36.stepsummary" using 2:44 w line
set output "run.36.stepsummary.switch.percentall.pdf"
set title "Percent task switches relative to population size"
set xlabel "Timestep"
set ylabel "Percent task switches"
plot [-2:][0:100] "run.36.stepsummary" using 2:46 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.36.stepsummary.switch.count.pdf"
set title "Number of task switches"
set xlabel "Timestep"
set ylabel "Number of task switches"
plot [-2:][0:50] "run.36.stepsummary" using 2:42 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set xlabel "Timestep"
set ylabel "Number of agents"
set output "run.36.stepsummary.actorstask0.pdf"
set title "Number of agents acting for task 0"
plot [-2:][0:50] "run.36.stepsummary" using 2:17 w impulse
set output "run.36.stepsummary.actorstask1.pdf"
set title "Number of agents acting for task 1"
plot [-2:][0:50] "run.36.stepsummary" using 2:35 w impulse
set output "run.36.stepsummary.pushnone.pdf"
set title "Number of idle agents"
plot [-2:][0:50] "run.36.stepsummary" using 2:40 w impulse
set output "run.36.stepsummary.pushall.pdf"
set title "Total number of agents pushing"
plot [-2:][0:50] "run.36.stepsummary" using 2:($18 + $36) w impulse
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size square
set output "run.36.initpop.task0rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 0 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.36.initpop" using 2:5 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.36.initpop.task1rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 1 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.36.initpop" using 2:7 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.36.task0initpop.scaledthresh.pdf"
set ylabel "Task 0 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:12.000000]\
     "run.36.initpop" using 2:12 w dots
unset size
unset ylabel
unset title

set term pdf color
set size square
set output "run.36.task1initpop.scaledthresh.pdf"
set ylabel "Task 1 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:12.000000]\
     "run.36.initpop" using 2:14 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.36.finalpop.task0scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:12.000000]\
     "run.36.finalpop" using 2:12 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.36.finalpop.task1scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:12.000000]\
     "run.36.finalpop" using 2:14 w dots
unset size
unset ylabel
unset title

