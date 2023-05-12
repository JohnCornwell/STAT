set term pdf color
set xlabel "Timestep"
set ylabel "Demand"
set output "run.17.stepdemandtask0.pdf"
set title "Demand and Delivered, Task 0"
plot "run.17.stepdemand" using 2:5 title "Demand"  w lines,\
     "run.17.stepdemand" using 2:8 title "Delivered" w lines
set output "run.17.stepdemandtask1.pdf"
set title "Demand and Delivered, Task 1"
plot "run.17.stepdemand" using 2:17 title "Demand"  w lines,\
     "run.17.stepdemand" using 2:20 title "Delivered" w lines
set output "run.17.stepdemandtask2.pdf"
set title "Demand and Delivered, Task 2"
plot "run.17.stepdemand" using 2:29 title "Demand"  w lines,\
     "run.17.stepdemand" using 2:32 title "Delivered" w lines
set output "run.17.stepdemandtask3.pdf"
set title "Demand and Delivered, Task 3"
plot "run.17.stepdemand" using 2:41 title "Demand"  w lines,\
     "run.17.stepdemand" using 2:44 title "Delivered" w lines
set output "run.17.stepdemandtask4.pdf"
set title "Demand and Delivered, Task 4"
plot "run.17.stepdemand" using 2:53 title "Demand"  w lines,\
     "run.17.stepdemand" using 2:56 title "Delivered" w lines
unset size
unset title

set term pdf color
set output "run.17.stepsummary.steplen.pdf"
set title "Change in each step"
set xlabel "Timestep"
set ylabel "Change"
plot [-2:] "run.17.stepsummary" using 2:($13 + $31 + $49 + $67 + $85) title "Target" w line,\
     "run.17.stepsummary" using 2:($15 + $33 + $51 + $69 + $87) title "Tracker" w line lc 3
unset xlabel
unset ylabel
unset title

set term pdf color
set output "run.17.stepsummary.paths.task0total.pdf"
set title "Target and Tracker Total Action for Task 0"
plot[-2:]\
     "run.17.stepsummary" using 2:5 title "Target Total" w line,\
     "run.17.stepsummary" using 2:7 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.17.stepsummary.paths.task1total.pdf"
set title "Target and Tracker Total Action for Task 1"
plot[-2:]\
     "run.17.stepsummary" using 2:23 title "Target Total" w line,\
     "run.17.stepsummary" using 2:25 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.17.stepsummary.paths.task2total.pdf"
set title "Target and Tracker Total Action for Task 2"
plot[-2:]\
     "run.17.stepsummary" using 2:41 title "Target Total" w line,\
     "run.17.stepsummary" using 2:43 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.17.stepsummary.paths.task3total.pdf"
set title "Target and Tracker Total Action for Task 3"
plot[-2:]\
     "run.17.stepsummary" using 2:59 title "Target Total" w line,\
     "run.17.stepsummary" using 2:61 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.17.stepsummary.paths.task4total.pdf"
set title "Target and Tracker Total Action for Task 4"
plot[-2:]\
     "run.17.stepsummary" using 2:77 title "Target Total" w line,\
     "run.17.stepsummary" using 2:79 title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set output "run.17.stepsummary.paths.simtotal.pdf"
set title "Target and Tracker Total Action for Sim"
plot[-2:]\
     "run.17.stepsummary" using 2:($5 + $23 + $41 + $59 + $77) title "Target Total" w line,\
     "run.17.stepsummary" using 2:($7 + $25 + $43 + $61 + $79)  title "Tracker Total" w line lc 3
unset size
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.task0accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.17.stepsummary" using 2:19 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.task1accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.17.stepsummary" using 2:37 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.task2accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.17.stepsummary" using 2:55 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.task3accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.17.stepsummary" using 2:73 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.task4accuracy.pdf"
set title "Accuracy"
set xlabel "Timestep"
set ylabel "Swarm Accuracy"
plot [-2:] "run.17.stepsummary" using 2:91 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.swarmperformance.pdf"
set title "Performance of Swarm"
set xlabel "Timestep"
set ylabel "Swarm Performance"
plot [-2:] "run.17.stepsummary" using 2:102 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.switch.percentactors.pdf"
set title "Percent task switches relative to number of actors"
set xlabel "Timestep"
set ylabel "Percent task switches"
plot [-2:][0:200] "run.17.stepsummary" using 2:98 w line
set output "run.17.stepsummary.switch.percentall.pdf"
set title "Percent task switches relative to population size"
set xlabel "Timestep"
set ylabel "Percent task switches"
plot [-2:][0:100] "run.17.stepsummary" using 2:100 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set output "run.17.stepsummary.switch.count.pdf"
set title "Number of task switches"
set xlabel "Timestep"
set ylabel "Number of task switches"
plot [-2:][0:40] "run.17.stepsummary" using 2:96 w line
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size ratio 0.5
set xlabel "Timestep"
set ylabel "Number of agents"
set output "run.17.stepsummary.actorstask0.pdf"
set title "Number of agents acting for task 0"
plot [-2:][0:40] "run.17.stepsummary" using 2:17 w impulse
set output "run.17.stepsummary.actorstask1.pdf"
set title "Number of agents acting for task 1"
plot [-2:][0:40] "run.17.stepsummary" using 2:35 w impulse
set output "run.17.stepsummary.actorstask2.pdf"
set title "Number of agents acting for task 2"
plot [-2:][0:40] "run.17.stepsummary" using 2:53 w impulse
set output "run.17.stepsummary.actorstask3.pdf"
set title "Number of agents acting for task 3"
plot [-2:][0:40] "run.17.stepsummary" using 2:71 w impulse
set output "run.17.stepsummary.actorstask4.pdf"
set title "Number of agents acting for task 4"
plot [-2:][0:40] "run.17.stepsummary" using 2:89 w impulse
set output "run.17.stepsummary.pushnone.pdf"
set title "Number of idle agents"
plot [-2:][0:40] "run.17.stepsummary" using 2:94 w impulse
set output "run.17.stepsummary.pushall.pdf"
set title "Total number of agents pushing"
plot [-2:][0:40] "run.17.stepsummary" using 2:($18 + $36 + $54 + $72 + $90) w impulse
unset size
unset xlabel
unset ylabel
unset title

set term pdf color
set size square
set output "run.17.initpop.task0rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 0 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.17.initpop" using 2:5 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.17.initpop.task1rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 1 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.17.initpop" using 2:7 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.17.initpop.task2rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 2 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.17.initpop" using 2:9 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.17.initpop.task3rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 3 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.17.initpop" using 2:11 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.17.initpop.task4rawthresh.pdf"
set ylabel "Raw thresholds"
set title "Task 4 Initial population thresholds - raw"
plot [0:][0:1.2]\
     "run.17.initpop" using 2:13 w dots
unset size
unset ylabel

set term pdf color
set size square
set output "run.17.task0initpop.scaledthresh.pdf"
set ylabel "Task 0 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:24.000000]\
     "run.17.initpop" using 2:18 w dots
unset size
unset ylabel
unset title

set term pdf color
set size square
set output "run.17.task1initpop.scaledthresh.pdf"
set ylabel "Task 1 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:36.000000]\
     "run.17.initpop" using 2:20 w dots
unset size
unset ylabel
unset title

set term pdf color
set size square
set output "run.17.task2initpop.scaledthresh.pdf"
set ylabel "Task 2 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:48.000000]\
     "run.17.initpop" using 2:22 w dots
unset size
unset ylabel
unset title

set term pdf color
set size square
set output "run.17.task3initpop.scaledthresh.pdf"
set ylabel "Task 3 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:60.000000]\
     "run.17.initpop" using 2:24 w dots
unset size
unset ylabel
unset title

set term pdf color
set size square
set output "run.17.task4initpop.scaledthresh.pdf"
set ylabel "Task 4 Scaled thresholds"
set title "Initial population thresholds - scaled"
plot [0:][0:60.000000]\
     "run.17.initpop" using 2:26 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.17.finalpop.task0scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:24.000000]\
     "run.17.finalpop" using 2:18 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.17.finalpop.task1scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:36.000000]\
     "run.17.finalpop" using 2:20 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.17.finalpop.task2scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:48.000000]\
     "run.17.finalpop" using 2:22 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.17.finalpop.task3scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:60.000000]\
     "run.17.finalpop" using 2:24 w dots
unset size
unset ylabel
unset title

set term post eps color
set size square
set output "run.17.finalpop.task4scaledthresh.eps"
set ylabel "Scaled thresholds"
set title "Task -14540 Final population thresholds - scaled"
plot [0:][0:60.000000]\
     "run.17.finalpop" using 2:26 w dots
unset size
unset ylabel
unset title

